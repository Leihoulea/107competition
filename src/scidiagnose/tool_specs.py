"""The single, neutral catalog of planner-visible diagnostic actions."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal


@dataclass(frozen=True)
class ToolSpec:
    name: str
    category: Literal["compute_experiment", "knowledge_query"]
    cost: int
    arguments: dict[str, Any]


# Order intentionally preserves the pre-v0.3 compute action order.  Knowledge
# is an additional action category; it does not rank or privilege any transform.
TOOL_SPECS: dict[str, ToolSpec] = {
    "inspect": ToolSpec("inspect", "compute_experiment", 1, {}),
    "compare": ToolSpec("compare", "compute_experiment", 1, {}),
    "transform_and_compare": ToolSpec(
        "transform_and_compare", "compute_experiment", 4,
        {"operation": ["identity", "flip_x", "flip_y", "rot90", "rot180", "rot270", "transpose"]},
    ),
    "shift_and_compare": ToolSpec("shift_and_compare", "compute_experiment", 4, {"dr": "integer [-5, 5]", "dc": "integer [-5, 5]"}),
    "evaluate_candidate": ToolSpec("evaluate_candidate", "compute_experiment", 3, {"pipeline": "0 to 4 steps; each step is transform(operation) or shift(dr, dc)"}),
    "retrieve_scientific_knowledge": ToolSpec("retrieve_scientific_knowledge", "knowledge_query", 1, {"query": "non-empty scientific question", "top_k": "integer [1, 5]"}),
}

COSTS = {name: spec.cost for name, spec in TOOL_SPECS.items()}


def planner_tool_catalog(knowledge_enabled: bool = True) -> dict[str, dict[str, Any]]:
    return {
        name: {"category": spec.category, "cost": spec.cost, "arguments": spec.arguments}
        for name, spec in TOOL_SPECS.items()
        if knowledge_enabled or spec.category != "knowledge_query"
    }
