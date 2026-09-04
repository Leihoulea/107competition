"""Manifest loading and source-integrity checks."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .models import KnowledgeSource


def load_source_manifest(path: Path) -> list[KnowledgeSource]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("schema_version") != 1 or not isinstance(value.get("sources"), list):
        raise ValueError("knowledge manifest must contain schema_version=1 and a sources list")
    sources = [KnowledgeSource.from_dict(item) for item in value["sources"]]
    identifiers = [item.source_id for item in sources]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("knowledge manifest source_id values must be unique")
    return sources


def source_path(knowledge_root: Path, source: KnowledgeSource) -> Path:
    candidate = (knowledge_root / "sources" / source.path).resolve()
    allowed = (knowledge_root / "sources").resolve()
    if allowed not in candidate.parents:
        raise ValueError(f"knowledge source path escapes sources directory: {source.path}")
    return candidate


def verify_source_sha256(path: Path, source: KnowledgeSource) -> None:
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != source.sha256:
        raise ValueError(f"sha256 mismatch for knowledge source {source.source_id}")
