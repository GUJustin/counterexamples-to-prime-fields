"""Inspect signed negacyclic translates of ternary rows from the bounded pilot.

No random search. The fixed finite search is each available ternary basis row
plus or minus each of its 127 nonidentity signed shifts. Exact verification
uses all six moments and the root product on the original 256 roots.
"""

import json
import math
from pathlib import Path
import time

D = Path(__file__).parent
p = 2130706433
zeta = pow(3, (p - 1) // 256, p)
start = time.monotonic()
assert pow(zeta, 128, p) == p - 1


def shift(v, s):
    ans = [0] * 128
    for j, c in enumerate(v):
        ans[(j + s) % 128] = c if j + s < 128 else -c
    return ans


def anchor(v):
    j = next(i for i, x in enumerate(v) if x == 0)
    ans = shift(v, (-j) % 128)
    assert ans[0] == 0
    if next(x for x in ans if x) < 0:
        ans = [-x for x in ans]
    return tuple(ans)


found, checked, sources = {}, 0, []
for stage in ("lll", "bkz20", "bkz40", "bkz50"):
    path = D / (stage + "_basis.json")
    if not path.exists():
        continue
    rows = json.loads(path.read_text())
    for i, row in enumerate(rows):
        if max(abs(x) for x in row) > 1 or not any(row):
            continue
        v = [0] + row
        assert all(sum(c * pow(zeta, k * j, p) for j, c in enumerate(v)) % p == 0 for k in (1, 3, 5))
        sources.append(dict(stage=stage, row=i, support=sum(x != 0 for x in v)))
        for s in range(1, 128):
            w = shift(v, s)
            for sign in (-1, 1):
                checked += 1
                c = [x + sign * y for x, y in zip(v, w)]
                if max(abs(x) for x in c) <= 1 and any(c) and sum(c) % 2 == 0 and 0 in c:
                    found.setdefault(anchor(c), dict(stage=stage, row=i, shift=s, sign=sign))

verified = []
for d in sorted(found, key=lambda v: (sum(x != 0 for x in v), v)):
    A, B = [], []
    for j, v in enumerate(d):
        if v == 1:
            A.append(j)
            B.append(j + 128)
        elif v == -1:
            A.append(j + 128)
            B.append(j)
    A.sort()
    B.sort()
    differences = [(sum(pow(zeta, k * a, p) for a in A) - sum(pow(zeta, k * b, p) for b in B)) % p
                   for k in range(1, 7)]
    pa = math.prod(pow(zeta, a, p) for a in A) % p
    pb = math.prod(pow(zeta, b, p) for b in B) % p
    assert A and len(A) == len(B) and len(A) % 2 == 0
    assert 0 not in A + B and 128 not in A + B and not set(A) & set(B)
    assert sorted((a + 128) % 256 for a in A) == B
    assert differences == [0] * 6 and pa == pb
    assert (sum(A) - sum(B)) % 256 == 0
    assert any((j in A) != ((j + 64) % 256 in A) for j in range(256))
    verified.append(dict(provenance=found[d], d=list(d), support=len(A),
                         A_exponents=A, B_exponents=B, six_moment_differences=differences,
                         product_a=pa, product_b=pb, product_exponent_difference=0,
                         genuinely_cross_partial_pattern=True))

result = dict(p=p, zeta=zeta, root_order=256, sources=sources,
              signed_translate_combinations_checked=checked,
              verified_relations=verified,
              min_support=verified[0]["support"] if verified else None,
              seconds=time.monotonic() - start,
              scope="exact cross-pattern exchanges, not a large-fiber certificate")
(D / "rotated_result.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "verified_relations"}, indent=2))
print("verified", len(verified))
