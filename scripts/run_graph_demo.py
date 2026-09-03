"""Run the auditable LangGraph diagnosis workflow against a public case."""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from scidiagnose.agent import AgentAPIError, ManualAgent, OpenAICompatibleAgent
from scidiagnose.config import Settings
from scidiagnose.diagnosis_graph import DiagnosisGraph
from scidiagnose.experiment_tools import ExperimentTools
from scidiagnose.ssh_executor import RemoteExecutionError, SSHDirectExecutor


ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--case", default="b02")
parser.add_argument("--host")
parser.add_argument("--agent", choices=["manual", "api"], default="manual")
parser.add_argument("--max-steps", type=int, default=8)
args = parser.parse_args()

case = ROOT / "cases" / args.case
task = json.loads((case / "task.json").read_text())
initial = json.loads((case / "initial_result.json").read_text())
run = ROOT / "runs" / f"RUN_{task['case_id']}_GRAPH_{int(time.time())}"
run.mkdir(parents=True)

try:
    settings = Settings(remote_host=args.host) if args.host else Settings()
    executor = SSHDirectExecutor(settings)
    agent = OpenAICompatibleAgent(settings) if args.agent == "api" else ManualAgent()
    state = {
        "run_id": run.name,
        "case_id": task["case_id"],
        "task": task,
        "initial_observation": initial,
        "experiments": [],
        "evidence": [],
        "budget_total": task["budget"],
        "budget_remaining": task["budget"],
        "steps_used": 0,
        "max_steps": args.max_steps,
        "quality_threshold": task["expected_quality_threshold"],
        "diagnosis_status": "new",
        "knowledge_queries": [],
        "knowledge_evidence": [],
    }
    result = DiagnosisGraph(agent, ExperimentTools(executor, case, run), run).run(state)
except (RemoteExecutionError, TimeoutError, AgentAPIError) as exc:
    raise SystemExit(f"SciDiagnose graph execution error: {exc}")

print(f"Trace: {run / 'trace.jsonl'}")
print("FINAL DIAGNOSIS\n" + json.dumps(result["final_diagnosis"], indent=2))
