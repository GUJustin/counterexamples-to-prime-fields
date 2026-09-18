#!/usr/bin/env python3
"""Bounded owned-process runner for the exact finite verifier."""
from pathlib import Path
import json
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
started = time.monotonic()
proc = subprocess.Popen([sys.executable, str(root / "verify_fixture.py")],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
peak_rss_kib = 0
termination = None
while proc.poll() is None:
    if time.monotonic() - started > 58:
        termination = "wall-time limit"
        proc.kill()
        break
    sample = subprocess.run(["ps", "-o", "rss=", "-p", str(proc.pid)],
                            capture_output=True, text=True).stdout.strip()
    if sample:
        peak_rss_kib = max(peak_rss_kib, int(sample))
        if int(sample) > 512 * 1024:
            termination = "RSS limit"
            proc.kill()
            break
    time.sleep(0.05)
stdout, stderr = proc.communicate()
resources = {"wall_time_seconds": time.monotonic() - started,
             "polled_peak_rss_kib": peak_rss_kib,
             "returncode": proc.returncode, "termination": termination,
             "wall_limit_seconds": 58, "memory_limit_mib": 512}
(root / "resources.json").write_text(json.dumps(resources, indent=2) + "\n")
print(stdout, end="")
if stderr:
    print(stderr, file=sys.stderr, end="")
print(json.dumps(resources, indent=2))
raise SystemExit(proc.returncode or (1 if termination else 0))
