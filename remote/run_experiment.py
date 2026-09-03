"""Restricted NumPy runner for composable scientific diagnostic experiments."""
from __future__ import annotations
import argparse, json, os, platform, time, traceback
from pathlib import Path
import numpy as np

OPS={"identity":lambda x:x,"flip_x":np.fliplr,"flip_y":np.flipud,"rot90":lambda x:np.rot90(x,1),"rot180":lambda x:np.rot90(x,2),"rot270":lambda x:np.rot90(x,3),"transpose":np.transpose}
def shift_without_wrap(a:np.ndarray,dr:int,dc:int)->tuple[np.ndarray,np.ndarray]:
    if not -5<=dr<=5 or not -5<=dc<=5: raise ValueError("shift must be in [-5, 5]")
    out=np.zeros_like(a); valid=np.zeros(a.shape,bool); sr=slice(max(0,-dr),min(a.shape[0],a.shape[0]-dr)); drs=slice(max(0,dr),min(a.shape[0],a.shape[0]+dr)); sc=slice(max(0,-dc),min(a.shape[1],a.shape[1]-dc)); dcs=slice(max(0,dc),min(a.shape[1],a.shape[1]+dc));out[drs,dcs]=a[sr,sc];valid[drs,dcs]=True;return out,valid
def metrics(a:np.ndarray,b:np.ndarray,v:np.ndarray|None=None)->dict[str,float|int]:
    v=np.ones(a.shape,bool) if v is None else v
    if not v.any():raise ValueError("candidate has no valid pixels")
    a,b=a[v],b[v];i=int(np.logical_and(a==1,b==1).sum());u=int(np.logical_or(a==1,b==1).sum());p=int((b==1).sum());r=int((a==1).sum())
    return {"agreement":float((a==b).mean()),"intersection":i,"union":u,"iou":float(i/u) if u else 1.0,"precision":float(i/p) if p else 1.0,"recall":float(i/r) if r else 1.0,"valid_pixels":int(v.sum()),"valid_fraction":float(v.mean())}
def describe(a:np.ndarray)->dict[str,object]:return {"shape":list(a.shape),"dtype":str(a.dtype),"min":float(a.min()),"max":float(a.max()),"mean":float(a.mean()),"std":float(a.std()),"unique_count":int(np.unique(a).size),"nan_fraction":float(np.isnan(a).mean())}
def apply_pipeline(target:np.ndarray,pipeline:list[dict[str,object]])->tuple[np.ndarray,np.ndarray]:
    if not isinstance(pipeline,list) or len(pipeline)>4:raise ValueError("pipeline length must be 0 to 4")
    value,valid=target.copy(),np.ones(target.shape,bool)
    for step in pipeline:
        if step.get("type")=="transform":
            op=step.get("operation")
            if op not in OPS:raise ValueError("invalid transform operation")
            value,valid=OPS[op](value),OPS[op](valid)
        elif step.get("type")=="shift":
            dr,dc=step.get("dr"),step.get("dc")
            if type(dr) is not int or type(dc) is not int:raise ValueError("shift values must be integers")
            value,valid=shift_without_wrap(value,dr,dc)
        else:raise ValueError("pipeline step type must be transform or shift")
    return value,valid
def main()->None:
    p=argparse.ArgumentParser();p.add_argument("--input-dir",required=True);p.add_argument("--experiment-json",required=True);p.add_argument("--output-json",default="result.json");args=p.parse_args();t=time.monotonic()
    try:
        req=json.loads(Path(args.experiment_json).read_text());tool=req["tool"];arg=req.get("arguments",{});d=Path(args.input_dir);ref=np.load(d/"reference.npy");target=np.load(d/"target_faulty.npy")
        if tool=="inspect":out={"reference":describe(ref),"target":describe(target)}
        elif tool=="compare":out=metrics(ref,target)
        elif tool=="transform_and_compare":op=arg.get("operation");v,m=apply_pipeline(target,[{"type":"transform","operation":op}]);out={"operation":op,**metrics(ref,v,m)}
        elif tool=="shift_and_compare":dr,dc=arg.get("dr"),arg.get("dc");v,m=apply_pipeline(target,[{"type":"shift","dr":dr,"dc":dc}]);out={"dr":dr,"dc":dc,**metrics(ref,v,m)}
        elif tool=="evaluate_candidate":pipeline=arg.get("pipeline");v,m=apply_pipeline(target,pipeline);out={"pipeline":pipeline,**metrics(ref,v,m)}
        else:raise ValueError("tool is not allowed")
        result={"status":"success","experiment_id":req["experiment_id"],"tool":tool,"arguments":arg,"metrics":out,"hostname":platform.node(),"pid":os.getpid(),"elapsed_seconds":round(time.monotonic()-t,3)};Path(args.output_json).write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)
    except BaseException as e:Path("failure.json").write_text(json.dumps({"status":"failed","error_type":type(e).__name__,"message":str(e),"traceback":traceback.format_exc()},indent=2));raise
if __name__=="__main__":main()
