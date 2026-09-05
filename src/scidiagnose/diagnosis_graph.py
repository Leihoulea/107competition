"""LangGraph orchestration for the v0.2.1 cognitive diagnosis loop."""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

from .agent import AgentAPIError
from .experiment_tools import ExperimentTools
from .graph_state import DiagnosisGraphState
from .knowledge.tool import ScientificKnowledgeTool
from .tool_specs import COSTS, TOOL_SPECS


def agreement(metrics: dict[str, Any]) -> float | None:
    value = metrics.get("agreement_valid", metrics.get("agreement"))
    return float(value) if value is not None else None


REPAIR_IMPROVEMENT_MARGIN = 1e-3


def _is_non_identity_repair(record: dict[str, Any]) -> bool:
    """Return whether a recorded experiment applied an actual repair candidate."""
    tool = record.get("tool")
    arguments = record.get("arguments", {})
    if tool == "transform_and_compare":
        return arguments.get("operation") != "identity"
    if tool == "shift_and_compare":
        return bool(arguments.get("dr") or arguments.get("dc"))
    if tool == "evaluate_candidate":
        return isinstance(arguments.get("pipeline"), list) and bool(arguments["pipeline"])
    return False


def _system_tested_scope(tool: str, arguments: dict[str, Any]) -> dict[str, Any]:
    """Derive the authoritative execution scope from the normalized action."""
    if tool == "shift_and_compare":
        return {"kind": "candidate", "signature": f"shift(dr={arguments.get('dr')},dc={arguments.get('dc')})"}
    if tool == "transform_and_compare":
        return {"kind": "candidate", "signature": f"transform({arguments.get('operation')})"}
    if tool == "evaluate_candidate":
        steps = []
        for step in arguments.get("pipeline", []):
            if step.get("type") == "transform":
                steps.append(f"transform({step.get('operation')})")
            elif step.get("type") == "shift":
                steps.append(f"shift(dr={step.get('dr')},dc={step.get('dc')})")
        return {"kind": "pipeline", "signature": steps}
    if tool == "retrieve_scientific_knowledge":
        return {"kind": "knowledge", "signature": str(arguments.get("query", ""))}
    return {"kind": "observation", "signature": tool}


def _scope_signature(scope: dict[str, Any]) -> str:
    value = scope.get("signature")
    return "|".join(value) if isinstance(value, list) else str(value)


def _hypothesis_scope_kind(hypothesis: dict[str, Any]) -> str:
    """Classify update semantics conservatively without symbolic reasoning."""
    explicit = hypothesis.get("scope_kind")
    if explicit in {"specific_candidate", "fault_family", "no_fault", "knowledge_claim"}:
        return explicit
    text = " ".join(str(value).lower() for value in (
        hypothesis.get("category", ""), hypothesis.get("description", ""), *hypothesis.get("testable_scope", [])
    ))
    if "knowledge" in text:
        return "knowledge_claim"
    if "no_fault" in text or "no fault" in text or "normal variation" in text:
        return "no_fault"
    if "transform(" in text or "shift(dr=" in text:
        return "specific_candidate"
    return "fault_family"


def _scope_compatible(hypothesis: dict[str, Any], scope: dict[str, Any]) -> bool:
    kind = _hypothesis_scope_kind(hypothesis)
    if kind == "knowledge_claim":
        return False
    if kind == "no_fault":
        return True
    if kind == "fault_family":
        return scope.get("kind") in {"candidate", "pipeline"}
    signature = _scope_signature(scope)
    declared = " ".join(str(value) for value in hypothesis.get("testable_scope", []))
    return signature in declared


def _scope(values: Any) -> list[str]:
    """Normalize the small, auditable vocabulary used for evidence coverage."""
    if not isinstance(values, list): values = [values]
    return list(dict.fromkeys(str(value) for value in values if str(value).strip()))


def _argument_distance(left: Any, right: Any) -> float:
    """A conservative structural distance for rejecting almost repeated probes."""
    if type(left) is not type(right): return 99.0
    if isinstance(left, dict):
        if set(left) != set(right): return 99.0
        return sum(_argument_distance(left[key], right[key]) for key in left)
    if isinstance(left, list):
        if len(left) != len(right): return 99.0
        return sum(_argument_distance(a, b) for a, b in zip(left, right))
    if isinstance(left, (int, float)) and not isinstance(left, bool): return min(abs(left - right), 2.0)
    return 0.0 if left == right else 2.0


