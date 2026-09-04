"""LangGraph orchestration for the v0.2.1 cognitive diagnosis loop."""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

from .experiment_tools import COSTS, ExperimentTools
from .graph_state import DiagnosisGraphState


def agreement(metrics: dict[str, Any]) -> float | None:
    value = metrics.get("agreement_valid", metrics.get("agreement"))
    return float(value) if value is not None else None


class DiagnosisGraph:
    """State transitions are auditable; model calls receive only public cognitive state."""
    def __init__(self, agent: Any, tools: ExperimentTools, run_dir: Path) -> None:
        self.agent, self.tools, self.run_dir = agent, tools, run_dir
        self.trace = run_dir / "trace.jsonl"
        self.checkpointer = InMemorySaver()
        graph = StateGraph(DiagnosisGraphState)
        for name, node in (("observe", self.observe), ("hypothesize", self.hypothesize), ("plan", self.plan), ("budget_check", self.budget_check), ("execute", self.execute), ("extract_evidence", self.extract_evidence), ("update_hypotheses", self.update_hypotheses), ("reflect", self.reflect), ("validation_gate", self.validation_gate), ("finalize", self.finalize)):
            graph.add_node(name, node)
        graph.add_edge(START, "observe")
        graph.add_edge("observe", "hypothesize")
        graph.add_edge("hypothesize", "plan")
        graph.add_edge("plan", "budget_check")
        graph.add_conditional_edges("budget_check", lambda s: "reflect" if s.get("budget_blocked") else "execute", {"reflect": "reflect", "execute": "execute"})
        graph.add_edge("execute", "extract_evidence")
        graph.add_edge("extract_evidence", "update_hypotheses")
        graph.add_edge("update_hypotheses", "reflect")
        graph.add_conditional_edges("reflect", lambda s: "plan" if s["diagnosis_status"] == "continue" else "validation_gate", {"plan": "plan", "validation_gate": "validation_gate"})
        graph.add_conditional_edges("validation_gate", lambda s: "finalize" if s["diagnosis_status"] in {"accepted_fault", "accepted_no_fault", "budget_exhausted"} else "plan", {"finalize": "finalize", "plan": "plan"})
        graph.add_edge("finalize", END)
        self.app = graph.compile(checkpointer=self.checkpointer)

    def log(self, node: str, **data: Any) -> None:
        self.trace.open("a").write(json.dumps({"node": node, "timestamp": time.time(), **data}) + "\n")

    @staticmethod
    def _context(s: DiagnosisGraphState) -> dict[str, Any]:
        return {"case_id": s["case_id"], "task": s["task"], "initial_observation": s["initial_observation"], "hypotheses": s.get("hypotheses", []), "evidence": s.get("evidence", []), "experiments": [{key: item.get(key) for key in ("experiment_id", "tool", "arguments", "cost", "result")} for item in s.get("experiments", [])], "budget_total": s["budget_total"], "budget_remaining": s["budget_remaining"], "tool_costs": COSTS, "quality_threshold": s["quality_threshold"], "steps_used": s["steps_used"], "max_steps": s["max_steps"]}

    def observe(self, s: DiagnosisGraphState) -> dict[str, Any]:
        self.log("observe", initial=s["initial_observation"])
        return {"diagnosis_status": "investigating"}

    def hypothesize(self, s: DiagnosisGraphState) -> dict[str, Any]:
        context = self._context(s)
        hypotheses = self.agent.generate_hypotheses(context) if not s.get("hypotheses") else s["hypotheses"]
        self.log("hypothesize", hypotheses=hypotheses)
        return {"hypotheses": hypotheses}

    def plan(self, s: DiagnosisGraphState) -> dict[str, Any]:
        plan = self.agent.plan_experiment(self._context(s))
        if "final" in plan:
            raise RuntimeError("planner may only return an experiment plan; final decisions require reflection and validation")
        plan_id = f"PLAN{len(s.get('experiments', [])) + 1:03d}"
        pipeline = plan.get("arguments", {}).get("pipeline", [])
        estimated = COSTS[plan["tool"]] + (len(pipeline) if plan["tool"] == "evaluate_candidate" else 0)
        plan = {"plan_id": plan_id, **plan, "estimated_cost": estimated}
        self.log("plan", selected_experiment=plan)
        return {"current_plan": plan}

    def budget_check(self, s: DiagnosisGraphState) -> dict[str, Any]:
        plan = s["current_plan"] or {}
        blocked = plan.get("estimated_cost", 0) > s["budget_remaining"] or s["steps_used"] >= s["max_steps"]
        self.log("budget_check", plan_id=plan.get("plan_id"), estimated_cost=plan.get("estimated_cost", 0), budget_remaining=s["budget_remaining"], blocked=blocked)
        return {"budget_blocked": blocked}

    def execute(self, s: DiagnosisGraphState) -> dict[str, Any]:
        plan = s["current_plan"] or {}
        record = self.tools.execute(plan["tool"], plan["arguments"])
        remaining = s["budget_remaining"] - record["cost"]
        if remaining < 0: raise RuntimeError("budget guard failed before remote execution")
        self.log("execute", plan_id=plan["plan_id"], experiment_id=record["experiment_id"], backend=record["backend"], remote_host=record["remote_host"], remote_pid=record["remote_pid"], result=record["result"])
        return {"experiments": s.get("experiments", []) + [record], "latest_result": record, "budget_remaining": remaining, "steps_used": s["steps_used"] + 1}

    def extract_evidence(self, s: DiagnosisGraphState) -> dict[str, Any]:
        record = s["latest_result"]
        metrics = record["result"].get("metrics", {})
        baseline = agreement(s["initial_observation"])
        observed = agreement(metrics)
        delta = observed - baseline if baseline is not None and observed is not None else None
        evidence_id = f"E{len(s.get('evidence', [])) + 1:03d}"
        residual = max(0.0, s["quality_threshold"] - observed) if observed is not None else None
        item = {"evidence_id": evidence_id, "experiment_id": record["experiment_id"], "baseline_metric": baseline, "observed_metric": observed, "delta": delta, "threshold": s["quality_threshold"], "residual_gap": residual, "valid_pixels": metrics.get("valid_pixels"), "valid_fraction": metrics.get("valid_fraction"), "interpretation": "Metric evidence pending hypothesis update.", "supports": [], "contradicts": []}
        self.log("extract_evidence", evidence=item)
        return {"evidence": s.get("evidence", []) + [item]}

    def update_hypotheses(self, s: DiagnosisGraphState) -> dict[str, Any]:
        context = self._context(s)
        context["latest_evidence"] = s["evidence"][-1]
        hypotheses = self.agent.update_hypotheses(context)
        self.log("update_hypotheses", evidence_id=context["latest_evidence"]["evidence_id"], hypotheses=hypotheses)
        return {"hypotheses": hypotheses}

    def reflect(self, s: DiagnosisGraphState) -> dict[str, Any]:
        best = max((item["observed_metric"] or 0.0 for item in s.get("evidence", [])), default=0.0)
        context = self._context(s)
        context.update({"best_metric": best, "budget_blocked": s.get("budget_blocked", False)})
        reflection = self.agent.reflect(context)
        decision = reflection["decision"]
        if s.get("budget_blocked") or s["budget_remaining"] <= 0 or s["steps_used"] >= s["max_steps"]:
            # A valid fault or a properly supported no-fault conclusion may still be
            # assessed by the gate at the limit.  An unsupported conclusion becomes
            # inconclusive rather than being silently accepted as no_fault.
            status = decision if decision == "propose_fault" or (decision == "propose_no_fault" and self._no_fault_supported(s)) else "budget_exhausted"
        else:
            status = decision
        self.log("reflect", reflection=reflection, best_metric=best, status=status)
        return {"reflection": reflection, "diagnosis_status": status, "budget_blocked": False}

    def validation_gate(self, s: DiagnosisGraphState) -> dict[str, Any]:
        best = max((item["observed_metric"] or 0.0 for item in s.get("evidence", [])), default=0.0)
        proposed = s["diagnosis_status"]
        initial_metric = agreement(s.get("initial_observation", {}))
        no_fault_supported = self._no_fault_supported(s)
        if proposed == "propose_fault":
            status = "accepted_fault" if best >= s["quality_threshold"] else "continue"
        elif proposed == "propose_no_fault":
            status = "accepted_no_fault" if no_fault_supported else "continue"
        else:
            status = "budget_exhausted"
        validated = {"accepted_fault": "fault", "accepted_no_fault": "no_fault", "budget_exhausted": "inconclusive"}.get(status)
        self.log("validation_gate", proposed=proposed, best_metric=best, initial_metric=initial_metric, no_fault_supported=no_fault_supported, accepted=status, validated_decision=validated)
        return {"diagnosis_status": status, "validated_decision": validated}

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
        context.update({"reflection": s.get("reflection"), "best_experiment": best, "allowed_evidence_ids": [item["experiment_id"] for item in experiments], "validated_decision": validated})
        if validated == "inconclusive":
            final = {"decision":"inconclusive","fault_family":None,"root_cause":"The available budget ended before either a fault repair or a scientifically supported no-fault conclusion was validated.","confidence":0.0,"evidence_experiment_ids":[item["experiment_id"] for item in experiments],"recommended_repair":{},"remaining_uncertainty":["Additional diagnostic experiments or explicit normal-range scientific evidence are required."]}
            self.log("finalize", final=final, validated_decision=validated)
            return {"final_diagnosis": final}
        final = self.agent.final_diagnosis(context)
        if final.get("decision") != validated:
            correction_context = {**context, "final_correction": f"validation gate requires decision={validated}; model returned decision={final.get('decision')!r}"}
            final = self.agent.final_diagnosis(correction_context)
        if final.get("decision") != validated:
            raise RuntimeError(f"finalizer decision conflicts with validation gate: required {validated!r}, received {final.get('decision')!r}")
        self.log("finalize", final=final, validated_decision=validated)
        return {"final_diagnosis": final}

    def run(self, state: DiagnosisGraphState) -> DiagnosisGraphState:
        return self.app.invoke(state, {"configurable": {"thread_id": state["run_id"]}})
