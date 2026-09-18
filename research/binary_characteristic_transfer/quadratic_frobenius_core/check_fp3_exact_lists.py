"""Exact physical-fiber and label census; no enumeration of all quadratics.

The separate proved quadratic classification excludes competitors.
These small primes test the spectrum, not the p>=4099 uniform certificate.
"""
import json
from collections import Counter
from math import isqrt
from pathlib import Path


def check(p):
    aa, bb = next((a, b) for a in range(p) for b in range(1, p)
                  if all((t**3+a*t+b) % p for t in range(p)))
    zero, one, eta = (0, 0, 0), (1, 0, 0), (0, 0, 1)

    def sub(x, y):
        return tuple((a-b) % p for a, b in zip(x, y))

    def mul(x, y):
        c0, c1, c2 = x[0]*y[0], x[0]*y[1]+x[1]*y[0], x[0]*y[2]+x[1]*y[1]+x[2]*y[0]
        c3, c4 = x[1]*y[2]+x[2]*y[1], x[2]*y[2]
        return ((c0-bb*c3) % p, (c1-aa*c3-bb*c4) % p, (c2-aa*c4) % p)

    def power(x, n):
        r = one
        while n:
            if n & 1:
                r = mul(r, x)
            x = mul(x, x)
            n //= 2
        return r

    W = [(a, b, 0) for a in range(p) for b in range(p)]
    yp = {y: power(y, p) for y in W}
    weight = {y: (0 if y == zero else 2*int(power(y, (p**3-1)//2) == one)) for y in W}
    assert sum(weight.values()) == p*p-1
    deleted = [y for y in W if mul(eta, y)[2] == 0]
    assert len(deleted) == p and sum(weight[y] for y in deleted) == p-1
    ceilroot = isqrt(16*p)+int(isqrt(16*p)**2 < 16*p)
    A = 2*p-ceilroot-2
    assert (A-p)**2 > 4*p and A > p and A > 16
    lists, best = Counter(), {}
    for u in [one]+[(a, 1, 0) for a in range(p)]:
        a = power(u, p-1)
        core, removed = Counter(), Counter()
        for y in W:
            b = sub(yp[y], mul(a, y))
            core[b] += weight[y]
        for y in deleted:
            removed[sub(yp[y], mul(a, y))] += weight[y]
        assert len(core) == p
        fresh = {v: count-removed[v] for v, count in core.items()}
        for b, c0 in core.items():
            for v, c1 in fresh.items():
                lam = sub(b, mul(eta, v))
                agreement = c0+c1
                best[lam] = max(best.get(lam, 0), agreement)
                if agreement >= A:
                    lists[lam] += 1
    assert len(lists) == p**3
    histogram = Counter(lists.values())
    assert histogram == {1: p**3-p, p: p}
    return dict(p=p, defining_cubic=[bb, aa, 0, 1], eta=eta,
                N=2*p*p-p-1, A=A, label_count=len(lists),
                list_size_histogram=dict(histogram),
                minimum_best_canonical_agreement=min(best.values()),
                maximum_best_canonical_agreement=max(best.values()), passed=True)


if __name__ == '__main__':
    rows = [check(p) for p in (47, 53)]
    Path(__file__).with_suffix('.json').write_text(json.dumps(rows, indent=2)+'\n')
    print(json.dumps(rows, indent=2))
