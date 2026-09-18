"""Exact canonical-bank census for the proposed Fp^3 two-block transfer.

This is not a census of all quadratics or a better.codes certificate.
"""
import itertools
import json
from collections import Counter
from functools import lru_cache
from pathlib import Path


def check(p):
    aa, bb = next((a, b) for a in range(p) for b in range(1, p)
                  if all((t**3 + a*t + b) % p for t in range(p)))
    E = list(itertools.product(range(p), repeat=3))
    zero, one = (0, 0, 0), (1, 0, 0)

    def add(x, y):
        return tuple((a+b) % p for a, b in zip(x, y))

    def sub(x, y):
        return tuple((a-b) % p for a, b in zip(x, y))

    @lru_cache(None)
    def mul(x, y):
        c = [0]*5
        for i in range(3):
            for j in range(3):
                c[i+j] += x[i]*y[j]
        for i in (4, 3):
            c[i-2] -= aa*c[i]
            c[i-3] -= bb*c[i]
        return tuple(v % p for v in c[:3])

    def power(x, n):
        r = one
        while n:
            if n & 1:
                r = mul(r, x)
            x = mul(x, x)
            n //= 2
        return r

    W = {(a, b, 0) for a in range(p) for b in range(p)}
    eta = next(power(s, 2) for s in E if s != zero
               and power(s, 2)[1:] != (0, 0))
    eta_inv = power(eta, p**3-2)
    scaled_W = {mul(eta, y) for y in W}
    squares = {x: mul(x, x) for x in E}
    D0 = [x for x in E if x != zero and squares[x] in W]
    D1_full = [x for x in E if x != zero and squares[x] in scaled_W]
    D1 = [x for x in D1_full if squares[x] not in W]
    assert len(D0) == p*p-1
    assert len(D1_full)-len(D1) == p-1
    directions = [one] + [(a, 1, 0) for a in range(p)]
    bank = []
    for u in directions:
        a = power(u, p-1)
        image = {sub(power(y, p), mul(a, y)) for y in W}
        assert len(image) == p
        bank.extend((a, b) for b in image)
    assert len(set(bank)) == p*(p+1)
    best = {lam: 0 for lam in E}
    f0 = {x: power(squares[x], p) for x in D0}
    f1 = {x: mul(eta, power(mul(eta_inv, squares[x]), p)) for x in D1}
    for a, b in bank:
        core = sum(add(mul(a, squares[x]), b) == f0[x] for x in D0)
        fresh = Counter(sub(add(mul(a, squares[x]), b), f1[x]) for x in D1)
        for lam in E:
            best[lam] = max(best[lam], core + fresh[lam])
    return dict(p=p, cubic=[bb, aa, 0, 1], eta=eta,
                core_length=len(D0), fresh_length=len(D1), bank_size=len(bank),
                minimum_over_labels=min(best.values()),
                maximum_over_labels=max(best.values()),
                maximum_bank_agreement_histogram=dict(sorted(Counter(best.values()).items())),
                scope="canonical bank only; overlap assigned to core")


if __name__ == '__main__':
    rows = [check(p) for p in (3, 5, 7, 11)]
    Path(__file__).with_suffix('.json').write_text(json.dumps(rows, indent=2)+'\n')
    print(json.dumps(rows, indent=2))
