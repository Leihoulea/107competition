from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from scidiagnose.diagnosis_graph import DiagnosisGraph


class FakeCognitiveAgent:
    def __init__(self): self.plan_context = None; self.update_context = None
    def generate_hypotheses(self, context):
        return [{"hypothesis_id":"H001","category":"systematic","description":"A repeatable cause is plausible.","status":"active","confidence":.5,"evidence_for":[],"evidence_against":[]},{"hypothesis_id":"H002","category":"normal","description":"Expected variation is plausible.","status":"active","confidence":.4,"evidence_for":[],"evidence_against":[]}]
    def update_hypotheses(self, context):
        self.update_context = context
        return [{**context["hypotheses"][0],"status":"supported","confidence":.75,"evidence_for":["E001"]}, {**context["hypotheses"][1],"status":"weakened","confidence":.2,"evidence_against":["E001"]}]
    def plan_experiment(self, context):
        self.plan_context = context
        return {"objective":"distinguish H001 from H002","target_hypotheses":["H001","H002"],"tool":"compare","arguments":{},"expected_evidence":"A baseline metric distinguishes the explanations."}
    def reflect(self, context): return {"decision":"continue","best_hypothesis_id":"H001","unresolved_questions":[],"summary":"Continue."}
    def final_diagnosis(self, context): return {}


def state():
    return {"run_id":"test","case_id":"CASE","task":{"expected_quality_threshold":.85},"initial_observation":{"agreement_valid":.57},"experiments":[],"evidence":[],"budget_total":30,"budget_remaining":30,"steps_used":0,"max_steps":8,"quality_threshold":.85,"diagnosis_status":"investigating","knowledge_queries":[],"knowledge_evidence":[]}


def test_hypothesis_evidence_and_planner_share_explicit_cognitive_state():
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        agent = FakeCognitiveAgent(); graph = DiagnosisGraph(agent, object(), Path(directory))
        current = state(); current.update(graph.hypothesize(current))
        current["latest_result"] = {"experiment_id":"EXP_001","tool":"evaluate_candidate","arguments":{"pipeline":[]},"result":{"metrics":{"agreement_valid":.74,"valid_pixels":100,"valid_fraction":1.0}}}
        current.update(graph.extract_evidence(current))
        current.update(graph.update_hypotheses(current))
        current.update(graph.plan(current))
        evidence = current["evidence"][0]
        assert evidence["baseline_metric"] == .57 and evidence["delta"] == pytest.approx(.17) and evidence["residual_gap"] == pytest.approx(.11)
        assert current["hypotheses"][0]["status"] == "supported"
        assert agent.update_context["latest_evidence"]["evidence_id"] == "E001"
        assert agent.plan_context["hypotheses"][0]["evidence_for"] == ["E001"]
        assert agent.plan_context["evidence"][0]["delta"] == pytest.approx(.17)
        assert agent.plan_context["budget_remaining"] == 30 and agent.plan_context["tool_costs"]["compare"] == 1
        assert current["current_plan"]["target_hypotheses"] == ["H001", "H002"]
