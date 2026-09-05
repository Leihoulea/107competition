from scidiagnose.rag_ablation import rag_ablation_cohort
from scidiagnose.tool_specs import TOOL_SPECS, planner_tool_catalog


def test_b_c_ablation_changes_only_knowledge_action_visibility():
    b, c = rag_ablation_cohort("B"), rag_ablation_cohort("C")
    assert b.knowledge_enabled is False and c.knowledge_enabled is True
    assert b.query_cost == c.query_cost == 1
    assert b.shared_contract == c.shared_contract
    b_catalog, c_catalog = planner_tool_catalog(b.knowledge_enabled), planner_tool_catalog(c.knowledge_enabled)
    assert list(b_catalog) == [name for name, spec in TOOL_SPECS.items() if spec.category == "compute_experiment"]
    assert list(c_catalog)[:-1] == list(b_catalog)
    assert list(c_catalog)[-1] == "retrieve_scientific_knowledge"
