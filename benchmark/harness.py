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
SHIFT_VALUES = range(-5, 6)
REPAIR_IMPROVEMENT_MARGIN = 1e-3


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


def _shift_without_wrap(array: np.ndarray, dr: int, dc: int) -> tuple[np.ndarray, np.ndarray]:
    """Match the public remote runner's non-wrapping shift semantics."""
    output = np.zeros_like(array)
    coverage = np.zeros(array.shape, dtype=bool)
    source_rows = slice(max(0, -dr), min(array.shape[0], array.shape[0] - dr))
    destination_rows = slice(max(0, dr), min(array.shape[0], array.shape[0] + dr))
    source_columns = slice(max(0, -dc), min(array.shape[1], array.shape[1] - dc))
    destination_columns = slice(max(0, dc), min(array.shape[1], array.shape[1] + dc))
    output[destination_rows, destination_columns] = array[source_rows, source_columns]
    coverage[destination_rows, destination_columns] = True
    return output, coverage


def _apply_pipeline(target: np.ndarray, valid: np.ndarray, pipeline: list[dict[str, Any]]) -> tuple[np.ndarray, np.ndarray]:
    if not isinstance(pipeline, list) or len(pipeline) > 4:
        raise ValueError("candidate pipeline must contain 0 to 4 steps")
    candidate, candidate_valid = target.copy(), valid.astype(bool).copy()
    for step in pipeline:
        if not isinstance(step, dict):
            raise ValueError("candidate pipeline step must be an object")
        if step.get("type") == "transform":
            operation = step.get("operation")
            if operation not in TRANSFORMS:
                raise ValueError("candidate transform operation is unsupported")
            candidate, candidate_valid = TRANSFORMS[operation](candidate), TRANSFORMS[operation](candidate_valid)
        elif step.get("type") == "shift":
            dr, dc = step.get("dr"), step.get("dc")
            if type(dr) is not int or type(dc) is not int or dr not in SHIFT_VALUES or dc not in SHIFT_VALUES:
                raise ValueError("candidate shift must use integer dr and dc in [-5, 5]")
            candidate, _ = _shift_without_wrap(candidate, dr, dc)
            shifted_valid, _ = _shift_without_wrap(candidate_valid.astype(np.uint8), dr, dc)
            candidate_valid = shifted_valid.astype(bool)
        else:
            raise ValueError("candidate pipeline step must be transform or shift")
    return candidate, candidate_valid


def _pipeline(experiment: dict[str, Any]) -> list[dict[str, Any]]:
    arguments = experiment.get("arguments", experiment) or {}
    if isinstance(arguments.get("pipeline"), list):
        return arguments["pipeline"]
    if "operation" in arguments:
        return [{"type": "transform", "operation": arguments["operation"]}]
    if "dr" in arguments and "dc" in arguments:
        return [{"type": "shift", "dr": arguments["dr"], "dc": arguments["dc"]}]
    return []


def _is_non_identity_repair(experiment: dict[str, Any]) -> bool:
    pipeline = _pipeline(experiment)
    return bool(pipeline) and any(
        step.get("type") == "shift" and (step.get("dr") or step.get("dc"))
        or step.get("type") == "transform" and step.get("operation") != "identity"
        for step in pipeline
    )


def _metrics(experiment: dict[str, Any]) -> dict[str, Any]:
    result = experiment.get("result", experiment)
    return result.get("metrics", result) if isinstance(result, dict) else {}


def _number(value: Any) -> float | None:
    return float(value) if isinstance(value, (int, float)) and not isinstance(value, bool) else None


def _compute_metrics(experiment: dict[str, Any]) -> dict[str, Any]:
    result = experiment.get("result", experiment)
    observation = experiment.get("compute_observation", {})
    if isinstance(observation, dict) and isinstance(observation.get("compute_metrics"), dict):
        return observation["compute_metrics"]
    if isinstance(result, dict) and isinstance(result.get("compute_metrics"), dict):
        return result["compute_metrics"]
    return _metrics(experiment)


