"""Restricted NumPy experiment runner. It writes result.json or failure.json."""
from __future__ import annotations
import argparse, json, os, platform, time, traceback
from pathlib import Path
import numpy as np

OPS = {"identity":lambda x:x, "flip_x":np.fliplr, "flip_y":np.flipud, "rot90":lambda x:np.rot90(x,1), "rot180":lambda x:np.rot90(x,2), "rot270":lambda x:np.rot90(x,3), "transpose":np.transpose}
def metrics(a: np.ndarray, b: np.ndarray) -> dict[str, float | int]:
    same = a == b; intersection = int(np.logical_and(a==1,b==1).sum()); union = int(np.logical_or(a==1,b==1).sum())
    return {"agreement":float(same.mean()), "intersection":intersection, "union":union, "iou":float(intersection/union) if union else 1.0}
def describe(a: np.ndarray) -> dict[str, object]: return {"shape":list(a.shape),"dtype":str(a.dtype),"min":float(np.nanmin(a)),"max":float(np.nanmax(a)),"mean":float(np.nanmean(a)),"std":float(np.nanstd(a)),"unique_count":int(np.unique(a).size),"nan_fraction":float(np.isnan(a).mean())}
def main() -> None:
    parser=argparse.ArgumentParser(); parser.add_argument("--input-dir",required=True); parser.add_argument("--experiment-json",required=True); parser.add_argument("--output-json",default="result.json"); args=parser.parse_args(); started=time.monotonic()
    try:
        request=json.loads(Path(args.experiment_json).read_text()); tool=request["tool"]; arguments=request.get("arguments",{}); directory=Path(args.input_dir); ref=np.load(directory/"reference.npy"); target=np.load(directory/"target_faulty.npy")
        if tool=="inspect": output={"reference":describe(ref),"target":describe(target)}
        elif tool=="compare": output=metrics(ref,target)
        elif tool=="transform_and_compare":
            op=arguments.get("operation");
            if op not in OPS: raise ValueError("operation must be an allowed transform")
            output={"operation":op, **metrics(ref,OPS[op](target))}
        elif tool=="shift_and_compare":
            dr,dc=arguments.get("dr"),arguments.get("dc")
            if not isinstance(dr,int) or not isinstance(dc,int) or not -5<=dr<=5 or not -5<=dc<=5: raise ValueError("dr and dc must be integers from -5 to 5")
            output={"dr":dr,"dc":dc,**metrics(ref,np.roll(target,(dr,dc),(0,1)))}
        else: raise ValueError("tool is not allowed")
        result={"status":"success","experiment_id":request["experiment_id"],"tool":tool,"arguments":arguments,"metrics":output,"hostname":platform.node(),"pid":os.getpid(),"elapsed_seconds":round(time.monotonic()-started,3)}; Path(args.output_json).write_text(json.dumps(result,indent=2)); print(json.dumps(result),flush=True)
    except BaseException as exc:
        Path("failure.json").write_text(json.dumps({"status":"failed","error_type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()},indent=2)); raise
if __name__=="__main__": main()
