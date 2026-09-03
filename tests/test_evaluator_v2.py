from pathlib import Path

from scidiagnose.evaluator import evaluate


ROOT = Path(__file__).resolve().parents[1]


def record(exp_id, pipeline, agreement):
    return {"experiment_id": exp_id, "arguments": {"pipeline": pipeline}, "result": {"metrics": {"agreement_valid": agreement}}}


def test_fault_case_rewards_real_validated_repair_not_text():
    pipeline = [{"type": "transform", "operation": "rot180"}]
    final = {"decision": "fault", "fault_family": "spatial_transform", "root_cause": "unrelated wording", "evidence_experiment_ids": ["EXP_001"], "recommended_repair": {"pipeline": pipeline}}
    scores = evaluate(ROOT / "cases" / "b01", final, [record("EXP_001", pipeline, .93)], .85, 30, 20)
    assert scores["fault_detection"] == 20 and scores["fault_family"] == 20
    assert scores["repair_validation"] == 30 and scores["evidence_quality"] == 15


def test_compound_repair_is_result_based_and_requires_cited_experiment():
    pipeline = [{"type": "transform", "operation": "rot180"}, {"type": "shift", "dr": -5, "dc": 5}]
    final = {"decision": "fault", "fault_family": "compound_spatial_misalignment", "evidence_experiment_ids": [], "recommended_repair": {"pipeline": pipeline}}
    scores = evaluate(ROOT / "cases" / "b02", final, [record("EXP_007", pipeline, .97)], .85, 30, 22)
    assert scores["repair_validation"] == 30 and scores["evidence_quality"] == 0


def test_no_fault_uses_clean_baseline_and_does_not_require_repair():
    final = {"decision": "no_fault", "fault_family": "no_fault", "evidence_experiment_ids": [], "recommended_repair": {}}
    scores = evaluate(ROOT / "cases" / "b03", final, [], .85, 30, 30)
    assert scores["fault_detection"] == 20 and scores["fault_family"] == 20
    assert scores["repair_validation"] == 0 and scores["evidence_quality"] == 15
