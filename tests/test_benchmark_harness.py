import json
from pathlib import Path

from benchmark.harness import BenchmarkHarness, PublicCase, RunReader
from benchmark.baselines import DeterministicExhaustiveBaseline


ROOT = Path(__file__).resolve().parents[1]


def test_exhaustive_uses_public_arrays_and_writes_all_report_formats(tmp_path):
    row = BenchmarkHarness().deterministic_exhaustive(PublicCase.load(ROOT / "cases" / "b01"), 1)
    assert row["completed"] and row["experiment_count"] == 7
    assert row["best_agreement_valid"] >= row["initial_agreement"]
    BenchmarkHarness.write_reports([row], tmp_path)
    assert {p.name for p in tmp_path.iterdir()} == {"results.json", "results.csv", "results.md"}
    assert json.loads((tmp_path / "results.json").read_text())[0]["method"] == "deterministic_exhaustive"
    assert DeterministicExhaustiveBaseline().run(PublicCase.load(ROOT / "cases" / "b01"), 1)["completed"]


def test_one_shot_uses_real_public_measurement_and_cites_it():
    def fake_llm(context):
        if context["mode"] == "one_shot_plan": return {"operation": "rot180"}
        return {"decision": "fault", "confidence": .9, "evidence_experiment_ids": ["BASE_001"]}
    row = BenchmarkHarness(fake_llm).one_shot_llm(PublicCase.load(ROOT / "cases" / "b01"), 1)
    assert row["completed"] and row["experiment_count"] == 1
    assert row["cited_evidence_count"] == 1
    assert row["best_agreement_valid"] is not None


def test_run_reader_reads_existing_artifact_without_executing(tmp_path):
    case = PublicCase.load(ROOT / "cases" / "b01")
    (tmp_path / "state.json").write_text(json.dumps({"case_id": "B01", "experiments": [{"experiment_id": "EXP_001", "agreement_valid": .91}]}))
    (tmp_path / "final.json").write_text(json.dumps({"decision": "fault", "confidence": .8, "evidence_experiment_ids": ["EXP_001"]}))
    row = RunReader(tmp_path).read(case, 2)
    assert row["completed"] and row["method"] == "scidiagnose_run_reader"
    assert row["repeat"] == 2 and row["cited_evidence_count"] == 1
