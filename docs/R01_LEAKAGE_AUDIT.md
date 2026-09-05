# R01 public-data leakage audit

## Scope

This audit covers every artifact available to a frozen SciDiagnose run: `task.json`, `initial_result.json`, files under `public/`, and their filenames. It does not treat evaluator-private records or repository documentation as Agent-visible runtime inputs.

## Result: pass

The public task states only a completed Meteosat/EPIC cloud-mask comparison-quality anomaly and asks for public experiments. The initial result contains process status and measured agreement. Public metadata identifies products, time, metric, grid, and data kind, but does not name a diagnosis or repair.

The public file names are neutral: `reference.npy`, `target_faulty.npy`, and `target_valid.npy`. They contain only the binary comparison arrays and valid support required by the frozen remote runner. The use of `target_faulty.npy` is the pre-existing frozen runner contract, not a hidden cause label.

The following private-only concepts are absent from Agent-visible JSON and filenames: the benchmark diagnostic transform, orientation/navigation diagnosis, production remediation, evaluator ground truth, repair landscape, validation thresholds beyond the public quality threshold, and provenance notes. A numeric longitude value of 180 would not itself be considered leakage; no such string-only rule is used.

## Remote boundary

`ExperimentTools._ensure_data()` has an explicit three-array allowlist plus the remote runner. The R01 integration test records the upload calls and proves that no `evaluator_private` artifact, private filename, corrected target, validation record, or provenance note is selected for upload.