def _signature(tool: Any, arguments: Any) -> str:
    return f"{tool}:{json.dumps(arguments if isinstance(arguments, dict) else {}, sort_keys=True, separators=(',', ':'))}"


def _normalized_knowledge_query(value: Any) -> str:
    return " ".join(str(value).lower().split())


class DiagnosisGraph:
    """State transitions are auditable; model calls receive only public cognitive state."""
    def __init__(self, agent: Any, tools: ExperimentTools, run_dir: Path, knowledge_tool: ScientificKnowledgeTool | None = None) -> None:
        self.agent, self.tools, self.run_dir, self.knowledge_tool = agent, tools, run_dir, knowledge_tool
        self.trace = run_dir / "trace.jsonl"
        self.checkpointer = InMemorySaver()
        graph = StateGraph(DiagnosisGraphState)
        for name, node in (("observe", self.observe), ("hypothesize", self.hypothesize), ("plan", self.plan), ("budget_check", self.budget_check), ("execute", self.execute), ("extract_evidence", self.extract_evidence), ("extract_knowledge_evidence", self.extract_knowledge_evidence), ("update_hypotheses", self.update_hypotheses), ("update_hypotheses_from_knowledge", self.update_hypotheses_from_knowledge), ("reflect", self.reflect), ("validation_gate", self.validation_gate), ("finalize", self.finalize)):
            graph.add_node(name, node)
        graph.add_edge(START, "observe")
        graph.add_edge("observe", "hypothesize")
        graph.add_edge("hypothesize", "plan")
        graph.add_edge("plan", "budget_check")
        graph.add_conditional_edges("budget_check", lambda s: "reflect" if s.get("budget_blocked") else "execute", {"reflect": "reflect", "execute": "execute"})
        graph.add_conditional_edges("execute", lambda s: "extract_knowledge_evidence" if s.get("latest_action_kind") == "knowledge_query" else "extract_evidence", {"extract_evidence": "extract_evidence", "extract_knowledge_evidence": "extract_knowledge_evidence"})
        graph.add_edge("extract_evidence", "update_hypotheses")
        graph.add_edge("extract_knowledge_evidence", "update_hypotheses_from_knowledge")
        graph.add_edge("update_hypotheses_from_knowledge", "reflect")
        graph.add_edge("update_hypotheses", "reflect")
        graph.add_conditional_edges("reflect", lambda s: "plan" if s["diagnosis_status"] == "continue" else "validation_gate", {"plan": "plan", "validation_gate": "validation_gate"})
        graph.add_conditional_edges("validation_gate", lambda s: "finalize" if s["diagnosis_status"] in {"accepted_fault", "accepted_no_fault", "max_steps_reached", "budget_exhausted", "no_affordable_novel_action", "provider_failure"} else "plan", {"finalize": "finalize", "plan": "plan"})
        graph.add_edge("finalize", END)
        self.app = graph.compile(checkpointer=self.checkpointer)

    def log(self, node: str, **data: Any) -> None:
        self.trace.open("a").write(json.dumps({"node": node, "timestamp": time.time(), **data}) + "\n")

    @staticmethod
    def _experiment_coverage(s: DiagnosisGraphState) -> dict[str, Any]:
        """Summarize executed probes without exposing any unexecuted candidate."""
        baseline = agreement(s.get("initial_observation", {}))
        families: dict[str, dict[str, Any]] = {}
        signatures: list[str] = []
        for record in s.get("experiments", []):
            family = str(record.get("family", record.get("tool", "unknown")))
            signature = _signature(record.get("tool"), record.get("arguments", {}))
            signatures.append(signature)
            summary = families.setdefault(family, {"count": 0, "best_delta": None, "low_information_count": 0, "informative_count": 0})
            summary["count"] += 1
            observed = agreement(record.get("result", {}).get("metrics", {}))
            delta = observed - baseline if observed is not None and baseline is not None else None
            if delta is None:
                continue
            summary["best_delta"] = delta if summary["best_delta"] is None else max(summary["best_delta"], delta)
            if abs(delta) < .01:
                summary["low_information_count"] += 1
            else:
                summary["informative_count"] += 1
        return {"tested_signatures": list(dict.fromkeys(signatures)), "families": families}

    def _context(self, s: DiagnosisGraphState) -> dict[str, Any]:
        coverage = s.get("experiment_coverage") or self._experiment_coverage(s)
        experimental = s.get("experimental_evidence", s.get("evidence", []))
        return {"case_id": s["case_id"], "task": s["task"], "initial_observation": s["initial_observation"], "hypotheses": s.get("hypotheses", []), "experimental_evidence": experimental, "knowledge_evidence": s.get("knowledge_evidence", []), "evidence": experimental, "experiments": [{key: item.get(key) for key in ("experiment_id", "tool", "arguments", "cost", "result")} for item in s.get("experiments", [])], "knowledge_queries": s.get("knowledge_queries", []), "experiment_coverage": coverage, "budget_total": s["budget_total"], "budget_remaining": s["budget_remaining"], "tool_costs": COSTS, "knowledge_enabled": bool(self.knowledge_tool) and bool(s.get("knowledge_enabled", False)), "quality_threshold": s["quality_threshold"], "steps_used": s["steps_used"], "max_steps": s["max_steps"]}

    def observe(self, s: DiagnosisGraphState) -> dict[str, Any]:
        self.log("observe", initial=s["initial_observation"])
        return {"diagnosis_status": "investigating"}

    def hypothesize(self, s: DiagnosisGraphState) -> dict[str, Any]:
        context = self._context(s)
        hypotheses = self.agent.generate_hypotheses(context) if not s.get("hypotheses") else s["hypotheses"]
        hypotheses = [
            {
                **item,
                "testable_scope": _scope(item.get("testable_scope", [item.get("category", "unspecified")])) or ["unspecified"],
                # Scope type controls deterministic evidence propagation.  It
                # is normalized once at the graph boundary, rather than being
                # trusted later as unconstrained model-authored prose.
                "scope_kind": _hypothesis_scope_kind(item),
            }
            for item in hypotheses
        ]
        self.log("hypothesize", hypotheses=hypotheses)
        return {"hypotheses": hypotheses}

    def plan(self, s: DiagnosisGraphState) -> dict[str, Any]:
        proposed = self.agent.plan_experiment(self._context(s))
        if "final" in proposed:
            raise RuntimeError("planner may only return an experiment plan; final decisions require reflection and validation")
        hypotheses = {item["hypothesis_id"]: item for item in s.get("hypotheses", [])}
        def select(value: dict[str, Any]) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
            if value.get("rejected_candidates"):
                self.log("plan_candidates_filtered", rejected_candidates=value["rejected_candidates"])
            candidates = value.get("candidate_plans") if isinstance(value.get("candidate_plans"), list) else [value]
            rejected: list[dict[str, Any]] = []
            for candidate in candidates[:3]:
                tool = str(candidate.get("tool", ""))
                if tool not in TOOL_SPECS or (TOOL_SPECS[tool].category == "knowledge_query" and not self._context(s)["knowledge_enabled"]):
                    rejected.append({"reason": "unsupported or disabled diagnostic action"}); continue
                targets = [item for item in candidate.get("target_hypotheses", []) if item in hypotheses]
                model_scope = _scope(candidate.get("tested_scope", []))
                system_scope = _system_tested_scope(tool, candidate.get("arguments", {}))
                # Model text may explain diagnostic intent, but the executed
                # action alone defines authoritative evidence provenance.
                covered = targets if targets and system_scope.get("signature") else []
                novelty = self._novelty(s, candidate)
                if covered and novelty["status"] == "novel":
                    return {
                        **candidate,
                        "target_hypotheses": covered,
                        "diagnostic_rationale": str(candidate.get("diagnostic_rationale", candidate.get("objective", ""))),
                        "predicted_observation": str(candidate.get("predicted_observation", candidate.get("expected_evidence", ""))),
                        "model_tested_scope": model_scope,
                        "system_tested_scope": system_scope,
                        "coverage": {"hypothesis_ids": covered, "system_tested_scope": system_scope, "novelty": novelty},
                    }, rejected
                rejected.append({"target_hypotheses": targets, "system_tested_scope": system_scope, "novelty": novelty, "reason": "no covered hypothesis" if not covered else "not novel"})
            return None, rejected

        plan, rejected = select(proposed)
        if plan is None:
            feedback = "proposed experiment too similar to previous low-information experiments; select materially different diagnostic experiment"
            self.log("plan_replan", rejected_candidates=rejected, planner_feedback=feedback)
            retry_context = {**self._context(s), "planner_feedback": feedback}
            proposed = self.agent.plan_experiment(retry_context)
            if "final" in proposed:
                raise RuntimeError("planner may only return an experiment plan; final decisions require reflection and validation")
            plan, retry_rejected = select(proposed)
            rejected += retry_rejected
        if plan is None:
            self.log("plan_rejected", candidates=rejected)
            return {"current_plan": None, "stop_reason": "no_affordable_novel_action"}
        plan_id = f"PLAN{len(s.get('experiments', [])) + len(s.get('knowledge_queries', [])) + 1:03d}"
        pipeline = plan.get("arguments", {}).get("pipeline", [])
        estimated = COSTS[plan["tool"]] + (len(pipeline) if plan["tool"] == "evaluate_candidate" else 0)
        plan = {"plan_id": plan_id, **plan, "estimated_cost": estimated}
        self.log("plan", selected_experiment=plan)
        return {"current_plan": plan}

    @staticmethod
    def _novelty(s: DiagnosisGraphState, candidate: dict[str, Any]) -> dict[str, Any]:
        if candidate.get("tool") == "retrieve_scientific_knowledge":
            query = _normalized_knowledge_query(candidate.get("arguments", {}).get("query", ""))
            for previous in s.get("knowledge_queries", []):
                if _normalized_knowledge_query(previous.get("query", "")) == query:
                    return {"status": "duplicate", "query_id": previous.get("query_id"), "query": query}
            return {"status": "novel"}
        coverage = s.get("experiment_coverage") or DiagnosisGraph._experiment_coverage(s)
        family = str(candidate.get("family", candidate.get("tool", "unknown")))
        family_coverage = coverage.get("families", {}).get(family, {})
        stagnated = family_coverage.get("count", 0) >= 2 and family_coverage.get("low_information_count", 0) >= 2
        for previous in s.get("experiments", []):
            if previous.get("tool") != candidate.get("tool"): continue
            distance = _argument_distance(previous.get("arguments", {}), candidate.get("arguments", {}))
            if distance == 0:
                return {"status": "duplicate", "experiment_id": previous.get("experiment_id"), "distance": distance}
            if distance <= 1 and stagnated:
                return {"status": "near_duplicate", "experiment_id": previous.get("experiment_id"), "distance": distance, "family": family}
        return {"status": "novel"}

    def budget_check(self, s: DiagnosisGraphState) -> dict[str, Any]:
        plan = s["current_plan"] or {}
        if s.get("stop_reason"):
            reason = s["stop_reason"]
        elif s["steps_used"] >= s["max_steps"]:
            reason = "max_steps_reached"
        elif plan.get("estimated_cost", 0) > s["budget_remaining"]:
            reason = "budget_exhausted"
        else:
            reason = None
        self.log("budget_check", plan_id=plan.get("plan_id"), estimated_cost=plan.get("estimated_cost", 0), budget_remaining=s["budget_remaining"], blocked=reason is not None, stop_reason=reason)
        return {"budget_blocked": reason is not None, "stop_reason": reason}

    def execute(self, s: DiagnosisGraphState) -> dict[str, Any]:
        plan = s["current_plan"] or {}
        if plan.get("tool") == "retrieve_scientific_knowledge":
            if self.knowledge_tool is None:
                raise RuntimeError("knowledge action selected while knowledge retrieval is disabled")
            record = self.knowledge_tool.execute(plan["arguments"])
            remaining = s["budget_remaining"] - record["cost"]
            query = {
                "query_id": f"Q{len(s.get('knowledge_queries', [])) + 1:03d}", "plan_id": plan["plan_id"],
                "target_hypotheses": list(plan.get("target_hypotheses", [])),
                "diagnostic_rationale": plan.get("diagnostic_rationale", ""),
                "predicted_observation": plan.get("predicted_observation", ""),
                **record,
            }
            self.log("execute_knowledge", plan_id=plan["plan_id"], query=query)
            return {"knowledge_queries": s.get("knowledge_queries", []) + [query], "latest_result": query, "latest_action_kind": "knowledge_query", "budget_remaining": remaining, "steps_used": s["steps_used"] + 1}
        record = self.tools.execute(plan["tool"], plan["arguments"])
        remaining = s["budget_remaining"] - record["cost"]
        if remaining < 0: raise RuntimeError("budget guard failed before remote execution")
        self.log("execute", plan_id=plan["plan_id"], experiment_id=record["experiment_id"], tool=record["tool"], arguments=record["arguments"], cost=record["cost"], backend=record["backend"], remote_host=record["remote_host"], remote_pid=record["remote_pid"], compute_observation=record.get("compute_observation"), result=record["result"])
        record = {
            **record,
            "plan_id": plan["plan_id"],
            "coverage": plan.get("coverage", {}),
            "diagnostic_rationale": plan.get("diagnostic_rationale", ""),
            "predicted_observation": plan.get("predicted_observation", ""),
        }
        experiments = s.get("experiments", []) + [record]
        experiment_coverage = self._experiment_coverage({**s, "experiments": experiments})
        return {"experiments": experiments, "latest_result": record, "latest_action_kind": "compute_experiment", "experiment_coverage": experiment_coverage, "budget_remaining": remaining, "steps_used": s["steps_used"] + 1}

    def extract_evidence(self, s: DiagnosisGraphState) -> dict[str, Any]:
        record = s["latest_result"]
        metrics = record["result"].get("metrics", {})
        baseline = agreement(s["initial_observation"])
        observed = agreement(metrics)
        delta = observed - baseline if baseline is not None and observed is not None else None
        evidence_id = f"E{len(s.get('evidence', [])) + 1:03d}"
        residual = max(0.0, s["quality_threshold"] - observed) if observed is not None else None
        coverage = record.get("coverage", {})
        # Direct callers from the pre-policy API have no plan record.  Treat
        # those legacy records as broad observations so they retain their old,
        # explicitly all-hypothesis update behaviour.
        tested_hypotheses = list(coverage.get("hypothesis_ids", [])) or [item["hypothesis_id"] for item in s.get("hypotheses", [])]
        system_scope = _system_tested_scope(record.get("tool", ""), record.get("arguments", {}))
        item = {"evidence_id": evidence_id, "experiment_id": record["experiment_id"], "baseline_metric": baseline, "observed_metric": observed, "delta": delta, "threshold": s["quality_threshold"], "residual_gap": residual, "valid_pixels": metrics.get("valid_pixels"), "valid_fraction": metrics.get("valid_fraction"), "interpretation": "Metric evidence pending hypothesis update.", "supports": [], "contradicts": [], "tested_hypotheses": tested_hypotheses, "system_tested_scope": system_scope, "diagnostic_rationale": record.get("diagnostic_rationale", ""), "predicted_observation": record.get("predicted_observation", "")}
        self.log("extract_evidence", evidence=item)
        experimental = s.get("evidence", []) + [item]
        return {"evidence": experimental, "experimental_evidence": experimental}

    def extract_knowledge_evidence(self, s: DiagnosisGraphState) -> dict[str, Any]:
        query = s.get("latest_result") or {}
        evidence = list(s.get("knowledge_evidence", []))
        for hit in query.get("hits", []):
            evidence.append({
                "evidence_id": f"K{len(evidence) + 1:03d}", "kind": "knowledge",
                "query_id": query.get("query_id"),
                "source": {key: hit.get(key) for key in ("source_id", "title", "authority", "version", "section", "page", "chunk_id")},
                "claim": f"Retrieved documentary material relevant to: {query.get('query', '')}",
                "supports_hypotheses": [], "contradicts_hypotheses": [], "validated": False,
                "excerpt": hit.get("excerpt", ""), "retrieval_score": hit.get("retrieval_score"),
                "target_hypotheses": list(query.get("target_hypotheses", [])),
            })
        self.log("extract_knowledge_evidence", query_id=query.get("query_id"), evidence=evidence[len(s.get("knowledge_evidence", [])):])
        return {"knowledge_evidence": evidence}

    def update_hypotheses_from_knowledge(self, s: DiagnosisGraphState) -> dict[str, Any]:
        query = s.get("latest_result") or {}
        targets = set(query.get("target_hypotheses", []))
        new_evidence = [item for item in s.get("knowledge_evidence", []) if item.get("query_id") == query.get("query_id")]
        evidence_ids = {item.get("evidence_id") for item in new_evidence if item.get("evidence_id")}
        if not targets or not evidence_ids or not hasattr(self.agent, "update_hypotheses_from_knowledge"):
            return {}
        context = self._context(s)
        context.update({"latest_knowledge_evidence": new_evidence, "knowledge_evidence_ids": sorted(evidence_ids), "knowledge_target_hypothesis_ids": sorted(targets)})
        returned = self.agent.update_hypotheses_from_knowledge(context)
        if isinstance(returned, list):
            returned = {"hypotheses": returned, "evidence_interpretations": []}
        proposed = {item.get("hypothesis_id"): item for item in returned.get("hypotheses", []) if isinstance(item, dict)} if isinstance(returned, dict) else {}
        hypotheses = []
        for old in s.get("hypotheses", []):
            update = proposed.get(old["hypothesis_id"])
            if old["hypothesis_id"] not in targets or not update:
                hypotheses.append(old); continue
            cited = set(update.get("evidence_for", [])) | set(update.get("evidence_against", []))
            if not (cited & evidence_ids):
                hypotheses.append(old); continue
            hypotheses.append({**update, "hypothesis_id": old["hypothesis_id"], "testable_scope": old.get("testable_scope", []), "scope_kind": old.get("scope_kind", _hypothesis_scope_kind(old))})
        by_id = {item["hypothesis_id"]: item for item in hypotheses}
        interpretations = {item.get("evidence_id"): item for item in returned.get("evidence_interpretations", []) if isinstance(item, dict)} if isinstance(returned, dict) else {}
        knowledge = []
        for item in s.get("knowledge_evidence", []):
            interpretation = interpretations.get(item.get("evidence_id"), {})
            supports = [hid for hid in interpretation.get("supports_hypotheses", []) if hid in targets and item.get("evidence_id") in by_id.get(hid, {}).get("evidence_for", [])]
            contradicts = [hid for hid in interpretation.get("contradicts_hypotheses", []) if hid in targets and item.get("evidence_id") in by_id.get(hid, {}).get("evidence_against", [])]
            claim = str(interpretation.get("claim", "")).strip() or item.get("claim", "")
            knowledge.append({**item, "claim": claim, "supports_hypotheses": supports, "contradicts_hypotheses": contradicts})
        self.log("update_hypotheses_from_knowledge", query_id=query.get("query_id"), target_hypotheses=sorted(targets), knowledge_evidence_ids=sorted(evidence_ids), hypotheses=hypotheses)
        return {"hypotheses": hypotheses, "knowledge_evidence": knowledge}

    def update_hypotheses(self, s: DiagnosisGraphState) -> dict[str, Any]:
        context = self._context(s)
        context["latest_evidence"] = s["evidence"][-1]
        system_scope = context["latest_evidence"].get("system_tested_scope", {})
        allowed = {
            item["hypothesis_id"] for item in s.get("hypotheses", [])
            if item["hypothesis_id"] in set(context["latest_evidence"].get("tested_hypotheses", []))
            and _scope_compatible(item, system_scope)
        }
        context["scope_hypothesis_ids"] = sorted(allowed)
        returned = {item["hypothesis_id"]: item for item in self.agent.update_hypotheses(context) if item.get("hypothesis_id") in allowed}
        latest = context["latest_evidence"]
        material_improvement = (latest.get("delta") or 0.0) >= REPAIR_IMPROVEMENT_MARGIN
        validated_repairs = set(self._validated_repairs(s))
        hypotheses = []
        for old in s.get("hypotheses", []):
            update = returned.get(old["hypothesis_id"])
            scope_kind = _hypothesis_scope_kind(old)
            if scope_kind == "knowledge_claim":
                hypotheses.append(old)
            elif scope_kind == "no_fault":
                if validated_repairs:
                    evidence_against = list(dict.fromkeys(old.get("evidence_against", []) + [latest["evidence_id"]]))
                    hypotheses.append({**old, "status": "weakened", "confidence": min(float(old.get("confidence", .5)), .1), "evidence_against": evidence_against})
                else:
                    # Failed or unnecessary repair probes never count against a
                    # valid no-fault explanation.
                    hypotheses.append(old)
            elif scope_kind == "fault_family" and not material_improvement:
                # One failed candidate cannot reject its broader family.
                hypotheses.append(old)
            elif update:
                hypotheses.append({**update, "testable_scope": old.get("testable_scope", []), "scope_kind": old.get("scope_kind", scope_kind)})
            else:
                hypotheses.append(old)
        latest = dict(latest)
        latest["supports"] = [item["hypothesis_id"] for item in hypotheses if item["hypothesis_id"] in allowed and latest["evidence_id"] in item.get("evidence_for", [])]
        latest["contradicts"] = [item["hypothesis_id"] for item in hypotheses if item["hypothesis_id"] in allowed and latest["evidence_id"] in item.get("evidence_against", [])]
        evidence = s["evidence"][:-1] + [latest]
        self.log("update_hypotheses", evidence_id=context["latest_evidence"]["evidence_id"], hypotheses=hypotheses)
        return {"hypotheses": hypotheses, "evidence": evidence}

    def reflect(self, s: DiagnosisGraphState) -> dict[str, Any]:
        best = max((item["observed_metric"] or 0.0 for item in s.get("evidence", [])), default=0.0)
        context = self._context(s)
        context.update({"best_metric": best, "budget_blocked": s.get("budget_blocked", False)})
        reflection = self.agent.reflect(context)
        decision = reflection["decision"]
        # A clean initial observation is already an explicit no-fault evidence
        # contract for the current benchmark.  Do not keep consuming budget when
        # the model merely continues despite having no validated repair evidence.
        if decision == "continue" and self._no_fault_supported(s) and not self._validated_repairs(s):
            decision = "propose_no_fault"
            reflection = {
                **reflection,
                "decision": decision,
                "summary": f"{reflection.get('summary', '')} Initial quality already satisfies the no-fault evidence contract.",
            }
        stop_reason = s.get("stop_reason")
        if stop_reason is None and s["steps_used"] >= s["max_steps"]:
            stop_reason = "max_steps_reached"
        elif stop_reason is None and s["budget_remaining"] <= 0:
            stop_reason = "budget_exhausted"
        if stop_reason:
            # A valid fault or a properly supported no-fault conclusion may still be
            # assessed by the gate at the limit.  An unsupported conclusion becomes
            # inconclusive rather than being silently accepted as no_fault.
            status = decision if decision == "propose_fault" or (decision == "propose_no_fault" and self._no_fault_supported(s)) else stop_reason
        else:
            status = decision
        self.log("reflect", reflection=reflection, best_metric=best, status=status)
        return {"reflection": reflection, "diagnosis_status": status, "budget_blocked": False, "stop_reason": stop_reason}

    def validation_gate(self, s: DiagnosisGraphState) -> dict[str, Any]:
        best = max((item["observed_metric"] or 0.0 for item in s.get("evidence", [])), default=0.0)
        proposed = s["diagnosis_status"]
        initial_metric = agreement(s.get("initial_observation", {}))
        no_fault_supported = self._no_fault_supported(s)
        validated_repairs = self._validated_repairs(s)
        if proposed == "propose_fault":
            status = "accepted_fault" if validated_repairs else "continue"
        elif proposed == "propose_no_fault":
            status = "accepted_no_fault" if no_fault_supported else "continue"
        elif proposed in {"max_steps_reached", "budget_exhausted", "no_affordable_novel_action", "provider_failure"}:
            status = proposed
        else:
            status = "continue"
        validated = {"accepted_fault": "fault", "accepted_no_fault": "no_fault"}.get(status)
        if status in {"max_steps_reached", "budget_exhausted", "no_affordable_novel_action", "provider_failure"}:
            validated = "inconclusive"
        self.log("validation_gate", proposed=proposed, best_metric=best, initial_metric=initial_metric, no_fault_supported=no_fault_supported, validated_repair_experiment_ids=validated_repairs, accepted=status, validated_decision=validated, stop_reason=s.get("stop_reason"))
        return {"diagnosis_status": status, "validated_decision": validated}

    def _validated_repairs(self, s: DiagnosisGraphState) -> list[str]:
        """Require a real, materially improving repair before accepting fault."""
        initial = agreement(s.get("initial_observation", {}))
        threshold = s.get("quality_threshold")
        if initial is None or threshold is None or initial >= threshold:
            return []
        validated = []
        for record in s.get("experiments", []):
            observed = agreement(record.get("result", {}).get("metrics", {}))
            if (
                _is_non_identity_repair(record)
                and observed is not None
                and observed >= threshold
                and observed - initial >= REPAIR_IMPROVEMENT_MARGIN
            ):
                validated.append(record.get("experiment_id"))
        return [item for item in validated if isinstance(item, str)]

    @staticmethod
    def _no_fault_supported(s: DiagnosisGraphState) -> bool:
        """Require a clean initial result or explicitly validated normal-range evidence."""
        initial_metric = agreement(s.get("initial_observation", {}))
        if initial_metric is not None and initial_metric >= s["quality_threshold"]:
            return True
        return any(
            isinstance(item, dict)
            and item.get("kind") == "scientific_normal_range"
            and item.get("validated") is True
            for item in s.get("knowledge_evidence", [])
        )

    def finalize(self, s: DiagnosisGraphState) -> dict[str, Any]:
        experiments = s.get("experiments", [])
        best = max(experiments, key=lambda item: agreement(item.get("result", {}).get("metrics", {})) or 0.0, default=None)
        context = self._context(s)
        validated = s.get("validated_decision")
        if validated not in {"fault", "no_fault", "inconclusive"}:
            raise RuntimeError("finalize requires a validated_decision from validation_gate")
        context.update({"reflection": s.get("reflection"), "best_experiment": best, "allowed_evidence_ids": [item["experiment_id"] for item in experiments], "allowed_knowledge_evidence_ids": [item["evidence_id"] for item in s.get("knowledge_evidence", [])], "validated_decision": validated})
        if validated == "inconclusive":
            stop_reason = s.get("stop_reason", "no_affordable_novel_action")
            explanations = {
                "max_steps_reached": "The maximum diagnostic step limit was reached before either a fault repair or a scientifically supported no-fault conclusion was validated.",
                "budget_exhausted": "The available diagnostic budget was exhausted before either a fault repair or a scientifically supported no-fault conclusion was validated.",
                "no_affordable_novel_action": "No affordable novel diagnostic action remained before either a fault repair or a scientifically supported no-fault conclusion was validated.",
                "provider_failure": "The model provider failed before either a fault repair or a scientifically supported no-fault conclusion was validated.",
            }
            final = {"decision":"inconclusive","fault_family":None,"root_cause":explanations[stop_reason],"confidence":0.0,"evidence_experiment_ids":[item["experiment_id"] for item in experiments],"recommended_repair":{},"remaining_uncertainty":["Additional diagnostic experiments or explicit normal-range scientific evidence are required."], "stop_reason": stop_reason}
            self.log("finalize", final=final, validated_decision=validated)
            final["evidence_summary"] = {"experimental_evidence_ids": [item["evidence_id"] for item in s.get("experimental_evidence", s.get("evidence", []))], "knowledge_evidence_ids": [item["evidence_id"] for item in s.get("knowledge_evidence", [])], "final_inference": final["root_cause"]}
            return {"final_diagnosis": final}
        final = self.agent.final_diagnosis(context)
        if final.get("decision") != validated:
            correction_context = {**context, "final_correction": f"validation gate requires decision={validated}; model returned decision={final.get('decision')!r}"}
            final = self.agent.final_diagnosis(correction_context)
        if final.get("decision") != validated:
            raise RuntimeError(f"finalizer decision conflicts with validation gate: required {validated!r}, received {final.get('decision')!r}")
        if validated == "no_fault":
            # Use one canonical evaluator-facing representation for an accepted
            # abstention; a no-fault conclusion cannot carry a repair candidate.
            # With no knowledge-evidence channel enabled, the only generic
            # positive no-fault evidence is the validated initial threshold.
            # Do not let a prose finalizer turn untested alternatives into a
            # broader negative scientific claim.
            initial_metric = agreement(s.get("initial_observation", {}))
            final = {
                **final,
                "fault_family": "no_fault",
                "root_cause": (
                    f"The initial observed agreement ({initial_metric}) meets or exceeds the "
                    f"quality threshold ({s['quality_threshold']}); the validation gate accepted no_fault. "
                    "No untested fault family is ruled out by this conclusion."
                ),
                "recommended_repair": {},
            }
        final["evidence_summary"] = {"experimental_evidence_ids": [item["evidence_id"] for item in s.get("experimental_evidence", s.get("evidence", []))], "knowledge_evidence_ids": [item["evidence_id"] for item in s.get("knowledge_evidence", [])], "final_inference": final.get("root_cause", "")}
        self.log("finalize", final=final, validated_decision=validated)
        return {"final_diagnosis": final}

    def run(self, state: DiagnosisGraphState) -> DiagnosisGraphState:
        try:
            return self.app.invoke(state, {"configurable": {"thread_id": state["run_id"]}})
        except AgentAPIError as exc:
            self.log("provider_failure", stop_reason="provider_failure", error=str(exc))
            raise
