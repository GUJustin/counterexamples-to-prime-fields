"""Recompute the degree-40 conditional moments with exact integers."""
from pathlib import Path
import json
import sys
import time

ROOT = Path(__file__).parent
sys.path.insert(0,str(ROOT.parent.parent/'moment_certificates'))
from compute_moments import moments, centered

start = time.perf_counter()
rows, updates = moments(64,34,1071,40)
raw = rows[1071]
result = dict(n=64,t=34,q=1071,center=22138,degree=40,
    raw_moments=raw,centered_moments=centered(raw,22138),updates=updates,
    seconds=time.perf_counter()-start)
(ROOT/'moments40.json').write_text(json.dumps(result,indent=2)+'\n')
print('Computed exact moments through degree 40 in',result['seconds'],'seconds.')
