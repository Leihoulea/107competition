"""Provider-independent agents; no hidden case data is read here."""
from __future__ import annotations
import json
import time
from typing import Any
from urllib import error, request
from .config import Settings
from .models import AgentAction, DiagnosisState
from .tool_specs import TOOL_SPECS, planner_tool_catalog

SYSTEM_PROMPT = """You are an autonomous scientific computing diagnosis agent.

A computation may finish successfully while still containing a scientific silent failure.
Maintain multiple plausible explanations whenever the current evidence is ambiguous.
Use real computational experiments to distinguish competing hypotheses.
Choose experiments based on their expected diagnostic value, prior evidence, and computational cost.
After every executed experiment, reassess the hypotheses.
A partial improvement is evidence, but it does not necessarily identify the complete root cause.
An experiment directly tests only its stated candidate; do not generalize one inconclusive result
to a broader explanation without supporting evidence. Prefer a materially different experiment
over a near-duplicate when prior results have low diagnostic value.
Do not assume that every anomaly implies a fault. A scientifically valid conclusion may be no_fault.
Never claim an experiment, metric, document, or evidence item that is not present in the provided state.
Only use evidence produced by executed experiments. Do not expose hidden reasoning.
Return only concise structured scientific state updates or requested actions, matching the supplied schema."""

PLANNER_TOOL_CATALOG = planner_tool_catalog()

class AgentAPIError(RuntimeError): pass
class StructuredOutputError(AgentAPIError): pass

