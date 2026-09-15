#!/usr/bin/env python3
"""Exact finite checks for Gram concentration; standard library only."""
from fractions import Fraction
from math import comb, factorial, isqrt, prod
from pathlib import Path
import json


def ceil_sqrt(q):
    v = isqrt(q.numerator // q.denominator)
    return v if v * v * q.denominator == q.numerator else v + 1


def norm(n, j):
    return Fraction(prod(n*n-i*i for i in range(1, j+1)),
                    (2*j+1)*comb(2*j, j)**2*factorial(j)**2)


def gram(n, j, x):
    def f(y):
        return prod(y-i for i in range(j))*prod(y-n-i for i in range(j))
    return Fraction(sum((-1)**(j-a)*comb(j, a)*f(x+a)
                        for a in range(j+1)), factorial(2*j))


def ceil_ratio(a, b):
    return (a+b-1)//b


def floor_log_ratio(a, b):
    """floor(log2(a/b)), without floating point."""
    e = a.bit_length()-b.bit_length()
    if e >= 0:
        return e if a >= b << e else e-1
    return e if a << -e >= b else e-1


checks = 0
for n in range(3, 19):
    rows = []
    for j in range(1, min(n-1, 8)+1):
        row = [gram(n, j, x) for x in range(n)]
        assert sum(row) == 0
        assert sum(x*x for x in row)/n == norm(n, j)
        for earlier in rows:
            assert sum(a*b for a, b in zip(row, earlier)) == 0
        if j > 1:
            assert norm(n,j)/norm(n,j-1) == Fraction(n*n-j*j,4*(2*j-1)*(2*j+1))
        rows.append(row)
        checks += 1

fixtures = []
for n, m in [(64, 2), (128, 4), (256, 6), (512, 8),
             (1024, 10), (4096, 20), (16384, 40)]:
    t = n//2+m
    count = comb(n, t)
    variances = [Fraction(t*(n-t), n-1)*norm(n, j) for j in range(1, m+1)]
    hs = [ceil_sqrt((m+2)*v) for v in variances]
    for h, v in zip(hs, variances):
        assert (h-1)**2 < (m+2)*v <= h*h
    dg2 = (m+2)*prod(2*h+1 for h in hs)
    dr = prod(comb(n,j+1)-comb(n-t,j+1)-comb(t,j+1)+1 for j in range(1,m+1))
    lg = ceil_ratio(2*count, dg2)
    lr = ceil_ratio(count, dr)
    assert lg >= lr
    fixtures.append({
        "n": n, "k": n//2, "m": m, "t": t,
        "gram_list_lower_bound_floor_log2": lg.bit_length()-1,
        "range_list_lower_bound_floor_log2": lr.bit_length()-1,
        "unrounded_improvement_floor_log2": floor_log_ratio(2*dr, dg2),
    })

result = {"status": "all exact assertions passed",
          "gram_norm_fixtures": checks,
          "finite_bound_fixtures": fixtures}
destination = Path(__file__).with_name("growing_m_verified.json")
destination.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
