"""Restricted NumPy runner for composable scientific diagnostic experiments."""
from __future__ import annotations
import argparse, hashlib, json, os, platform, time, traceback
from pathlib import Path
import numpy as np


def _site_profile() -> dict[str, object]:
    """Stable, anonymous execution-site metadata (stdlib only)."""
    site_id = hashlib.sha256(platform.node().encode("utf-8")).hexdigest()[:16]
    return {"profile_version": "1", "site_id": f"remote-{site_id}", "os_family": platform.system().lower()}


def _compute_metrics(started: float, input_bytes: int) -> dict[str, object]:
    metrics: dict[str, object] = {
        "wall_seconds": round(time.monotonic() - started, 6),
        "process_cpu_seconds": round(time.process_time(), 6),
        "pid": os.getpid(),
        "python_version": platform.python_version(),
        "input_bytes": input_bytes,
    }
    if hasattr(os, "getloadavg"):
        metrics["load_average_1m"] = round(os.getloadavg()[0], 4)
    try:
        import resource  # Available on Unix; intentionally optional.
        usage = resource.getrusage(resource.RUSAGE_SELF)
        metrics["user_cpu_seconds"] = round(usage.ru_utime, 6)
        metrics["system_cpu_seconds"] = round(usage.ru_stime, 6)
        # Linux reports ru_maxrss in KiB (not bytes); preserve that unit in-band.
        metrics["max_rss_kib"] = int(usage.ru_maxrss)
        metrics["max_rss_unit"] = "KiB (Linux ru_maxrss)"
    except ImportError:
        pass
    return metrics


def _scientific_metrics(metrics: dict[str, object]) -> dict[str, object]:
    """Flatten numerical scientific evidence for generic observability consumers."""
    values = {key: value for key, value in metrics.items() if isinstance(value, (int, float)) and not isinstance(value, bool)}
    primary_name = "agreement_valid" if "agreement_valid" in values else "agreement" if "agreement" in values else None
    return {"metric_count": len(values), "primary_metric": primary_name, "primary_value": values.get(primary_name) if primary_name else None, "values": values}

OPS={"identity":lambda x:x,"flip_x":np.fliplr,"flip_y":np.flipud,"rot90":lambda x:np.rot90(x,1),"rot180":lambda x:np.rot90(x,2),"rot270":lambda x:np.rot90(x,3),"transpose":np.transpose}
def shift_without_wrap(a:np.ndarray,dr:int,dc:int)->tuple[np.ndarray,np.ndarray]:
    if not -5<=dr<=5 or not -5<=dc<=5: raise ValueError("shift must be in [-5, 5]")
    out=np.zeros_like(a); valid=np.zeros(a.shape,bool); sr=slice(max(0,-dr),min(a.shape[0],a.shape[0]-dr)); drs=slice(max(0,dr),min(a.shape[0],a.shape[0]+dr)); sc=slice(max(0,-dc),min(a.shape[1],a.shape[1]-dc)); dcs=slice(max(0,dc),min(a.shape[1],a.shape[1]+dc));out[drs,dcs]=a[sr,sc];valid[drs,dcs]=True;return out,valid
def metrics(a:np.ndarray,b:np.ndarray,v:np.ndarray|None=None)->dict[str,float|int]:
    v=np.ones(a.shape,bool) if v is None else v.astype(bool)
    if not v.any():raise ValueError("candidate has no valid pixels")
    agreement_all=float((a==b).mean())
    a,b=a[v],b[v];i=int(np.logical_and(a==1,b==1).sum());u=int(np.logical_or(a==1,b==1).sum());p=int((b==1).sum());r=int((a==1).sum());agreement_valid=float((a==b).mean())
    return {"agreement":agreement_valid,"agreement_all":agreement_all,"agreement_valid":agreement_valid,"intersection":i,"union":u,"iou":float(i/u) if u else 1.0,"precision":float(i/p) if p else 1.0,"recall":float(i/r) if r else 1.0,"valid_pixels":int(v.sum()),"valid_fraction":float(v.mean())}
def describe(a:np.ndarray)->dict[str,object]:return {"shape":list(a.shape),"dtype":str(a.dtype),"min":float(a.min()),"max":float(a.max()),"mean":float(a.mean()),"std":float(a.std()),"unique_count":int(np.unique(a).size),"nan_fraction":float(np.isnan(a).mean())}
def apply_pipeline(target:np.ndarray,pipeline:list[dict[str,object]],initial_valid:np.ndarray|None=None)->tuple[np.ndarray,np.ndarray]:
    if not isinstance(pipeline,list) or len(pipeline)>4:raise ValueError("pipeline length must be 0 to 4")
    value,valid=target.copy(),(np.ones(target.shape,bool) if initial_valid is None else initial_valid.astype(bool).copy())
    for step in pipeline:
        if step.get("type")=="transform":
            op=step.get("operation")
            if op not in OPS:raise ValueError("invalid transform operation")
            value,valid=OPS[op](value),OPS[op](valid)
        elif step.get("type")=="shift":
            dr,dc=step.get("dr"),step.get("dc")
            if type(dr) is not int or type(dc) is not int:raise ValueError("shift values must be integers")
            value,_=shift_without_wrap(value,dr,dc); shifted_valid,_=shift_without_wrap(valid.astype(np.uint8),dr,dc); valid=shifted_valid.astype(bool)
        else:raise ValueError("pipeline step type must be transform or shift")
    return value,valid
def main()->None:
    p=argparse.ArgumentParser();p.add_argument("--input-dir",required=True);p.add_argument("--experiment-json",required=True);p.add_argument("--output-json",default="result.json");args=p.parse_args();t=time.monotonic()
    try:
        req=json.loads(Path(args.experiment_json).read_text());tool=req["tool"];arg=req.get("arguments",{});d=Path(args.input_dir);input_bytes=sum(path.stat().st_size for path in d.iterdir() if path.is_file());ref=np.load(d/"reference.npy");target=np.load(d/"target_faulty.npy");initial_valid=np.load(d/"target_valid.npy") if (d/"target_valid.npy").exists() else None
        if tool=="inspect":out={"reference":describe(ref),"target":describe(target)}
        elif tool=="compare":out=metrics(ref,target,initial_valid)
        elif tool=="transform_and_compare":op=arg.get("operation");v,m=apply_pipeline(target,[{"type":"transform","operation":op}],initial_valid);out={"operation":op,**metrics(ref,v,m)}
        elif tool=="shift_and_compare":dr,dc=arg.get("dr"),arg.get("dc");v,m=apply_pipeline(target,[{"type":"shift","dr":dr,"dc":dc}],initial_valid);out={"dr":dr,"dc":dc,**metrics(ref,v,m)}
        elif tool=="evaluate_candidate":pipeline=arg.get("pipeline");v,m=apply_pipeline(target,pipeline,initial_valid);out={"pipeline":pipeline,**metrics(ref,v,m)}
        else:raise ValueError("tool is not allowed")
        result={"status":"success","experiment_id":req["experiment_id"],"tool":tool,"arguments":arg,"metrics":out,"scientific_metrics":_scientific_metrics(out),"compute_metrics":_compute_metrics(t,input_bytes),"site_profile":_site_profile(),"elapsed_seconds":round(time.monotonic()-t,3)};Path(args.output_json).write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)
    except BaseException as e:Path("failure.json").write_text(json.dumps({"status":"failed","error_type":type(e).__name__,"message":str(e),"traceback":traceback.format_exc()},indent=2));raise
if __name__=="__main__":main()
