from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from scidiagnose.diagnosis_graph import DiagnosisGraph
from scidiagnose.agent import OpenAICompatibleAgent
from scidiagnose.agent import ManualAgent


def state(experiments=None):
    return {
        "run_id": "search-policy", "case_id": "CASE", "task": {},
        "initial_observation": {"agreement_valid": .4},
        "hypotheses": [
            {"hypothesis_id": "H001", "category": "a", "description": "a", "testable_scope": ["scope-a"], "status": "active", "confidence": .5, "evidence_for": [], "evidence_against": []},
            {"hypothesis_id": "H002", "category": "b", "description": "b", "testable_scope": ["scope-b"], "status": "active", "confidence": .5, "evidence_for": [], "evidence_against": []},
        ],
        "experiments": experiments or [], "evidence": [], "budget_total": 20,
        "budget_remaining": 20, "steps_used": 0, "max_steps": 5,
        "quality_threshold": .85, "diagnosis_status": "investigating",
    }


class CandidateAgent:
    def plan_experiment(self, context):
        return {"candidate_plans": [
            {"objective": "duplicate", "target_hypotheses": ["H001"], "tested_scope": ["scope-a"], "tool": "compare", "arguments": {}},
            {"objective": "near duplicate", "target_hypotheses": ["H001"], "tested_scope": ["scope-a"], "tool": "shift_and_compare", "arguments": {"dr": 0, "dc": 0}},
            {"objective": "new covered probe", "target_hypotheses": ["H001", "H002"], "tested_scope": ["scope-a"], "tool": "inspect", "arguments": {}},
        ]}


def test_planner_selects_novel_ranked_candidate_and_records_coverage():
    previous = [
        {"experiment_id": "EXP_1", "tool": "compare", "arguments": {}},
        {"experiment_id": "EXP_2", "tool": "shift_and_compare", "arguments": {"dr": 0, "dc": 1}},
    ]
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        graph = DiagnosisGraph(CandidateAgent(), object(), Path(directory))
        planned = graph.plan(state(previous))["current_plan"]
    assert planned["tool"] == "shift_and_compare"
    assert planned["coverage"]["hypothesis_ids"] == ["H001"]
    assert planned["coverage"]["novelty"] == {"status": "novel"}


def test_planner_rejects_when_every_candidate_repeats_existing_probe():
    class RepeatAgent:
        def plan_experiment(self, context):
            return {"candidate_plans": [{"target_hypotheses": ["H001"], "tested_scope": ["scope-a"], "tool": "compare", "arguments": {}}]}
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        graph = DiagnosisGraph(RepeatAgent(), object(), Path(directory))
        with pytest.raises(RuntimeError, match="no novel candidate"):
            graph.plan(state([{"experiment_id": "EXP_1", "tool": "compare", "arguments": {}}]))


def test_novelty_rejection_gets_one_graph_replan_and_trace_event():
    class ReplanningAgent:
        def __init__(self): self.contexts = []
        def plan_experiment(self, context):
            self.contexts.append(context)
            if len(self.contexts) == 1:
                return {"target_hypotheses": ["H001"], "tested_scope": ["scope-a"], "tool": "compare", "arguments": {}}
            return {"target_hypotheses": ["H001"], "tested_scope": ["scope-a"], "tool": "inspect", "arguments": {}}
    previous = [{"experiment_id": "EXP_1", "tool": "compare", "arguments": {}}]
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        agent = ReplanningAgent()
        graph = DiagnosisGraph(agent, object(), Path(directory))
        planned = graph.plan(state(previous))["current_plan"]
        trace = (Path(directory) / "trace.jsonl").read_text()
    assert planned["tool"] == "inspect"
    assert len(agent.contexts) == 2
    assert agent.contexts[1]["planner_feedback"] == "proposed experiment too similar to previous low-information experiments; select materially different diagnostic experiment"
    assert '"node": "plan_replan"' in trace


def test_semantically_different_scope_text_still_covers_explicit_target():
    class ScopeTextAgent:
        def plan_experiment(self, context):
            return {"target_hypotheses": ["H001"], "tested_scope": ["independent measurement description"], "tool": "inspect", "arguments": {}}
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        planned = DiagnosisGraph(ScopeTextAgent(), object(), Path(directory)).plan(state())["current_plan"]
    assert planned["coverage"]["hypothesis_ids"] == ["H001"]


def test_planner_receives_coverage():
    class CoverageAgent:
        def plan_experiment(self, context):
            self.context = context
            return {"target_hypotheses": ["H001"], "tested_scope": ["scope-a"], "tool": "inspect", "arguments": {}}
    agent = CoverageAgent()
    previous = [{"experiment_id": "EXP_1", "tool": "compare", "arguments": {}, "result": {"metrics": {"agreement_valid": .6}}}]
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        DiagnosisGraph(agent, object(), Path(directory)).plan(state(previous))
    coverage = agent.context["experiment_coverage"]
    assert coverage["tested_signatures"] == ["compare:{}"]
    assert coverage["families"]["compare"] == {"count": 1, "best_delta": pytest.approx(.2), "low_information_count": 0, "informative_count": 1}


