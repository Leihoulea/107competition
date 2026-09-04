from pathlib import Path

from scidiagnose.run_artifacts import write_failure_artifact


def test_failure_artifact_preserves_diagnostics_and_redacts_credentials(tmp_path: Path) -> None:
    try:
        raise RuntimeError("api_key=super-secret Bearer token-value planner failed")
    except RuntimeError as exc:
        artifact = write_failure_artifact(tmp_path, exc)

    content = artifact.read_text(encoding="utf-8")
    assert artifact.name == "run_failure.json"
    assert '"status": "failed"' in content
    assert "RuntimeError" in content
    assert "super-secret" not in content
    assert "token-value" not in content
    assert "[REDACTED]" in content
