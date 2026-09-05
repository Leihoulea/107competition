"""Explicit B/C cohort contract for reproducible RAG ablations."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal

from .tool_specs import COSTS


@dataclass(frozen=True)
class RAGAblationCohort:
    cohort: Literal["B", "C"]
    knowledge_enabled: bool
    query_cost: int
    shared_contract: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


_SHARED = (
    "same_planner_implementation",
    "same_hypothesis_prompt",
    "same_compute_tool_specs_and_order",
    "same_budget_and_max_steps",
    "same_validation_and_evidence_semantics",
    "same_public_case_inputs",
)


def rag_ablation_cohort(cohort: Literal["B", "C"]) -> RAGAblationCohort:
    return RAGAblationCohort(cohort, cohort == "C", COSTS["retrieve_scientific_knowledge"], _SHARED)
