"""Run the auditable LangGraph diagnosis workflow against a public case."""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from scidiagnose.agent import ManualAgent, OpenAICompatibleAgent
from scidiagnose.config import Settings
from scidiagnose.diagnosis_graph import DiagnosisGraph
from scidiagnose.experiment_tools import ExperimentTools
from scidiagnose.run_artifacts import write_failure_artifact
from scidiagnose.ssh_executor import SSHDirectExecutor


parser = argparse.ArgumentParser()
parser.add_argument("--case", default="b02")
parser.add_argument("--case-dir", type=Path, help="public case directory outside cases/ (for example cases_real/r01)")
parser.add_argument("--host")
parser.add_argument("--agent", choices=["manual", "api"], default="manual")
parser.add_argument("--max-steps", type=int, default=8)
parser.add_argument("--run-id", help="Optional stable run directory name under runs/.")
args = parser.parse_args()


case = args.case_dir.resolve() if args.case_dir else ROOT / "cases" / args.case
task = json.loads((case / "task.json").read_text())
initial = json.loads((case / "initial_result.json").read_text())
run = ROOT / "runs" / (args.run_id or f"RUN_{task['case_id']}_GRAPH_{int(time.time())}")
if run.exists():
    raise SystemExit(f"Run directory already exists: {run}")
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
    (run / "state.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (run / "final.json").write_text(json.dumps(result["final_diagnosis"], indent=2), encoding="utf-8")
except BaseException as exc:
    # Persist partial traces for ordinary errors and user/process interrupts.
    # This is intentionally after the run directory is created, so a failed
    # real backend invocation is still a reviewable benchmark artifact.
    artifact = write_failure_artifact(run, exc)
    raise SystemExit(f"SciDiagnose graph execution error: {exc}\nFailure artifact: {artifact}")

print(f"Trace: {run / 'trace.jsonl'}")
print("FINAL DIAGNOSIS\n" + json.dumps(result["final_diagnosis"], indent=2))
