import hashlib
import json
from pathlib import Path

from scidiagnose.knowledge.index import load_bm25_index
from scidiagnose.knowledge.retrieve import retrieve_scientific_knowledge


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"


def manifest_sources():
    return json.loads((KNOWLEDGE / "manifest.json").read_text(encoding="utf-8"))["sources"]


def test_manifest_all_sources_exist_and_raw_hashes_match():
    sources = manifest_sources()
    assert len(sources) == 4
    assert {item["original_filename"] for item in sources} == {
        "pdf_fg15_msg_native_format_15_6b513c5bb3.pdf", "pdf_ten_05105_msg_img_data_e7c8b315e6.pdf",
        "pdf_msg_met_prod_atbd_15e4917e25.pdf", "reading.rst.txt",
    }
    for source in sources:
        raw = KNOWLEDGE / "sources" / "raw" / source["raw_name"]
        normalized = KNOWLEDGE / "sources" / source["path"]
        assert raw.is_file() and normalized.is_file()
        assert hashlib.sha256(raw.read_bytes()).hexdigest() == source["raw_sha256"]
        assert hashlib.sha256(normalized.read_bytes()).hexdigest() == source["normalized_sha256"]


def test_manifest_paths_are_repo_relative_and_source_metadata_is_reviewed():
    sources = {item["source_id"]: item for item in manifest_sources()}
    for source in sources.values():
        serialized = json.dumps(source)
        assert ":\\" not in serialized
        assert not Path(source["path"]).is_absolute()
        assert not Path(source["normalized_path"]).is_absolute()
        assert "title" in source and "publisher" in source and "product" in source
        assert "document_id" in source and "document_date" in source
    atbd = sources["EUMETSAT_MSG_MET_PRODUCTS_ATBD"]
    assert atbd["document_id"] == "EUM/MSG/SPE/022"
    assert atbd["version"] == "v7B e-signed"
    assert atbd["document_date"] == "2015-10-23"


def test_normalized_sources_have_provenance_and_correct_authority():
    sources = {item["source_id"]: item for item in manifest_sources()}
    assert all(item["authority"] == "official" for key, item in sources.items() if key.startswith("EUMETSAT_"))
    assert sources["SATPY_SEVIRI_READER"]["authority"] == "project_documentation"
    for source in sources.values():
        text = (KNOWLEDGE / "sources" / source["path"]).read_text(encoding="utf-8")
        assert text.strip() and "<!-- source_page:" in text
        if source["page_count"] is not None:
            assert text.count("<!-- source_page:") == source["page_count"]


def test_index_chunks_keep_source_and_page_provenance():
    index = load_bm25_index(KNOWLEDGE / "index" / "bm25.json")
    assert len(index.chunks) > 100
    assert all(chunk.source_id and chunk.section for chunk in index.chunks)
    assert all(chunk.page for chunk in index.chunks if chunk.source_id != "SATPY_SEVIRI_READER")
    assert all(chunk.page_start and chunk.page_end for chunk in index.chunks if chunk.source_id != "SATPY_SEVIRI_READER")
    assert all(chunk.page_start == chunk.page_end for chunk in index.chunks if chunk.source_id != "SATPY_SEVIRI_READER")


def test_bm25_chunk_store_rebuilds_at_load_time_without_a_database(tmp_path):
    from scidiagnose.knowledge.index import build_bm25_index

    persisted = tmp_path / "bm25.json"
    original = load_bm25_index(KNOWLEDGE / "index" / "bm25.json")
    rebuilt = build_bm25_index(original.chunks, persisted)
    loaded = load_bm25_index(persisted)
    assert len(rebuilt.chunks) == len(loaded.chunks) == len(original.chunks)
    assert loaded.search("SEVIRI scan directions", top_k=1)[0].source_id == "EUMETSAT_MSG_IMAGE_DATA"


def test_orientation_scan_and_satpy_queries_retrieve_relevant_sources():
    index = load_bm25_index(KNOWLEDGE / "index" / "bm25.json")
    orientation = retrieve_scientific_knowledge("native image orientation MSG SEVIRI", top_k=3, index=index)
    scan = retrieve_scientific_knowledge("SEVIRI image scan directions", top_k=3, index=index)
    satpy = retrieve_scientific_knowledge("upper_right_corner Satpy SEVIRI reader", top_k=3, index=index)
    assert any(hit.source_id in {"SATPY_SEVIRI_READER", "EUMETSAT_MSG_IMAGE_DATA", "EUMETSAT_MSG_NATIVE_FORMAT"} for hit in orientation)
    assert any(hit.source_id in {"EUMETSAT_MSG_IMAGE_DATA", "EUMETSAT_MSG_NATIVE_FORMAT"} for hit in scan)
    assert satpy[0].source_id == "SATPY_SEVIRI_READER"


def test_cloud_mask_query_retrieves_official_atbd_source():
    index = load_bm25_index(KNOWLEDGE / "index" / "bm25.json")
    hits = retrieve_scientific_knowledge("MSG Cloud Mask product cloud classes", top_k=3, index=index)
    assert any(hit.source_id == "EUMETSAT_MSG_MET_PRODUCTS_ATBD" for hit in hits)


def test_normalized_knowledge_excludes_project_repair_and_evaluator_terms():
    targets = [
        KNOWLEDGE / "manifest.json", KNOWLEDGE / "corpus" / "chunks.json", KNOWLEDGE / "index" / "bm25.json",
        *(KNOWLEDGE / "sources" / "normalized").glob("*.md"),
    ]
    text = "\n".join(path.read_text(encoding="utf-8") for path in targets).lower()
    for forbidden in ("rot180", "known_repair", "ground_truth", "r01", "validated_repair", "navigation_error"):
        assert forbidden not in text
