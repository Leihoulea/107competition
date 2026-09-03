from pathlib import Path
from tempfile import TemporaryDirectory

from scidiagnose.diagnosis_graph import DiagnosisGraph


class Agent:
    def __init__(self): self.context = None
    def generate_hypotheses(self, context): return []
    def update_hypotheses(self, context): return []
    def plan_experiment(self, context): return {}
    def reflect(self, context): return {}
    def final_diagnosis(self, context):
        self.context = context
        return {"decision":"fault","fault_family":"spatial_transform","root_cause":"Evidence supports the candidate.","confidence":.9,"evidence_experiment_ids":["EXP_001"],"recommended_repair":{"pipeline":[]}}


def test_finalizer_uses_cognitive_state_not_placeholder_text():
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        agent = Agent(); graph = DiagnosisGraph(agent, object(), Path(directory))
        state = {"case_id":"CASE","task":{},"initial_observation":{"agreement_valid":.5},"hypotheses":[{"hypothesis_id":"H001"}],"evidence":[{"evidence_id":"E001"}],"experiments":[{"experiment_id":"EXP_001","arguments":{"pipeline":[]},"result":{"metrics":{"agreement_valid":.9}}}],"budget_total":30,"budget_remaining":20,"steps_used":1,"max_steps":8,"quality_threshold":.85,"reflection":{"decision":"propose_fault"}}
        final = graph.finalize(state)["final_diagnosis"]
        assert final["fault_family"] == "spatial_transform"
        assert agent.context["hypotheses"][0]["hypothesis_id"] == "H001"
        assert agent.context["evidence"][0]["evidence_id"] == "E001"
