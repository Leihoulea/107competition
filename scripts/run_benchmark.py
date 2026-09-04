"""Run truth-blind SciDiagnose benchmark baselines."""
from __future__ import annotations
import argparse
from pathlib import Path
from benchmark.harness import BenchmarkHarness, PublicCase, RunReader
from scidiagnose.agent import OpenAICompatibleAgent
from scidiagnose.config import Settings

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--cases", nargs="+", default=["b01", "b02", "b03"])
parser.add_argument("--methods", nargs="+", default=["deterministic_exhaustive"])
parser.add_argument("--repeats", type=int, default=1)
parser.add_argument("--output-dir", type=Path, default=ROOT / "benchmark" / "results")
parser.add_argument("--run-dir", type=Path, help="completed SciDiagnose artifact for scidiagnose_run_reader")
parser.add_argument("--use-api-llm", action="store_true", help="use configured OpenAI-compatible credentials for LLM baselines")
args = parser.parse_args()
if args.repeats < 1: parser.error("--repeats must be at least one")
cases = [PublicCase.load(ROOT / "cases" / name) for name in args.cases]
def api_llm(context):
    agent = OpenAICompatibleAgent(Settings())
    mode = context["mode"]
    schemas = {
        "direct_final": {"decision": "fault|no_fault", "fault_family": "string", "root_cause": "string", "confidence": 0.0, "evidence_experiment_ids": [], "recommended_repair": {}},
        "one_shot_plan": {"operation": "identity|flip_x|flip_y|rot90|rot180|rot270|transpose"},
        "one_shot_final": {"decision": "fault|no_fault", "fault_family": "string", "root_cause": "string", "confidence": 0.0, "evidence_experiment_ids": ["BASE_001"], "recommended_repair": {}},
    }
    return agent._request_json("benchmark " + mode + "; use only the supplied public context and do not claim unexecuted evidence", context, schemas[mode])

llm = api_llm if args.use_api_llm else None
rows = BenchmarkHarness(llm).run(cases, args.methods, args.repeats, RunReader(args.run_dir) if args.run_dir else None)
BenchmarkHarness.write_reports(rows, args.output_dir)
print(f"Wrote {len(rows)} records to {args.output_dir}")
