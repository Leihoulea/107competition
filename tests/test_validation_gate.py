from pathlib import Path
from tempfile import TemporaryDirectory

from scidiagnose.diagnosis_graph import DiagnosisGraph


def gate_state(initial_agreement):
    return {
        "case_id": "GENERIC_CASE",
        "task": {},
        "initial_observation": {"agreement_valid": initial_agreement},
        "evidence": [],
        "knowledge_evidence": [],
        "quality_threshold": .85,
        "diagnosis_status": "propose_no_fault",
    }


def test_no_fault_gate_rejects_low_quality_initial():
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        result = DiagnosisGraph(object(), object(), Path(directory)).validation_gate(gate_state(.60))
    assert result == {"diagnosis_status": "continue", "validated_decision": None}


def test_no_fault_gate_accepts_valid_initial():
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        result = DiagnosisGraph(object(), object(), Path(directory)).validation_gate(gate_state(.93))
    assert result == {"diagnosis_status": "accepted_no_fault", "validated_decision": "no_fault"}
