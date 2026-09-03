"""Direct-SSH smoke workload with structured success/failure outputs."""
from __future__ import annotations
import json, os, platform, time, traceback
from pathlib import Path
def main() -> None:
    started = time.monotonic()
    try:
        value = sum(range(10_000)); time.sleep(2.5)
        result = {"status":"success", "hostname":platform.node(), "pid":os.getpid(), "python_version":platform.python_version(), "result":value, "elapsed_seconds":round(time.monotonic()-started,3)}
        Path("result.json").write_text(json.dumps(result, indent=2), encoding="utf-8"); print(json.dumps(result), flush=True)
    except BaseException as exc:
        Path("failure.json").write_text(json.dumps({"status":"failed", "error_type":type(exc).__name__, "message":str(exc), "traceback":traceback.format_exc()}, indent=2), encoding="utf-8"); raise
if __name__ == "__main__": main()
