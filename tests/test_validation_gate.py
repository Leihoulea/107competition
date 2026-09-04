from pathlib import Path
from tempfile import TemporaryDirectory

from scidiagnose.diagnosis_graph import DiagnosisGraph


def gate_state(initial_agreement, experiments=None, decision="propose_no_fault"):
    return {
        "case_id": "GENERIC_CASE",
        "task": {},
        "initial_observation": {"agreement_valid": initial_agreement},
        "evidence": [],
        "experiments": experiments or [],
        "knowledge_evidence": [],
        "quality_threshold": .85,
        "diagnosis_status": decision,
    }


def test_no_fault_gate_rejects_low_quality_initial():
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        result = DiagnosisGraph(object(), object(), Path(directory)).validation_gate(gate_state(.60))
    assert result == {"diagnosis_status": "continue", "validated_decision": None}


def test_no_fault_gate_accepts_valid_initial():
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        result = DiagnosisGraph(object(), object(), Path(directory)).validation_gate(gate_state(.93))
    assert result == {"diagnosis_status": "accepted_no_fault", "validated_decision": "no_fault"}


def test_fault_gate_rejects_high_quality_baseline_without_a_repair():
    experiments = [{"experiment_id": "EXP_001", "tool": "compare", "arguments": {}, "result": {"metrics": {"agreement_valid": .93}}}]
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        result = DiagnosisGraph(object(), object(), Path(directory)).validation_gate(gate_state(.93, experiments, "propose_fault"))
    assert result == {"diagnosis_status": "continue", "validated_decision": None}


def test_fault_gate_accepts_real_improving_repair_after_low_quality_initial():
    experiments = [{"experiment_id": "EXP_001", "tool": "transform_and_compare", "arguments": {"operation": "flip_x"}, "result": {"metrics": {"agreement_valid": .93}}}]
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        result = DiagnosisGraph(object(), object(), Path(directory)).validation_gate(gate_state(.60, experiments, "propose_fault"))
    assert result == {"diagnosis_status": "accepted_fault", "validated_decision": "fault"}
