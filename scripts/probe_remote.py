from __future__ import annotations
import argparse, json
from scidiagnose.config import Settings
from scidiagnose.ssh_executor import SSHDirectExecutor
parser = argparse.ArgumentParser(); parser.add_argument("--host"); args = parser.parse_args()
settings = Settings(remote_host=args.host) if args.host else Settings(); executor = SSHDirectExecutor(settings)
report = {"connection":executor.check_connection(), "probe":executor.probe()}
print(json.dumps(report, indent=2)); print("\nSummary:", "SSH OK" if report["connection"]["ok"] else "SSH FAILED"); print("Python:", report["probe"]["python_version"], "| NumPy:", report["probe"]["numpy"], "| GPU:", report["probe"]["gpu"])