class OpenAICompatibleAgent:
    """Minimal stdlib client for school endpoints implementing /chat/completions."""
    def __init__(self, settings: Settings | None = None, timeout: int = 60, max_retries: int | None = None) -> None:
        self.settings=settings or Settings(); self.timeout=timeout
        self.max_retries=int(getattr(self.settings, "api_max_retries", 2) if max_retries is None else max_retries)
        self.retry_base_seconds=float(getattr(self.settings, "api_retry_base_seconds", 1))
        if not (self.settings.base_url and self.settings.model_name and self.settings.api_key):
            raise AgentAPIError("SCIDIAG_BASE_URL, SCIDIAG_MODEL_NAME, and SCIDIAG_API_KEY are required for API mode")

    @staticmethod
    def _unwrap_structured_response(value: Any) -> dict[str, Any]:
        """Accept only explicit, provider-standard object envelopes."""
        if not isinstance(value, dict):
            raise StructuredOutputError("response must be a JSON object")
        if value.get("type") == "json_object":
            for key in ("obj", "data", "result", "response"):
                if isinstance(value.get(key), dict):
                    return value[key]
        # Some compatible gateways use a single named payload wrapper.  Do not
        # recursively unwrap arbitrary objects: that would hide schema errors.
        if set(value) == {"output"} and isinstance(value["output"], dict):
            return value["output"]
        return value

    def _request_json(self, request_name: str, context: dict[str, Any], response_schema: dict[str, Any]) -> dict[str, Any]:
        """Send a concise structured cognitive request; hidden case files never enter context."""
        visible = {"request": request_name, "context": context, "response_schema": response_schema}
        payload={"model":self.settings.model_name,"messages":[{"role":"system","content":SYSTEM_PROMPT},{"role":"user","content":json.dumps(visible)}],"temperature":0,"response_format":{"type":"json_object"}}
        url=self.settings.base_url.rstrip("/")+"/chat/completions"; body=json.dumps(payload).encode(); req=request.Request(url,body,headers={"Authorization":f"Bearer {self.settings.api_key}","Content-Type":"application/json"},method="POST")
        for attempt in range(self.max_retries + 1):
            try:
                with request.urlopen(req,timeout=self.timeout) as response: data=json.loads(response.read())
                raw=data["choices"][0]["message"]["content"]
                value=self._unwrap_structured_response(json.loads(raw))
                return value
            except error.HTTPError as exc:
                if exc.code in {429,500,502,503,504} and attempt < self.max_retries:
                    time.sleep(self.retry_base_seconds * (2 ** attempt)); continue
                raise AgentAPIError(f"School LLM API request failed: {exc}") from exc
            except OSError as exc:
                if attempt < self.max_retries:
                    time.sleep(self.retry_base_seconds * (2 ** attempt)); continue
                raise AgentAPIError(f"School LLM API transport failed: {exc}") from exc
            except (error.URLError,json.JSONDecodeError,KeyError,IndexError,TypeError,ValueError,StructuredOutputError) as exc:
                if attempt < self.max_retries:
                    time.sleep(self.retry_base_seconds * (2 ** attempt)); continue
                raise StructuredOutputError(f"School LLM API returned invalid structured output after {attempt + 1} attempts: {exc}") from exc

    @staticmethod
    def _hypotheses(value: dict[str, Any], existing: list[dict[str, Any]] | None = None, minimum: int = 2) -> list[dict[str, Any]]:
        raw=value.get("hypotheses")
        if not isinstance(raw,list) or not minimum <= len(raw) <= 5: raise AgentAPIError(f"model must provide {minimum} to 5 hypotheses")
        prior={item["hypothesis_id"] for item in existing or []}; result=[]
        for index,item in enumerate(raw,1):
            if not isinstance(item,dict): raise AgentAPIError("hypothesis must be an object")
            hypothesis_id=str(item.get("hypothesis_id") or (f"H{index:03d}" if not prior else next(iter(prior))))
            status=item.get("status","active")
            if status not in {"active","supported","weakened","rejected","validated"}: status="active"
            scope=item.get("testable_scope", [str(item.get("category", "unspecified"))])
            if not isinstance(scope, list): scope=[scope]
            scope=[str(x) for x in scope if str(x).strip()] or ["unspecified"]
            scope_kind = item.get("scope_kind") if item.get("scope_kind") in {"specific_candidate", "fault_family", "no_fault", "knowledge_claim"} else None
            normalized={"hypothesis_id":hypothesis_id,"category":str(item.get("category","unspecified")),"description":str(item.get("description","Plausible explanation requiring evidence.")),"status":status,"confidence":max(0.0,min(1.0,float(item.get("confidence",.5)))),"testable_scope":scope,"evidence_for":[str(x) for x in item.get("evidence_for",[])],"evidence_against":[str(x) for x in item.get("evidence_against",[])]}
            if scope_kind: normalized["scope_kind"] = scope_kind
            result.append(normalized)
        return result

    def generate_hypotheses(self, context: dict[str, Any]) -> list[dict[str, Any]]:
        schema={"hypotheses":[{"hypothesis_id":"H001","category":"short label","description":"concise explanation","scope_kind":"specific_candidate|fault_family|no_fault|knowledge_claim","testable_scope":["named measurable condition"],"status":"active","confidence":0.5,"evidence_for":[],"evidence_against":[]}]}
        return self._hypotheses(self._request_json("generate competing hypotheses",context,schema))

    def update_hypotheses(self, context: dict[str, Any]) -> list[dict[str, Any]]:
        schema={"hypotheses":[{"hypothesis_id":"existing ID","category":"short label","description":"concise explanation","scope_kind":"preserve existing value","testable_scope":["preserve existing scope"],"status":"supported|weakened|rejected|validated|active","confidence":0.5,"evidence_for":["E001"],"evidence_against":[]}]}
        existing=context.get("hypotheses",[]); updates=self._hypotheses(self._request_json("update only hypotheses covered by the latest experiment. Preserve every uncovered hypothesis exactly; link changes to the supplied evidence.",context,schema), existing, minimum=1)
        allowed=set(context.get("scope_hypothesis_ids", []))
        if allowed: updates=[item for item in updates if item["hypothesis_id"] in allowed]
        by_id={item["hypothesis_id"]:item for item in updates}
        return [by_id.get(item["hypothesis_id"],item) for item in existing] + [item for item in updates if item["hypothesis_id"] not in {old["hypothesis_id"] for old in existing}]

    def plan_experiment(self, context: dict[str, Any]) -> dict[str, Any]:
        schema={"candidates":[{"objective":"distinguish named hypotheses","target_hypotheses":["H001"],"diagnostic_rationale":"why the action is useful","predicted_observation":"expected measurable outcome","experiment":{"tool":"one supported tool name","arguments":{}}}]}
        def parse(value: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
            raw=value.get("candidates")
            if not isinstance(raw, list):
                experiment=value.get("experiment")
                raw=[{**value, **experiment}] if isinstance(experiment, dict) else [value]
            valid={item["hypothesis_id"] for item in context["hypotheses"]}; candidates=[]; rejected=[]
            for index, candidate in enumerate(raw[:3], 1):
                if not isinstance(candidate, dict):
                    rejected.append({"rank": index, "reason": "candidate must be an object"}); continue
                experiment=candidate.get("experiment", candidate)
                try:
                    action=self._validate({"type":"tool_call","tool":experiment.get("tool"),"arguments":experiment.get("arguments",{}),"reason":candidate.get("objective",candidate.get("reason",""))})
                except (AttributeError, ValueError) as exc:
                    rejected.append({"rank": index, "reason": str(exc)}); continue
                targets=[item for item in candidate.get("target_hypotheses",[]) if item in valid] or list(valid)
                scope=candidate.get("tested_scope", [])
                if not isinstance(scope, list): scope=[scope]
                candidates.append({"objective":str(candidate.get("objective",action.reason)),"diagnostic_rationale":str(candidate.get("diagnostic_rationale",candidate.get("objective",action.reason))),"predicted_observation":str(candidate.get("predicted_observation",candidate.get("expected_evidence","Measure evidence that distinguishes the target hypotheses."))),"target_hypotheses":targets,"tested_scope":[str(x) for x in scope if str(x).strip()],"tool":action.tool,"arguments":action.arguments,"expected_evidence":str(candidate.get("expected_evidence","Measure evidence that distinguishes the target hypotheses."))})
            return candidates, rejected

        planner_context={**context, "tool_catalog": planner_tool_catalog(bool(context.get("knowledge_enabled", False)))}
        value=self._request_json("propose two or three ranked, cost-aware experiment candidates. Each must use the supplied neutral tool catalog, cover named hypotheses, and state a measurable scope. Avoid candidates equivalent or near-equivalent to executed experiments.",planner_context,schema)
        candidates, rejected=parse(value)
        if not candidates:
            correction={**planner_context, "planner_correction": {"rejected_candidates": rejected}}
            value=self._request_json("Correct the planner response once. Every candidate must contain one supported experiment contract with valid arguments; omit any candidate that cannot meet that contract.",correction,schema)
            candidates, retry_rejected=parse(value)
            rejected += retry_rejected
            if not candidates:
                raise AgentAPIError(f"Planner returned no valid experiment candidates after correction; payload={json.dumps(value)[:1200]}")
        return {**candidates[0], "candidate_plans": candidates, "rejected_candidates": rejected}

    def reflect(self, context: dict[str, Any]) -> dict[str, Any]:
        schema={"decision":"continue|propose_fault|propose_no_fault","best_hypothesis_id":"H001 or null","unresolved_questions":["short question"],"summary":"short evidence summary"}
        value=self._request_json("reflect on hypotheses and evidence",context,schema)
        value, decision=self._normalize_reflection(value)
        return {"decision":decision,"best_hypothesis_id":value.get("best_hypothesis_id"),"unresolved_questions":[str(x) for x in value.get("unresolved_questions",[])],"summary":str(value.get("summary",""))}

    @staticmethod
    def _normalize_reflection(value: dict[str, Any]) -> tuple[dict[str, Any], str]:
        """Accept equivalent decision dialects used by OpenAI-compatible models.

        The graph deliberately has only three internal reflection states.  Providers
        nevertheless often return a nested ``reflection`` object, call the field
        ``action``, or spell ``continue`` as "needs more evidence".  Normalize only
        explicit semantic equivalents; unknown values still fail loudly with a
        bounded payload summary so a new provider dialect can be diagnosed.
        """
        if isinstance(value.get("reflection"), dict):
            value=value["reflection"]
        raw=value.get("decision", value.get("action"))
        normalized=str(raw).strip().lower().replace("-","_").replace(" ","_") if raw is not None else ""
        aliases={
            "continue":"continue",
            "replan":"continue",
            "continue_investigation":"continue",
            "investigate_further":"continue",
            "needs_more_evidence":"continue",
            "need_more_evidence":"continue",
            "collect_more_evidence":"continue",
            "propose_fault":"propose_fault",
            "fault":"propose_fault",
            "confirm_fault":"propose_fault",
            "propose_no_fault":"propose_no_fault",
            "no_fault":"propose_no_fault",
            "confirm_no_fault":"propose_no_fault",
        }
        decision=aliases.get(normalized)
        if decision is None:
            payload=json.dumps(value, ensure_ascii=False, default=str)[:1200]
            raise AgentAPIError(f"reflection decision is invalid: {raw!r}; payload={payload}")
        return value, decision

    def final_diagnosis(self, context: dict[str, Any]) -> dict[str, Any]:
        required=context.get("validated_decision")
        decision_schema=required if required in {"fault", "no_fault"} else "fault|no_fault"
        schema={"decision":decision_schema,"fault_family":"canonical category","root_cause":"concise evidence-based statement","confidence":0.0,"evidence_experiment_ids":["EXP_001"],"recommended_repair":{},"remaining_uncertainty":[]}
        request_name=(
            "produce the final evidence-backed diagnosis. Claims must not exceed the scope of executed evidence; "
            "a failed candidate only weakens that tested candidate unless multiple independent experiments justify a broader claim. "
            "Distinguish observed, supported, not supported, validated, and inconclusive evidence. "
            "Separately state experimental evidence, documentary knowledge evidence, and the final inference."
        )
        if required in {"fault", "no_fault"}:
            request_name += f". The validation gate has accepted {required}; return exactly decision={required}."
        if context.get("final_correction"):
            request_name += " Your previous final decision conflicted with the validation gate. Correct it now using only the supplied evidence."
        value=self._request_json(request_name,context,schema)
        return self._validate({"type":"final","final":value}).final or {}
    def decide(self,state:DiagnosisState,task:dict[str,object])->AgentAction:
        schema={"type":"tool_call|final","tool":"inspect|compare|transform_and_compare|shift_and_compare|evaluate_candidate (tool_call only)","arguments":{},"reason":"short evidence-based rationale","final":{"decision":"fault|no_fault","fault_family":"string","root_cause":"string","confidence":"0..1","evidence_experiment_ids":["EXP_001"],"recommended_repair":{}}}
        visible={"task":task,"state":{"case_id":state.case_id,"budget_remaining":state.budget_remaining,"observations":state.observations,"experiments":[{"experiment_id":x["experiment_id"],"tool":x["tool"],"arguments":x["arguments"],"result":x["result"]} for x in state.experiments]},"action_schema":schema}
        if task.get("force_final"):
            visible["instruction"] = "Tool budget/step limit reached. Return type=final now. Do not request a tool call. Base the conclusion only on real experiment IDs already in state."
        payload={"model":self.settings.model_name,"messages":[{"role":"system","content":SYSTEM_PROMPT},{"role":"user","content":json.dumps(visible)}],"temperature":0,"response_format":{"type":"json_object"}}
        url=self.settings.base_url.rstrip("/")+"/chat/completions"; body=json.dumps(payload).encode(); req=request.Request(url,body,headers={"Authorization":f"Bearer {self.settings.api_key}","Content-Type":"application/json"},method="POST")
        # School-hosted endpoints occasionally return transient overload errors.  Retrying
        # a deterministic, stateless planning request is safe; malformed responses are not retried.
        for attempt in range(self.max_retries + 1):
            try:
                with request.urlopen(req,timeout=self.timeout) as response: data=json.loads(response.read())
                break
            except error.HTTPError as exc:
                retryable=exc.code in {429,500,502,503,504}
                if retryable and attempt < self.max_retries:
                    time.sleep(self.retry_base_seconds * (2 ** attempt))
                    continue
                raise AgentAPIError(f"School LLM API request failed: {exc}") from exc
            except (error.URLError, OSError) as exc:
                if attempt < self.max_retries:
                    time.sleep(self.retry_base_seconds * (2 ** attempt))
                    continue
                raise AgentAPIError(f"School LLM API request failed: {exc}") from exc
            except json.JSONDecodeError as exc:
                raise AgentAPIError(f"School LLM API request failed: {exc}") from exc
        try: raw=data["choices"][0]["message"]["content"]; action=json.loads(raw); return self._validate(action)
        except (KeyError,IndexError,TypeError,json.JSONDecodeError,ValueError) as exc: raise AgentAPIError(f"School LLM API returned an invalid action: {exc}; response={raw[:1200]!r}") from exc
    @staticmethod
    def _validate(value:dict[str,Any])->AgentAction:
        # Tolerate common model wrappers while normalizing to SciDiagnose's contract.
        if isinstance(value.get("tool_call"), dict): value = value["tool_call"]
        if value.get("type")=="json_object" and ("tool" in value or "tool_name" in value): value={**value,"type":"tool_call"}
        if isinstance(value.get("final_diagnosis"), dict) and value.get("type")=="json_object": value={"type":"final","final":value["final_diagnosis"]}
        if isinstance(value.get("final"), dict) and value.get("type")=="json_object": value={"type":"final","reason":value.get("reason",""),"final":value["final"]}
        if isinstance(value.get("action"), dict): value = {**value, **value["action"]}
        if isinstance(value.get("action"), str) and "type" not in value: value["type"] = value["action"]
        if "type" not in value and ("tool" in value or "tool_name" in value): value["type"] = "tool_call"
        if "type" not in value and ("decision" in value or "final_diagnosis" in value): value["type"] = "final"
        kind=value.get("type")
        if kind in {"tool", "tool_call", "call_tool"}:
            tool=value.get("tool", value.get("tool_name")); args=value.get("arguments", value.get("args", {}))
            if tool not in TOOL_SPECS or not isinstance(args,dict): raise ValueError("invalid tool action")
            return AgentAction("tool_call",tool,OpenAICompatibleAgent._normalize_arguments(tool,args),str(value.get("reason","")))
        if kind in {"final", "diagnosis", "conclusion"}:
            final=value.get("final", value.get("final_diagnosis"))
            if not isinstance(final,dict): final={key:value[key] for key in ("decision","fault_family","root_cause","confidence","evidence_experiment_ids","recommended_repair") if key in value}
            required={"decision","fault_family","root_cause","confidence","evidence_experiment_ids","recommended_repair"}
            if required <= final.keys(): return AgentAction("final",reason=str(value.get("reason","")),final=final)
        raise ValueError("action type must be tool_call or final")

    @staticmethod
    def _normalize_arguments(tool:str, arguments:dict[str,Any])->dict[str,Any]:
        if tool in {"inspect","compare"}: return {}
        if tool == "retrieve_scientific_knowledge":
            query, top_k = arguments.get("query"), arguments.get("top_k", 5)
            if not isinstance(query, str) or not query.strip(): raise ValueError("knowledge query must be a non-empty string")
            if type(top_k) is not int or not 1 <= top_k <= 5: raise ValueError("knowledge top_k must be an integer in [1, 5]")
            return {"query": query.strip(), "top_k": top_k}
        if tool == "transform_and_compare":
            operation=arguments.get("operation",arguments.get("transform",arguments.get("transformation")))
            if not isinstance(operation,str): raise ValueError("transform operation is required")
            normalized=operation.strip().lower().replace("-","_").replace(" ","_")
            aliases={"rotate90":"rot90","rotate_90":"rot90","rotation_90":"rot90","rotate180":"rot180","rotate_180":"rot180","rotation_180":"rot180","rotate270":"rot270","rotate_270":"rot270","rotation_270":"rot270","horizontal_flip":"flip_x","flip_horizontal":"flip_x","vertical_flip":"flip_y","flip_vertical":"flip_y"}
            normalized=aliases.get(normalized,normalized)
            if normalized not in {"identity","flip_x","flip_y","rot90","rot180","rot270","transpose"}: raise ValueError("unsupported transform operation")
            return {"operation":normalized}
        if tool=="evaluate_candidate":
            pipeline=arguments.get("pipeline")
            if not isinstance(pipeline,list) or len(pipeline)>4: raise ValueError("candidate pipeline must contain 0 to 4 steps")
            normalized=[]
            for step in pipeline:
                if not isinstance(step,dict): raise ValueError("candidate step must be an object")
                kind=step.get("type", step.get("kind"))
                # Some OpenAI-compatible models express a pipeline step as
                # {"operation": "shift", ...}; treat it as the same schema.
                if kind is None and step.get("operation")=="shift": kind="shift"
                elif kind is None and isinstance(step.get("operation"),str): kind="transform"
                if kind=="transform": normalized.append({"type":"transform",**OpenAICompatibleAgent._normalize_arguments("transform_and_compare",step)})
                elif kind=="shift": normalized.append({"type":"shift",**OpenAICompatibleAgent._normalize_arguments("shift_and_compare",step)})
                else: raise ValueError("candidate step must be transform or shift")
            return {"pipeline":normalized}
        dr,dc=arguments.get("dr",arguments.get("row_shift")),arguments.get("dc",arguments.get("col_shift"))
        if type(dr) is not int or type(dc) is not int or not -5<=dr<=5 or not -5<=dc<=5: raise ValueError("shift dr and dc must be integers in [-5, 5]")
        return {"dr":dr,"dc":dc}
class ManualAgent:
    """Deterministic demonstration policy that reacts only to visible experiment evidence."""
    def generate_hypotheses(self, context: dict[str, Any]) -> list[dict[str, Any]]:
        return [{"hypothesis_id":"H001","category":"systematic_mismatch","description":"A repeatable discrepancy may affect the computation.","testable_scope":["measured agreement"],"status":"active","confidence":.5,"evidence_for":[],"evidence_against":[]},{"hypothesis_id":"H002","category":"normal_variation","description":"The observation may be consistent with expected variation.","testable_scope":["measured agreement"],"status":"active","confidence":.4,"evidence_for":[],"evidence_against":[]}]
    def update_hypotheses(self, context: dict[str, Any]) -> list[dict[str, Any]]:
        evidence=context["latest_evidence"]; updated=[dict(item) for item in context["hypotheses"]]
        if (evidence.get("delta") or 0) > 0:
            updated[0]={**updated[0],"status":"supported","confidence":.7,"evidence_for":updated[0]["evidence_for"]+[evidence["evidence_id"]]}
        return updated
    def plan_experiment(self, context: dict[str, Any]) -> dict[str, Any]:
        # This adapter is used by the graph, whose planner deliberately never
        # accepts final decisions.  Keep the demonstration policy in the same
        # experiment-only contract and let reflect/gate/finalize end the run.
        candidates=(
            ("inspect", {}), ("compare", {}),
            ("shift_and_compare", {"dr": 0, "dc": 2}),
            ("shift_and_compare", {"dr": 0, "dc": 4}),
            ("shift_and_compare", {"dr": 2, "dc": 0}),
            ("shift_and_compare", {"dr": 4, "dc": 0}),
            ("shift_and_compare", {"dr": 2, "dc": 2}),
            ("shift_and_compare", {"dr": -2, "dc": -2}),
        )
        tool, arguments=candidates[min(len(context["experiments"]), len(candidates)-1)]
        targets=[item["hypothesis_id"] for item in context["hypotheses"] if item["status"] in {"active","supported"}]
        plan={"objective":"Obtain a distinct measurement for the active hypotheses.","target_hypotheses":targets,"tested_scope":["measured agreement"],"tool":tool,"arguments":arguments,"expected_evidence":"A measurable result will distinguish the active hypotheses."}
        return {**plan,"candidate_plans":[plan]}
    def reflect(self, context: dict[str, Any]) -> dict[str, Any]:
        best=context["best_metric"]
        return {"decision":"propose_fault" if best>=context["quality_threshold"] else "continue","best_hypothesis_id":"H001","unresolved_questions":[],"summary":"Deterministic demonstration reflection."}
    def final_diagnosis(self, context: dict[str, Any]) -> dict[str, Any]:
        if context.get("validated_decision") == "no_fault":
            return {"decision":"no_fault","fault_family":"no_fault","root_cause":"The validation gate accepted the initial quality or explicit normal-range evidence.","confidence":.8,"evidence_experiment_ids":[],"recommended_repair":{}}
        best=context.get("best_experiment")
        return {"decision":"fault" if best else "no_fault","fault_family":"validated_candidate" if best else "no_fault","root_cause":"A real candidate experiment supplied the final evidence." if best else "No fault evidence was validated.","confidence":.8,"evidence_experiment_ids":[best["experiment_id"]] if best else [],"recommended_repair":best["arguments"] if best else {}}
    def decide(self,state:DiagnosisState,task:dict[str,object])->AgentAction:
        if not state.experiments: return AgentAction("tool_call","inspect",reason="Establish array structure and value ranges before testing hypotheses.")
        if len(state.experiments)==1: return AgentAction("tool_call","compare",reason="Repeat the general comparison after the initial structural observation.")
        latest=state.experiments[-1]["result"].get("metrics",{}); improved=float(latest.get("agreement",0))>=float(task["expected_quality_threshold"])
        return AgentAction("final",reason="Two real experiments supplied the evidence.",final={"decision":"fault" if improved else "no_fault","fault_family":"measured_mismatch" if improved else "undetermined","root_cause":"measured_discrepancy" if improved else "insufficient_evidence","confidence":.95 if improved else .4,"evidence_experiment_ids":[item["experiment_id"] for item in state.experiments],"recommended_repair":{}})
