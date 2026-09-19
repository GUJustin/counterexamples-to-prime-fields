#!/usr/bin/env python3
"""One fixed pair; exact CRT intersection test using only Python integers.

No curve search, direct syndrome matrix, or other verifier is imported.
Polynomial coefficients are ascending. Run from any directory.
"""
from pathlib import Path
import hashlib
import json
import time

BASE = Path(__file__).resolve().parent
fixture_path = BASE / "fixture.json"
fixture = json.loads(fixture_path.read_text())
p = fixture["p"]


def trim(a):
    a = [x % p for x in a]
    while a and a[-1] == 0:
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


def divmod_poly(a, b):
    assert b
    a = trim(a)
    q = [0] * max(0, len(a) - len(b) + 1)
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b):
        shift = len(a) - len(b)
        coefficient = a[-1] * inv % p
        q[shift] = coefficient
        for j, v in enumerate(b):
            a[shift + j] = (a[shift + j] - coefficient * v) % p
        a = trim(a)
    return trim(q), a


def mod(a, modulus):
    return divmod_poly(a, modulus)[1]


def exact_div(a, b):
    q, r = divmod_poly(a, b)
    assert not r
    return q


def invmod(a, modulus):
    r0, r1 = modulus, mod(a, modulus)
    t0, t1 = [], [1]
    while r1:
        q, r2 = divmod_poly(r0, r1)
        r0, r1 = r1, r2
        t0, t1 = t1, sub(t0, mul(q, t1))
    assert len(r0) == 1 and r0[0]
    result = mod(scale(t0, pow(r0[0], -1, p)), modulus)
    assert mod(mul(a, result), modulus) == [1]
    return result


def power(a, exponent):
    result = [1]
    while exponent:
        if exponent & 1:
            result = mul(result, a)
        a = mul(a, a)
        exponent //= 2
    return result


def product(polynomials):
    result = [1]
    for a in polynomials:
        result = mul(result, a)
    return result


def coeff(a, i):
    return a[i] if i < len(a) else 0