def _record(case: PublicCase, method: str, repeat: int, started: float, final: dict[str, Any] | None, experiments: list[dict[str, Any]], error: str | None = None, compute_summary: dict[str, Any] | None = None) -> dict[str, Any]:
    values = [_number(_metrics(x).get("agreement_valid", _metrics(x).get("agreement"))) for x in experiments]
    values = [value for value in values if value is not None]
    evidence_ids = final.get("evidence_experiment_ids", []) if isinstance(final, dict) else []
    valid_ids = {x.get("experiment_id") for x in experiments}
    costs = [_number(x.get("cost")) for x in experiments]
    wall = [_number(_compute_metrics(x).get("wall_seconds", _compute_metrics(x).get("elapsed_seconds"))) for x in experiments]
    cpu = [
        (_number(_compute_metrics(x).get("user_cpu_seconds")) or 0.0) + (_number(_compute_metrics(x).get("system_cpu_seconds")) or 0.0)
        if _number(_compute_metrics(x).get("user_cpu_seconds")) is not None or _number(_compute_metrics(x).get("system_cpu_seconds")) is not None
        else _number(_compute_metrics(x).get("process_cpu_seconds", _compute_metrics(x).get("cpu_seconds")))
        for x in experiments
    ]
    budget_used = sum(cost for cost in costs if cost is not None) if costs and all(cost is not None for cost in costs) else None
    initial = _number(case.initial.get("agreement_valid", case.initial.get("agreement")))
    best = max(values, default=None)
    cited = len([x for x in evidence_ids if x in valid_ids])
    threshold = float(case.task["expected_quality_threshold"])
    repaired = [
        experiment for experiment in experiments
        if _is_non_identity_repair(experiment)
        and (metric := _number(_metrics(experiment).get("agreement_valid", _metrics(experiment).get("agreement")))) is not None
        and initial is not None
        and initial < threshold
        and metric >= threshold
        and metric - initial >= REPAIR_IMPROVEMENT_MARGIN
    ]
    repair_success = bool(cited and any(experiment.get("experiment_id") in evidence_ids for experiment in repaired)) if isinstance(final, dict) and final.get("decision") == "fault" else None
    summary = compute_summary or {}
    summary_wall, summary_cpu = _number(summary.get("total_wall_seconds")), _number(summary.get("total_cpu_seconds"))
    return {
        "case_id": case.task["case_id"], "method": method, "repeat": repeat,
        "completed": error is None, "error": error, "elapsed_seconds": round(time.monotonic() - started, 6),
        "decision": final.get("decision") if isinstance(final, dict) else None,
        "confidence": final.get("confidence") if isinstance(final, dict) else None,
        "fault_family": final.get("fault_family") if isinstance(final, dict) else None,
        "root_cause": final.get("root_cause") if isinstance(final, dict) else None,
        "recommended_repair": final.get("recommended_repair") if isinstance(final, dict) else None,
        "experiment_count": len(experiments), "best_agreement_valid": max(values, default=None),
        "initial_agreement": initial,
        "threshold": case.task.get("expected_quality_threshold"),
        "cited_evidence_count": cited, "validated_repair_success": repair_success,
        "false_positive": None, "budget_units_used": budget_used,
        "remote_jobs": len(summary["remote_jobs"]) if isinstance(summary.get("remote_jobs"), list) else sum(1 for x in experiments if x.get("backend") not in {None, "local", "fake"}),
        "compute_wall_seconds": summary_wall if summary_wall is not None else sum(x for x in wall if x is not None) if any(x is not None for x in wall) else None,
        "compute_cpu_seconds": summary_cpu if summary_cpu is not None else sum(x for x in cpu if x is not None) if any(x is not None for x in cpu) else None,
        "evidence_backed": bool(cited),
        "diagnostic_efficiency": ((best - initial) / budget_used if best is not None and initial is not None and budget_used else None),
        "final": final, "experiments": experiments,
    }


