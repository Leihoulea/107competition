"""Agent-facing experiment API; SSH/PID details do not escape this layer."""
from __future__ import annotations
import json, time
from pathlib import Path
from typing import Any
from .executor_base import ComputeExecutor
from .models import ExperimentRequest
from .ssh_executor import SSHDirectExecutor
from .tool_specs import COSTS, TOOL_SPECS

class ExperimentTools:
    def __init__(self, executor: ComputeExecutor, case_dir: Path, run_dir: Path) -> None:
        self.executor,self.case_dir,self.run_dir,self.count,self.uploaded=executor,case_dir,run_dir,0,False; (run_dir/"experiments").mkdir(parents=True,exist_ok=True)
    def _ensure_data(self) -> None:
        if self.uploaded:return
        if not isinstance(self.executor,SSHDirectExecutor): raise NotImplementedError("ExperimentTools remote workflow currently requires SSHDirectExecutor")
        self.executor.warm_connection()
        base=f"{self.executor.workspace}/inputs/{self.case_dir.name}"; self.executor._ssh(f"mkdir -p {base}")
        for name in ("reference.npy","target_faulty.npy","target_valid.npy"):
            path=self.case_dir/"public"/"data"/name
            if path.exists(): self.executor.upload(path,f"{base}/{name}")
        self.executor.upload(Path(__file__).resolve().parents[2]/"remote"/"run_experiment.py",f"{self.executor.workspace}/scripts/run_experiment.py"); self.uploaded=True

    def _write_compute_summary(self) -> None:
        """Persist a compact, host-anonymous compute view alongside diagnosis artifacts."""
        records: list[dict[str, Any]] = []
        for path in sorted((self.run_dir / "experiments").glob("EXP_*.json")):
            if path.name.endswith(".request.json"):
                continue
            try:
                records.append(json.loads(path.read_text()))
            except json.JSONDecodeError:
                continue
        observations = [item.get("compute_observation", {}) for item in records]
        terminal = sum(item.get("lifecycle_state") in {"COMPLETED", "FAILED"} for item in observations)
        compute = [item.get("compute_metrics", {}) for item in observations]
        def numeric(metrics: dict[str, Any], key: str) -> float:
            value = metrics.get(key, 0)
            return float(value) if isinstance(value, (int, float)) else 0.0
        total_wall = sum(numeric(metrics, "wall_seconds") for metrics in compute)
        total_cpu = sum(
            numeric(metrics, "user_cpu_seconds") + numeric(metrics, "system_cpu_seconds")
            if "user_cpu_seconds" in metrics or "system_cpu_seconds" in metrics
            else numeric(metrics, "cpu_seconds") if "cpu_seconds" in metrics else numeric(metrics, "process_cpu_seconds")
            for metrics in compute
        )
        peak_memory_mib = max((numeric(metrics, "peak_rss_kib") / 1024 if "peak_rss_kib" in metrics else numeric(metrics, "max_rss_kib") / 1024 for metrics in compute), default=0.0)
        experiments = [{"experiment_id": item.get("experiment_id"), "status": item.get("status"), "compute_observation": item.get("compute_observation", {})} for item in records]
        summary = {
            "schema_version": "1",
            "experiment_count": len(records),
            "terminal_observation_count": terminal,
            "status_counts": {state: sum(item.get("status") == state for item in records) for state in ("COMPLETED", "FAILED", "RUNNING")},
            "budget_units_used": sum(int(item.get("cost", 0)) for item in records),
            "total_cost": sum(int(item.get("cost", 0)) for item in records),
            "total_wall_seconds": round(total_wall, 6),
            "total_cpu_seconds": round(total_cpu, 6),
            "peak_memory_mb": round(peak_memory_mib, 6),
            "site_profiles": sorted({json.dumps(item.get("site_profile", {}), sort_keys=True) for item in observations}),
            "experiments": experiments,
            "remote_jobs": [{"job_id": item.get("job_id"), "backend": item.get("backend"), "remote_pid": item.get("remote_pid"), "status": item.get("status"), "lifecycle_state": item.get("compute_observation", {}).get("lifecycle_state"), "lifecycle": item.get("compute_observation", {}).get("compute_metrics", {}).get("lifecycle", [])} for item in records],
        }
        # Convert the set-friendly representation back to JSON objects.
        summary["site_profiles"] = [json.loads(item) for item in summary["site_profiles"]]
        (self.run_dir / "compute_summary.json").write_text(json.dumps(summary, indent=2))
    def execute(self, tool: str, arguments: dict[str,Any] | None=None) -> dict[str,Any]:
        if tool not in TOOL_SPECS or TOOL_SPECS[tool].category != "compute_experiment": raise ValueError(f"Unsupported compute tool: {tool}")
        if tool=="evaluate_candidate":
            pipeline=(arguments or {}).get("pipeline")
            if not isinstance(pipeline,list) or len(pipeline)>4: raise ValueError("pipeline must contain 0 to 4 steps")
        self.count+=1; exp_id=f"EXP_{self.count:03d}"; request=ExperimentRequest(exp_id,tool,arguments or {}); local=self.run_dir/"experiments"/f"{exp_id}.request.json"; local.write_text(json.dumps(request.to_dict(),indent=2))
        self._ensure_data(); assert isinstance(self.executor,SSHDirectExecutor); remote_exp_id=f"{self.run_dir.name}_{exp_id}"; job_dir=self.executor.create_job_dir(remote_exp_id); upload_started=time.monotonic(); self.executor.upload(local,f"{job_dir}/experiment.json"); upload_seconds=time.monotonic()-upload_started
        job=self.executor.submit(remote_exp_id,[self.executor.remote_python,f"{self.executor.workspace}/scripts/run_experiment.py","--input-dir",f"{self.executor.workspace}/inputs/{self.case_dir.name}","--experiment-json","experiment.json","--output-json","result.json"])
        wait_started=time.monotonic(); status=self.executor.wait(job,callback=lambda s: print("Status:",s)); wait_seconds=time.monotonic()-wait_started; stdout,stderr=self.executor.logs(job)
        fetch_started=time.monotonic(); result=self.executor.fetch_result(job) if status=="COMPLETED" else self.executor.fetch_failure(job); result_fetch_seconds=time.monotonic()-fetch_started
        cost=COSTS[tool]+(len((arguments or {}).get("pipeline",[])) if tool=="evaluate_candidate" else 0)
        observation = self.executor.observe(job).to_dict()
        observation["compute_metrics"] = {**observation["compute_metrics"], **result.get("compute_metrics", {}), "executor_durations_seconds": {"upload": round(upload_seconds, 6), "wait": round(wait_seconds, 6), "result_fetch": round(result_fetch_seconds, 6)}}
        observation["scientific_metrics"] = result.get("scientific_metrics", {})
        record={"experiment_id":exp_id,"tool":tool,"arguments":arguments or {},"backend":job.backend,"remote_host":job.remote_host,"remote_pid":job.remote_pid,"job_id":job.job_id,"status":status,"cost":cost,"result":result,"compute_observation":observation,"stdout":stdout,"stderr":stderr}; (self.run_dir/"experiments"/f"{exp_id}.json").write_text(json.dumps(record,indent=2)); self._write_compute_summary(); return record
    def inspect(self)->dict[str,Any]: return self.execute("inspect")
    def compare(self)->dict[str,Any]: return self.execute("compare")
    def transform_and_compare(self,operation:str)->dict[str,Any]: return self.execute("transform_and_compare",{"operation":operation})
    def shift_and_compare(self,dr:int,dc:int)->dict[str,Any]: return self.execute("shift_and_compare",{"dr":dr,"dc":dc})
    def evaluate_candidate(self,pipeline:list[dict[str,Any]])->dict[str,Any]: return self.execute("evaluate_candidate",{"pipeline":pipeline})
