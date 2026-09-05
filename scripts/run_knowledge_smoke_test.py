"""Generate auditable retrieval smoke-test artifacts for the MSG/SEVIRI corpus."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from scidiagnose.knowledge.index import load_bm25_index
from scidiagnose.knowledge.retrieve import retrieve_scientific_knowledge


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
QUERIES = (
    ("A", "What is the native image orientation of MSG SEVIRI data?", {"SATPY_SEVIRI_READER", "EUMETSAT_MSG_NATIVE_FORMAT", "EUMETSAT_MSG_IMAGE_DATA"}),
    ("B", "What are the SEVIRI image scan directions?", {"EUMETSAT_MSG_IMAGE_DATA", "EUMETSAT_MSG_NATIVE_FORMAT"}),
    ("C", "How are MSG image line and column coordinates defined?", {"EUMETSAT_MSG_IMAGE_DATA", "EUMETSAT_MSG_NATIVE_FORMAT"}),
    ("D", "How does Satpy handle the native SEVIRI image orientation?", {"SATPY_SEVIRI_READER"}),
    ("E", "What does upper_right_corner mean for the Satpy SEVIRI reader?", {"SATPY_SEVIRI_READER"}),
    ("F", "What is the MSG Cloud Mask Product Generation and how are cloud classes defined?", {"EUMETSAT_MSG_MET_PRODUCTS_ATBD"}),
)


def _excerpt(text: str, query: str, limit: int = 700) -> str:
    compact = " ".join(text.split())
    terms = sorted({item.lower() for item in re.findall(r"[A-Za-z_]{4,}", query)}, key=len, reverse=True)
    # Prefer the most specific query token (the terms are longest first), not
    # the first generic word such as "Satpy" at the beginning of a long chunk.
    position = next((compact.lower().find(term) for term in terms if compact.lower().find(term) >= 0), -1)
    start = max(0, position - 120) if position >= 0 else 0
    return compact[start:start + limit]


def run_smoke_test() -> list[dict[str, object]]:
    index = load_bm25_index(KNOWLEDGE / "index" / "bm25.json")
    output: list[dict[str, object]] = []
    for label, query, expected in QUERIES:
        hits = retrieve_scientific_knowledge(query, top_k=5, index=index)
        serialized = [
            {"rank": rank, "source_id": hit.source_id, "title": hit.title, "section": hit.section,
             "page": hit.page, "score": hit.score, "authority": hit.authority, "version": hit.version,
             "chunk_id": hit.chunk_id, "text_excerpt": _excerpt(hit.text, query)}
            for rank, hit in enumerate(hits, 1)
        ]
        output.append({
            "query_id": label, "query": query, "expected_source_ids": sorted(expected), "top_hits": serialized,
            # This relevance assessment is against the source/claim pairing
            # defined above, not raw keyword overlap. It is intentionally
            # recorded next to the retrieval ranks for human review.
            "relevant_at_1": bool(serialized and serialized[0]["source_id"] in expected),
            "relevant_at_3": any(item["source_id"] in expected for item in serialized[:3]),
        })
    (KNOWLEDGE / "retrieval_smoke_test.json").write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# MSG/SEVIRI Retrieval Smoke Test", "", "This report records lexical retrieval only. It does not infer a repair and contains no evaluator/private case data.", ""]
    for item in output:
        lines.extend([
            f"## Query {item['query_id']}", "", f"> {item['query']}", "",
            f"Manual relevance assessment — Relevant@1: **{item['relevant_at_1']}**; Relevant@3: **{item['relevant_at_3']}**.",
            "The assessment checks whether the returned passage comes from a source suitable for the stated semantic question, not merely whether lexical tokens overlap.", "",
        ])
        lines.extend(["| Rank | Source | Section | Page | BM25 | Excerpt |", "| ---: | --- | --- | --- | ---: | --- |"])
        for hit in item["top_hits"]:
            lines.append(f"| {hit['rank']} | {hit['source_id']} | {str(hit['section']).replace('|', ' ')} | {hit['page'] or '—'} | {hit['score']:.4f} | {str(hit['text_excerpt']).replace('|', ' ')} |")
        lines.append("")
    (KNOWLEDGE / "RETRIEVAL_SMOKE_TEST.md").write_text("\n".join(lines), encoding="utf-8")
    return output


def write_source_report() -> None:
    manifest = json.loads((KNOWLEDGE / "manifest.json").read_text(encoding="utf-8"))["sources"]
    chunks = load_bm25_index(KNOWLEDGE / "index" / "bm25.json").chunks
    counts = Counter(chunk.source_id for chunk in chunks)
    authority_counts = Counter(source["authority"] for source in manifest)
    smoke = json.loads((KNOWLEDGE / "retrieval_smoke_test.json").read_text(encoding="utf-8"))
    focus = {
        "EUMETSAT_MSG_NATIVE_FORMAT": "format / navigation / line-column representation",
        "EUMETSAT_MSG_IMAGE_DATA": "scan / grid / image geometry / navigation",
        "EUMETSAT_MSG_MET_PRODUCTS_ATBD": "cloud products / algorithm semantics / Cloud Mask",
        "SATPY_SEVIRI_READER": "reader behavior / native orientation / upper_right_corner",
    }
    lines = ["# MSG/SEVIRI Knowledge Source Report", "", "The corpus preserves source statements and provenance. It does not encode or rank any historical repair operation.", "", "| Source | Authority | Pages | Chunks | Main relevant topics |", "| --- | --- | ---: | ---: | --- |"]
    for source in manifest:
        pages = source["page_count"] if source["page_count"] is not None else "—"
        lines.append(f"| {source['title']} | {source['authority']} | {pages} | {counts[source['source_id']]} | {focus[source['source_id']]} |")
    lines.extend([
        "", "## Corpus summary", "",
        f"- Source count: {len(manifest)}",
        f"- Chunk count: {len(chunks)}",
        "- Authority distribution: " + ", ".join(f"{authority}: {authority_counts[authority]}" for authority in sorted(authority_counts)),
        f"- Retrieval relevance: Relevant@1 {sum(bool(item['relevant_at_1']) for item in smoke)}/{len(smoke)}; Relevant@3 {sum(bool(item['relevant_at_3']) for item in smoke)}/{len(smoke)}.",
        "", "## Known limitations", "",
        "- PDF text was extracted from an existing text layer with pypdf; OCR was not used.",
        "- Page markers are `<!-- source_page: N -->`; section labels are recovered only by deterministic heading rules when present.",
        "- Complex tables and formulas remain extracted text. No formula or scientific statement was reconstructed from inference.",
        "- The native-format document does not state a cover document identifier or issue in the retained extract; the Satpy snapshot does not state a version/date. These fields remain `unknown` or `null` rather than being inferred.",
        "- Satpy is classified as `project_documentation`; it is not used as an EUMETSAT product-definition authority.", "",
    ])
    (KNOWLEDGE / "KNOWLEDGE_SOURCE_REPORT.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    run_smoke_test(); write_source_report()
    print(f"Wrote smoke test and source report under {KNOWLEDGE}")