class RunReader:
    """Reads a completed SciDiagnose run artifact; it does not re-execute an agent."""
    def __init__(self, run_dir: Path) -> None: self.run_dir = run_dir

    def _experiment_artifacts(self) -> list[dict[str, Any]]:
        artifacts = self.run_dir / "experiments"
        records = []
        for path in sorted(artifacts.glob("EXP_*.json")) if artifacts.exists() else []:
            if path.name.endswith(".request.json"):
                continue
            records.append(json.loads(path.read_text()))
        return records

    def read(self, case: PublicCase, repeat: int) -> dict[str, Any]:
        started = time.monotonic()
        try:
            state_path, trace_path = self.run_dir / "state.json", self.run_dir / "trace.jsonl"
            final_path, summary_path = self.run_dir / "final.json", self.run_dir / "compute_summary.json"
            experiments = self._experiment_artifacts()
            summary = json.loads(summary_path.read_text()) if summary_path.exists() else None
            if state_path.exists():
                state = json.loads(state_path.read_text())
                final = json.loads(final_path.read_text()) if final_path.exists() else state.get("final_diagnosis")
                if state.get("case_id") != case.task["case_id"]: raise ValueError("run artifact case_id does not match public case")
                return _record(case, "scidiagnose_run_reader", repeat, started, final, experiments or state.get("experiments", []), compute_summary=summary)
            events = [json.loads(line) for line in trace_path.read_text().splitlines() if line.strip()]
            trace_experiments = [{key: event.get(key) for key in ("experiment_id", "tool", "arguments", "cost", "backend", "remote_host", "remote_pid", "result", "compute_observation")} for event in events if event.get("node") == "execute"]
            final_events = [event for event in events if event.get("node") == "finalize"]
            if not final_events: raise ValueError("trace has no finalize event")
            return _record(case, "scidiagnose_run_reader", repeat, started, final_events[-1].get("final"), experiments or trace_experiments, compute_summary=summary)
        except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
            return _record(case, "scidiagnose_run_reader", repeat, started, None, [], str(exc))


