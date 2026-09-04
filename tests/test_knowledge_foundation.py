import hashlib
import json

import pytest

from scidiagnose.knowledge.evidence import knowledge_evidence_from_hit
from scidiagnose.knowledge.ingest import build_knowledge_index
from scidiagnose.knowledge.retrieve import retrieve_scientific_knowledge


def make_source(root, name="manual.md", text="# Units\n[page: 4]\nReflectance is dimensionless. Valid range is 0 to 1.\n"):
    sources = root / "sources"; sources.mkdir(parents=True)
    path = sources / name; path.write_text(text, encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "sources": [{
            "source_id": "DOC-001", "title": "Product manual", "authority": "official",
            "publisher": "Example agency", "version": "2024.1", "retrieved_at": "2026-09-04",
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "domain": "remote_sensing",
            "product": "Example product", "license_or_usage_note": "test fixture", "path": name,
        }],
    }
    (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")


def test_ingestion_preserves_source_section_page_and_version(tmp_path):
    make_source(tmp_path)
    index = build_knowledge_index(tmp_path)
    hit = retrieve_scientific_knowledge("dimensionless valid range", index=index)[0]
    assert (hit.source_id, hit.section, hit.page, hit.version) == ("DOC-001", "Units", "4", "2024.1")
    assert hit.authority == "official"


def test_retrieval_filter_and_persisted_index_are_auditable(tmp_path):
    make_source(tmp_path)
    build_knowledge_index(tmp_path)
    hits = retrieve_scientific_knowledge("reflectance", index_path=tmp_path / "index" / "bm25.json", filters={"domain": "remote_sensing"})
    assert len(hits) == 1
    assert retrieve_scientific_knowledge("reflectance", index_path=tmp_path / "index" / "bm25.json", filters={"product": "other"}) == []


def test_equal_lexical_hits_prefer_official_authority(tmp_path):
    make_source(tmp_path)
    extra = tmp_path / "sources" / "note.md"; extra.write_text("# Units\n[page: 4]\nReflectance is dimensionless. Valid range is 0 to 1.\n", encoding="utf-8")
    manifest_path = tmp_path / "manifest.json"; manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    note = {**manifest["sources"][0], "source_id": "DOC-002", "authority": "project_note", "path": "note.md", "sha256": hashlib.sha256(extra.read_bytes()).hexdigest()}
    manifest["sources"].append(note); manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    hits = retrieve_scientific_knowledge("dimensionless", index=build_knowledge_index(tmp_path))
    assert [hit.authority for hit in hits] == ["official", "project_note"]


def test_knowledge_evidence_requires_explicit_conversion_and_is_not_auto_validated(tmp_path):
    make_source(tmp_path)
    hit = retrieve_scientific_knowledge("dimensionless", index=build_knowledge_index(tmp_path))[0]
    evidence = knowledge_evidence_from_hit("K001", hit, "The manual defines reflectance as dimensionless.", supports_hypotheses=["H001"])
    assert evidence.kind == "knowledge"
    assert evidence.validated is False
    assert evidence.source == {"source_id": "DOC-001", "section": "Units", "page": "4", "version": "2024.1"}


def test_ingestion_rejects_tampered_or_raw_pdf_sources(tmp_path):
    make_source(tmp_path)
    (tmp_path / "sources" / "manual.md").write_text("tampered", encoding="utf-8")
    with pytest.raises(ValueError, match="sha256 mismatch"):
        build_knowledge_index(tmp_path)
