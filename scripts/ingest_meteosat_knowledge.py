"""Ingest the first auditable MSG/SEVIRI knowledge sources.

This is intentionally a deterministic document-processing script, not an LLM
summarizer.  It retains every extracted page behind a stable provenance marker.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"

SOURCES = (
    {
        "source_id": "EUMETSAT_MSG_NATIVE_FORMAT",
        "raw_name": "eumetsat_fg15_msg_native_format.pdf",
        "original_filename": "pdf_fg15_msg_native_format_15_6b513c5bb3.pdf",
        "original_resolved_path": "E:\\107competition\\pdf_fg15_msg_native_format_15_6b513c5bb3.pdf",
        "normalized_name": "EUMETSAT_FG15_MSG_Native_Format.md",
        "authority": "official",
        "publisher": "EUMETSAT",
        "domain": "remote_sensing",
        "product": "MSG / SEVIRI",
        "source_type": "technical_documentation",
        "usage_note": "Official MSG Level 1.5 native-format documentation.",
    },
    {
        "source_id": "EUMETSAT_MSG_IMAGE_DATA",
        "raw_name": "eumetsat_ten_05105_msg_image_data.pdf",
        "original_filename": "pdf_ten_05105_msg_img_data_e7c8b315e6.pdf",
        "original_resolved_path": "E:\\107competition\\pdf_ten_05105_msg_img_data_e7c8b315e6.pdf",
        "normalized_name": "EUMETSAT_TEN_05105_MSG_Image_Data.md",
        "authority": "official",
        "publisher": "EUMETSAT",
        "domain": "remote_sensing",
        "product": "MSG / SEVIRI",
        "source_type": "technical_documentation",
        "usage_note": "Official MSG image-data documentation.",
    },
    {
        "source_id": "EUMETSAT_MSG_MET_PRODUCTS_ATBD",
        "raw_name": "eumetsat_msg_met_products_atbd.pdf",
        "original_filename": "pdf_msg_met_prod_atbd_15e4917e25.pdf",
        "original_resolved_path": "E:\\107competition\\pdf_msg_met_prod_atbd_15e4917e25.pdf",
        "normalized_name": "EUMETSAT_MSG_Meteorological_Products_ATBD.md",
        "authority": "official",
        "publisher": "EUMETSAT",
        "domain": "remote_sensing",
        "product": "MSG / SEVIRI",
        "source_type": "algorithm_theoretical_basis_document",
        "usage_note": "Official MSG meteorological-products ATBD.",
    },
    {
        "source_id": "SATPY_SEVIRI_READER",
        "raw_name": "satpy_seviri_reading.rst.txt",
        "original_filename": "reading.rst.txt",
        "original_resolved_path": "E:\\107competition\\reading.rst.txt",
        "normalized_name": "SATPY_SEVIRI_Reader_Documentation.md",
        "authority": "project_documentation",
        "publisher": "Satpy project",
        "domain": "remote_sensing",
        "product": "MSG / SEVIRI",
        "source_type": "project_documentation",
        "usage_note": "Software reader documentation; not an EUMETSAT product-definition authority.",
    },
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _require_pypdf():
    try:
        from pypdf import PdfReader
    except ImportError as exc:  # pragma: no cover - deployment guidance
        raise SystemExit("pypdf is required for PDF ingestion; install the project PDF dependency.") from exc
    return PdfReader


def _clean_extracted_page(text: str) -> str:
    """Repair only mechanical extraction damage; never infer scientific meaning."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"(?<=[A-Za-z])-\n(?=[a-z])", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    return text.strip()


def _first_text_line(text: str) -> str:
    for line in text.splitlines():
        candidate = re.sub(r"\s+", " ", line).strip()
        if len(candidate) >= 8 and not candidate.lower().startswith(("file:", "printed on:")):
            return candidate
    return "Untitled source; see page 1 text"


def inventory() -> list[dict[str, object]]:
    PdfReader = _require_pypdf()
    records: list[dict[str, object]] = []
    for spec in SOURCES:
        raw = KNOWLEDGE / "sources" / "raw" / spec["raw_name"]
        is_pdf = raw.suffix.lower() == ".pdf"
        record: dict[str, object] = {
            "source_id": spec["source_id"], "original_filename": spec["original_filename"],
            "resolved_path": spec["original_resolved_path"], "ingested_raw_path": str(raw.resolve()),
            "file_type": "pdf" if is_pdf else "rst",
            "size_bytes": raw.stat().st_size, "sha256": sha256(raw),
        }
        if is_pdf:
            reader = PdfReader(str(raw)); first = reader.pages[0].extract_text() or ""
            record.update({"text_extractable": bool(first.strip()), "page_count": len(reader.pages), "pdf_metadata": dict(reader.metadata or {}), "first_page_title_candidate": _first_text_line(first)})
        else:
            text = raw.read_text(encoding="utf-8")
            record.update({"text_extractable": bool(text.strip()), "page_count": None, "first_page_title_candidate": _first_text_line(text)})
        records.append(record)
    (KNOWLEDGE / "source_inventory.json").write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")
    return records