def rank(matrix):
    a = [row[:] for row in matrix]
    row = 0
    pivots = []
    for col in range(len(a[0])):
        pivot = next((j for j in range(row, len(a)) if a[j][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        a[row] = [(x * pow(a[row][col], -1, p)) % p for x in a[row]]
        for j in range(row + 1, len(a)):
            if a[j][col]:
                factor = a[j][col]
                a[j] = [(x - factor * y) % p for x, y in zip(a[j], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return row, pivots


started = time.perf_counter()
ell, n, k = fixture["ell"], fixture["n"], fixture["k"]
t = (ell - 1) // 2
Z = [7, 231, 340, 411, 470]
d = len(Z)
indices = [1, 2]
assert ell == 23 and p == 1657 and n == 264 and k == 173
assert d < t and ell > 2 * d
domain = fixture["domain"]
assert len(domain) == len(set(domain)) == n and set(Z) <= set(domain)
Phi = product([[-x, 1] for x in domain])
J = product([[-x, 1] for x in Z])
groups = [fixture["subgroups"][i] for i in indices]
K = [trim(g["K"]) for g in groups]
N = [trim(g["N"]) for g in groups]
for side in range(2):
    assert len(K[side]) - 1 == t and len(N[side]) - 1 == ell
    assert not (set(Z) & set(groups[side]["kernel_x"]))
    assert K[side] == product([[-x, 1] for x in groups[side]["kernel_x"]])
    assert power(K[side], 2) == groups[side]["B"]
    tags = [a["tag"] for a in groups[side]["fibers"]]
    assert len(tags) == len(set(tags)) == t
    factors = [sub(N[side], scale(power(K[side], 2), a)) for a in tags]
    assert mul(K[side], product(factors)) == Phi

F = exact_div(Phi, product([J, K[0], K[1]]))
K5 = [power(a, 5) for a in K]
K6 = [power(a, 6) for a in K]
modulus = mul(K6[0], K6[1])
invF = [invmod(F, m) for m in K6]
crt_inverse = invmod(K6[0], K6[1])
qcap = 2 * ell + 2 * d - 3
degree_top = n + ell - 2 + d
assert len(modulus) - 1 == 132 and qcap == 53 and degree_top == 290


def crt(a, b):
    result = add(a, mul(K6[0], mod(mul(sub(b, a), crt_inverse), K6[1])))
    assert len(result) < len(modulus)
    assert mod(result, K6[0]) == a
    assert mod(result, K6[1]) == b
    return result


# Independently evaluate the local expansion from the first two tag sums.
local_shortcut = []
for side in range(2):
    m = K6[side]
    other = 1 - side
    ni = invmod(N[side], m)
    u = mod(mul(power(K[side], 2), ni), m)
    u2 = mod(mul(u, u), m)
    assert not mod(mul(u2, u), m)
    tags = [a["tag"] for a in groups[side]["fibers"]]
    sigma1 = sum(tags) % p
    sigma2 = sum(tags[i] * tags[j] for i in range(t) for j in range(i)) % p
    leading = mod(product([J, K6[other], ni]), m)
    pieces = [
        u2,
        add(u, scale(u2, sigma1)),
        add(add([1], scale(u, sigma1)), scale(u2, sigma1 * sigma1 - sigma2)),
    ]
    local_shortcut.append([mod(mul(leading, a), m) for a in pieces])

columns = []
shortcut_checks = 0
for side in range(2):
    for i in range(3):
        numerator = product([power(N[side], t - 3 + i), power(K[side], 4 - 2 * i)])
        for j in range(d + 1):
            A = [0] * j + numerator
            cross = mul(A, K5[1 - side])
            if side == 1:
                cross = scale(cross, -1)
            residue = mod(mul(cross, invF[side]), K6[side])
            shortcut = mod([0] * j + local_shortcut[side][i], K6[side])
            if side == 1:
                shortcut = scale(shortcut, -1)
            assert residue == shortcut
            shortcut_checks += 1
            Q = crt(residue, []) if side == 0 else crt([], residue)
            cutoff = [coeff(Q, z) for z in range(qcap + 1, len(modulus) - 1)]
            # The cutoff equations make replacing Q by this truncation exact.
            residual = sub(cross, mul(F, Q[:qcap + 1]))
            infinity = [coeff(residual, degree_top - j0) for j0 in range(3)]
            columns.append(cutoff + infinity)

matrix = [list(row) for row in zip(*columns)]
assert len(matrix) == 81 and len(matrix[0]) == 36
matrix_rank, pivots = rank(matrix)
assert matrix_rank == 36
matrix_serialized = json.dumps(matrix, separators=(",", ":")).encode()
receipt = {
    "PASS": True,
    "method": "Independent polynomial CRT conditions; no direct syndrome matrix imported",
    "p": p, "ell": ell, "n": n, "k": k, "d": d,
    "subgroup_indices": indices, "fixed_extra_set": Z,
    "crt_modulus_degree": len(modulus) - 1,
    "cofactor_degree_cap": qcap,
    "cofactor_cutoff_equations": len(matrix) - 3,
    "infinity_equations": 3,
    "matrix_rows": len(matrix), "matrix_columns": len(matrix[0]),
    "rank": matrix_rank, "intersection_dimension": len(matrix[0]) - matrix_rank,
    "pivot_columns": pivots,
    "local_factorization_shortcut_checks": shortcut_checks,
    "domain_factorizations_rechecked": 2,
    "kernel_values": "Encoded by congruences modulo the sixth powers of both kernel locators",
    "scope": "This fixed extra set and subgroup pair only; no varying-set or growing-family conclusion",
    "sha256": {
        "fixture.json": hashlib.sha256(fixture_path.read_bytes()).hexdigest(),
        Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "matrix_json_compact": hashlib.sha256(matrix_serialized).hexdigest(),
    },
    "seconds": time.perf_counter() - started,
}
(BASE / "fixed_extra_crt_pair_1_2.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
