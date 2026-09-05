"""Build an auditable corpus from manifest-declared plaintext/Markdown sources."""
from __future__ import annotations

import json
from pathlib import Path

from .chunking import chunk_scientific_text
from .cleaning import clean_scientific_text
from .index import KnowledgeIndex, build_bm25_index
from .models import KnowledgeChunk
from .sources import load_source_manifest, source_path, verify_source_sha256


def build_knowledge_corpus(knowledge_root: Path, max_chars: int = 4000) -> list[KnowledgeChunk]:
    """Read only manifest-listed .txt/.md sources and emit provenance-rich chunks."""
    chunks: list[KnowledgeChunk] = []
    for source in load_source_manifest(knowledge_root / "manifest.json"):
        path = source_path(knowledge_root, source)
        if path.suffix.lower() not in {".txt", ".md"}:
            raise ValueError("MVP ingestion accepts cleaned .txt or .md sources, not raw documents")
        verify_source_sha256(path, source)
        chunks.extend(chunk_scientific_text(source, clean_scientific_text(path.read_text(encoding="utf-8")), max_chars))
    corpus_path = knowledge_root / "corpus" / "chunks.json"
    corpus_path.parent.mkdir(parents=True, exist_ok=True)
    corpus_path.write_text(json.dumps({"schema_version": 1, "chunks": [item.to_dict() for item in chunks]}, indent=2), encoding="utf-8")
    return chunks


def build_knowledge_index(knowledge_root: Path, max_chars: int = 4000) -> KnowledgeIndex:
    return build_bm25_index(build_knowledge_corpus(knowledge_root, max_chars), knowledge_root / "index" / "bm25.json")
