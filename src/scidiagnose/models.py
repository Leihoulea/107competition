"""Small dependency-free domain models."""
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from typing import Any, Literal
@dataclass
class ExperimentRequest:
    experiment_id: str; tool: Literal["inspect","compare","transform_and_compare","shift_and_compare"]; arguments: dict[str,Any]=field(default_factory=dict)
    def to_dict(self) -> dict[str,Any]: return asdict(self)
@dataclass
class ExperimentResult:
    experiment_id: str; tool: str; job_id: str; backend: str; cost: int; result: dict[str,Any]
@dataclass
class FinalDiagnosis:
    decision: Literal["fault","no_fault"]; fault_family: str; root_cause: str; confidence: float; evidence_experiment_ids: list[str]; recommended_repair: dict[str,Any]
@dataclass
class DiagnosisState:
    case_id: str; budget_total: int; budget_remaining: int; observations: list[dict[str,Any]]=field(default_factory=list); experiments: list[dict[str,Any]]=field(default_factory=list); final_diagnosis: dict[str,Any] | None=None
@dataclass
class AgentAction:
    type: Literal["tool_call","final"]; tool: str | None=None; arguments: dict[str,Any]=field(default_factory=dict); reason: str=""; final: dict[str,Any] | None=None
