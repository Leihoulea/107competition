from pathlib import Path
from tempfile import TemporaryDirectory

from scidiagnose.diagnosis_graph import DiagnosisGraph


class Agent:
    def generate_hypotheses(self, context): return []
    def update_hypotheses(self, context): return []
    def plan_experiment(self, context): return {}
    def reflect(self, context): return {"decision":"propose_fault","best_hypothesis_id":"H001","unresolved_questions":[],"summary":"partial improvement"}
    def final_diagnosis(self, context): return {}


def test_partial_improvement_cannot_pass_fault_validation_gate():
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        graph = DiagnosisGraph(Agent(), object(), Path(directory))
        state = {"diagnosis_status":"propose_fault","evidence":[{"observed_metric":.74}],"quality_threshold":.85}
        assert graph.validation_gate(state)["diagnosis_status"] == "continue"
