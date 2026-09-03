"""Post-run evaluator; this is the only module that reads hidden ground truth."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
def evaluate(case_dir:Path, final:dict[str,Any], experiments:list[dict[str,Any]], threshold:float,budget_total:int,budget_remaining:int)->dict[str,float]:
    truth=json.loads((case_dir/"hidden"/"ground_truth.json").read_text()); root=final.get("root_cause","").lower(); aliases=("orientation","rotation","rotated","array orientation","spatial orientation")
    root_score=40 if truth["root_cause"] in root or any(alias in root for alias in aliases) else 0
    ids={x["experiment_id"] for x in experiments}; cited=set(final.get("evidence_experiment_ids",[])); evidence=20 if cited and cited<=ids else 0
    validated=any(float(x.get("result",{}).get("metrics",{}).get("agreement",0))>=threshold for x in experiments); repair=final.get("recommended_repair",{}).get("operation")==truth["expected_transform"]; validation=30 if validated and repair else 0
    efficiency=10*max(0,1-(budget_total-budget_remaining)/budget_total) if root_score else 0
    return {"root_cause":root_score,"validation":validation,"evidence":evidence,"efficiency":efficiency,"total":root_score+validation+evidence+efficiency}
