"""LangGraph orchestration for hypothesis-evidence diagnosis (v0.2)."""
from __future__ import annotations
import json,time
from dataclasses import asdict
from pathlib import Path
from typing import Any
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END,START,StateGraph
from .agent import ManualAgent,OpenAICompatibleAgent
from .experiment_tools import COSTS,ExperimentTools
from .graph_state import DiagnosisGraphState

class DiagnosisGraph:
    def __init__(self,agent:ManualAgent|OpenAICompatibleAgent,tools:ExperimentTools,run_dir:Path)->None:
        self.agent,self.tools,self.run_dir=agent,tools,run_dir;self.trace=run_dir/'trace.jsonl';self.checkpointer=InMemorySaver();g=StateGraph(DiagnosisGraphState)
        g.add_node('observe',self.observe);g.add_node('hypothesize',self.hypothesize);g.add_node('plan',self.plan);g.add_node('execute',self.execute);g.add_node('evidence',self.evidence);g.add_node('reflect',self.reflect);g.add_node('finalize',self.finalize)
        g.add_edge(START,'observe');g.add_conditional_edges('observe',lambda s:'finalize' if s['diagnosis_status']=='no_fault' else 'hypothesize',{'finalize':'finalize','hypothesize':'hypothesize'});g.add_edge('hypothesize','plan');g.add_conditional_edges('plan',lambda s:'finalize' if 'final' in (s.get('current_plan') or {}) else 'execute',{'finalize':'finalize','execute':'execute'});g.add_edge('execute','evidence');g.add_edge('evidence','reflect');g.add_conditional_edges('reflect',lambda s:'finalize' if s['diagnosis_status'] in {'validated_fault','no_fault','budget_exhausted'} else 'hypothesize',{'finalize':'finalize','hypothesize':'hypothesize'});g.add_edge('finalize',END);self.app=g.compile(checkpointer=self.checkpointer)
    def log(self,node:str,**data:Any)->None:self.trace.open('a').write(json.dumps({'node':node,'timestamp':time.time(),**data})+'\n')
    def observe(self,s:DiagnosisGraphState)->dict[str,Any]:
        self.log('observe',initial=s['initial_observation'])
        return {'diagnosis_status':'no_fault' if float(s['initial_observation'].get('agreement',0))>=s['quality_threshold'] else 'investigating'}
    def hypothesize(self,s:DiagnosisGraphState)->dict[str,Any]:
        if s.get('hypotheses'):return {}
        hs=[{'hypothesis_id':'H1','description':'A systematic mismatch may be present.','category':'data_relationship','status':'active','confidence':.4,'evidence_for':[],'evidence_against':[]},{'hypothesis_id':'H2','description':'The observed disagreement may be within expected variation.','category':'normal_variation','status':'active','confidence':.3,'evidence_for':[],'evidence_against':[]}]
        self.log('hypothesize',hypotheses=hs);return {'hypotheses':hs}
    def plan(self,s:DiagnosisGraphState)->dict[str,Any]:
        from .models import DiagnosisState
        ds=DiagnosisState(s['case_id'],s['budget_total'],s['budget_remaining'],[s['initial_observation']],s.get('experiments',[]));action=self.agent.decide(ds,{**s['task'],'force_final':False})
        if action.type=='final':
            status='no_fault' if action.final and action.final.get('decision')=='no_fault' else 'budget_exhausted'
            self.log('plan',selected_final=action.final,budget_remaining=s['budget_remaining'])
            return {'current_plan':{'final':action.final},'diagnosis_status':status}
        plan={'tool':action.tool,'arguments':action.arguments,'reason':action.reason,'target_hypotheses':['H1','H2']};self.log('plan',selected_experiment=plan,hypotheses=s['hypotheses'],budget_remaining=s['budget_remaining']);return {'current_plan':plan}
    def execute(self,s:DiagnosisGraphState)->dict[str,Any]:
        plan=s['current_plan']
        if 'final' in plan:return {}
        record=self.tools.execute(plan['tool'],plan['arguments']);self.log('execute',experiment_id=record['experiment_id'],backend=record['backend'],remote_host=record['remote_host'],remote_pid=record['remote_pid'],result=record['result']);return {'experiments':s.get('experiments',[])+[record],'latest_result':record,'budget_remaining':s['budget_remaining']-record['cost'],'steps_used':s['steps_used']+1}
    def evidence(self,s:DiagnosisGraphState)->dict[str,Any]:
        r=s.get('latest_result');
        if not r:return {}
        m=r['result'].get('metrics',{});e={'evidence_id':f"E{len(s.get('evidence',[]))+1:03d}",'experiment_id':r['experiment_id'],'statement':f"{r['tool']} produced agreement {m.get('agreement','n/a')}",'metrics':m,'supports':['H1'] if m.get('agreement',0)>=s['quality_threshold'] else [],'contradicts':[]};self.log('evidence',evidence=e);return {'evidence':s.get('evidence',[])+[e]}
    def reflect(self,s:DiagnosisGraphState)->dict[str,Any]:
        best=max((x['metrics'].get('agreement',0) for x in s.get('evidence',[])),default=0);status='validated_fault' if best>=s['quality_threshold'] else ('budget_exhausted' if s['steps_used']>=s['max_steps'] or s['budget_remaining']<=0 else 'needs_more_evidence');self.log('reflect',decision=status,best_agreement=best);return {'diagnosis_status':status}
    def finalize(self,s:DiagnosisGraphState)->dict[str,Any]:
        requested=(s.get('current_plan') or {}).get('final')
        if s['diagnosis_status']=='no_fault' and isinstance(requested,dict): final=requested
        else:
            best=max(s.get('experiments',[]),key=lambda x:x['result'].get('metrics',{}).get('agreement',0),default=None);final={'decision':'fault' if s['diagnosis_status']=='validated_fault' else 'no_fault','fault_family':'validated_candidate' if best else 'no_fault','root_cause':'evidence-backed candidate' if best else 'initial agreement meets quality threshold','confidence':.8,'evidence_experiment_ids':[best['experiment_id']] if best else [],'recommended_repair':best['arguments'] if best else {}}
        self.log('finalize',final=final);return {'final_diagnosis':final}
    def run(self,state:DiagnosisGraphState)->DiagnosisGraphState:
        return self.app.invoke(state,{'configurable':{'thread_id':state['run_id']}})
