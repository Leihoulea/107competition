"""Generate deterministic v0.2 public cases without leaking hidden recipes."""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
def shift(a:np.ndarray,dr:int,dc:int)->np.ndarray:
    out=np.zeros_like(a);sr=slice(max(0,-dr),min(a.shape[0],a.shape[0]-dr));drs=slice(max(0,dr),min(a.shape[0],a.shape[0]+dr));sc=slice(max(0,-dc),min(a.shape[1],a.shape[1]-dc));dcs=slice(max(0,dc),min(a.shape[1],a.shape[1]+dc));out[drs,dcs]=a[sr,sc];return out
def agreement(a:np.ndarray,b:np.ndarray)->float:return float((a==b).mean())
def base(seed:int,fine:bool=False)->tuple[np.ndarray,np.ndarray]:
    y,x=np.mgrid[-1:1:256j,-1:1:256j];f=np.zeros((256,256));
    for cx,cy,sx,sy,amp in [(-.58,-.36,.17,.11,1.3),(.41,.30,.24,.15,1.0),(-.18,.56,.12,.18,.9),(.62,-.60,.09,.12,.8)]:f+=amp*np.exp(-(((x-cx)/sx)**2+((y-cy)/sy)**2)/2)
    rng=np.random.default_rng(seed)
    if fine:
        f=np.zeros_like(f)
        for cx,cy in rng.uniform(-.9,.9,(180,2)):
            f+=.75*np.exp(-(((x-cx)/.035)**2+((y-cy)/.035)**2)/2)
        threshold=.18
    else: threshold=.06
    ref=(f+rng.normal(0,.025,f.shape)>threshold).astype(np.uint8);clean=(f+rng.normal(0,.025,f.shape)>threshold+.005).astype(np.uint8);return ref,clean
def write_case(name:str,recipe:list[dict[str,object]],repair:list[dict[str,object]],seed:int)->dict[str,float]:
    ref,clean=base(seed,recipe and len(recipe)>1);target=clean.copy();valid=np.ones(clean.shape,dtype=np.uint8)
    for step in recipe:
        if step["type"]=="transform": target=np.rot90(target,2);valid=np.rot90(valid,2)
        else: target=shift(target,int(step["dr"]),int(step["dc"]));valid=shift(valid,int(step["dr"]),int(step["dc"]))
    case=ROOT/"cases"/name;data=case/"public"/"data";data.mkdir(parents=True,exist_ok=True);(case/"hidden").mkdir(exist_ok=True)
    for n,a in {"reference.npy":ref,"target_clean.npy":clean,"target_faulty.npy":target,"target_valid.npy":valid}.items():np.save(data/n,a)
    threshold=.85;task={"case_id":name.upper(),"title":"Unexpected spatial disagreement between scientific products","task":"A completed scientific comparison may contain a silent failure. Use available experiments to determine whether a fault exists and validate any repair.","budget":30,"expected_quality_threshold":threshold};(case/"task.json").write_text(json.dumps(task,indent=2));(case/"public"/"README.md").write_text("Public diagnostic inputs only. Hidden ground truth is inaccessible to the agent.\n")
    stats={"clean":agreement(ref,clean),"initial":agreement(ref,target)};(case/"initial_result.json").write_text(json.dumps({"process_status":"COMPLETED","exit_code":0,"agreement":stats["initial"],"valid_pixels":int(ref.size)},indent=2));hidden={"fault":bool(recipe),"fault_family":"compound_spatial_misalignment" if len(recipe)>1 else ("spatial_transform" if recipe else "no_fault"),"injected_recipe":recipe,"repair_recipe":repair,"clean_baseline":{"agreement":stats["clean"]}};(case/"hidden"/"ground_truth.json").write_text(json.dumps(hidden,indent=2));return stats
def main()->None:
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,default=3);p.add_argument("--seed",type=int,default=20260904);a=p.parse_args()
    specs=[("b01",[{"type":"transform","operation":"rot180"}],[{"type":"transform","operation":"rot180"}]),("b02",[{"type":"shift","dr":5,"dc":-5},{"type":"transform","operation":"rot180"}],[{"type":"transform","operation":"rot180"},{"type":"shift","dr":-5,"dc":5}]),("b03",[],[])]
    results={name:write_case(name,r,fix,a.seed+i) for i,(name,r,fix) in enumerate(specs[:a.count])};print(json.dumps(results,indent=2))
if __name__=="__main__":main()
