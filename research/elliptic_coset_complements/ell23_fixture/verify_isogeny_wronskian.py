#!/usr/bin/env python3
"""Exact identity replay on the existing fixture; no locator or curve search."""
import hashlib
import json
from pathlib import Path
import time

base = Path(__file__).resolve().parent
fixture_path = base / "fixture.json"
fixture = json.loads(fixture_path.read_text())
p = fixture["p"]


def trim(a):
    a = [x % p for x in a]
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return trim(c)


def scale(a, c):
    return trim([c * x for x in a])


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def power(a, e):
    out = [1]
    for _ in range(e):
        out = mul(out, a)
    return out


def derivative(a):
    return trim([i * a[i] for i in range(1, len(a))])


def divide(a, b):
    assert b
    a = trim(a)
    q = [0] * max(0, len(a) - len(b) + 1)
    inverse = pow(b[-1], -1, p)
    while len(a) >= len(b):
        j = len(a) - len(b)
        c = a[-1] * inverse % p
        q[j] = c
        for i, v in enumerate(b):
            a[i + j] = (a[i + j] - c * v) % p
        a = trim(a)
    return trim(q), a


def exact_divide(a, b):
    q, r = divide(a, b)
    assert not r
    return q


def gcd(a, b):
    while b:
        a, b = b, divide(a, b)[1]
    return scale(a, pow(a[-1], -1, p))


started = time.perf_counter()
ell = fixture["ell"]
t = (ell - 1) // 2
assert p == 1657 and ell == 23
Phi = [1]
for x in fixture["domain"]:
    Phi = mul(Phi, [-x, 1])
F = [fixture["curve"]["b"], fixture["curve"]["a"], 0, 1]
results = []
for index, group in enumerate(fixture["subgroups"]):
    K, B, N = group["K"], group["B"], group["N"]
    assert B == power(K, 2)
    R = sub(mul(derivative(N), K), scale(mul(N, derivative(K)), 2))
    W = sub(mul(derivative(N), B), mul(N, derivative(B)))
    assert len(R) - 1 == 3 * t and R[-1] == 1
    assert W == mul(K, R)
    assert gcd(Phi, R) == [1]
    assert gcd(Phi, W) == K

    # Recover the unique quotient curve coefficients from the exact identity.
    quotient = exact_divide(sub(mul(F, power(R, 2)), power(N, 3)), power(K, 4))
    assert len(quotient) <= ell + 1
    a_curve = quotient[ell] if len(quotient) > ell else 0
    constant = exact_divide(sub(quotient, scale(N, a_curve)), B)
    assert len(constant) <= 1
    b_curve = constant[0] if constant else 0
    rhs = add(add(power(N, 3), scale(mul(N, power(K, 4)), a_curve)),
              scale(power(K, 6), b_curve))
    assert mul(F, power(R, 2)) == rhs

    a_tag, b_tag = [entry["tag"] for entry in group["fibers"][:2]]
    assert a_tag != b_tag
    La, Lb = sub(N, scale(B, a_tag)), sub(N, scale(B, b_tag))
    pair_wronskian = sub(mul(derivative(La), Lb), mul(La, derivative(Lb)))
    assert pair_wronskian == scale(W, a_tag - b_tag)
    assert gcd(Phi, pair_wronskian) == K
    results.append({"subgroup_index": index, "ramification_degree": len(R) - 1,
                    "ramification_domain_gcd_degree": 0,
                    "wronskian_domain_gcd_degree": len(K) - 1,
                    "quotient_curve_a": a_curve, "quotient_curve_b": b_curve})

receipt = {
    "PASS": True,
    "p": p, "ell": ell, "subgroups_checked": len(results),
    "differential_identities_checked": len(results),
    "domain_gcd_identities_checked": 3 * len(results),
    "pair_wronskian_sign_checks": len(results),
    "ramification_domain_roots": 0,
    "wronskian_domain_roots": "Exactly the subgroup kernel; independent of the tag pair",
    "scope": "Identity replay on the saved fixture; no shifted-derivative or locator search",
    "results": results,
    "sha256": {
        "fixture.json": hashlib.sha256(fixture_path.read_bytes()).hexdigest(),
        Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    },
    "seconds": time.perf_counter() - started,
}
(base / "isogeny_wronskian_verified.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps({key: value for key, value in receipt.items() if key != "results"}, indent=2))
