"""Agent-facing experiment API; SSH/PID details do not escape this layer."""
from __future__ import annotations
import json, time
from pathlib import Path
from typing import Any
from .executor_base import ComputeExecutor
from .models import ExperimentRequest
from .ssh_executor import SSHDirectExecutor

COSTS={"inspect":1,"compare":1,"transform_and_compare":4,"shift_and_compare":4,"evaluate_candidate":3}
class ExperimentTools:
    def __init__(self, executor: ComputeExecutor, case_dir: Path, run_dir: Path) -> None:
        self.executor,self.case_dir,self.run_dir,self.count,self.uploaded=executor,case_dir,run_dir,0,False; (run_dir/"experiments").mkdir(parents=True,exist_ok=True)
    def _ensure_data(self) -> None:
        if self.uploaded:return
        if not isinstance(self.executor,SSHDirectExecutor): raise NotImplementedError("ExperimentTools remote workflow currently requires SSHDirectExecutor")
        base=f"{self.executor.workspace}/inputs/{self.case_dir.name}"; self.executor._ssh(f"mkdir -p {base}")
        for name in ("reference.npy","target_faulty.npy","target_valid.npy"):
            path=self.case_dir/"public"/"data"/name
            if path.exists(): self.executor.upload(path,f"{base}/{name}")
        self.executor.upload(Path(__file__).resolve().parents[2]/"remote"/"run_experiment.py",f"{self.executor.workspace}/scripts/run_experiment.py"); self.uploaded=True
    def execute(self, tool: str, arguments: dict[str,Any] | None=None) -> dict[str,Any]:
        if tool not in COSTS: raise ValueError(f"Unsupported tool: {tool}")
        if tool=="evaluate_candidate":
            pipeline=(arguments or {}).get("pipeline")
            if not isinstance(pipeline,list) or len(pipeline)>4: raise ValueError("pipeline must contain 0 to 4 steps")
        self.count+=1; exp_id=f"EXP_{self.count:03d}"; request=ExperimentRequest(exp_id,tool,arguments or {}); local=self.run_dir/"experiments"/f"{exp_id}.request.json"; local.write_text(json.dumps(request.to_dict(),indent=2))
        self._ensure_data(); assert isinstance(self.executor,SSHDirectExecutor); remote_exp_id=f"{self.run_dir.name}_{exp_id}"; job_dir=self.executor.create_job_dir(remote_exp_id); self.executor.upload(local,f"{job_dir}/experiment.json")
        job=self.executor.submit(remote_exp_id,[self.executor.remote_python,f"{self.executor.workspace}/scripts/run_experiment.py","--input-dir",f"{self.executor.workspace}/inputs/{self.case_dir.name}","--experiment-json","experiment.json","--output-json","result.json"])
        status=self.executor.wait(job,callback=lambda s: print("Status:",s)); stdout,stderr=self.executor.logs(job)
        result=self.executor.fetch_result(job) if status=="COMPLETED" else self.executor.fetch_failure(job)
        cost=COSTS[tool]+(len((arguments or {}).get("pipeline",[])) if tool=="evaluate_candidate" else 0)
        record={"experiment_id":exp_id,"tool":tool,"arguments":arguments or {},"backend":job.backend,"remote_host":job.remote_host,"remote_pid":job.remote_pid,"job_id":job.job_id,"status":status,"cost":cost,"result":result,"stdout":stdout,"stderr":stderr}; (self.run_dir/"experiments"/f"{exp_id}.json").write_text(json.dumps(record,indent=2)); return record
    def inspect(self)->dict[str,Any]: return self.execute("inspect")
    def compare(self)->dict[str,Any]: return self.execute("compare")
    def transform_and_compare(self,operation:str)->dict[str,Any]: return self.execute("transform_and_compare",{"operation":operation})
    def shift_and_compare(self,dr:int,dc:int)->dict[str,Any]: return self.execute("shift_and_compare",{"dr":dr,"dc":dc})
    def evaluate_candidate(self,pipeline:list[dict[str,Any]])->dict[str,Any]: return self.execute("evaluate_candidate",{"pipeline":pipeline})
