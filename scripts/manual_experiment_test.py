from __future__ import annotations
import argparse, json, subprocess, sys, time
from pathlib import Path
from scidiagnose.config import Settings
from scidiagnose.experiment_tools import ExperimentTools
from scidiagnose.ssh_executor import SSHDirectExecutor
ROOT=Path(__file__).resolve().parents[1]
if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--host");args=parser.parse_args()
    subprocess.run([sys.executable,str(ROOT/"scripts"/"create_demo_case.py")],check=True)
    run=ROOT/"runs"/f"MANUAL_{int(time.time())}"; executor=SSHDirectExecutor(Settings(remote_host=args.host) if args.host else Settings()); tools=ExperimentTools(executor,ROOT/"cases"/"geo_001",run)
    identity=tools.compare(); repaired=tools.transform_and_compare("rot180")
    print(json.dumps({"identity":identity["result"],"rot180":repaired["result"]},indent=2))
