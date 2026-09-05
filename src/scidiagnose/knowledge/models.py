"""Typed, serializable records for source-grounded knowledge retrieval."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Literal


Authority = Literal["official", "peer_reviewed", "project_documentation", "project_note"]


@dataclass(frozen=True)
class KnowledgeSource:
    source_id: str
    title: str
    authority: Authority
    publisher: str
    version: str
    retrieved_at: str
    sha256: str
    domain: str
    product: str
    license_or_usage_note: str
    path: str
    document_id: str | None = None
    document_date: str | None = None

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "KnowledgeSource":
        value = {**value, "license_or_usage_note": value.get("license_or_usage_note", value.get("usage_note", ""))}
        required = (
            "source_id", "title", "authority", "publisher", "version", "retrieved_at",
            "sha256", "domain", "product", "license_or_usage_note", "path",
        )
        missing = [name for name in required if not str(value.get(name, "")).strip()]
        if missing:
            raise ValueError(f"knowledge source missing required fields: {', '.join(missing)}")
        if value["authority"] not in {"official", "peer_reviewed", "project_documentation", "project_note"}:
            raise ValueError("knowledge source authority must be official, peer_reviewed, project_documentation, or project_note")
        fields = {name: str(value[name]) for name in required}
        fields["document_id"] = None if value.get("document_id") is None else str(value["document_id"])
        fields["document_date"] = None if value.get("document_date") is None else str(value["document_date"])
        return cls(**fields)  # type: ignore[arg-type]

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


@dataclass(frozen=True)
class KnowledgeChunk:
    chunk_id: str
    source_id: str
    title: str
    section: str
    page: str | None
    version: str
    authority: Authority
    domain: str
    product: str
    text: str
    # ``page`` is retained for the first public index schema. The explicit
    # range fields make page provenance unambiguous for future multi-page
    # chunks without invalidating existing readers.
    page_start: int | None = None
    page_end: int | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "KnowledgeChunk":
        return cls(**value)


@dataclass(frozen=True)
class KnowledgeHit:
    source_id: str
    title: str
    section: str
    page: str | None
    text: str
    score: float
    authority: Authority
    version: str
    chunk_id: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class KnowledgeEvidence:
    evidence_id: str
    kind: Literal["knowledge"]
    claim: str
    source: dict[str, str | None]
    supports_hypotheses: list[str]
    contradicts_hypotheses: list[str]
    validated: bool
    excerpt: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
