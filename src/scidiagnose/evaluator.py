"""Post-run v0.2.1 evaluator; only this module reads hidden ground truth."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _agreement(metrics: dict[str, Any]) -> float:
    """Use the v0.2.1 valid-region metric, with legacy trace compatibility."""
    return float(metrics.get("agreement_valid", metrics.get("agreement", 0.0)))


def _pipeline(value: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize all public repair representations to an executable pipeline."""
    if isinstance(value.get("pipeline"), list):
        return value["pipeline"]
    if "operation" in value:
        return [{"type": "transform", "operation": value["operation"]}]
    if "dr" in value and "dc" in value:
        return [{"type": "shift", "dr": value["dr"], "dc": value["dc"]}]
    return []


def _same_pipeline(left: list[dict[str, Any]], right: list[dict[str, Any]]) -> bool:
    return json.dumps(left, sort_keys=True, separators=(",", ":")) == json.dumps(right, sort_keys=True, separators=(",", ":"))


def evaluate(case_dir: Path, final: dict[str, Any], experiments: list[dict[str, Any]], threshold: float, budget_total: int, budget_remaining: int) -> dict[str, float]:
    """Score detection (20), family (20), validated repair (30), evidence (15), efficiency (15)."""
    truth = json.loads((case_dir / "hidden" / "ground_truth.json").read_text())
    expected_decision = "fault" if truth["fault"] else "no_fault"
    detected = final.get("decision") == expected_decision
    family = detected and final.get("fault_family") == truth["fault_family"]
    cited = set(final.get("evidence_experiment_ids", []))
    by_id = {item.get("experiment_id"): item for item in experiments}
    valid_ids = {exp_id for exp_id, item in by_id.items() if exp_id and _agreement(item.get("result", {}).get("metrics", {})) >= threshold}
    repair = _pipeline(final.get("recommended_repair", {}))
    repair_validated = bool(truth["fault"] and repair and any(exp_id in valid_ids and _same_pipeline(repair, _pipeline(item.get("arguments", {}))) for exp_id, item in by_id.items()))
    if truth["fault"]:
        evidence_supported = bool(cited) and cited <= by_id.keys() and bool(cited & valid_ids)
    else:
        initial = json.loads((case_dir / "initial_result.json").read_text())
        evidence_supported = _agreement(initial) >= threshold and (not cited or cited <= by_id.keys())
    used_budget = max(0, budget_total - budget_remaining)
    efficiency = 15 * max(0.0, 1 - used_budget / budget_total) if detected and budget_total else 0.0
    scores = {"fault_detection": 20.0 if detected else 0.0, "fault_family": 20.0 if family else 0.0, "repair_validation": 30.0 if repair_validated else 0.0, "evidence_quality": 15.0 if evidence_supported else 0.0, "efficiency": efficiency}
    scores["total"] = sum(scores.values())
    return scores
