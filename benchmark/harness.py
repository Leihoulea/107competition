"""Repeatable, truth-blind benchmark execution and report generation.

This module deliberately never opens ``hidden`` directories.  Benchmark metrics
describe observable execution quality, not hidden-label accuracy.  A separate
competition evaluator may score labels after this harness has completed.
"""
from __future__ import annotations

import csv
import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable

import numpy as np


PUBLIC_FILES = ("task.json", "initial_result.json", "public/data/reference.npy", "public/data/target_faulty.npy")
TRANSFORMS: dict[str, Callable[[np.ndarray], np.ndarray]] = {
    "identity": lambda a: a,
    "flip_x": np.fliplr,
    "flip_y": np.flipud,
    "rot90": lambda a: np.rot90(a, 1),
    "rot180": lambda a: np.rot90(a, 2),
    "rot270": lambda a: np.rot90(a, 3),
    "transpose": np.transpose,
}


@dataclass(frozen=True)
class PublicCase:
    """The only case representation supplied to a benchmark method."""
    directory: Path
    task: dict[str, Any]
    initial: dict[str, Any]

    @classmethod
    def load(cls, directory: Path) -> "PublicCase":
        directory = directory.resolve()
        if "hidden" in {part.lower() for part in directory.parts}:
            raise ValueError("benchmark cases must be rooted outside hidden directories")
        missing = [name for name in PUBLIC_FILES if not (directory / name).is_file()]
        if missing:
            raise FileNotFoundError(f"missing public benchmark input(s): {', '.join(missing)}")
        return cls(directory, json.loads((directory / "task.json").read_text()), json.loads((directory / "initial_result.json").read_text()))

    def arrays(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Load only the named public arrays; hidden labels are not part of this API."""
        data = self.directory / "public" / "data"
        valid_path = data / "target_valid.npy"
        reference, target = np.load(data / "reference.npy"), np.load(data / "target_faulty.npy")
        valid = np.load(valid_path).astype(bool) if valid_path.exists() else np.ones(reference.shape, dtype=bool)
        return reference, target, valid


def _agreement(reference: np.ndarray, candidate: np.ndarray, valid: np.ndarray) -> float:
    if not valid.any():
        raise ValueError("candidate has no valid public pixels")
    return float((reference[valid] == candidate[valid]).mean())


def _record(case: PublicCase, method: str, repeat: int, started: float, final: dict[str, Any] | None, experiments: list[dict[str, Any]], error: str | None = None) -> dict[str, Any]:
    values = [float(x.get("agreement_valid", x.get("agreement", 0.0))) for x in experiments if x.get("agreement_valid", x.get("agreement")) is not None]
    evidence_ids = final.get("evidence_experiment_ids", []) if isinstance(final, dict) else []
    valid_ids = {x["experiment_id"] for x in experiments}
    return {
        "case_id": case.task["case_id"], "method": method, "repeat": repeat,
        "completed": error is None, "error": error, "elapsed_seconds": round(time.monotonic() - started, 6),
        "decision": final.get("decision") if isinstance(final, dict) else None,
        "confidence": final.get("confidence") if isinstance(final, dict) else None,
        "experiment_count": len(experiments), "best_agreement_valid": max(values, default=None),
        "initial_agreement": case.initial.get("agreement_valid", case.initial.get("agreement")),
        "threshold": case.task.get("expected_quality_threshold"),
        "cited_evidence_count": len([x for x in evidence_ids if x in valid_ids]),
        "final": final, "experiments": experiments,
    }


class RunReader:
    """Reads a completed SciDiagnose run artifact; it does not re-execute an agent."""
    def __init__(self, run_dir: Path) -> None: self.run_dir = run_dir

    def read(self, case: PublicCase, repeat: int) -> dict[str, Any]:
        started = time.monotonic()
        try:
            state = json.loads((self.run_dir / "state.json").read_text())
            final_path = self.run_dir / "final.json"
            final = json.loads(final_path.read_text()) if final_path.exists() else state.get("final_diagnosis")
            if state.get("case_id") != case.task["case_id"]:
                raise ValueError("run artifact case_id does not match public case")
            return _record(case, "scidiagnose_run_reader", repeat, started, final, state.get("experiments", []))
        except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
            return _record(case, "scidiagnose_run_reader", repeat, started, None, [], str(exc))


class BenchmarkHarness:
    """Runs public-data baselines and writes JSON, CSV, and Markdown reports."""
    def __init__(self, llm: Callable[[dict[str, Any]], dict[str, Any]] | None = None) -> None: self.llm = llm

    def deterministic_exhaustive(self, case: PublicCase, repeat: int) -> dict[str, Any]:
        started = time.monotonic()
        try:
            reference, target, valid = case.arrays(); experiments = []
            for index, (name, transform) in enumerate(TRANSFORMS.items(), 1):
                candidate, candidate_valid = transform(target), transform(valid)
                experiments.append({"experiment_id": f"BASE_{index:03d}", "operation": name, "agreement_valid": _agreement(reference, candidate, candidate_valid)})
            best = max(experiments, key=lambda item: item["agreement_valid"])
            threshold = float(case.task["expected_quality_threshold"])
            final = {"decision": "fault" if best["agreement_valid"] >= threshold else "no_fault", "confidence": 1.0, "evidence_experiment_ids": [best["experiment_id"]], "recommended_repair": {"operation": best["operation"]}}
            return _record(case, "deterministic_exhaustive", repeat, started, final, experiments)
        except (OSError, ValueError, TypeError) as exc:
            return _record(case, "deterministic_exhaustive", repeat, started, None, [], str(exc))

    def direct_llm(self, case: PublicCase, repeat: int) -> dict[str, Any]:
        return self._llm_run(case, repeat, "direct_llm", [])

    def one_shot_llm(self, case: PublicCase, repeat: int) -> dict[str, Any]:
        """One model-selected public operation, then a final model response."""
        started = time.monotonic()
        try:
            if self.llm is None: raise RuntimeError("LLM baseline requires an explicitly configured client")
            proposal = self.llm({"mode": "one_shot_plan", "task": case.task, "initial": case.initial, "allowed_operations": list(TRANSFORMS)})
            operation = proposal.get("operation")
            if operation not in TRANSFORMS: raise ValueError("LLM selected an unsupported operation")
            reference, target, valid = case.arrays(); candidate, candidate_valid = TRANSFORMS[operation](target), TRANSFORMS[operation](valid)
            experiment = {"experiment_id": "BASE_001", "operation": operation, "agreement_valid": _agreement(reference, candidate, candidate_valid)}
            final = self.llm({"mode": "one_shot_final", "task": case.task, "initial": case.initial, "experiment": experiment})
            return _record(case, "one_shot_llm", repeat, started, final, [experiment])
        except (OSError, RuntimeError, ValueError, TypeError) as exc:
            return _record(case, "one_shot_llm", repeat, started, None, [], str(exc))

    def _llm_run(self, case: PublicCase, repeat: int, method: str, experiments: list[dict[str, Any]]) -> dict[str, Any]:
        started = time.monotonic()
        try:
            if self.llm is None: raise RuntimeError("LLM baseline requires an explicitly configured client")
            final = self.llm({"mode": "direct_final", "task": case.task, "initial": case.initial})
            return _record(case, method, repeat, started, final, experiments)
        except (RuntimeError, ValueError, TypeError) as exc:
            return _record(case, method, repeat, started, None, experiments, str(exc))

    def run(self, cases: Iterable[PublicCase], methods: Iterable[str], repeats: int, run_reader: RunReader | None = None) -> list[dict[str, Any]]:
        dispatch = {"direct_llm": self.direct_llm, "one_shot_llm": self.one_shot_llm, "deterministic_exhaustive": self.deterministic_exhaustive}
        rows = []
        for case in cases:
            for repeat in range(1, repeats + 1):
                for method in methods:
                    if method == "scidiagnose_run_reader":
                        if run_reader is None: raise ValueError("--run-dir is required for scidiagnose_run_reader")
                        rows.append(run_reader.read(case, repeat))
                    elif method in dispatch: rows.append(dispatch[method](case, repeat))
                    else: raise ValueError(f"unknown benchmark method: {method}")
        return rows

    @staticmethod
    def write_reports(rows: list[dict[str, Any]], output_dir: Path) -> None:
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "results.json").write_text(json.dumps(rows, indent=2))
        fields = ["case_id", "method", "repeat", "completed", "error", "elapsed_seconds", "decision", "confidence", "experiment_count", "best_agreement_valid", "initial_agreement", "threshold", "cited_evidence_count"]
        with (output_dir / "results.csv").open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader(); writer.writerows({key: row.get(key) for key in fields} for row in rows)
        table = ["| case | method | repeat | completed | decision | best agreement | experiments |", "|---|---|---:|---|---|---:|---:|"]
        table += [f"| {r['case_id']} | {r['method']} | {r['repeat']} | {r['completed']} | {r['decision'] or ''} | {r['best_agreement_valid'] if r['best_agreement_valid'] is not None else ''} | {r['experiment_count']} |" for r in rows]
        (output_dir / "results.md").write_text("# SciDiagnose public-input benchmark\n\nMetrics are truth-blind; no hidden case data was read.\n\n" + "\n".join(table) + "\n")
