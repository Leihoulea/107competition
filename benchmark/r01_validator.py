"""Deterministic evaluator-private validation for the R01 historical case."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np

from .harness import TRANSFORMS


HISTORICAL_BEFORE = 0.5381503121692608
HISTORICAL_AFTER = 0.7961290682839249
HISTORICAL_TOLERANCE = 0.01


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _manifest_sha256(paths: list[Path], root: Path) -> str:
    """Stable checksum for the complete public-case contract."""
    digest = hashlib.sha256()
    for path in sorted(paths):
        digest.update(str(path.relative_to(root)).replace("\\", "/").encode("utf-8"))
        digest.update(b"\0")
        digest.update(_sha256(path).encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def _agreement(reference: np.ndarray, candidate: np.ndarray, valid: np.ndarray) -> float:
    if reference.shape != candidate.shape or reference.shape != valid.shape:
        raise ValueError("R01 reference, target, and valid mask must have matching shapes")
    if not valid.any():
        raise ValueError("R01 valid mask is empty")
    return float((reference[valid] == candidate[valid]).mean())


def validate_case(case_dir: Path) -> dict[str, Any]:
    """Recompute all public single-transform metrics without reading truth."""
    data = case_dir / "public" / "data"
    reference = np.load(data / "reference.npy")
    target = np.load(data / "target_faulty.npy")
    valid = np.load(data / "target_valid.npy").astype(bool)
    if reference.dtype != np.uint8 or target.dtype != np.uint8:
        raise ValueError("R01 arrays must preserve uint8 cloud-mask encoding")
    if not np.isin(reference, (0, 1)).all() or not np.isin(target, (0, 1)).all():
        raise ValueError("R01 public arrays must be binary cloud-mask values")

    landscape: dict[str, float] = {}
    valid_counts: dict[str, int] = {}
    for name, transform in TRANSFORMS.items():
        candidate, candidate_valid = transform(target), transform(valid)
        landscape[name] = _agreement(reference, candidate, candidate_valid)
        valid_counts[name] = int(candidate_valid.sum())

    initial = json.loads((case_dir / "initial_result.json").read_text())
    initial_metric = float(initial.get("agreement_valid", initial["agreement"]))
    threshold = float(json.loads((case_dir / "task.json").read_text())["expected_quality_threshold"])
    ordered = sorted(landscape.items(), key=lambda item: item[1], reverse=True)
    best_name, best_metric = ordered[0]
    runner_path = Path(__file__).resolve().parents[1] / "remote" / "run_experiment.py"
    public_paths = [case_dir / "task.json", case_dir / "initial_result.json", case_dir / "public" / "metadata.json"]
    public_paths += [data / name for name in ("reference.npy", "target_faulty.npy", "target_valid.npy")]
    truth_path = case_dir / "evaluator_private" / "ground_truth.json"
    return {
        "case_id": "R01",
        "metric": "agreement",
        "landscape": landscape,
        "valid_pixels": valid_counts,
        "initial_metric": initial_metric,
        "recomputed_identity": landscape["identity"],
        "best_transform": best_name,
        "best_agreement": best_metric,
        "second_best_transform": ordered[1][0],
        "second_best_agreement": ordered[1][1],
        "separation": best_metric - ordered[1][1],
        "quality_threshold": threshold,
        "absolute_improvement": landscape["rot180"] - landscape["identity"],
        "valid_retention_fraction": valid_counts["rot180"] / valid_counts["identity"],
        "historical_reference": {"before": HISTORICAL_BEFORE, "after": HISTORICAL_AFTER, "tolerance": HISTORICAL_TOLERANCE},
        "historical_before_delta": landscape["identity"] - HISTORICAL_BEFORE,
        "historical_after_delta": landscape["rot180"] - HISTORICAL_AFTER,
        "checks": {
            "initial_metric_reproducible": bool(np.isclose(initial_metric, landscape["identity"], atol=1e-12)),
            "rot180_is_unique_best": best_name == "rot180" and best_metric > ordered[1][1],
            "rot180_exceeds_threshold": landscape["rot180"] >= threshold,
            "valid_support_retained": valid_counts["rot180"] == valid_counts["identity"],
            "historical_before_close": abs(landscape["identity"] - HISTORICAL_BEFORE) <= HISTORICAL_TOLERANCE,
            "historical_after_close": abs(landscape["rot180"] - HISTORICAL_AFTER) <= HISTORICAL_TOLERANCE,
        },
        "sha256": {name: _sha256(data / name) for name in ("reference.npy", "target_faulty.npy", "target_valid.npy")},
        "case_public_sha256": _manifest_sha256(public_paths, case_dir),
        "ground_truth_sha256": _sha256(truth_path) if truth_path.is_file() else None,
        "runner_sha256": _sha256(runner_path),
    }


def write_validation(case_dir: Path) -> dict[str, Any]:
    """Write reproducible evaluator-private landscape and validation records."""
    result = validate_case(case_dir)
    if not all(result["checks"].values()):
        raise ValueError(f"R01 validation failed: {result['checks']}")
    private = case_dir / "evaluator_private"
    private.mkdir(parents=True, exist_ok=True)
    repair_landscape = {
        "case_id": result["case_id"], "metric": result["metric"],
        **result["landscape"], "valid_pixels_each_candidate": result["valid_pixels"]["identity"],
        "best_transform": result["best_transform"], "second_best_transform": result["second_best_transform"],
        "separation": result["separation"],
    }
    validation = {key: value for key, value in result.items() if key not in {"landscape"}}
    (private / "repair_landscape.json").write_text(json.dumps(repair_landscape, indent=2) + "\n")
    (private / "validation.json").write_text(json.dumps(validation, indent=2) + "\n")
    return result
