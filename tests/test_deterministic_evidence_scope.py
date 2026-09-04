from pathlib import Path
from tempfile import TemporaryDirectory

from scidiagnose.diagnosis_graph import DiagnosisGraph


def state(hypotheses, initial=.6, experiments=None, evidence=None):
    return {
        "run_id": "scope", "case_id": "CASE", "task": {},
        "initial_observation": {"agreement_valid": initial},
        "hypotheses": hypotheses, "experiments": experiments or [], "evidence": evidence or [],
        "budget_total": 30, "budget_remaining": 20, "steps_used": len(experiments or []),
        "max_steps": 8, "quality_threshold": .85, "diagnosis_status": "investigating",
        "knowledge_evidence": [],
    }


def hypothesis(identifier, scope_kind="fault_family", status="active"):
    return {
        "hypothesis_id": identifier, "category": "spatial mismatch", "description": "A possible mismatch.",
        "scope_kind": scope_kind, "testable_scope": ["shift(dr=1,dc=0)"],
        "status": status, "confidence": .5, "evidence_for": [], "evidence_against": [],
    }


class Planner:
    def __init__(self, tool, arguments): self.tool, self.arguments = tool, arguments
    def plan_experiment(self, context):
        return {
            "objective": "Test one candidate.", "target_hypotheses": ["H001"],
            "tested_scope": ["the model incorrectly claims a broad family test"],
            "tool": self.tool, "arguments": self.arguments, "expected_evidence": "A metric.",
        }


def test_system_scope_matches_executed_shift():
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        graph = DiagnosisGraph(Planner("shift_and_compare", {"dr": 1, "dc": 0}), object(), Path(directory))
        plan = graph.plan(state([hypothesis("H001")]))["current_plan"]
    assert plan["system_tested_scope"] == {"kind": "candidate", "signature": "shift(dr=1,dc=0)"}


def test_evidence_scope_is_derived_from_executed_shift_not_model_text():
    current = state([hypothesis("H001")])
    current["latest_result"] = {
        "experiment_id": "EXP_001", "tool": "shift_and_compare", "arguments": {"dr": 1, "dc": 0},
        "coverage": {"hypothesis_ids": ["H001"]},
        "diagnostic_rationale": "Model claims several shifts were tested.",
        "result": {"metrics": {"agreement_valid": .59}},
    }
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        evidence = DiagnosisGraph(object(), object(), Path(directory)).extract_evidence(current)["evidence"][0]
    assert evidence["system_tested_scope"] == {"kind": "candidate", "signature": "shift(dr=1,dc=0)"}
    assert evidence["diagnostic_rationale"] == "Model claims several shifts were tested."


def test_system_scope_matches_executed_pipeline():
    pipeline = [{"type": "transform", "operation": "flip_x"}, {"type": "shift", "dr": -1, "dc": 2}]
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        graph = DiagnosisGraph(Planner("evaluate_candidate", {"pipeline": pipeline}), object(), Path(directory))
        plan = graph.plan(state([hypothesis("H001")]))["current_plan"]
    assert plan["system_tested_scope"] == {"kind": "pipeline", "signature": ["transform(flip_x)", "shift(dr=-1,dc=2)"]}


def test_llm_cannot_expand_tested_scope():
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        graph = DiagnosisGraph(Planner("shift_and_compare", {"dr": 1, "dc": 0}), object(), Path(directory))
        plan = graph.plan(state([hypothesis("H001")]))["current_plan"]
    assert plan["model_tested_scope"] == ["the model incorrectly claims a broad family test"]
    assert plan["coverage"]["system_tested_scope"]["signature"] == "shift(dr=1,dc=0)"


class RejectingUpdater:
    def update_hypotheses(self, context):
        return [{**item, "status": "rejected", "confidence": 0.0, "evidence_against": ["E001"]} for item in context["hypotheses"]]


def test_failed_candidate_does_not_reject_family():
    evidence = {
        "evidence_id": "E001", "experiment_id": "EXP_001", "tested_hypotheses": ["H001"],
        "system_tested_scope": {"kind": "candidate", "signature": "shift(dr=1,dc=0)"}, "delta": -.01,
        "supports": [], "contradicts": [],
    }
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        result = DiagnosisGraph(RejectingUpdater(), object(), Path(directory)).update_hypotheses(state([hypothesis("H001")], evidence=[evidence]))
    assert result["hypotheses"][0]["status"] == "active"


def test_failed_unnecessary_repair_does_not_weaken_valid_no_fault():
    evidence = {
        "evidence_id": "E001", "experiment_id": "EXP_001", "tested_hypotheses": ["H001"],
        "system_tested_scope": {"kind": "candidate", "signature": "shift(dr=1,dc=0)"}, "delta": -.01,
        "supports": [], "contradicts": [],
    }
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        result = DiagnosisGraph(RejectingUpdater(), object(), Path(directory)).update_hypotheses(state([hypothesis("H001", "no_fault")], initial=.93, evidence=[evidence]))
    assert result["hypotheses"][0]["status"] == "active"


def test_validated_repair_weakens_no_fault():
    experiment = {
        "experiment_id": "EXP_001", "tool": "transform_and_compare", "arguments": {"operation": "flip_x"},
        "result": {"metrics": {"agreement_valid": .93}},
    }
    evidence = {
        "evidence_id": "E001", "experiment_id": "EXP_001", "tested_hypotheses": ["H001"],
        "system_tested_scope": {"kind": "candidate", "signature": "transform(flip_x)"}, "delta": .33,
        "supports": [], "contradicts": [],
    }
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        result = DiagnosisGraph(RejectingUpdater(), object(), Path(directory)).update_hypotheses(
            state([hypothesis("H001", "no_fault")], experiments=[experiment], evidence=[evidence])
        )
    assert result["hypotheses"][0]["status"] == "weakened"
