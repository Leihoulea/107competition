# MSG/SEVIRI Knowledge Source Report

The corpus preserves source statements and provenance. It does not encode or rank any historical repair operation.

| Source | Authority | Pages | Chunks | Main relevant topics |
| --- | --- | ---: | ---: | --- |
| MSG Level 1.5 Native Format File Definition | official | 15 | 18 | format / navigation / line-column representation |
| MSG Level 1.5 Image Data Format Description | official | 129 | 182 | scan / grid / image geometry / navigation |
| MSG MPEF Algorithm Specification Document | official | 297 | 807 | cloud products / algorithm semantics / Cloud Mask |
| Satpy Reading Documentation | project_documentation | — | 14 | reader behavior / native orientation / upper_right_corner |

## Corpus summary

- Source count: 4
- Chunk count: 1021
- Authority distribution: official: 3, project_documentation: 1
- Retrieval relevance: Relevant@1 6/6; Relevant@3 6/6.

## Known limitations

- PDF text was extracted from an existing text layer with pypdf; OCR was not used.
- Page markers are `<!-- source_page: N -->`; section labels are recovered only by deterministic heading rules when present.
- Complex tables and formulas remain extracted text. No formula or scientific statement was reconstructed from inference.
- The native-format document does not state a cover document identifier or issue in the retained extract; the Satpy snapshot does not state a version/date. These fields remain `unknown` or `null` rather than being inferred.
- Satpy is classified as `project_documentation`; it is not used as an EUMETSAT product-definition authority.