class BenchmarkHarness:
    """Runs public-data baselines and writes JSON, CSV, and Markdown reports."""
    def __init__(self, llm: Callable[[dict[str, Any]], dict[str, Any]] | None = None) -> None: self.llm = llm

    @staticmethod
    def _baseline_final(case: PublicCase, best: dict[str, Any]) -> dict[str, Any]:
        initial = _number(case.initial.get("agreement_valid", case.initial.get("agreement")))
        threshold = float(case.task["expected_quality_threshold"])
        metric = _number(_metrics(best).get("agreement_valid", _metrics(best).get("agreement")))
        fault = bool(
            initial is not None and metric is not None and initial < threshold
            and metric >= threshold and metric - initial >= REPAIR_IMPROVEMENT_MARGIN
            and _is_non_identity_repair(best)
        )
        return {
            "decision": "fault" if fault else "no_fault",
            "fault_family": "spatial_transform" if fault else "no_fault",
            "root_cause": "best public repair candidate" if fault else "no validated public repair was required",
            "confidence": 1.0,
            "evidence_experiment_ids": [best["experiment_id"]] if fault else [],
            "recommended_repair": {"pipeline": _pipeline(best)} if fault else {},
        }

    def deterministic_transform_sweep(self, case: PublicCase, repeat: int) -> dict[str, Any]:
        started = time.monotonic()
        try:
            reference, target, valid = case.arrays(); experiments = []
            for index, (name, transform) in enumerate(TRANSFORMS.items(), 1):
                candidate, candidate_valid = transform(target), transform(valid)
                experiments.append({"experiment_id": f"BASE_{index:03d}", "arguments": {"pipeline": [{"type": "transform", "operation": name}]}, "cost": 4, "agreement_valid": _agreement(reference, candidate, candidate_valid)})
            best = max(experiments, key=lambda item: item["agreement_valid"])
            return _record(case, "deterministic_transform_sweep", repeat, started, self._baseline_final(case, best), experiments)
        except (OSError, ValueError, TypeError) as exc:
            return _record(case, "deterministic_transform_sweep", repeat, started, None, [], str(exc))

    def deterministic_full_search(self, case: PublicCase, repeat: int) -> dict[str, Any]:
        """Exhaustively evaluate all public transform-plus-shift candidates."""
        started = time.monotonic()
        try:
            reference, target, valid = case.arrays(); experiments = []
            for transform_name in TRANSFORMS:
                for dr in SHIFT_VALUES:
                    for dc in SHIFT_VALUES:
                        pipeline = [{"type": "transform", "operation": transform_name}, {"type": "shift", "dr": dr, "dc": dc}]
                        candidate, candidate_valid = _apply_pipeline(target, valid, pipeline)
                        experiments.append({"experiment_id": f"FULL_{len(experiments) + 1:03d}", "arguments": {"pipeline": pipeline}, "cost": 5, "agreement_valid": _agreement(reference, candidate, candidate_valid)})
            best = max(experiments, key=lambda item: item["agreement_valid"])
            return _record(case, "deterministic_full_search", repeat, started, self._baseline_final(case, best), experiments)
        except (OSError, ValueError, TypeError) as exc:
            return _record(case, "deterministic_full_search", repeat, started, None, [], str(exc))

    def deterministic_exhaustive(self, case: PublicCase, repeat: int) -> dict[str, Any]:
        """Backward-compatible alias for the original transform-only baseline."""
        return self.deterministic_transform_sweep(case, repeat)

    def direct_llm(self, case: PublicCase, repeat: int) -> dict[str, Any]:
        return self._llm_run(case, repeat, "direct_llm", [])

    def one_shot_llm(self, case: PublicCase, repeat: int) -> dict[str, Any]:
        """One model-selected complete public repair candidate, then a final response."""
        started = time.monotonic()
        try:
            if self.llm is None: raise RuntimeError("LLM baseline requires an explicitly configured client")
            contract = {"pipeline": "one to four steps; each step is transform(operation in allowed_transforms) or shift(dr/dc integers in [-5,5])", "allowed_transforms": list(TRANSFORMS)}
            proposal = self.llm({"mode": "one_shot_plan", "task": case.task, "initial": case.initial, "candidate_contract": contract})
            pipeline = proposal.get("pipeline")
            reference, target, valid = case.arrays(); candidate, candidate_valid = _apply_pipeline(target, valid, pipeline)
            experiment = {"experiment_id": "BASE_001", "arguments": {"pipeline": pipeline}, "cost": 3 + len(pipeline), "agreement_valid": _agreement(reference, candidate, candidate_valid)}
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
        dispatch = {
            "direct_llm": self.direct_llm,
            "one_shot_llm": self.one_shot_llm,
            "deterministic_transform_sweep": self.deterministic_transform_sweep,
            "deterministic_full_search": self.deterministic_full_search,
            "deterministic_exhaustive": self.deterministic_exhaustive,
        }
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
    def score_posthoc(rows: list[dict[str, Any]], truth_mapping: dict[str, Any] | None = None, evaluator: Callable[[dict[str, Any], Any], dict[str, Any]] | None = None) -> list[dict[str, Any]]:
        """Attach optional post-run scores from caller-supplied truth or evaluator.

        This API intentionally accepts values rather than paths: it never discovers or
        reads hidden files, and it is called only after all LLM/agent invocations end.
        """
        if truth_mapping is None and evaluator is None: raise ValueError("provide truth_mapping or evaluator explicitly")
        scored = []
        for row in rows:
            copy = dict(row); truth = truth_mapping.get(row["case_id"]) if truth_mapping else None
            if evaluator is not None:
                copy.update(evaluator(dict(row), truth))
            elif isinstance(truth, dict):
                expected = truth.get("decision"); copy["false_positive"] = row.get("decision") == "fault" and expected != "fault"
                copy["fault_detection_correct"] = row.get("decision") == expected if expected in {"fault", "no_fault"} else None
                expected_family = truth.get("fault_family")
                copy["fault_family_correct"] = row.get("fault_family") == expected_family if expected_family is not None else None
            else: copy["false_positive"] = None
            scored.append(copy)
        return scored

    @staticmethod
    def write_reports(rows: list[dict[str, Any]], output_dir: Path) -> None:
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "results.json").write_text(json.dumps(rows, indent=2))
        fields = ["case_id", "method", "repeat", "completed", "error", "elapsed_seconds", "decision", "confidence", "fault_family", "validated_repair_success", "false_positive", "budget_units_used", "remote_jobs", "compute_wall_seconds", "compute_cpu_seconds", "evidence_backed", "diagnostic_efficiency", "experiment_count", "best_agreement_valid", "initial_agreement", "threshold", "cited_evidence_count"]
        with (output_dir / "results.csv").open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader(); writer.writerows({key: row.get(key) for key in fields} for row in rows)
        table = ["| case | method | repeat | completed | decision | best agreement | experiments |", "|---|---|---:|---|---|---:|---:|"]
        table += [f"| {r['case_id']} | {r['method']} | {r['repeat']} | {r['completed']} | {r['decision'] or ''} | {r['best_agreement_valid'] if r['best_agreement_valid'] is not None else ''} | {r['experiment_count']} |" for r in rows]
        (output_dir / "results.md").write_text("# SciDiagnose public-input benchmark\n\nMetrics are truth-blind; no hidden case data was read.\n\n" + "\n".join(table) + "\n")
