"""Bounded evidence loop that records every agent decision and remote result."""
from __future__ import annotations
import json, time
from dataclasses import asdict
from pathlib import Path
from typing import Any
from .agent import ManualAgent, OpenAICompatibleAgent
from .experiment_tools import COSTS, ExperimentTools
from .models import DiagnosisState
class DiagnosisRunner:
    def __init__(self,agent:ManualAgent | OpenAICompatibleAgent,tools:ExperimentTools,run_dir:Path,max_steps:int=8)->None:self.agent,self.tools,self.run_dir,self.max_steps=agent,tools,run_dir,max_steps
    def run(self,task:dict[str,Any],initial:dict[str,Any])->DiagnosisState:
        state=DiagnosisState(task["case_id"],task["budget"],task["budget"],[initial]); trace=self.run_dir/"trace.jsonl"; task_context=dict(task)
        for _step in range(self.max_steps):
            action=self.agent.decide(state,task_context); event={"timestamp":time.time(),"agent_reason":action.reason,"agent_action":asdict(action)}
            if action.type=="final":
                validated=any(float(item.get("result",{}).get("metrics",{}).get("agreement",0))>=float(task["expected_quality_threshold"]) for item in state.experiments)
                if action.final and action.final.get("decision")=="fault" and not validated and _step < self.max_steps-1:
                    event["rejected_final"]="fault conclusion requires a real validation experiment"; trace.open("a").write(json.dumps(event)+"\n"); task_context={**task,"require_validation":True}; continue
                state.final_diagnosis=action.final; trace.open("a").write(json.dumps(event)+"\n"); break
            assert action.tool; cost=COSTS[action.tool]
            if state.budget_remaining<cost: continue
            print("Action:",action.tool,"-",action.reason); record=self.tools.execute(action.tool,action.arguments); state.experiments.append(record); state.budget_remaining-=cost; event.update({"experiment_id":record["experiment_id"],"backend":record["backend"],"status":record["status"],"result":record["result"],"budget_remaining":state.budget_remaining}); trace.open("a").write(json.dumps(event)+"\n")
        if state.final_diagnosis is None:
            final_action=self.agent.decide(state,{**task,"force_final":True})
            if final_action.type != "final": raise RuntimeError("Agent did not return a final diagnosis after reaching the step limit")
            state.final_diagnosis=final_action.final
            trace.open("a").write(json.dumps({"timestamp":time.time(),"agent_reason":final_action.reason,"agent_action":asdict(final_action),"forced_final":True})+"\n")
        (self.run_dir/"state.json").write_text(json.dumps(asdict(state),indent=2));
        if state.final_diagnosis:(self.run_dir/"final.json").write_text(json.dumps(state.final_diagnosis,indent=2))
        return state
