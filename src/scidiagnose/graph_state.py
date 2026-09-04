"""Explicit, auditable cognitive state for the v0.2.1 diagnosis graph."""
from __future__ import annotations

from typing import Any, Literal, TypedDict


class Hypothesis(TypedDict):
    hypothesis_id: str
    category: str
    description: str
    status: Literal["active", "supported", "weakened", "rejected", "validated"]
    confidence: float
    testable_scope: list[str]
    evidence_for: list[str]
    evidence_against: list[str]


class EvidenceItem(TypedDict):
    evidence_id: str
    experiment_id: str
    baseline_metric: float | None
    observed_metric: float | None
    delta: float | None
    threshold: float
    residual_gap: float | None
    valid_pixels: int | None
    valid_fraction: float | None
    interpretation: str
    supports: list[str]
    contradicts: list[str]
    tested_hypotheses: list[str]
    tested_scope: list[str]


class DiagnosisGraphState(TypedDict, total=False):
    run_id: str
    case_id: str
    task: dict[str, Any]
    initial_observation: dict[str, Any]
    hypotheses: list[Hypothesis]
    experiments: list[dict[str, Any]]
    # Planner-visible aggregate of what has been tested and how informative it was.
    experiment_coverage: dict[str, Any]
    evidence: list[EvidenceItem]
    current_plan: dict[str, Any] | None
    budget_blocked: bool
    latest_result: dict[str, Any] | None
    budget_total: int
    budget_remaining: int
    steps_used: int
    max_steps: int
    quality_threshold: float
    reflection: dict[str, Any] | None
    diagnosis_status: str
    validated_decision: Literal["fault", "no_fault", "inconclusive"] | None
    final_diagnosis: dict[str, Any] | None
    knowledge_queries: list[dict[str, Any]]
    knowledge_evidence: list[dict[str, Any]]