def test_near_duplicate_stagnation():
    class StagnationAgent:
        def plan_experiment(self, context):
            return {"candidate_plans": [
                {"target_hypotheses": ["H001"], "tested_scope": ["scope-a"], "tool": "shift_and_compare", "arguments": {"dr": 0, "dc": 0}},
                {"target_hypotheses": ["H001"], "tested_scope": ["scope-a"], "tool": "inspect", "arguments": {}},
            ]}
    previous = [
        {"experiment_id": "EXP_1", "tool": "shift_and_compare", "arguments": {"dr": 0, "dc": 1}, "result": {"metrics": {"agreement_valid": .4}}},
        {"experiment_id": "EXP_2", "tool": "shift_and_compare", "arguments": {"dr": 0, "dc": 2}, "result": {"metrics": {"agreement_valid": .4}}},
    ]
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        planned = DiagnosisGraph(StagnationAgent(), object(), Path(directory)).plan(state(previous))["current_plan"]
    assert planned["tool"] == "inspect"


def test_evidence_can_update_only_hypotheses_covered_by_its_scope():
    class ScopeAgent:
        def update_hypotheses(self, context):
            return [
                {**context["hypotheses"][0], "status": "supported", "evidence_for": ["E001"]},
                {**context["hypotheses"][1], "status": "rejected", "evidence_against": ["E001"]},
            ]
    current = state()
    current["evidence"] = [{"evidence_id": "E001", "experiment_id": "EXP_1", "tested_hypotheses": ["H001"], "tested_scope": ["independent measurement description"], "supports": [], "contradicts": []}]
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        result = DiagnosisGraph(ScopeAgent(), object(), Path(directory)).update_hypotheses(current)
    assert result["hypotheses"][0]["status"] == "supported"
    assert result["hypotheses"][1]["status"] == "active"
    assert result["evidence"][-1]["supports"] == ["H001"]
    assert result["evidence"][-1]["contradicts"] == []


def test_api_policy_preserves_ranked_top_k_candidate_contract():
    agent = object.__new__(OpenAICompatibleAgent)
    agent._request_json = lambda *args: {"candidates": [
        {"objective": "first", "target_hypotheses": ["H001"], "tested_scope": ["scope-a"], "experiment": {"tool": "compare", "arguments": {}}},
        {"objective": "second", "target_hypotheses": ["H002"], "tested_scope": ["scope-b"], "experiment": {"tool": "inspect", "arguments": {}}},
    ]}
    planned = agent.plan_experiment({"hypotheses": state()["hypotheses"]})
    assert [item["objective"] for item in planned["candidate_plans"]] == ["first", "second"]
    assert planned["candidate_plans"][1]["tested_scope"] == ["scope-b"]


def test_invalid_top_k_candidate_is_filtered_before_selecting_valid_candidate():
    agent = object.__new__(OpenAICompatibleAgent)
    agent._request_json = lambda *args: {"candidates": [
        {"objective": "invalid", "target_hypotheses": ["H001"], "experiment": {"tool": "shift_and_compare", "arguments": {"shifts": [[1, 0]]}}},
        {"objective": "valid", "target_hypotheses": ["H001"], "tested_scope": ["scope-a"], "experiment": {"tool": "inspect", "arguments": {}}},
    ]}
    planned = agent.plan_experiment({"hypotheses": state()["hypotheses"]})
    assert planned["tool"] == "inspect"
    assert planned["rejected_candidates"] == [{"rank": 1, "reason": "shift dr and dc must be integers in [-5, 5]"}]


def test_all_invalid_candidates_get_one_contract_correction():
    agent = object.__new__(OpenAICompatibleAgent)
    calls = []
    def request(name, context, schema):
        calls.append((name, context))
        if len(calls) == 1:
            return {"candidates": [{"experiment": {"tool": "shift_and_compare", "arguments": {"shifts": [[1, 0]]}}}]}
        return {"candidates": [{"target_hypotheses": ["H001"], "tested_scope": ["scope-a"], "experiment": {"tool": "compare", "arguments": {}}}]}
    agent._request_json = request
    planned = agent.plan_experiment({"hypotheses": state()["hypotheses"]})
    assert len(calls) == 2
    assert "planner_correction" in calls[1][1]
    assert planned["tool"] == "compare"


def test_api_planner_receives_a_neutral_tool_catalog():
    agent = object.__new__(OpenAICompatibleAgent)
    contexts = []

    def request(name, context, schema):
        contexts.append(context)
        return {"candidates": [{"target_hypotheses": ["H001"], "tested_scope": ["scope-a"], "experiment": {"tool": "compare", "arguments": {}}}]}

    agent._request_json = request
    agent.plan_experiment({"hypotheses": state()["hypotheses"]})
    assert contexts[0]["tool_catalog"]["compare"] == {"arguments": {}}
    assert contexts[0]["tool_catalog"]["shift_and_compare"]["arguments"]["dr"] == "integer [-5, 5]"


def test_manual_agent_graph_never_returns_a_planner_final_action():
    class Tools:
        def __init__(self): self.calls = 0
        def execute(self, tool, arguments):
            self.calls += 1
            return {"experiment_id": f"EXP_{self.calls}", "tool": tool, "arguments": arguments, "backend": "fake", "remote_host": "fake", "remote_pid": 1, "cost": 1, "result": {"metrics": {"agreement_valid": .4}}}
    current = state()
    current.update({"task": {"expected_quality_threshold": .85}, "hypotheses": [], "max_steps": 3, "steps_used": 0})
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        tools = Tools()
        result = DiagnosisGraph(ManualAgent(), tools, Path(directory)).run(current)
    assert tools.calls == 3
    assert result["final_diagnosis"]["decision"] == "inconclusive"
