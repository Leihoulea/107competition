"""Local backend with the same structured result contract as SSH Direct."""
from __future__ import annotations
import json, subprocess, time
from pathlib import Path
from typing import Any
from .executor_base import ComputeExecutor, JobHandle
class LocalExecutor(ComputeExecutor):
    def __init__(self, workspace: Path = Path(".scidiagnose-local")) -> None: self.workspace=workspace; self.jobs:dict[str,subprocess.Popen[str]]={}
    def probe(self)->dict[str,Any]: return {"backend":"local"}
    def upload(self,local_path:str,remote_path:str)->None: Path(remote_path).parent.mkdir(parents=True,exist_ok=True); Path(remote_path).write_bytes(Path(local_path).read_bytes())
    def submit(self,experiment_id:str,command:list[str])->JobHandle:
        directory=self.workspace/"jobs"/experiment_id; directory.mkdir(parents=True,exist_ok=True); out=(directory/"stdout.log").open("w"); err=(directory/"stderr.log").open("w"); self.jobs[experiment_id]=subprocess.Popen(command,cwd=directory,text=True,stdout=out,stderr=err); return JobHandle(experiment_id,"local",None,self.jobs[experiment_id].pid,str(directory))
    def status(self,job:JobHandle)->str:
        d=Path(job.job_dir)
        if (d/"result.json").exists(): return "COMPLETED"
        if (d/"failure.json").exists() or self.jobs[job.job_id].poll() is not None: return "FAILED"
        return "RUNNING"
    def logs(self,job:JobHandle,tail:int=100)->tuple[str,str]:
        d=Path(job.job_dir); return ((d/"stdout.log").read_text() if (d/"stdout.log").exists() else "",(d/"stderr.log").read_text() if (d/"stderr.log").exists() else "")
    def fetch_result(self,job:JobHandle)->dict[str,Any]: return json.loads((Path(job.job_dir)/"result.json").read_text())
