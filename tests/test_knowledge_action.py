from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from scidiagnose.diagnosis_graph import DiagnosisGraph
from scidiagnose.knowledge.tool import ScientificKnowledgeTool
from scidiagnose.tool_specs import COSTS, TOOL_SPECS, planner_tool_catalog


ROOT = Path(__file__).resolve().parents[1]


def graph_state() -> dict:
    return {
        "run_id": "knowledge-action", "case_id": "B01", "task": {},
        "initial_observation": {"agreement_valid": .9}, "experiments": [], "evidence": [],
        "experimental_evidence": [], "knowledge_queries": [], "knowledge_evidence": [],
        "budget_total": 8, "budget_remaining": 8, "steps_used": 0, "max_steps": 3,
        "quality_threshold": .85, "diagnosis_status": "investigating", "knowledge_enabled": True,
    }


def test_knowledge_tool_returns_provenance_not_a_repair_recommendation():
    result = ScientificKnowledgeTool(ROOT / "knowledge").execute({"query": "MSG SEVIRI image scan convention", "top_k": 2})
    assert result["cost"] == COSTS["retrieve_scientific_knowledge"] == 1
    assert result["category"] == "knowledge_query"
    assert result["hits"]
    assert set(result["hits"][0]) == {"source_id", "title", "authority", "version", "section", "page", "chunk_id", "excerpt", "retrieval_score"}
    assert all("recommended_transform" not in hit and "known_repair" not in hit for hit in result["hits"])


def test_knowledge_tool_refuses_private_corpus_root(tmp_path: Path):
    private = tmp_path / "evaluator_private"; private.mkdir()
    with pytest.raises(ValueError, match="evaluator-private"):
        ScientificKnowledgeTool(private)


def test_graph_records_knowledge_and_experimental_evidence_separately():
    class Agent:
        def generate_hypotheses(self, context):
            return [{"hypothesis_id": "H001", "category": "metadata", "description": "Product conventions may explain the observation.", "status": "active", "confidence": .5, "testable_scope": ["documentation"], "evidence_for": [], "evidence_against": []}]
        def plan_experiment(self, context):
            assert context["knowledge_enabled"] is True
            return {"target_hypotheses": ["H001"], "tested_scope": ["documentation"], "tool": "retrieve_scientific_knowledge", "arguments": {"query": "MSG SEVIRI image scan convention", "top_k": 1}}
        def reflect(self, context):
            return {"decision": "propose_no_fault", "best_hypothesis_id": None, "unresolved_questions": [], "summary": "The initial observation is already within threshold."}
        def final_diagnosis(self, context):
            return {"decision": "no_fault", "fault_family": "no_fault", "root_cause": "The initial observation meets the validation threshold.", "confidence": .8, "evidence_experiment_ids": [], "recommended_repair": {}}

    with TemporaryDirectory(dir=Path.cwd()) as directory:
        result = DiagnosisGraph(Agent(), object(), Path(directory), ScientificKnowledgeTool(ROOT / "knowledge")).run(graph_state())
    assert result["experiments"] == [] and result["experimental_evidence"] == []
    assert len(result["knowledge_queries"]) == len(result["knowledge_evidence"]) == 1
    evidence = result["knowledge_evidence"][0]
    assert evidence["evidence_id"] == "K001" and evidence["validated"] is False
    assert {"source", "claim", "supports_hypotheses", "contradicts_hypotheses", "excerpt"} <= evidence.keys()
    summary = result["final_diagnosis"]["evidence_summary"]
    assert summary["experimental_evidence_ids"] == [] and summary["knowledge_evidence_ids"] == ["K001"]


def test_b_and_c_cohorts_share_specs_but_b_hides_query_action():
    assert TOOL_SPECS["retrieve_scientific_knowledge"].cost == 1
    assert "retrieve_scientific_knowledge" not in planner_tool_catalog(False)
    assert planner_tool_catalog(True)["retrieve_scientific_knowledge"]["category"] == "knowledge_query"


def test_knowledge_update_changes_only_targeted_hypothesis_with_cited_k_evidence():
    class Agent:
        def generate_hypotheses(self, context):
            return [
                {"hypothesis_id": "H001", "category": "metadata", "description": "A convention may matter.", "status": "active", "confidence": .3, "testable_scope": ["documentation"], "evidence_for": [], "evidence_against": []},
                {"hypothesis_id": "H002", "category": "other", "description": "Another possibility.", "status": "active", "confidence": .4, "testable_scope": ["other"], "evidence_for": [], "evidence_against": []},
            ]
        def plan_experiment(self, context):
            return {"target_hypotheses": ["H001"], "tested_scope": ["documentation"], "tool": "retrieve_scientific_knowledge", "arguments": {"query": "MSG SEVIRI image scan convention", "top_k": 1}}
        def update_hypotheses_from_knowledge(self, context):
            return {"hypotheses": [
                {**context["hypotheses"][0], "status": "supported", "confidence": .7, "evidence_for": ["K001"]},
                {**context["hypotheses"][1], "status": "rejected", "confidence": .1, "evidence_against": ["K001"]},
            ], "evidence_interpretations": [{"evidence_id": "K001", "claim": "The cited documentation describes an image-orientation convention.", "supports_hypotheses": ["H001"], "contradicts_hypotheses": ["H002"]}]}
        def reflect(self, context):
            return {"decision": "propose_no_fault", "best_hypothesis_id": None, "unresolved_questions": [], "summary": "Initial quality is sufficient."}
        def final_diagnosis(self, context):
            return {"decision": "no_fault", "fault_family": "no_fault", "root_cause": "Initial quality meets threshold.", "confidence": .8, "evidence_experiment_ids": [], "recommended_repair": {}}

    with TemporaryDirectory(dir=Path.cwd()) as directory:
        result = DiagnosisGraph(Agent(), object(), Path(directory), ScientificKnowledgeTool(ROOT / "knowledge")).run(graph_state())
    first, second = result["hypotheses"]
    assert first["status"] == "supported" and first["evidence_for"] == ["K001"]
    assert second["status"] == "active" and second["evidence_against"] == []
    evidence = result["knowledge_evidence"][0]
    assert evidence["supports_hypotheses"] == ["H001"] and evidence["contradicts_hypotheses"] == []
    assert evidence["source"]["version"] and evidence["source"]["chunk_id"]


def test_duplicate_knowledge_query_is_not_novel():
    state = {"knowledge_queries": [{"query_id": "Q001", "query": "MSG  SEVIRI native image orientation"}], "experiments": []}
    candidate = {"tool": "retrieve_scientific_knowledge", "arguments": {"query": " msg seviri native image orientation "}}
    assert DiagnosisGraph._novelty(state, candidate)["status"] == "duplicate"
