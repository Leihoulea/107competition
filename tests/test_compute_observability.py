import json
import subprocess
import sys
import tempfile
from pathlib import Path

from scidiagnose.executor_base import ComputeObservation, JobHandle
from scidiagnose.experiment_tools import ExperimentTools
from scidiagnose.ssh_executor import SSHDirectExecutor


ROOT = Path(__file__).resolve().parents[1]


def test_compute_observation_is_serializable_and_host_anonymous():
    observation = ComputeObservation("EXP_001", "ssh_direct", "COMPLETED", remote_pid=7, site_profile={"site_id": "ssh-opaque"})
    assert observation.to_dict()["site_profile"]["site_id"] == "ssh-opaque"


def test_ssh_observation_tracks_lifecycle_without_leaking_host(monkeypatch):
    executor = SSHDirectExecutor()
    responses = iter(["RUNNING", "COMPLETED"])

    class Result:
        returncode = 0
        stderr = ""
        @property
        def stdout(self):
            return next(responses)

    monkeypatch.setattr(executor, "_ssh", lambda *args, **kwargs: Result())
    job = JobHandle("EXP_001", "ssh_direct", "sensitive-alias", 91, "/safe/job")
    executor._record_lifecycle(job.job_id, "SUBMITTED")
    assert executor.status(job) == "RUNNING"
    observation = executor.observe(job).to_dict()
    assert observation["lifecycle_state"] == "COMPLETED"
    assert "sensitive-alias" not in json.dumps(observation)
    assert [event["state"] for event in observation["compute_metrics"]["lifecycle"]] == ["SUBMITTED", "RUNNING", "COMPLETED"]
    assert "submit_timestamp" in observation["compute_metrics"]
    assert "start_timestamp" in observation["compute_metrics"]
    assert "finish_timestamp" in observation["compute_metrics"]


def test_remote_runner_emits_scientific_and_compute_metrics():
    import numpy as np
    with tempfile.TemporaryDirectory(dir=ROOT / "runs") as temporary:
        tmp_path = Path(temporary)
        np.save(tmp_path / "reference.npy", np.array([[0, 1], [1, 0]]))
        np.save(tmp_path / "target_faulty.npy", np.array([[0, 1], [1, 0]]))
        (tmp_path / "request.json").write_text(json.dumps({"experiment_id": "EXP_001", "tool": "compare", "arguments": {}}))
        completed = subprocess.run([sys.executable, str(ROOT / "remote" / "run_experiment.py"), "--input-dir", str(tmp_path), "--experiment-json", "request.json"], cwd=tmp_path, text=True, capture_output=True)
        assert completed.returncode == 0, completed.stderr
        result = json.loads((tmp_path / "result.json").read_text())
    assert result["scientific_metrics"]["primary_value"] == 1.0
    assert result["compute_metrics"]["wall_seconds"] >= 0
    assert result["compute_metrics"]["cpu_seconds"] >= 0
    assert "process_cpu_cumulative_seconds" in result["compute_metrics"]
    assert result["compute_metrics"]["cpu_seconds"] <= result["compute_metrics"]["process_cpu_cumulative_seconds"]
    assert result["elapsed_seconds"] >= result["compute_metrics"]["wall_seconds"] - .01
    assert result["compute_metrics"]["input_bytes"] > 0
    assert result["compute_metrics"]["python_version"]
    if "peak_rss_kib" in result["compute_metrics"]:
        assert result["compute_metrics"]["user_cpu_seconds"] >= 0
        assert result["compute_metrics"]["system_cpu_seconds"] >= 0
        assert result["compute_metrics"]["peak_rss_kib"] > 0
        assert result["compute_metrics"]["peak_rss_unit"] == "KiB (Linux ru_maxrss)"
    assert result["site_profile"]["site_id"].startswith("remote-")
    assert "hostname" not in result


def test_compute_summary_contains_only_observability_fields():
    with tempfile.TemporaryDirectory(dir=ROOT / "runs") as temporary:
        run_dir = Path(temporary) / "run"
        experiments = run_dir / "experiments"
        experiments.mkdir(parents=True)
        (experiments / "EXP_001.json").write_text(json.dumps({
            "experiment_id": "EXP_001", "job_id": "REMOTE_001", "backend": "ssh_direct", "remote_pid": 9, "status": "COMPLETED", "cost": 3,
            "compute_observation": {"lifecycle_state": "COMPLETED", "site_profile": {"site_id": "ssh-opaque"}, "compute_metrics": {"wall_seconds": 2.5, "cpu_seconds": 1.5, "user_cpu_seconds": 1.0, "system_cpu_seconds": 0.5, "peak_rss_kib": 2048, "lifecycle": [{"state": "COMPLETED"}]}},
        }))
        tools = ExperimentTools.__new__(ExperimentTools)
        tools.run_dir = run_dir
        tools._write_compute_summary()
        summary = json.loads((run_dir / "compute_summary.json").read_text())
    assert summary["total_cost"] == 3
    assert summary["budget_units_used"] == 3
    assert summary["terminal_observation_count"] == 1
    assert summary["total_wall_seconds"] == 2.5
    assert summary["total_cpu_seconds"] == 1.5
    assert summary["peak_memory_mb"] == 2.0
    assert summary["remote_jobs"] == [{"job_id": "REMOTE_001", "backend": "ssh_direct", "remote_pid": 9, "status": "COMPLETED", "lifecycle_state": "COMPLETED", "lifecycle": [{"state": "COMPLETED"}]}]
    assert summary["experiments"][0]["experiment_id"] == "EXP_001"
    assert summary["site_profiles"] == [{"site_id": "ssh-opaque"}]
