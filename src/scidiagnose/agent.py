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
    def decide(self,state:DiagnosisState,task:dict[str,object])->AgentAction:
        if not state.experiments: return AgentAction("tool_call","inspect",reason="Establish array structure and value ranges before testing hypotheses.")
        if len(state.experiments)==1: return AgentAction("tool_call","transform_and_compare",{"operation":"rot180"},"Test one general 2-D transform and measure whether agreement changes materially.")
        latest=state.experiments[-1]["result"].get("metrics",{}); improved=float(latest.get("agreement",0))>=float(task["expected_quality_threshold"])
        return AgentAction("final",reason="Two real experiments supplied the evidence.",final={"decision":"fault" if improved else "no_fault","fault_family":"spatial_alignment" if improved else "undetermined","root_cause":"orientation_mismatch" if improved else "insufficient_evidence","confidence":.95 if improved else .4,"evidence_experiment_ids":[item["experiment_id"] for item in state.experiments],"recommended_repair":{"operation":"rot180"} if improved else {}})
