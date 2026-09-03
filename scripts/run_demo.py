from __future__ import annotations
import argparse,json,time
from pathlib import Path
from scidiagnose.agent import AgentAPIError, ManualAgent, OpenAICompatibleAgent
from scidiagnose.config import Settings
from scidiagnose.experiment_tools import ExperimentTools
from scidiagnose.runner import DiagnosisRunner
from scidiagnose.ssh_executor import SSHDirectExecutor
from scidiagnose.ssh_executor import RemoteExecutionError
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(); parser.add_argument("--case",default="geo_001");parser.add_argument("--backend",choices=["ssh"],default="ssh");parser.add_argument("--host");parser.add_argument("--agent",choices=["manual","api"],default="manual");args=parser.parse_args()
case=ROOT/"cases"/args.case; task=json.loads((case/"task.json").read_text()); initial=json.loads((case/"initial_result.json").read_text()); run=ROOT/"runs"/f"RUN_{int(time.time())}";run.mkdir(parents=True)
try:
    settings=Settings(remote_host=args.host) if args.host else Settings(); executor=SSHDirectExecutor(settings); agent=OpenAICompatibleAgent(settings) if args.agent=="api" else ManualAgent(); print(f"SciDiagnose\nCase: {task['case_id']}\nAgent: {args.agent}\nCompute backend: SSH Direct\nRemote host: {executor.settings.remote_host}\nBudget: {task['budget']}\nInitial agreement: {initial['agreement']}")
    state=DiagnosisRunner(agent,ExperimentTools(executor,case,run),run).run(task,initial)
except (RemoteExecutionError, TimeoutError, AgentAPIError) as exc:
    raise SystemExit(f"SciDiagnose execution error: {exc}")
print("FINAL DIAGNOSIS\n"+json.dumps(state.final_diagnosis,indent=2));print("Budget remaining:",state.budget_remaining)
