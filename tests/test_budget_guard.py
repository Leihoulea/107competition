from pathlib import Path
from tempfile import TemporaryDirectory

from scidiagnose.diagnosis_graph import DiagnosisGraph


class Agent:
    def generate_hypotheses(self, context): return []
    def update_hypotheses(self, context): return []
    def plan_experiment(self, context): return {}
    def reflect(self, context): return {"decision":"propose_no_fault","best_hypothesis_id":None,"unresolved_questions":[],"summary":"budget exhausted"}
    def final_diagnosis(self, context): return {}


class Tools:
    def execute(self, *args): raise AssertionError("budget-blocked plan must not execute")


def test_budget_guard_blocks_remote_execution_before_call():
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        graph = DiagnosisGraph(Agent(), Tools(), Path(directory))
        state = {"current_plan":{"plan_id":"PLAN001","tool":"evaluate_candidate","arguments":{"pipeline":[{"type":"transform","operation":"rot180"},{"type":"shift","dr":1,"dc":1}]},"estimated_cost":5},"budget_remaining":2,"steps_used":0,"max_steps":8}
        assert graph.budget_check(state)["budget_blocked"] is True


def test_budget_guard_distinguishes_step_and_budget_limits():
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        graph = DiagnosisGraph(Agent(), Tools(), Path(directory))
        step_limited = {"current_plan": {"estimated_cost": 1}, "budget_remaining": 5, "steps_used": 2, "max_steps": 2}
        budget_limited = {"current_plan": {"estimated_cost": 2}, "budget_remaining": 1, "steps_used": 0, "max_steps": 2}
        assert graph.budget_check(step_limited)["stop_reason"] == "max_steps_reached"
        assert graph.budget_check(budget_limited)["stop_reason"] == "budget_exhausted"
