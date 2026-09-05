# MSG/SEVIRI Knowledge Semantic Audit

## Scope and method

This audit checks the four manifest-declared normalized sources against their retained raw files and page markers. PDF text was extracted from the existing text layer with `pypdf`; OCR, summarisation, and inferred scientific corrections were not used. EUMETSAT sources are `official`; Satpy is `project_documentation` and describes reader behaviour rather than an EUMETSAT product definition.

## Source facts retained in the corpus

| Topic | Source fact | Provenance |
| --- | --- | --- |
| SEVIRI scan | SEVIRI acquires East-West lines through satellite spin and steps the flat scan mirror South-North after each East-West line. | EUMETSAT `EUM/MSG/ICD/105`, §2.1.1, source page 11 |
| Grid origin | The `ReferenceGridVIS_IR` record defines the VIS/IR grid; the documented `GridOrigin` options identify the corner and the origin coordinates are `(1,1)`. | EUMETSAT `EUM/MSG/ICD/105`, §7.2.4, source page 97 |
| Processing/pixel directions | `ImageProcDirection` records real-time image-production direction and `PixelGenDirection` identifies whether the first pixel in a line is eastern or western. | EUMETSAT `EUM/MSG/ICD/105`, §7.2.4, source page 98 |
| Native reader orientation | Satpy documents that MSG SEVIRI L1.5 data can be stored with the south-west corner in the upper right; its `upper_right_corner` load argument requests a desired orientation, while `native` leaves data unflipped. | Satpy `reading.rst`, `Load data`, source-document marker |
| Cloud Mask semantics | The Cloud Mask product is produced for every pixel as GRIB Edition 2 data, with classes including clear sky over water, clear sky over land, cloud, and no data. | EUMETSAT `EUM/MSG/SPE/022`, §20.4, source page 253 |

## Interpretation boundaries

- The EUMETSAT statements establish product-format, scan, grid, and Cloud Mask semantics; they do not alone diagnose a particular comparison result.
- The Satpy statement establishes the documented behaviour of that software reader. It must not be elevated to an EUMETSAT official product-definition claim.
- A relative orientation, navigation, resampling, temporal-pairing, or mask-definition diagnosis requires experiment-specific evidence. No such diagnosis is asserted by this corpus.

## Not supported by the four sources

- A project-specific repair operation or a preferred transform.
- The cause, correctness, or outcome of any SciDiagnose benchmark or historical case.
- The claim that one sensor's Cloud Mask is absolute cloud truth.

## Integrity result

All retained scientific statements above point to a source and page/section (or the Satpy source-document marker). The normalized corpus contains no added case diagnosis or evaluator conclusion.
