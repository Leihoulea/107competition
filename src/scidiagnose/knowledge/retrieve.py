"""Public retrieval API with no implicit graph or prompt integration."""
from __future__ import annotations

from pathlib import Path

from .index import KnowledgeIndex, load_bm25_index
from .models import KnowledgeHit


def retrieve_scientific_knowledge(query: str, top_k: int = 5, filters: dict[str, str] | None = None, *, index: KnowledgeIndex | None = None, index_path: Path | None = None) -> list[KnowledgeHit]:
    """Return auditable lexical hits; callers must explicitly convert them to evidence."""
    if index is None:
        resolved = index_path or Path("knowledge") / "index" / "bm25.json"
        index = load_bm25_index(resolved)
    return index.search(query, top_k=top_k, filters=filters)
