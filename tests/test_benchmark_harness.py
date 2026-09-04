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
        return {"decision": "fault", "fault_family": "spatial_transform", "root_cause": "public evidence", "confidence": .9, "evidence_experiment_ids": ["BASE_001"], "recommended_repair": {"operation": "rot180"}}
    row = BenchmarkHarness(fake_llm).one_shot_llm(PublicCase.load(ROOT / "cases" / "b01"), 1)
    assert row["completed"] and row["experiment_count"] == 1
    assert row["cited_evidence_count"] == 1
    assert row["best_agreement_valid"] is not None
    assert row["fault_family"] == "spatial_transform" and row["recommended_repair"] == {"operation": "rot180"}


def test_run_reader_reads_existing_artifact_without_executing(tmp_path):
    case = PublicCase.load(ROOT / "cases" / "b01")
    (tmp_path / "state.json").write_text(json.dumps({"case_id": "B01", "experiments": [{"experiment_id": "EXP_001", "agreement_valid": .91}]}))
    (tmp_path / "final.json").write_text(json.dumps({"decision": "fault", "confidence": .8, "evidence_experiment_ids": ["EXP_001"]}))
    row = RunReader(tmp_path).read(case, 2)
    assert row["completed"] and row["method"] == "scidiagnose_run_reader"
    assert row["repeat"] == 2 and row["cited_evidence_count"] == 1


def test_run_reader_supports_official_graph_trace_and_unavailable_metrics_are_null(tmp_path):
    case = PublicCase.load(ROOT / "cases" / "b01")
    events = [
        {"node": "execute", "experiment_id": "EXP_001", "backend": "ssh", "remote_host": "server", "remote_pid": 42, "result": {"metrics": {"agreement_valid": .91, "elapsed_seconds": 1.25}}},
        {"node": "finalize", "final": {"decision": "fault", "fault_family": "spatial", "root_cause": "trace evidence", "confidence": .8, "evidence_experiment_ids": ["EXP_001"], "recommended_repair": {}}},
    ]
    (tmp_path / "trace.jsonl").write_text("\n".join(json.dumps(event) for event in events))
    row = RunReader(tmp_path).read(case, 1)
    assert row["completed"] and row["remote_jobs"] == 1
    assert row["compute_wall_seconds"] == 1.25 and row["budget_units_used"] is None
    assert row["compute_cpu_seconds"] is None and row["validated_repair_success"] is True


def test_posthoc_scoring_is_explicit_and_never_required_for_a_run():
    row = BenchmarkHarness().deterministic_exhaustive(PublicCase.load(ROOT / "cases" / "b01"), 1)
    scored = BenchmarkHarness.score_posthoc([row], {"B01": {"decision": "no_fault"}})
    assert scored[0]["false_positive"] == (row["decision"] == "fault")
    custom = BenchmarkHarness.score_posthoc([row], evaluator=lambda result, truth: {"external_score": result["method"]})
    assert custom[0]["external_score"] == "deterministic_exhaustive"
