#!/usr/bin/env python3
"""Exact identities and a bounded census; no floating-point assertions."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


class Poly:
    """Sparse integer polynomials in s,t,m, sufficient for the two identities."""
    def __init__(self, value=0):
        self.c = ({(0, 0, 0): value} if value else {}) if isinstance(value, int) else {k: v for k, v in value.items() if v}

    @staticmethod
    def cast(v):
        return v if isinstance(v, Poly) else Poly(v)

    def __add__(self, other):
        other = self.cast(other)
        out = self.c.copy()
        for k, v in other.c.items():
            out[k] = out.get(k, 0) + v
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.c.items()})

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) + -self

    def __mul__(self, other):
        other = self.cast(other)
        out = {}
        for k, v in self.c.items():
            for j, w in other.c.items():
                key = tuple(a + b for a, b in zip(k, j))
                out[key] = out.get(key, 0) + v * w
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, n):
        out = Poly(1)
        for _ in range(n):
            out = out * self
        return out

    def __eq__(self, other):
        return self.c == self.cast(other).c


s = Poly({(1, 0, 0): 1})
t = Poly({(0, 1, 0): 1})
m = Poly({(0, 0, 1): 1})
R = s - t - 2
B = (s - t) * (8 * s - R) - 3 * R * s
H = 4 * s**2 * (t - 2) - 3 * s * t**2 - 16 * s - t**3 - 2 * t**2
assert B**2 - 4 * R * (5 * s - R) * (2 * s - R) * s == -(7 * s + t + 2) * H

N = m * s
R = (s - 4) * m + 1
B = m * (s - 2) * (8 * N - R) - 3 * R * N
E = m * s**2 - 7 * m**2 * s + 4 * m * s - 4 * m**2 + m - s
assert E == m * s * (s - 7 * m) + (4 * m - 1) * (s - m)
assert B**2 - 4 * R * (5 * N - R) * (2 * N - R) * N == -4 * m * (7 * m * s + 4 * m - 1) * E

assert 117 * 256 > 173**2  # rho_c < 3/16
assert [(19 * x - 108)**2 - 8 * x**3 for x in (16, 17)] == [5648, 6921]


def above_first_order(a, rho):
    assert 0 < rho < 1 and a > 0
    if (11 - rho)**2 <= 117:
        return (8 - rho) * a * a - 6 * rho * a + rho * (4 * rho - 5) > 0
    if a * a <= rho / 2:
        return False
    # For u*=a/sqrt(rho/2)-1>0, test u*²(u*+3)>sqrt(rho/2).
    A = a**3 - F(3, 2) * rho * a - rho**2 / 4
    return A >= 0 or A * A < rho**3 / 2


def check_one(s, m, r, powers=False):
    n = s * m
    if not above_first_order(F(r, s), F((r - 2) * m + 1, n)):
        return False
    assert r in (2, s - 2, s - 1), (s, m, r)
    if r == 2:
        assert 8 * m > s
    if r == s - 2:
        assert 7 * m > s
    bank = comb(s, r)
    assert bank < 4 * n
    if powers:
        assert bank < 2 * n
        if r in (2, s - 2):
            assert 4 * m >= s
    return True


integer_cases = integer_above = 0
for ss in range(16, 129):
    for mm in range(1, 33):
        for rr in range(2, ss):
            integer_cases += 1
            integer_above += check_one(ss, mm, rr)

power_cases = power_above = 0
for si in range(4, 11):
    ss = 2**si
    for mi in range(0, 11):
        mm = 2**mi
        for rr in range(2, ss):
            power_cases += 1
            power_above += check_one(ss, mm, rr, powers=True)

receipt = {
    "status": "PASS",
    "arithmetic": "exact integer polynomial coefficients and rational comparisons",
    "interior_factorization": True,
    "endpoint_factorization": True,
    "integer_census": {"s_range": [16, 128], "m_range": [1, 32], "cases": integer_cases, "above_first_order": integer_above},
    "power_of_two_census": {"s_exponents": [4, 10], "m_exponents": [0, 10], "cases": power_cases, "above_first_order": power_above},
    "scope": "Necessary condition for the canonical subset bank; not all line labels. The note supplies the unbounded proof."
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
