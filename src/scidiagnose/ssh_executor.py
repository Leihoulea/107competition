"""SSH Direct backend using nohup, a PID, and structured result files."""
from __future__ import annotations
import json, re, subprocess, time
from collections.abc import Callable
from pathlib import Path
from typing import Any
from .config import Settings
from .executor_base import ComputeExecutor, JobHandle

_EXP = re.compile(r"^[A-Za-z0-9_-]+$")
class RemoteExecutionError(RuntimeError): pass

class SSHDirectExecutor(ComputeExecutor):
    TERMINAL_STATES = {"COMPLETED", "FAILED"}
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or Settings()
        self._workspace = self._safe(self.settings.remote_workspace, "path")
        self._python = self._safe(self.settings.remote_python, "Python path")
    def _connection_options(self) -> list[str]:
        # Deliberately use short independent sessions. Windows OpenSSH control
        # sockets can become stale after an intermittent network disconnect.
        return ["-o", "BatchMode=yes", "-o", "ConnectTimeout=15", "-o", "ConnectionAttempts=1", "-o", "ServerAliveInterval=5", "-o", "ServerAliveCountMax=3", "-o", "TCPKeepAlive=yes", "-o", "ControlMaster=no"]
    @staticmethod
    def _safe(value: str, label: str) -> str:
        if not re.fullmatch(r"[A-Za-z0-9_./~$-]+", value): raise ValueError(f"Remote {label} contains unsupported characters")
        return value.replace("~", "$HOME", 1)
    def _run(self, args: list[str], check: bool = True, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
        try:
            limit = timeout or self.settings.command_timeout
            result = subprocess.run(args, text=True, capture_output=True, timeout=limit)
        except subprocess.TimeoutExpired as exc:
            target = " ".join(args[:5])
            raise RemoteExecutionError(f"Timed out after {limit}s: {target}. Check SSH connectivity and retry.") from exc
        if check and result.returncode:
            raise RemoteExecutionError(result.stderr.strip() or result.stdout.strip() or f"command failed ({result.returncode})")
        return result
    def _ssh(self, command: str, check: bool = True, retries: int = 1) -> subprocess.CompletedProcess[str]:
        """Retry idempotent SSH commands once."""
        args=["ssh", *self._connection_options(), self.settings.remote_host, command]
        for attempt in range(retries + 1):
            try:
                return self._run(args, check, timeout=self.settings.ssh_timeout)
            except RemoteExecutionError as exc:
                if attempt == retries:
                    if str(exc).startswith("Timed out"):
                        raise RemoteExecutionError(f"Remote SSH command timed out: {command}") from exc
                    raise
                time.sleep(2)
        raise AssertionError("unreachable")
    def check_connection(self) -> dict[str, Any]:
        result = self._ssh("hostname", False)
        return {"ok": result.returncode == 0, "hostname": result.stdout.strip(), "error": result.stderr.strip()}
    def probe(self) -> dict[str, Any]:
        commands = {"hostname":"hostname", "uname":"uname -a", "os_release":"cat /etc/os-release", "python3":"command -v python3", "python_version":"python3 --version", "pip3":"command -v pip3", "conda":"command -v conda", "micromamba":"command -v micromamba", "nvidia_smi":"command -v nvidia-smi", "cpu":"lscpu", "memory":"free -h", "home_disk":"df -h \"$HOME\"", "numpy":f"{self._python} -c 'import numpy; print(numpy.__version__)'"}
        info = {key:self._ssh(command, False).stdout.strip() or "NOT_AVAILABLE" for key, command in commands.items()}
        info["gpu"] = self._ssh("nvidia-smi", False).stdout.strip() if info["nvidia_smi"] != "NOT_AVAILABLE" else "NOT_AVAILABLE"
        return info
    def ensure_remote_workspace(self) -> None:
        self._ssh(f"mkdir -p {self._workspace}/inputs {self._workspace}/experiments {self._workspace}/results {self._workspace}/logs {self._workspace}/scripts {self._workspace}/jobs")
    @property
    def workspace(self) -> str: return self._workspace
    @property
    def remote_python(self) -> str: return self._python
    def job_dir(self, experiment_id: str) -> str:
        if not _EXP.fullmatch(experiment_id): raise ValueError("experiment_id must contain only letters, digits, _ or -")
        return f"{self._workspace}/jobs/{experiment_id}"
    def create_job_dir(self, experiment_id: str) -> str:
        directory = self.job_dir(experiment_id); self._ssh(f"mkdir -p {directory}"); return directory
    def upload(self, local_path: str | Path, remote_path: str) -> None:
        path = Path(local_path)
        if not path.is_file(): raise FileNotFoundError(f"Local file does not exist: {path}")
        self._safe(remote_path, "path")
        # scp expands a leading ~/ remotely; it does not expand a literal $HOME.
        scp_path = remote_path.replace("$HOME", "~", 1)
        self._run(["scp", *self._connection_options(), str(path), f"{self.settings.remote_host}:{scp_path}"])
    def submit(self, experiment_id: str, command: list[str]) -> JobHandle:
        if not command or any(not isinstance(v, str) for v in command): raise ValueError("command must be a non-empty list of strings")
        directory = self.create_job_dir(experiment_id)
        if any(not re.fullmatch(r"[A-Za-z0-9_./~$=-]+", value) for value in command): raise ValueError("command contains unsupported characters")
        # A durable PID marker makes retrying an interrupted SSH response safe: a retry
        # returns the already-started task instead of launching a duplicate task.
        launch = f"cd {directory}; if test -s remote.pid; then cat remote.pid; else nohup {' '.join(command)} > stdout.log 2> stderr.log < /dev/null & pid=$!; echo $pid > remote.pid; echo $pid; fi"
        output = self._ssh(launch, retries=1).stdout.strip()
        pid = output.splitlines()[-1] if output else ""
        if not pid.isdigit(): raise RemoteExecutionError(f"Could not parse remote PID from: {output!r}")
        return JobHandle(experiment_id, "ssh_direct", self.settings.remote_host, int(pid), directory)
    def is_process_alive(self, job: JobHandle) -> bool:
        return bool(job.remote_pid) and self._ssh(f"kill -0 {job.remote_pid}", False).returncode == 0
    def status(self, job: JobHandle) -> str:
        if job.remote_pid is None: return "FAILED"
        check = f"if test -f {job.job_dir}/result.json; then echo COMPLETED; elif test -f {job.job_dir}/failure.json; then echo FAILED; elif kill -0 {job.remote_pid} 2>/dev/null; then echo RUNNING; else echo FAILED; fi"
        state = self._ssh(check).stdout.strip()
        if state in {"COMPLETED", "FAILED", "RUNNING"}: return state
        raise RemoteExecutionError(f"Unexpected remote status response for {job.job_id}: {state!r}")
    def wait(self, job: JobHandle, poll_interval: float = 1, timeout: float = 300, callback: Callable[[str], None] | None = None) -> str:
        deadline, previous, last_error = time.monotonic() + timeout, None, None
        while time.monotonic() < deadline:
            try:
                state = self.status(job)
            except RemoteExecutionError as exc:
                last_error = exc
                if previous != "UNREACHABLE" and callback: callback("UNREACHABLE (retrying)")
                previous = "UNREACHABLE"; time.sleep(poll_interval); continue
            if state != previous and callback: callback(state)
            if state in self.TERMINAL_STATES: return state
            previous = state; time.sleep(poll_interval)
        suffix = f"; last connection error: {last_error}" if last_error else ""
        raise TimeoutError(f"Timed out waiting for {job.job_id}{suffix}")
    def logs(self, job: JobHandle, tail: int = 100) -> tuple[str, str]:
        if tail < 1: raise ValueError("tail must be positive")
        try:
            return (self._ssh(f"tail -n {tail} {job.job_dir}/stdout.log", False).stdout, self._ssh(f"tail -n {tail} {job.job_dir}/stderr.log", False).stdout)
        except RemoteExecutionError as exc:
            return ("", f"log retrieval unavailable: {exc}")
    def _json(self, path: str) -> dict[str, Any]:
        try: return json.loads(self._ssh(f"cat {path}").stdout)
        except json.JSONDecodeError as exc: raise RemoteExecutionError(f"Invalid remote JSON: {path}") from exc
    def fetch_result(self, job: JobHandle) -> dict[str, Any]: return self._json(f"{job.job_dir}/result.json")
    def fetch_failure(self, job: JobHandle) -> dict[str, Any]: return self._json(f"{job.job_dir}/failure.json")
