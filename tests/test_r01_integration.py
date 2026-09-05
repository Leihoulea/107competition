"""Integration checks for the evaluator-separated R01 historical-real case."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from benchmark.harness import PublicCase
from benchmark.r01_validator import validate_case
from scidiagnose.evaluator import evaluate, ground_truth_path
from scidiagnose.experiment_tools import ExperimentTools
from scidiagnose.ssh_executor import SSHDirectExecutor


ROOT = Path(__file__).resolve().parents[1]
R01 = ROOT / "cases_real" / "r01"


def test_r01_public_files_exist():
    assert PublicCase.load(R01).task["case_id"] == "R01"
    for relative in ("task.json", "initial_result.json", "public/metadata.json", "public/data/reference.npy", "public/data/target_faulty.npy", "public/data/target_valid.npy"):
        assert (R01 / relative).is_file()


def test_r01_public_arrays_valid():
    reference, target, valid = PublicCase.load(R01).arrays()
    assert reference.shape == target.shape == valid.shape == (3712, 3712)
    assert reference.dtype == target.dtype == np.uint8
    assert valid.dtype == bool and valid.any()
    assert np.isin(reference, (0, 1)).all() and np.isin(target, (0, 1)).all()


def test_r01_initial_metric_reproducible():
    result = validate_case(R01)
    assert result["checks"]["initial_metric_reproducible"]
    assert result["recomputed_identity"] == result["initial_metric"]


def test_r01_known_repair_reproducible():
    result = validate_case(R01)
    assert result["best_transform"] == "rot180"
    assert result["best_agreement"] >= result["quality_threshold"]
    assert result["absolute_improvement"] >= 0.15


def test_r01_repair_landscape():
    result = validate_case(R01)
    assert result["checks"]["rot180_is_unique_best"]
    assert result["separation"] > 0.2
    assert result["checks"]["valid_support_retained"]
    assert result["valid_retention_fraction"] == 1.0


def test_r01_private_truth_not_public():
    forbidden = ("rot180", "orientation_error", "navigation_bug", "known_repair", "corrected", "patched", "ground_truth", "fault_family")
    public_files = [R01 / "task.json", R01 / "initial_result.json", R01 / "public" / "metadata.json"]
    public_files += list((R01 / "public" / "data").iterdir())
    assert all("evaluator_private" not in path.parts for path in public_files)
    for path in public_files:
        if path.suffix == ".json":
            text = path.read_text().lower()
            assert not any(token in text for token in forbidden), path
    assert ground_truth_path(R01).parent.name == "evaluator_private"


def test_r01_private_truth_not_uploaded_remote(tmp_path, monkeypatch):
    executor = SSHDirectExecutor()
    uploads: list[tuple[Path, str]] = []
    monkeypatch.setattr(executor, "warm_connection", lambda: None)
    monkeypatch.setattr(executor, "_ssh", lambda *args, **kwargs: object())
    monkeypatch.setattr(executor, "upload", lambda local, remote: uploads.append((Path(local), remote)))
    tools = ExperimentTools(executor, R01, tmp_path)
    tools._ensure_data()
    uploaded_names = {path.name for path, _ in uploads}
    assert uploaded_names == {"reference.npy", "target_faulty.npy", "target_valid.npy", "run_experiment.py"}
    assert all("evaluator_private" not in str(path) for path, _ in uploads)
    assert all("ground_truth" not in remote and "validation" not in remote for _, remote in uploads)


def test_r01_validator_deterministic():
    first, second = validate_case(R01), validate_case(R01)
    assert first == second
    assert all(first["checks"].values())
    assert len(first["case_public_sha256"]) == len(first["ground_truth_sha256"]) == 64


def test_evaluator_private_path_supported(tmp_path):
    case = tmp_path / "case"; private = case / "evaluator_private"; private.mkdir(parents=True)
    (private / "ground_truth.json").write_text(json.dumps({"fault": False, "fault_family": "no_fault"}))
    (case / "initial_result.json").write_text(json.dumps({"agreement_valid": .9}))
    assert ground_truth_path(case) == private / "ground_truth.json"
    result = evaluate(case, {"decision": "no_fault", "fault_family": "no_fault", "recommended_repair": {}, "evidence_experiment_ids": []}, [], .85, 30, 30)
    assert result["total"] == 100.0


def test_old_hidden_cases_still_supported(tmp_path):
    case = tmp_path / "case"; hidden = case / "hidden"; hidden.mkdir(parents=True)
    (hidden / "ground_truth.json").write_text(json.dumps({"fault": False, "fault_family": "no_fault"}))
    (case / "initial_result.json").write_text(json.dumps({"agreement_valid": .9}))
    assert ground_truth_path(case) == hidden / "ground_truth.json"
    result = evaluate(case, {"decision": "no_fault", "fault_family": "no_fault", "recommended_repair": {}, "evidence_experiment_ids": []}, [], .85, 30, 30)
    assert result["total"] == 100.0
