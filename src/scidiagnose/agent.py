"""Provider-independent agents; no hidden case data is read here."""
from __future__ import annotations
import json
import time
from typing import Any
from urllib import error, request
from .config import Settings
from .models import AgentAction, DiagnosisState

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

class AgentAPIError(RuntimeError): pass

class OpenAICompatibleAgent:
    """Minimal stdlib client for school endpoints implementing /chat/completions."""
    def __init__(self, settings: Settings | None = None, timeout: int = 60, max_retries: int = 2) -> None:
        self.settings=settings or Settings(); self.timeout=timeout; self.max_retries=max_retries
        if not (self.settings.base_url and self.settings.model_name and self.settings.api_key):
            raise AgentAPIError("SCIDIAG_BASE_URL, SCIDIAG_MODEL_NAME, and SCIDIAG_API_KEY are required for API mode")

    def _request_json(self, request_name: str, context: dict[str, Any], response_schema: dict[str, Any]) -> dict[str, Any]:
        """Send a concise structured cognitive request; hidden case files never enter context."""
        visible = {"request": request_name, "context": context, "response_schema": response_schema}
        payload={"model":self.settings.model_name,"messages":[{"role":"system","content":SYSTEM_PROMPT},{"role":"user","content":json.dumps(visible)}],"temperature":0,"response_format":{"type":"json_object"}}
        url=self.settings.base_url.rstrip("/")+"/chat/completions"; body=json.dumps(payload).encode(); req=request.Request(url,body,headers={"Authorization":f"Bearer {self.settings.api_key}","Content-Type":"application/json"},method="POST")
        for attempt in range(self.max_retries + 1):
            try:
                with request.urlopen(req,timeout=self.timeout) as response: data=json.loads(response.read())
                raw=data["choices"][0]["message"]["content"]
                value=json.loads(raw)
                if not isinstance(value,dict): raise ValueError("response must be a JSON object")
                # School models sometimes wrap any structured payload in a generic envelope.
                if value.get("type") == "json_object":
                    for key in ("obj", "data", "result"):
                        if isinstance(value.get(key), dict):
                            value = value[key]
                            break
                return value
            except error.HTTPError as exc:
                if exc.code in {429,500,502,503,504} and attempt < self.max_retries:
                    time.sleep(2 ** attempt); continue
                raise AgentAPIError(f"School LLM API request failed: {exc}") from exc
            except OSError as exc:
                if attempt < self.max_retries:
                    time.sleep(2 ** attempt); continue
                raise AgentAPIError(f"School LLM API transport failed: {exc}") from exc
            except (error.URLError,json.JSONDecodeError,KeyError,IndexError,TypeError,ValueError) as exc:
                raise AgentAPIError(f"School LLM API returned invalid structured output: {exc}") from exc

    @staticmethod
    def _hypotheses(value: dict[str, Any], existing: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
        raw=value.get("hypotheses")
        if not isinstance(raw,list) or not 2 <= len(raw) <= 5: raise AgentAPIError("model must provide 2 to 5 hypotheses")
        prior={item["hypothesis_id"] for item in existing or []}; result=[]
        for index,item in enumerate(raw,1):
            if not isinstance(item,dict): raise AgentAPIError("hypothesis must be an object")
            hypothesis_id=str(item.get("hypothesis_id") or (f"H{index:03d}" if not prior else next(iter(prior))))
            status=item.get("status","active")
            if status not in {"active","supported","weakened","rejected","validated"}: status="active"
            result.append({"hypothesis_id":hypothesis_id,"category":str(item.get("category","unspecified")),"description":str(item.get("description","Plausible explanation requiring evidence.")),"status":status,"confidence":max(0.0,min(1.0,float(item.get("confidence",.5)))),"evidence_for":[str(x) for x in item.get("evidence_for",[])],"evidence_against":[str(x) for x in item.get("evidence_against",[])]})
        return result

    def generate_hypotheses(self, context: dict[str, Any]) -> list[dict[str, Any]]:
        schema={"hypotheses":[{"hypothesis_id":"H001","category":"short label","description":"concise explanation","status":"active","confidence":0.5,"evidence_for":[],"evidence_against":[]}]}
        return self._hypotheses(self._request_json("generate competing hypotheses",context,schema))

    def update_hypotheses(self, context: dict[str, Any]) -> list[dict[str, Any]]:
        schema={"hypotheses":[{"hypothesis_id":"existing ID","category":"short label","description":"concise explanation","status":"supported|weakened|rejected|validated|active","confidence":0.5,"evidence_for":["E001"],"evidence_against":[]}]}
        return self._hypotheses(self._request_json("update competing hypotheses using the latest evidence; link each change to the tested candidate and do not overgeneralize an inconclusive result",context,schema), context.get("hypotheses"))

    def plan_experiment(self, context: dict[str, Any]) -> dict[str, Any]:
        schema={"objective":"distinguish named hypotheses","target_hypotheses":["H001"],"experiment":{"tool":"inspect|compare|transform_and_compare|shift_and_compare|evaluate_candidate","arguments":"inspect/compare use {}; transform requires operation in identity,flip_x,flip_y,rot90,rot180,rot270,transpose; shift requires integer dr and dc in [-5,5]; evaluate_candidate requires pipeline of 0-4 steps, each transform or shift using the same fields"},"expected_evidence":"short measurable outcome"}
        value=self._request_json("select one cost-aware diagnostic experiment",context,schema)
        experiment=value.get("experiment",value)
        try:
            action=self._validate({"type":"tool_call","tool":experiment.get("tool"),"arguments":experiment.get("arguments",{}),"reason":value.get("objective",value.get("reason",""))})
        except (AttributeError, ValueError) as exc:
            raise AgentAPIError(f"Planner returned an invalid experiment contract: {exc}; payload={json.dumps(value)[:1200]}") from exc
        valid={item["hypothesis_id"] for item in context["hypotheses"]}
        targets=[item for item in value.get("target_hypotheses",[]) if item in valid] or list(valid)
        return {"objective":str(value.get("objective",action.reason)),"target_hypotheses":targets,"tool":action.tool,"arguments":action.arguments,"expected_evidence":str(value.get("expected_evidence","Measure evidence that distinguishes the target hypotheses."))}

    def reflect(self, context: dict[str, Any]) -> dict[str, Any]:
        schema={"decision":"continue|propose_fault|propose_no_fault","best_hypothesis_id":"H001 or null","unresolved_questions":["short question"],"summary":"short evidence summary"}
        value=self._request_json("reflect on hypotheses and evidence",context,schema)
        if isinstance(value.get("reflection"), dict): value=value["reflection"]
        decision=value.get("decision")
        if decision not in {"continue","propose_fault","propose_no_fault"}: raise AgentAPIError("reflection decision is invalid")
        return {"decision":decision,"best_hypothesis_id":value.get("best_hypothesis_id"),"unresolved_questions":[str(x) for x in value.get("unresolved_questions",[])],"summary":str(value.get("summary",""))}

    def final_diagnosis(self, context: dict[str, Any]) -> dict[str, Any]:
        schema={"decision":"fault|no_fault","fault_family":"canonical category","root_cause":"concise evidence-based statement","confidence":0.0,"evidence_experiment_ids":["EXP_001"],"recommended_repair":{},"remaining_uncertainty":[]}
        value=self._request_json("produce the final evidence-backed diagnosis",context,schema)
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
                    time.sleep(2 ** attempt)
                    continue
                raise AgentAPIError(f"School LLM API request failed: {exc}") from exc
            except (error.URLError,json.JSONDecodeError) as exc:
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
            if tool not in {"inspect","compare","transform_and_compare","shift_and_compare","evaluate_candidate"} or not isinstance(args,dict): raise ValueError("invalid tool action")
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
        return [{"hypothesis_id":"H001","category":"systematic_mismatch","description":"A repeatable discrepancy may affect the computation.","status":"active","confidence":.5,"evidence_for":[],"evidence_against":[]},{"hypothesis_id":"H002","category":"normal_variation","description":"The observation may be consistent with expected variation.","status":"active","confidence":.4,"evidence_for":[],"evidence_against":[]}]
    def update_hypotheses(self, context: dict[str, Any]) -> list[dict[str, Any]]:
        evidence=context["latest_evidence"]; updated=[dict(item) for item in context["hypotheses"]]
        if (evidence.get("delta") or 0) > 0:
            updated[0]={**updated[0],"status":"supported","confidence":.7,"evidence_for":updated[0]["evidence_for"]+[evidence["evidence_id"]]}
        return updated
    def plan_experiment(self, context: dict[str, Any]) -> dict[str, Any]:
        from .models import DiagnosisState
        action=self.decide(DiagnosisState(context["case_id"],context["budget_total"],context["budget_remaining"],[context["initial_observation"]],context["experiments"]),context["task"])
        if action.type=="final": return {"final":action.final}
        return {"objective":action.reason,"target_hypotheses":[item["hypothesis_id"] for item in context["hypotheses"] if item["status"] in {"active","supported"}],"tool":action.tool,"arguments":action.arguments,"expected_evidence":"A measurable result will distinguish the active hypotheses."}
    def reflect(self, context: dict[str, Any]) -> dict[str, Any]:
        best=context["best_metric"]
        return {"decision":"propose_fault" if best>=context["quality_threshold"] else "continue","best_hypothesis_id":"H001","unresolved_questions":[],"summary":"Deterministic demonstration reflection."}
    def final_diagnosis(self, context: dict[str, Any]) -> dict[str, Any]:
        best=context.get("best_experiment")
        return {"decision":"fault" if best else "no_fault","fault_family":"validated_candidate" if best else "no_fault","root_cause":"A real candidate experiment supplied the final evidence." if best else "No fault evidence was validated.","confidence":.8,"evidence_experiment_ids":[best["experiment_id"]] if best else [],"recommended_repair":best["arguments"] if best else {}}
    def decide(self,state:DiagnosisState,task:dict[str,object])->AgentAction:
        if not state.experiments: return AgentAction("tool_call","inspect",reason="Establish array structure and value ranges before testing hypotheses.")
        if len(state.experiments)==1: return AgentAction("tool_call","transform_and_compare",{"operation":"rot180"},"Test one general 2-D transform and measure whether agreement changes materially.")
        latest=state.experiments[-1]["result"].get("metrics",{}); improved=float(latest.get("agreement",0))>=float(task["expected_quality_threshold"])
        return AgentAction("final",reason="Two real experiments supplied the evidence.",final={"decision":"fault" if improved else "no_fault","fault_family":"spatial_alignment" if improved else "undetermined","root_cause":"orientation_mismatch" if improved else "insufficient_evidence","confidence":.95 if improved else .4,"evidence_experiment_ids":[item["experiment_id"] for item in state.experiments],"recommended_repair":{"operation":"rot180"} if improved else {}})
