"""Generate reproducible blind v0.2.1 cases without leaking hidden recipes."""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
def shift(a:np.ndarray,dr:int,dc:int)->np.ndarray:
    out=np.zeros_like(a);sr=slice(max(0,-dr),min(a.shape[0],a.shape[0]-dr));drs=slice(max(0,dr),min(a.shape[0],a.shape[0]+dr));sc=slice(max(0,-dc),min(a.shape[1],a.shape[1]-dc));dcs=slice(max(0,dc),min(a.shape[1],a.shape[1]+dc));out[drs,dcs]=a[sr,sc];return out
def agreement(a:np.ndarray,b:np.ndarray)->float:return float((a==b).mean())
OPS={"identity":lambda a:a,"flip_x":np.fliplr,"flip_y":np.flipud,"rot90":lambda a:np.rot90(a,1),"rot180":lambda a:np.rot90(a,2),"rot270":lambda a:np.rot90(a,3)}
INVERSE={"identity":"identity","flip_x":"flip_x","flip_y":"flip_y","rot90":"rot270","rot180":"rot180","rot270":"rot90"}
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
def apply_recipe(value:np.ndarray,recipe:list[dict[str,object]])->np.ndarray:
    for step in recipe:
        if step["type"]=="transform": value=OPS[str(step["operation"])](value)
        else: value=shift(value,int(step["dr"]),int(step["dc"]))
    return value

def repair_for(recipe:list[dict[str,object]])->list[dict[str,object]]:
    result=[]
    for step in reversed(recipe):
        if step["type"]=="transform": result.append({"type":"transform","operation":INVERSE[str(step["operation"])]})
        else: result.append({"type":"shift","dr":-int(step["dr"]),"dc":-int(step["dc"])})
    return result

def write_case(name:str,recipe:list[dict[str,object]],repair:list[dict[str,object]],seed:int,output_root:Path=ROOT/"cases")->dict[str,float]:
    ref,clean=base(seed,recipe and len(recipe)>1);target=clean.copy();valid=np.ones(clean.shape,dtype=np.uint8)
    target,valid=apply_recipe(target,recipe),apply_recipe(valid,recipe)
    case=output_root/name;data=case/"public"/"data";data.mkdir(parents=True,exist_ok=True);(case/"hidden").mkdir(exist_ok=True)
    for n,a in {"reference.npy":ref,"target_faulty.npy":target,"target_valid.npy":valid}.items():np.save(data/n,a)
    threshold=.85;task={"case_id":name.upper(),"title":"Unexpected spatial disagreement between scientific products","task":"A completed scientific comparison may contain a silent failure. Use available experiments to determine whether a fault exists and validate any repair.","budget":30,"expected_quality_threshold":threshold};(case/"task.json").write_text(json.dumps(task,indent=2));(case/"public"/"README.md").write_text("Public diagnostic inputs only. Hidden ground truth is inaccessible to the agent.\n")
    all_agreement=agreement(ref,target);mask=valid.astype(bool);valid_agreement=float((ref[mask]==target[mask]).mean());stats={"clean":agreement(ref,clean),"initial":valid_agreement};initial={"process_status":"COMPLETED","exit_code":0,"agreement":valid_agreement,"agreement_all":all_agreement,"agreement_valid":valid_agreement,"valid_pixels":int(mask.sum()),"valid_fraction":float(mask.mean())};(case/"initial_result.json").write_text(json.dumps(initial,indent=2));hidden={"fault":bool(recipe),"fault_family":"compound_spatial_misalignment" if len(recipe)>1 else ("spatial_shift" if recipe and recipe[0]["type"]=="shift" else ("spatial_transform" if recipe else "no_fault")),"injected_recipe":recipe,"repair_recipe":repair,"clean_baseline":{"agreement":stats["clean"],"agreement_valid":stats["clean"]},"generator_seed":seed};(case/"hidden"/"ground_truth.json").write_text(json.dumps(hidden,indent=2));return stats

def random_recipe(rng:np.random.Generator)->list[dict[str,object]]:
    family=int(rng.integers(0,4)); operations=["rot90","rot180","rot270","flip_x","flip_y"]
    if family==0:return []
    if family==1:return [{"type":"transform","operation":str(rng.choice(operations))}]
    dr=dc=0
    while dr==0 and dc==0: dr,dc=int(rng.integers(-5,6)),int(rng.integers(-5,6))
    if family==2:return [{"type":"shift","dr":dr,"dc":dc}]
    return [{"type":"transform","operation":str(rng.choice(operations))},{"type":"shift","dr":dr,"dc":dc}]
def main()->None:
    p=argparse.ArgumentParser();p.add_argument("--count",type=int);p.add_argument("--seed",type=int,default=20260904);p.add_argument("--output-root",type=Path,default=ROOT/"cases");a=p.parse_args()
    specs=[("b01",[{"type":"transform","operation":"rot180"}],[{"type":"transform","operation":"rot180"}]),("b02",[{"type":"shift","dr":5,"dc":-5},{"type":"transform","operation":"rot180"}],[{"type":"transform","operation":"rot180"},{"type":"shift","dr":-5,"dc":5}]),("b03",[],[])]
    if a.count is None: results={name:write_case(name,r,fix,a.seed+i,a.output_root) for i,(name,r,fix) in enumerate(specs)}
    else:
        if a.count<1: raise SystemExit("--count must be positive")
        rng=np.random.default_rng(a.seed);results={}
        for index in range(a.count):
            recipe=random_recipe(rng);name=f"case_{index+1:03d}";results[name]=write_case(name,recipe,repair_for(recipe),a.seed+index,a.output_root)
    print(json.dumps(results,indent=2))
if __name__=="__main__":main()