def _normalize_pdf(raw: Path, destination: Path, metadata: dict[str, str]) -> tuple[int, str]:
    PdfReader = _require_pypdf(); reader = PdfReader(str(raw))
    lines = [f"# {metadata['title']}", "", "## Document metadata", ""]
    for label in ("Publisher", "Version", "Original file", "Raw SHA-256"):
        key = label.lower().replace(" ", "_").replace("-", "_")
        lines.append(f"- {label}: {metadata[key]}")
    for number, page in enumerate(reader.pages, 1):
        text = _clean_extracted_page(page.extract_text() or "")
        lines.extend(["", f"<!-- source_page: {number} -->", "", text or "[TEXT_EXTRACTION_EMPTY]"])
    destination.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return len(reader.pages), sha256(destination)


def _normalize_rst(raw: Path, destination: Path, metadata: dict[str, str]) -> str:
    raw_text = raw.read_text(encoding="utf-8")
    # Convert only RST underline headings to Markdown headings.  The wording,
    # code examples, and all other source text remain unchanged.
    lines_in = raw_text.splitlines(); rendered: list[str] = []; index = 0
    while index < len(lines_in):
        line = lines_in[index]
        underline = lines_in[index + 1] if index + 1 < len(lines_in) else ""
        # RST permits an overline-and-underline document title.  The leading
        # ornament is not content and would otherwise resemble a Git conflict
        # marker in the normalized Markdown.
        if re.fullmatch(r"[=\-~^\"']{3,}", line.strip()) and index + 2 < len(lines_in) and lines_in[index + 1].strip() and lines_in[index + 2].strip() == line.strip():
            index += 1; continue
        if line.strip() and re.fullmatch(r"[=\-~^\"']{3,}", underline.strip()):
            level = "##" if underline.lstrip().startswith("=") else "###"
            rendered.extend([f"{level} {line.strip()}", ""]); index += 2; continue
        rendered.append(line); index += 1
    lines = [f"# {metadata['title']}", "", "## Document metadata", ""]
    for label in ("Publisher", "Version", "Original file", "Raw SHA-256"):
        key = label.lower().replace(" ", "_").replace("-", "_")
        lines.append(f"- {label}: {metadata[key]}")
    lines.extend(["", "<!-- source_page: source_document -->", "", "\n".join(rendered).strip()])
    destination.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return sha256(destination)


def normalize(records: list[dict[str, object]]) -> None:
    """Write page-marked Markdown and a manifest after metadata is reviewed."""
    by_id = {str(item["source_id"]): item for item in records}
    # Titles and versions are copied from the source's own extracted cover text,
    # not inferred from any diagnostic experiment or evaluator data.
    reviewed = {
        "EUMETSAT_MSG_NATIVE_FORMAT": ("MSG Level 1.5 Native Format File Definition", "not stated in extracted cover metadata"),
        "EUMETSAT_MSG_IMAGE_DATA": ("MSG Level 1.5 Image Data Format Description", "v8 e-signed, 26 September 2017"),
        "EUMETSAT_MSG_MET_PRODUCTS_ATBD": ("MSG MPEF Algorithm Specification Document", "not stated in extracted cover metadata"),
        "SATPY_SEVIRI_READER": ("Satpy Reading Documentation", "source snapshot; version not stated"),
    }
    manifest: list[dict[str, object]] = []
    normalized_dir = KNOWLEDGE / "sources" / "normalized"; normalized_dir.mkdir(parents=True, exist_ok=True)
    for spec in SOURCES:
        raw = KNOWLEDGE / "sources" / "raw" / spec["raw_name"]
        title, version = reviewed[spec["source_id"]]
        metadata = {"title": title, "publisher": str(spec["publisher"]), "version": version, "original_file": raw.name, "raw_sha_256": sha256(raw)}
        destination = normalized_dir / str(spec["normalized_name"])
        if raw.suffix.lower() == ".pdf":
            pages, normalized_hash = _normalize_pdf(raw, destination, metadata)
        else:
            pages, normalized_hash = None, _normalize_rst(raw, destination, metadata)
        inventory_record = by_id[str(spec["source_id"])]
        manifest.append({
            **spec, "title": title, "version": version, "retrieved_at": str(date.today()),
            "license_or_usage_note": str(spec["usage_note"]),
            "path": f"normalized/{destination.name}", "normalized_path": f"sources/normalized/{destination.name}",
            "sha256": normalized_hash, "raw_sha256": sha256(raw), "normalized_sha256": normalized_hash,
            "page_count": pages, "original_filename": inventory_record["original_filename"],
        })
    (KNOWLEDGE / "manifest.json").write_text(json.dumps({"schema_version": 1, "sources": manifest}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--normalize", action="store_true", help="write page-marked Markdown and manifest after inventory")
    args = parser.parse_args()
    records = inventory()
    if args.normalize:
        normalize(records)
    print(f"Wrote {KNOWLEDGE / 'source_inventory.json'}")
    if args.normalize:
        print(f"Wrote {KNOWLEDGE / 'manifest.json'} and normalized sources")


if __name__ == "__main__":
    main()
