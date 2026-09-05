from pathlib import Path
from tempfile import TemporaryDirectory
import pytest

from scidiagnose.diagnosis_graph import DiagnosisGraph
from scidiagnose.agent import OpenAICompatibleAgent


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
        state = {"case_id":"CASE","task":{},"initial_observation":{"agreement_valid":.5},"hypotheses":[{"hypothesis_id":"H001"}],"evidence":[{"evidence_id":"E001"}],"experiments":[{"experiment_id":"EXP_001","arguments":{"pipeline":[]},"result":{"metrics":{"agreement_valid":.9}}}],"budget_total":30,"budget_remaining":20,"steps_used":1,"max_steps":8,"quality_threshold":.85,"reflection":{"decision":"propose_fault"},"validated_decision":"fault"}
        final = graph.finalize(state)["final_diagnosis"]
        assert final["fault_family"] == "spatial_transform"
        assert agent.context["hypotheses"][0]["hypothesis_id"] == "H001"
        assert agent.context["evidence"][0]["evidence_id"] == "E001"


class ConflictingAgent(Agent):
    def __init__(self, decision): self.decision, self.contexts = decision, []
    def final_diagnosis(self, context):
        self.contexts.append(context)
        return {"decision":self.decision,"fault_family":"candidate","root_cause":"Conflicting model output.","confidence":.5,"evidence_experiment_ids":[],"recommended_repair":{}}


def finalizer_state(validated_decision):
    return {"case_id":"CASE","task":{},"initial_observation":{"agreement_valid":.9},"hypotheses":[],"evidence":[],"experiments":[],"budget_total":30,"budget_remaining":30,"steps_used":0,"max_steps":8,"quality_threshold":.85,"reflection":{},"validated_decision":validated_decision}


@pytest.mark.parametrize(("validated_decision", "model_decision"), [("fault", "no_fault"), ("no_fault", "fault")])
def test_finalizer_cannot_reverse_validated_decision(validated_decision, model_decision):
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        agent = ConflictingAgent(model_decision)
        graph = DiagnosisGraph(agent, object(), Path(directory))
        with pytest.raises(RuntimeError, match="conflicts with validation gate"):
            graph.finalize(finalizer_state(validated_decision))
        assert len(agent.contexts) == 2
        assert "final_correction" in agent.contexts[1]


def test_accepted_no_fault_is_canonicalized_for_the_evaluator():
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        agent = ConflictingAgent("no_fault")
        final = DiagnosisGraph(agent, object(), Path(directory)).finalize(finalizer_state("no_fault"))["final_diagnosis"]
    assert final["fault_family"] == "no_fault"
    assert final["recommended_repair"] == {}
    assert "No untested fault family is ruled out" in final["root_cause"]


def test_finalizer_request_forbids_overclaiming_evidence_scope():
    agent = object.__new__(OpenAICompatibleAgent)
    calls = []
    agent._request_json = lambda name, context, schema: calls.append(name) or {
        "decision": "no_fault", "fault_family": "no_fault", "root_cause": "Specific candidate was not supported.",
        "confidence": .5, "evidence_experiment_ids": [], "recommended_repair": {}, "remaining_uncertainty": [],
    }
    agent.final_diagnosis({"validated_decision": "no_fault"})
    assert "Claims must not exceed the scope" in calls[0]


def test_inconclusive_final_uses_the_actual_stop_reason():
    current = finalizer_state("inconclusive")
    current["stop_reason"] = "max_steps_reached"
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        final = DiagnosisGraph(object(), object(), Path(directory)).finalize(current)["final_diagnosis"]
    assert final["stop_reason"] == "max_steps_reached"
    assert "step limit" in final["root_cause"]
