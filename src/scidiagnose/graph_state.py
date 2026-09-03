"""Explicit, auditable state for the v0.2 diagnosis graph."""
from __future__ import annotations
from typing import Any, TypedDict
class Hypothesis(TypedDict):
    hypothesis_id:str;description:str;category:str;status:str;confidence:float;evidence_for:list[str];evidence_against:list[str]
class EvidenceItem(TypedDict):
    evidence_id:str;experiment_id:str;statement:str;metrics:dict[str,Any];supports:list[str];contradicts:list[str]
class DiagnosisGraphState(TypedDict, total=False):
    run_id:str;case_id:str;task:dict[str,Any];initial_observation:dict[str,Any];hypotheses:list[Hypothesis];experiments:list[dict[str,Any]];evidence:list[EvidenceItem];current_plan:dict[str,Any]|None;latest_result:dict[str,Any]|None;budget_total:int;budget_remaining:int;steps_used:int;max_steps:int;quality_threshold:float;diagnosis_status:str;final_diagnosis:dict[str,Any]|None;knowledge_queries:list[dict[str,Any]];knowledge_evidence:list[dict[str,Any]]
