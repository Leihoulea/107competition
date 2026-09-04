"""Configuration read exclusively from environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

def _load_local_env() -> None:
    """Load a user-created, git-ignored .env without overriding real env vars."""
    path = Path.cwd() / ".env"
    if not path.is_file(): return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line: continue
        key, value = line.split("=", 1)
        key, value = key.strip(), value.strip().strip("\"'")
        if key and key not in os.environ: os.environ[key] = value

_load_local_env()


@dataclass(frozen=True)
class Settings:
    remote_host: str = os.environ.get("SCIDIAG_REMOTE_HOST", "server-114")
    remote_workspace: str = os.environ.get(
        "SCIDIAG_REMOTE_WORKSPACE", "~/scidiagnose-demo"
    )
    remote_python: str = os.environ.get("SCIDIAG_REMOTE_PYTHON", "python3")
    command_timeout: int = int(os.environ.get("SCIDIAG_COMMAND_TIMEOUT", "90"))
    ssh_timeout: int = int(os.environ.get("SCIDIAG_SSH_TIMEOUT", "25"))
    model_provider: str = os.environ.get("SCIDIAG_MODEL_PROVIDER", "manual")
    model_name: str | None = os.environ.get("SCIDIAG_MODEL_NAME") or None
    api_key: str | None = os.environ.get("SCIDIAG_API_KEY") or None
    base_url: str | None = os.environ.get("SCIDIAG_BASE_URL") or None
    api_max_retries: int = int(os.environ.get("SCIDIAG_API_MAX_RETRIES", "4"))
    api_retry_base_seconds: float = float(os.environ.get("SCIDIAG_API_RETRY_BASE_SECONDS", "1"))
