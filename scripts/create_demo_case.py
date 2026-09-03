"""Generate the deterministic, public GEO-001 synthetic diagnosis case."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]; CASE = ROOT / "cases" / "geo_001"; DATA = CASE / "public" / "data"
def agreement(a: np.ndarray, b: np.ndarray) -> float: return float(np.mean(a == b))
def main() -> None:
    DATA.mkdir(parents=True, exist_ok=True); (CASE / "hidden").mkdir(exist_ok=True)
    y, x = np.mgrid[-1:1:256j, -1:1:256j]; field = np.zeros((256, 256), dtype=float)
    for cx, cy, sx, sy, amp in [(-.57,-.38,.16,.10,1.3), (.42,.31,.23,.16,1.0), (-.17,.55,.11,.19,.9), (.60,-.61,.08,.12,.8)]: field += amp*np.exp(-(((x-cx)/sx)**2+((y-cy)/sy)**2)/2)
    noise = np.random.default_rng(20260903).normal(0, .025, field.shape); reference = (field+noise > .06).astype(np.uint8)
    clean = reference.copy(); faulty = np.rot90(clean, 2)
    identity, repaired = agreement(reference, faulty), agreement(reference, np.rot90(faulty, 2))
    if not (identity < .65 and repaired > .85): raise RuntimeError(f"Synthetic case thresholds failed: {identity=}, {repaired=}")
    np.save(DATA/"reference.npy", reference); np.save(DATA/"target_clean.npy", clean); np.save(DATA/"target_faulty.npy", faulty)
    task = {"case_id":"GEO-001", "title":"Unexpected spatial disagreement between two scientific products", "task":"A scientific comparison process completed successfully, but two spatial scientific products show unexpectedly low agreement. Determine whether a scientific silent failure exists. Use available computational experiments to gather evidence, identify the most likely root cause, and validate a repair.", "budget":30, "expected_quality_threshold":.80}
    (CASE/"task.json").write_text(json.dumps(task, indent=2)); (CASE/"initial_result.json").write_text(json.dumps({"process_status":"COMPLETED","exit_code":0,"agreement":identity,"valid_pixels":int(reference.size)}, indent=2)); (CASE/"hidden"/"ground_truth.json").write_text(json.dumps({"fault":True,"fault_family":"spatial_alignment","root_cause":"orientation_mismatch","expected_transform":"rot180"}, indent=2)); (CASE/"public"/"README.md").write_text("Public GEO-001 inputs. The hidden directory is never available to the diagnosis agent.\n")
    print(json.dumps({"identity":identity,"rot180":repaired}, indent=2))
if __name__ == "__main__": main()
