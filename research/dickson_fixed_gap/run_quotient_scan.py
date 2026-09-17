"""Replay the bounded finite quotient census and preserve exact outputs."""
import json
from pathlib import Path
import subprocess

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
fixtures = [(4,17)] + [(r,65521) for r in range(1,8)] + [(8,65537),(9,65521)]
results = []
for r,p in fixtures:
    result = subprocess.run([str(ROOT/'tmp/dickson-quotient-scan'),str(r),str(p)],
                            capture_output=True,text=True,check=True)
    record = json.loads(result.stdout)
    results.append(record)
    print(json.dumps(record),flush=True)
    (BASE/'quotient_scan_results.json').write_text(json.dumps(results,indent=2)+'\n')
