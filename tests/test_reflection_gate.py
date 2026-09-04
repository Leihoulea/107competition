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


def test_clean_initial_quality_converges_to_no_fault_from_reflection():
    class ContinuingAgent(Agent):
        def reflect(self, context): return {"decision":"continue","best_hypothesis_id":None,"unresolved_questions":[],"summary":"continue"}
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        graph = DiagnosisGraph(ContinuingAgent(), object(), Path(directory))
        state = {
            "case_id": "CASE", "task": {}, "budget_total": 30,
            "initial_observation": {"agreement_valid": .93},
            "experiments": [{"experiment_id": "EXP_001", "tool": "compare", "arguments": {}, "result": {"metrics": {"agreement_valid": .93}}}],
            "evidence": [{"observed_metric": .93}],
            "quality_threshold": .85,
            "budget_remaining": 20,
            "steps_used": 1,
            "max_steps": 8,
        }
        assert graph.reflect(state)["diagnosis_status"] == "propose_no_fault"
