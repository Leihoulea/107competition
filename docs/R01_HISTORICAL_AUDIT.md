# R01 Historical Evidence Audit

## Case disposition

`R01` is a **historical-real reconstructed** benchmark based on a real Meteosat-0deg CLM versus EPIC L2 CLM silent failure at `2024-03-10T12:00:00Z`. The original computation completed normally and produced legal arrays; its scientific comparison was wrong because cloud values and navigation were in a relative spatial mismatch.

## Confirmed historical evidence

- Stage 09G retained the faulty-state native comparison result: agreement `0.5381503122`, cloud F1 `0.5919133044`, IoU `0.4203670883`, and MCC `0.0661277879` over `1,647,824` valid pixels.
- In the same historical diagnostic, applying a relative 180-degree relation between cloud values and navigation gave agreement `0.7961290683`, F1 `0.8163847213`, IoU `0.6897382418`, and MCC `0.5918923501` over `1,647,562` valid pixels. Rotating both values and navigation returned the faulty-state result.
- Stage 09H independently verified that raw GRIB cloud-mask storage and the existing native cloud-mask array agreed in identity order. It then compared current navigation with an official SEVIRI L1.5 area reference: identity navigation had p95 geodesic error about `15,267 km`; the relative 180-degree navigation transform reduced p95 to about `15.25 km`.
- Stage 09H Gate 3B changed navigation only, retained the CLM mask, and recovered EPIC-view agreement from `0.528463` to `0.801647` for `2024-03-12T15:00:00Z`.
- The reconstructed R01 native-grid package reproduces the same separation without a display-grid resampling: agreement is `0.5368982307` on `9,515,524` fixed common-valid pixels and `0.7982679672` under the diagnostic relative 180-degree relation, an absolute gain of `0.2613697364`.

## Inferred but not independently proven here

- EPIC is an independent diagnostic reference, not absolute cloud truth.
- The historical failure is attributable to navigation-orientation handling rather than a defect in the Meteosat cloud-mask classifier. This is supported by the independent navigation audit and preservation checks, not by the EPIC metric alone.

## Missing evidence and packaging level

- The original EPIC L2 input `DSCOVR_EPIC_L2_CLOUD_03_20240310115251_03.nc4` is now locally available, together with the retained Meteosat native NPZ.
- R01 is consequently Level B (`historical_real_reconstructed`): it reconstructs the historical relationship using those two raw inputs, instead of using the old `256 by 256` display-oriented artifact.
- The public pair preserves every `3712 by 3712` Meteosat native pixel. EPIC policy-A labels are nearest-neighbour sampled at the retained historical navigation with the Stage 09G `0.15 degree` limit. There is no 256 by 256 resampling and no locally selected patch.

## Repair interpretation

The public diagnostic transform is `rot180`, because it is the executable representation of the archived relative spatial mismatch for the frozen benchmark tools. The historical **production** correction was not a cloud-mask rotation: it replaced faulty navigation with verified SEVIRI native-area navigation and kept cloud-mask values identity-preserved.

## Evidence locations

- `stage_09g_orientation_root_cause_audit_202403/source_data/stage_09g_case_20240310_1200_diagnostic_plot_source.csv`
- `stage_09g_orientation_root_cause_audit_202403/source_data/stage_09g_20240310_1200_meteosat_native_transform_reprojection_metrics.csv`
- `stage_09h_meteosat_mask_navigation_root_cause_202403/reports/stage_09h_gate3b_navigation_direct_confirmation_report_cn.md`
- `stage_09h_meteosat_mask_navigation_root_cause_202403/source_data/stage_09h_gate3b_navigation_replacement_metrics.csv`
