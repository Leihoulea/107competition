# R01 Case Specification

## Scientific scenario

Meteosat operational cloud-mask output was compared with a temporally paired EPIC L2 cloud mask. The job completed successfully, but agreement was far below the historically diagnosed comparison result.

## Silent-failure mechanism

The error was spatial: the cloud-mask values and navigation had a relative orientation mismatch. Normal process completion, valid dtypes, and nonempty output did not detect it.

## Agent-visible material

- `task.json` and `initial_result.json`
- `public/reference.npy`, `public/target.npy`, and `public/valid_mask.npy`
- neutral product/time/metric metadata

The remote adapter maps these canonical public files to the frozen runner input names without duplicating the large native arrays.

## Evaluator-private material

- historical evidence and missing-evidence boundary
- the diagnostic transform and deterministic validation rule
- production remediation, provenance, and wrong-repair landscape

Private files must never be sent to `server-114`.

## Candidate hypotheses for benchmark design

- spatial orientation or navigation mismatch
- translation or navigation offset
- temporal mismatch
- mask-definition mismatch
- genuine inter-sensor/product disagreement

These are benchmark documentation only; they are not inserted into an agent prompt.

## Validation rule

The packaged transform must improve agreement by at least `0.15`, retain all initial valid support, and rank above the enumerated wrong-transform controls. The public quality threshold `0.75` is derived from the native-grid package's before/after separation, not from a universal accuracy requirement.

## Scope and claim

R01 is a historical real failure packaged with evaluator separation. It is not claimed to be a wholly unseen blind case, and EPIC is not asserted as absolute truth.
