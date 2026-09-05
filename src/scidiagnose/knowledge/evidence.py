"""Explicit conversion from retrieval hit to reviewable knowledge evidence."""
from __future__ import annotations

from .models import KnowledgeEvidence, KnowledgeHit


def knowledge_evidence_from_hit(evidence_id: str, hit: KnowledgeHit, claim: str, *, supports_hypotheses: list[str] | None = None, contradicts_hypotheses: list[str] | None = None, validated: bool = False) -> KnowledgeEvidence:
    if not evidence_id.strip() or not claim.strip():
        raise ValueError("knowledge evidence requires a non-empty evidence_id and claim")
    return KnowledgeEvidence(
        evidence_id=evidence_id, kind="knowledge", claim=claim.strip(),
        source={"source_id": hit.source_id, "section": hit.section, "page": hit.page, "version": hit.version},
        supports_hypotheses=list(supports_hypotheses or []),
        contradicts_hypotheses=list(contradicts_hypotheses or []),
        validated=validated, excerpt=hit.text,
    )
