import json
from pathlib import Path

from scidiagnose.evaluator import evaluate


def record(exp_id, pipeline, agreement):
    return {"experiment_id": exp_id, "arguments": {"pipeline": pipeline}, "result": {"metrics": {"agreement_valid": agreement}}}


def case_fixture(tmp_path: Path, fault: bool, family: str, initial: float) -> Path:
    (tmp_path / "hidden").mkdir()
    (tmp_path / "hidden" / "ground_truth.json").write_text(json.dumps({"fault": fault, "fault_family": family}))
    (tmp_path / "initial_result.json").write_text(json.dumps({"agreement_valid": initial}))
    return tmp_path


def test_fault_case_rewards_real_validated_repair_not_text(tmp_path):
    pipeline = [{"type": "transform", "operation": "rot180"}]
    final = {"decision": "fault", "fault_family": "spatial_transform", "root_cause": "unrelated wording", "evidence_experiment_ids": ["EXP_001"], "recommended_repair": {"pipeline": pipeline}}
    scores = evaluate(case_fixture(tmp_path, True, "spatial_transform", .60), final, [record("EXP_001", pipeline, .93)], .85, 30, 20)
    assert scores["fault_detection"] == 20 and scores["fault_family"] == 20
    assert scores["repair_validation"] == 30 and scores["evidence_quality"] == 15


def test_compound_repair_is_result_based_and_requires_cited_experiment(tmp_path):
    pipeline = [{"type": "transform", "operation": "rot180"}, {"type": "shift", "dr": -5, "dc": 5}]
    final = {"decision": "fault", "fault_family": "compound_spatial_misalignment", "evidence_experiment_ids": [], "recommended_repair": {"pipeline": pipeline}}
    scores = evaluate(case_fixture(tmp_path, True, "compound_spatial_misalignment", .57), final, [record("EXP_007", pipeline, .97)], .85, 30, 22)
    assert scores["repair_validation"] == 30 and scores["evidence_quality"] == 0


def test_no_fault_uses_clean_baseline_and_does_not_require_repair(tmp_path):
    final = {"decision": "no_fault", "fault_family": "no_fault", "evidence_experiment_ids": [], "recommended_repair": {}}
    scores = evaluate(case_fixture(tmp_path, False, "no_fault", .93), final, [], .85, 30, 30)
    assert scores["fault_detection"] == 20 and scores["fault_family"] == 20
    assert scores["repair_validation"] == 30 and scores["evidence_quality"] == 15 and scores["total"] == 100
