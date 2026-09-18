"""Exact p17 support audit; no parameter search or lifting claims."""
import json
from math import comb
from itertools import combinations
from pathlib import Path

p = 17
supports = []
for a in range(1, 9):
    coeffs = [comb(9, 2*j+1)*pow(a, 8-2*j, p) % p for j in range(4)]
    support = [x for x in range(1, p)
               if sum(c*pow(x, j, p) for j, c in enumerate(coeffs)) % p
               == ((1+pow(x, 8, p))*9-pow(x, 4, p)) % p]
    assert len(support) == 6
    supports.append(support)
pairs = [{"a": i+1, "b": j+1,
          "intersection": sorted(set(supports[i]) & set(supports[j]))}
         for i, j in combinations(range(8), 2)]
hist = {str(k): sum(len(q["intersection"]) == k for q in pairs)
        for k in range(7)}
assert hist == {"0": 0, "1": 4, "2": 20, "3": 4,
                "4": 0, "5": 0, "6": 0}
out = {"prime": p, "supports": supports, "pairs": pairs,
       "intersection_histogram": hist,
       "scope": "Exact support data only; gluing obstruction uses root counting."}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print("PASS: eight six-point supports and all 28 intersections")
