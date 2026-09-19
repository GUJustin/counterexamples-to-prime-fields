"""Small exact fixture, not a parameter search or quadratic census.

Checks Q=9 in F_(3^6), a trace-dual q=3 subplane, both projective
orientations, and the integer field-intersection formula. Standard library.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import gcd
from pathlib import Path
import json


P, DEG, SIZE, Q = 3, 6, 729, 9
# Ascending coefficients: T^6 + T + 2. Irreducibility is checked below.
MODULUS = [2, 1, 0, 0, 0, 0, 1]
DIGITS = [tuple((x // P**i) % P for i in range(DEG)) for x in range(SIZE)]


def encode(xs):
    return sum((v % P) * P**i for i, v in enumerate(xs))


def add(x, y):
    return encode(a + b for a, b in zip(DIGITS[x], DIGITS[y]))


def neg(x):
    return encode(-a for a in DIGITS[x])


def sub(x, y):
    return add(x, neg(y))


@lru_cache(maxsize=100000)
def mul(x, y):
    h = [0] * (2 * DEG - 1)
    for i, a in enumerate(DIGITS[x]):
        for j, b in enumerate(DIGITS[y]):
            h[i + j] += a * b
    for i in range(2 * DEG - 2, DEG - 1, -1):
        for j in range(DEG):
            h[i - DEG + j] -= h[i] * MODULUS[j]
    return encode(h[:DEG])


def power(x, n):
    if n < 0:
        assert x
        n %= SIZE - 1
    z = 1
    while n:
        if n & 1:
            z = mul(z, x)
        x = mul(x, x)
        n //= 2
    return z


def divide(x, y):
    assert y
    return mul(x, power(y, SIZE - 2))


def trim(xs):
    while xs and not xs[-1]:
        xs.pop()
    return xs


def poly_rem(a, b):
    a = trim(a[:])
    while len(a) >= len(b):
        c = a[-1] * pow(b[-1], -1, P) % P
        shift = len(a) - len(b)
        for j in range(len(b)):
            a[shift + j] = (a[shift + j] - c * b[j]) % P
        trim(a)
    return a


def poly_gcd(a, b):
    a, b = trim(a[:]), trim(b[:])
    while b:
        a, b = b, poly_rem(a, b)
    return [(v * pow(a[-1], -1, P)) % P for v in a]


alpha = P  # residue class of T
assert power(alpha, P**DEG) == alpha
for exponent in (2, 3):
    residual = sub(power(alpha, P**exponent), alpha)
    assert poly_gcd(MODULUS, list(DIGITS[residual])) == [1]
assert all(power(x, SIZE - 1) == 1 for x in range(1, SIZE))


def trace(x):
    return add(add(x, power(x, Q)), power(x, Q * Q))


def norm(x):
    return power(x, Q * Q + Q + 1)


FQ = [x for x in range(SIZE) if power(x, Q) == x]
assert len(FQ) == Q
domain = [x for x in range(1, SIZE) if power(norm(x), 2) == 1]
assert len(domain) == 2 * (Q * Q + Q + 1)
word = {x: power(x, 2 * Q + 2) for x in domain}
minus_one = neg(1)
native_bank = [a for a in range(1, SIZE) if norm(a) == minus_one]
native_counts = Counter(
    sum(sub(mul(a, power(x, 2)), power(a, Q * Q + 1)) == word[x]
        for x in domain)
    for a in native_bank)
assert native_counts == {2 * Q + 2: Q * Q + Q + 1}

# An E/F_Q basis and its trace dual. This includes characteristic 3,
# where Tr(1)=0; nondegeneracy of the pairing still gives a unique dual.
basis = [1, alpha, power(alpha, 2)]
dual = []
for j in range(3):
    candidates = [d for d in range(SIZE)
                  if all(trace(mul(b, d)) == int(i == j)
                         for i, b in enumerate(basis))]
    assert len(candidates) == 1
    dual.append(candidates[0])


def linear_combination(cs, bs):
    z = 0
    for c, b in zip(cs, bs):
        z = add(z, mul(c, b))
    return z


q = 3
projective = [cs for cs in product(range(q), repeat=3)
              if any(cs) and next(c for c in cs if c) == 1]
us = [linear_combination(cs, basis) for cs in projective]
ds = [linear_combination(cs, dual) for cs in projective]
ys = {power(u, Q - 1) for u in us}
small_domain = [x for x in domain if power(x, 2) in ys]
assert len(us) == len(ds) == len(ys) == q * q + q + 1
assert len(small_domain) == 2 * (q * q + q + 1)
small_bank = [(neg(power(d, Q - Q * Q)), neg(power(d, 1 - Q * Q)))
              for d in ds]
assert len(set(small_bank)) == q * q + q + 1
counts, incidences, supports = [], Counter(), []
trace_checks = 0
for d, (a, c) in zip(ds, small_bank):
    support = set()
    for u in us:
        y = power(u, Q - 1)
        matches = power(y, Q + 1) == add(mul(a, y), c)
        assert matches == (trace(mul(d, u)) == 0)
        trace_checks += 1
    for x in small_domain:
        if add(mul(a, power(x, 2)), c) == word[x]:
            support.add(x)
            incidences[x] += 1
    counts.append(len(support))
    supports.append(support)
assert set(counts) == {2 * q + 2}
assert set(incidences.values()) == {q + 1}
assert all(len(supports[i] & supports[j]) == 2
           for i in range(len(supports)) for j in range(i))

# Finite and infinite projective points in both norm-constant orientations.
b = alpha
bq, bqq = power(b, Q), power(b, Q * Q)
assert len({b, bq, bqq}) == 3
orientation_counts = {}
for v, orientation in ((bq, "quartic"), (bqq, "quadratic")):
    for t in FQ:
        x = divide(sub(t, b), sub(t, v))
        assert norm(x) == 1 and x in domain
        twisted = mul(power(sub(t, v), 2), word[x])
        if orientation == "quartic":
            expected = divide(mul(power(sub(t, bq), 2), power(sub(t, b), 2)),
                              power(sub(t, bqq), 2))
        else:
            expected = power(sub(t, bq), 2)
        assert twisted == expected
    # At infinity phi(infinity)=1, and all degree-two section leading values
    # in the displayed identities are 1.
    assert word[1] == 1
    orientation_counts[orientation] = len(FQ) + 1
# The quartic difference has a genuine pole at b^(Q^2), independent of
# which polynomial of degree at most two is subtracted.
assert mul(power(sub(bqq, bq), 2), power(sub(bqq, b), 2)) != 0


def v3(n):
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


intersection_checks = 0
for ell in (3, 5, 7, 11):
    for r in range(1, 13):
        base = ell**r
        L = base * base + base + 1
        for m in range(1, 13):
            d, g = gcd(r, m), gcd(3 * r, m)
            actual_g = gcd(L, ell**g - 1)
            actual_d = gcd(2 * L, ell**g - 1)
            if v3(m) <= v3(r):
                expected_g = gcd(3, ell**d - 1)
                expected_d = gcd(6, ell**d - 1)
                assert g == d
            else:
                q0 = ell**d
                expected_g = q0 * q0 + q0 + 1
                expected_d = 2 * expected_g
                assert g == 3 * d and (r // d) % 3
            assert (actual_g, actual_d) == (expected_g, expected_d)
            intersection_checks += 1

receipt = dict(
    passed=True,
    scope="Exact small fixture and formula checks; no exhaustive quadratic census.",
    characteristic=P, prime_power_base=Q, ambient_degree=DEG,
    modulus_ascending=MODULUS, irreducibility="Rabin degree-6 test passed",
    native=dict(domain=len(domain), bank=len(native_bank),
                agreements=dict(native_counts)),
    trace_dual_subplane=dict(base=q, basis=basis, dual_basis=dual,
                            domain=len(small_domain), bank=len(small_bank),
                            agreement=counts[0], trace_identity_checks=trace_checks,
                            coordinate_incidence=q+1, pair_intersection=2),
    projective_orientation_checks=orientation_counts,
    integer_intersection_formula_checks=intersection_checks,
)
Path(__file__).with_suffix('.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
