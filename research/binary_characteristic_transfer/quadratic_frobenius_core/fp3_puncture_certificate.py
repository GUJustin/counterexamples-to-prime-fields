"""Worst-length exact arithmetic for the punctured far-endpoint theorem."""
import json
from math import isqrt
from pathlib import Path

rows = []
for p in (4099, 8191, 65537):
    nmin, nmax = 2*p*p-4*p+1, 2*p*p-p-1
    ceilroot = isqrt(16*p)+int(isqrt(16*p)**2 < 16*p)
    T = 2*p-ceilroot-8
    B, H = 3*T, 120*T
    G, R = 4*B*B-2*B, 62
    margin = (H-B+1)*G-(H+1)*nmax*R
    assert T*T < 2*nmin
    assert T > p and (T-p)**2 > 4*p
    assert 5*B >= 29*p and margin > 0
    rows.append(dict(p=p, n_min=nmin, n_max=nmax, T=T,
                     guaranteed_singleton_labels=p**3-p*p,
                     deleted_coordinate_bound=3*p-2,
                     graded_margin_at_largest_length=margin,
                     characteristic_guard=p>3, passed=True))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows, indent=2)+'\n')
print(json.dumps(rows, indent=2))
