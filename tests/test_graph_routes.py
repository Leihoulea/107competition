from pathlib import Path
from tempfile import TemporaryDirectory
import pytest

from scidiagnose.diagnosis_graph import DiagnosisGraph


class Agent:
    def generate_hypotheses(self, context):
        return [{"hypothesis_id":"H001","category":"candidate","description":"A candidate explanation.","status":"active","confidence":.5,"evidence_for":[],"evidence_against":[]},{"hypothesis_id":"H002","category":"alternative","description":"An alternative explanation.","status":"active","confidence":.5,"evidence_for":[],"evidence_against":[]}]
    def update_hypotheses(self, context): return context["hypotheses"]
    def plan_experiment(self, context): return {"objective":"obtain evidence","target_hypotheses":["H001","H002"],"tool":"compare","arguments":{},"expected_evidence":"A metric."}
    def reflect(self, context): return {"decision":"propose_no_fault","best_hypothesis_id":"H002","unresolved_questions":[],"summary":"No fault evidence."}
    def final_diagnosis(self, context): return {"decision":"no_fault","fault_family":"no_fault","root_cause":"The evidence does not support a fault.","confidence":.8,"evidence_experiment_ids":["EXP_001"],"recommended_repair":{}}


class Tools:
    def __init__(self): self.calls = 0
    def execute(self, tool, arguments):
        self.calls += 1
        return {"experiment_id":"EXP_001","tool":tool,"arguments":arguments,"backend":"fake","remote_host":"fake","remote_pid":1,"cost":1,"result":{"metrics":{"agreement_valid":.9,"valid_pixels":10,"valid_fraction":1.0}}}


def initial(run_id, case_id):
    return {"run_id":run_id,"case_id":case_id,"task":{},"initial_observation":{"agreement_valid":.9},"experiments":[],"evidence":[],"budget_total":30,"budget_remaining":30,"steps_used":0,"max_steps":3,"quality_threshold":.85,"diagnosis_status":"investigating","knowledge_queries":[],"knowledge_evidence":[]}


def test_graph_routes_to_no_fault_and_checkpoint_threads_do_not_cross():
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        tools = Tools(); graph = DiagnosisGraph(Agent(), tools, Path(directory))
        first = graph.run(initial("run-a", "CASE_A")); second = graph.run(initial("run-b", "CASE_B"))
        assert first["final_diagnosis"]["decision"] == "no_fault"
        assert second["case_id"] == "CASE_B" and tools.calls == 2


def test_planner_cannot_bypass_reflection_with_final_output():
    class FinalPlanner(Agent):
        def plan_experiment(self, context): return {"final": {"decision": "no_fault"}}
    with TemporaryDirectory(dir=Path.cwd()) as directory:
        graph = DiagnosisGraph(FinalPlanner(), Tools(), Path(directory))
        with pytest.raises(RuntimeError, match="planner may only return an experiment plan"):
            graph.plan(initial("run", "CASE"))
