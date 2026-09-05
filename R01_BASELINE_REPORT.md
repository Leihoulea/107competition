# R01 no-RAG baseline report

## Frozen benchmark identity

- Integration commit: `c90b87d6166679b0f107693da5a9cbe7f6b50bc8` (`benchmark: integrate and freeze R01 historical case`).
- Freeze tag: `r01-no-rag-baseline-freeze`.
- Case level: `historical_real_reconstructed`; provenance and historical-evidence boundary are in `cases_real/r01/evaluator_private/provenance.json` and `docs/R01_HISTORICAL_AUDIT.md`.
- Public case SHA-256: `8eec34174a6911c5078771bcb0ec400aaa6cb26c9d88894989acaef78494cfa3`.
- Public array SHA-256 values: reference `1d0498087227a63908b2207208e31d4796a3f68b2844590d7ac4657baedf7951`; target `798efef55c73a5635c264ad17bee1665ab8d8e84a47121b81ad94fbf7650c2a4`; valid mask `d68a32fca5b06ac815707bd9beb34e98e6f239a856883d54dbfebc4602fdd498`.
- Evaluator ground-truth SHA-256: `9e42f733c16abf26a64753f64c902cfb6647aeb721a6a91ffff1f5dcf7a2be3e`.
- Frozen remote runner SHA-256: `0498e8d88ec4d54a35e10a990108772176caa05d3d740cde135bf02126f55083`.

## Case and deterministic validation

The public initial agreement is `0.5368982307` on `9,515,524` valid pixels (`0.6905844` of the native grid). The evaluator-private validator recomputed every frozen single-transform control from the public arrays. The diagnostic candidate scored `0.7982679672`; the second-best control scored `0.5605946661`, a separation of `0.2376733010`. Every control retained `9,515,524` valid pixels. Reconstructed before/after values are within `0.01` of the historical references.

The transform label is an executable benchmark diagnostic, not a claim about a production product mutation. The historical production remediation remains evaluator-private navigation handling evidence.

## Deterministic baselines

| Method | Candidates | Best public candidate | Agreement | Budget equivalent | Wall time | CPU / remote jobs |
|---|---:|---|---:|---:|---:|---|
| Transform Sweep | 7 | single diagnostic transform | 0.7982679672 | 28 | 0.409774 s | not instrumented / 0 |
| Full Search | 847 | diagnostic transform then shift `(4, 1)` | 0.8094529529 | 4235 | 70.373104 s | not instrumented / 0 |

The deterministic artifacts are in `benchmark/results/R01_TRANSFORM_SWEEP/` and `benchmark/results/R01_FULL_SEARCH/`. The full-search action space is the frozen 7 transforms × 11 row shifts × 11 column shifts; it was not changed for R01.

## Frozen SciDiagnose no-RAG runs

All three runs used the same commit, public case, school OpenAI-compatible API configuration (`deepseek-v4-flash`, `temperature=0`), SSH Direct on `server-114`, `budget=30`, and `max_steps=8`. No RAG data, private evaluator artifact, or corrected target was presented to the Agent or uploaded remotely.

| Run | Completion / decision | Raw fault family | Experiments | Budget used | Remote jobs | Remote wall | Remote CPU | Peak memory | Evaluator |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| `R01_V022_NORAG_01` | API transport failure after `EXP_001` | — | 1 | 1 | 1 | 0.666664 s | 0.654129 s | 191.8125 MB | not scored |
| `R01_V022_NORAG_02` | schema failure before execution | — | 0 | 0 | 0 | — | — | — | not scored |
| `R01_V022_NORAG_03` | `inconclusive` (budget exhausted) | `null` | 8 | 26 | 8 | 2.433613 s | 3.455024 s | 191.8125 MB | 0.0 / 100 |

Run 01 reached a real remote inspect experiment, then the school API connection reset (`WinError 10054`) during hypothesis update. Run 02 failed because the provider returned a hypothesis count outside the frozen 2–5 item response schema. Run 03 completed eight real remote experiments but spent its budget on small shifts, `flip_x`, `rot90`, identity evaluation, and transpose. It did not test the high-value diagnostic candidate, so no repair reached the `0.75` threshold; the validation gate correctly emitted `inconclusive` rather than accepting a fault or no-fault claim.

Each run directory contains `trace.jsonl`, `compute_summary.json`, its per-experiment artifacts, and `evaluator.json`; run 03 also contains `state.json` and `final.json`.

## Failure analysis and frozen-Agent proof

The observed failure modes are: provider transport instability (run 01), provider schema non-compliance (run 02), and hypothesis generation / experiment-selection inefficiency leading to budget exhaustion (run 03). They are benchmark observations, not targets for prompt tuning. `git diff v0.2.2-agent-freeze..c90b87d -- src/scidiagnose/agent.py src/scidiagnose/diagnosis_graph.py` is empty: no frozen Agent prompt, planner, reflection, validation, search policy, or experiment-selection policy was modified for R01.

No RAG implementation, new scientific tool, or UI work was started. This baseline is ready for integration review.
