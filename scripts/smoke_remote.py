from __future__ import annotations
import argparse, json, sys, time
from pathlib import Path
from scidiagnose.config import Settings
from scidiagnose.ssh_executor import RemoteExecutionError, SSHDirectExecutor
ROOT = Path(__file__).resolve().parents[1]
def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--host"); args = parser.parse_args()
    settings = Settings(remote_host=args.host) if args.host else Settings(); executor = SSHDirectExecutor(settings); connection = executor.check_connection()
    print("=== SciDiagnose Remote Smoke Test ===\nBackend: SSH Direct\nHost:", connection.get("hostname"))
    if not connection["ok"]: print(connection["error"], file=sys.stderr); return 1
    try:
        executor.ensure_remote_workspace(); executor.upload(ROOT / "remote" / "hello_job.py", f"{executor.workspace}/scripts/hello_job.py")
        job = executor.submit(f"EXP_SMOKE_{int(time.time())}", [executor.remote_python, f"{executor.workspace}/scripts/hello_job.py"])
        print(f"Experiment: {job.job_id}\nRemote PID: {job.remote_pid}"); state = executor.wait(job, callback=print); print("Final state:", state)
        stdout, stderr = executor.logs(job)
        if state != "COMPLETED": print("stdout:\n"+stdout); print("stderr:\n"+stderr, file=sys.stderr); print(json.dumps(executor.fetch_failure(job), indent=2), file=sys.stderr); return 1
        print("Result:\n"+json.dumps(executor.fetch_result(job), indent=2)); print("PASS"); return 0
    except (RemoteExecutionError, TimeoutError, FileNotFoundError) as exc: print(f"FAIL: {exc}", file=sys.stderr); return 1
if __name__ == "__main__": raise SystemExit(main())
