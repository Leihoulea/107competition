"""Run-level artifacts that make failed diagnosis attempts auditable."""
from __future__ import annotations

import json
import re
import time
import traceback
from pathlib import Path


def safe_error_text(value: object) -> str:
    """Redact common credential labels while retaining useful error diagnostics."""
    text = str(value)
    text = re.sub(r"(?i)(bearer\s+|api[_-]?key\s*[=:]\s*)\S+", r"\1[REDACTED]", text)
    return text[:4000]


def write_failure_artifact(run_dir: Path, exc: BaseException) -> Path:
    """Persist an unexpected runner failure next to its partial trace."""
    artifact = run_dir / "run_failure.json"
    artifact.write_text(json.dumps({
        "status": "failed",
        "timestamp": time.time(),
        "exception_type": type(exc).__name__,
        "message": safe_error_text(exc),
        "traceback": safe_error_text(traceback.format_exc(limit=20)),
    }, indent=2), encoding="utf-8")
    return artifact
