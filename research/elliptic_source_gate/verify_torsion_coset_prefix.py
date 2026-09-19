#!/usr/bin/env python3
"""Exact characteristic-zero heads and the existing E[5]/F211 fixture.
No curve search, received-word search, or prefix-to-cofactor inference.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def sadd(*polys):
    out = {}
    for poly in polys:
        for key, value in poly.items():
            out[key] = out.get(key, 0) + value
    return {key: value for key, value in out.items() if value}


def sscale(poly, scalar):
    return {key: value * scalar for key, value in poly.items()}


def smul(left, right):
    out = {}
    for key, value in left.items():
        for key2, value2 in right.items():
            dest = tuple(a + b for a, b in zip(key, key2))
            out[dest] = out.get(dest, 0) + value * value2
    return {key: value for key, value in out.items() if value}


def spow(poly, exponent):
    out = {(0, 0, 0): 1}
    for _ in range(exponent):
        out = smul(out, poly)
    return out


# Monomial keys are (A exponent, B exponent, X exponent).
curve = {(0, 0, 3): 1, (1, 0, 1): 1, (0, 1, 0): 1}
psi3 = {(0, 0, 4): 3, (1, 0, 2): 6,
        (0, 1, 1): 12, (2, 0, 0): -1}
psi4_over_4y = {(0, 0, 6): 1, (1, 0, 4): 5,
               (0, 1, 3): 20, (2, 0, 2): -5,
               (1, 1, 1): -4, (0, 2, 0): -8, (3, 0, 0): -1}
phi5 = sscale(sadd(sscale(smul(spow(curve, 2), psi4_over_4y), 32),
                  sscale(spow(psi3, 3), -1)), F(1, 5))
expected = {
    12: {(0, 0): F(1)}, 11: {},
    10: {(1, 0): F(62, 5)},
    9: {(0, 1): F(76)}, 8: {(2, 0): F(-21)},
}
for degree, coefficients in expected.items():
    actual = {(a, b): value for (a, b, x), value in phi5.items()
              if x == degree}
    assert actual == coefficients

fixture = json.loads((ROOT / "shared_pole/pilot.json").read_text())
p = fixture["p"]
assert (p, fixture["ell"], fixture["curve_A"], fixture["curve_B"]) == (211, 5, 0, 16)
A, B = fixture["curve_A"], fixture["curve_B"]
points = {tuple(label): (tuple(point) if point is not None else None)
          for label, point in fixture["torsion_label_points"]}


def trim(poly):
    poly = [value % p for value in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(*polys):
    out = [0] * max(map(len, polys))
    for poly in polys:
        for i, value in enumerate(poly):
            out[i] += value
    return trim(out)


def scale(poly, scalar):
    return trim([scalar * value for value in poly])


def mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, value in enumerate(left):
        for j, value2 in enumerate(right):
            out[i + j] += value * value2
    return trim(out)


def div_exact(poly, divisor):
    rem = trim(poly)
    out = [0] * (len(rem) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, p)
    while len(rem) >= len(divisor) and rem != [0]:
        shift = len(rem) - len(divisor)
        coefficient = rem[-1] * inverse % p
        out[shift] = coefficient
        for i, value in enumerate(divisor):
            rem[i + shift] -= coefficient * value
        rem = trim(rem)
    assert rem == [0]
    return trim(out)


def ev(poly, x):
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def locator(roots):
    out = [1]
    for x in sorted(roots):
        out = mul(out, [-x, 1])
    return out


torsion_x = {point[0] for point in points.values() if point is not None}
assert len(torsion_x) == 12
Phi = locator(torsion_x)
assert Phi[-2] == 0 and Phi[-3] == 62 * A * pow(5, -1, p) % p
assert Phi[-4] == 76 * B % p
rows = []
for generator in [(1, j) for j in range(5)] + [(0, 1)]:
    subgroup = {tuple(k * coordinate % 5 for coordinate in generator)
                for k in range(5)}
    roots = {points[label][0] for label in subgroup if points[label] is not None}
    assert len(roots) == 2
    K = locator(roots)
    D = mul(K, K)
    N = [0] + D
    for x in roots:
        first = div_exact(D, [-x, 1])
        second = div_exact(first, [-x, 1])
        N = add(N, scale(first, 6 * x * x + 2 * A),
                scale(second, 4 * (x**3 + A * x + B)))
    S = sum(roots) % p
    product = K[0]
    c = 2 * S % p
    th = sum(6 * x * x + 2 * A for x in roots) % p
    assert N[-2] == D[-2] == -c % p
    assert N[-3] == (D[-3] + th) % p
    fibers = {}
    for label, point in points.items():
        if label in subgroup:
            continue
        x = point[0]
        xi = ev(N, x) * pow(ev(D, x), -1, p) % p
        fibers.setdefault(xi, set()).add(x)
    assert len(fibers) == 2
    for xi, fiber in fibers.items():
        assert len(fiber) == 5
        assert locator(fiber) == add(N, scale(D, -xi))
    xi, zeta = sorted(fibers)
    s, t = (xi + zeta) % p, xi * zeta % p
    U = mul(add(N, scale(D, -xi)), add(N, scale(D, -zeta)))
    assert mul(K, U) == Phi
    assert s == -5 * S % p
    assert t == (3 * S * S + 19 * product + 22 * A * pow(5, -1, p)) % p
    C1 = (2 * c + s) % p
    C2 = (Phi[-3] + 3 * c*c - 2 * D[-3] - 2 * th
          + 2 * c*s + s*s - t) % p
    assert [C2, C1, 1] == K
    rows.append(dict(generator=generator, kernel_x=sorted(roots),
                     K=K, quotient_fiber_values=sorted(fibers),
                     omitted_first_heads=[U[-2], U[-3], U[-4]],
                     retained_first_heads=[C1, C2]))

receipt = {
    "status": "PASS",
    "scope": "Formal division-polynomial heads and six existing order-five subgroups; no line search.",
    "characteristic_zero_phi5_heads": ["1", "0", "62*A/5", "76*B", "-21*A^2"],
    "fixture": {"p": p, "A": A, "B": B, "ell": 5,
                "domain_size": 12, "subgroups": rows},
    "small_order_caveat": "ell=3 has no pair of distinct full fibers; ell=5 retained complement is the quadratic kernel locator.",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
