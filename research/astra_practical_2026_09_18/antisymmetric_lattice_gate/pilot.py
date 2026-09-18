"""Bounded 127-dimensional ternary modular-relation pilot.

Run under the repository's owned-process watchdog (60 s / 512 MiB).
The construction and all reported relations are checked with exact integers.
LLL/BKZ is only a discovery step and is never treated as a counting proof.
"""

import hashlib
import json
import math
from pathlib import Path
import time

from flint import fmpz_mat, fmpz_poly

D = Path(__file__).parent
p = 2130706433
zeta = pow(3, (p - 1) // 256, p)
indices = list(range(1, 128))
moments = (1, 3, 5)
started = time.monotonic()
assert pow(zeta, 256, p) == 1 and pow(zeta, 128, p) == p - 1


def dump(name, obj):
    (D / name).write_text(json.dumps(obj, indent=2) + "\n")


def inv3(A):
    R = [row[:] + [int(i == j) for j in range(3)] for i, row in enumerate(A)]
    det = 1
    for k in range(3):
        t = next(i for i in range(k, 3) if R[i][k] % p)
        if t != k:
            R[k], R[t] = R[t], R[k]
            det = -det
        pivot = R[k][k] % p
        det = det * pivot % p
        inv = pow(pivot, -1, p)
        R[k] = [x * inv % p for x in R[k]]
        for i in range(3):
            if i != k:
                s = R[i][k]
                R[i] = [(x - s * y) % p for x, y in zip(R[i], R[k])]
    inverse = [row[3:] for row in R]
    assert all(sum(A[i][k] * inverse[k][j] for k in range(3)) % p == (i == j)
               for i in range(3) for j in range(3))
    return inverse, det % p


columns = [[pow(zeta, k * j, p) for k in moments] for j in indices]
pivot = [[columns[j][i] for j in range(3)] for i in range(3)]
inverse, pivot_det = inv3(pivot)
basis = []
for j in range(127):
    row = [0] * 127
    if j < 3:
        row[j] = p
    else:
        row[j] = 1
        for i in range(3):
            v = -sum(inverse[i][k] * columns[j][k] for k in range(3)) % p
            row[i] = v - p if v > p // 2 else v
    assert all(sum(row[j] * columns[j][k] for j in range(127)) % p == 0 for k in range(3))
    basis.append(row)
matrix = fmpz_mat(basis)
determinant = int(matrix.det())
assert determinant == p ** 3
dump("basis.json", dict(p=p, zeta=zeta, indices=indices, moments=moments,
                        pivot_indices=[1, 2, 3], pivot_matrix=pivot,
                        pivot_determinant_mod_p=pivot_det, pivot_inverse_mod_p=inverse,
                        determinant=str(determinant), basis=basis))


def check_vector(row):
    assert len(row) == 127
    assert all(sum(row[j] * columns[j][k] for j in range(127)) % p == 0 for k in range(3))
    return max(abs(x) for x in row) <= 1 and any(row) and sum(row) % 2 == 0


def canonical(row):
    first = next(x for x in row if x)
    return tuple(row if first > 0 else [-x for x in row])


def inspect(rows, stage):
    found = {}
    counts = dict(ternary_basis_even=0, ternary_basis_odd=0,
                  ternary_pair_even=0, pair_combinations_checked=0)
    for i, row in enumerate(rows):
        assert all(sum(row[j] * columns[j][k] for j in range(127)) % p == 0 for k in range(3))
        if max(abs(x) for x in row) <= 1 and any(row):
            if sum(row) % 2:
                counts["ternary_basis_odd"] += 1
            else:
                counts["ternary_basis_even"] += 1
                found[canonical(row)] = dict(stage=stage, kind="basis", rows=[i], signs=[1])
    for i in range(len(rows)):
        for j in range(i):
            for sign in (-1, 1):
                counts["pair_combinations_checked"] += 1
                row = [x + sign * y for x, y in zip(rows[i], rows[j])]
                if max(abs(x) for x in row) <= 1 and any(row) and sum(row) % 2 == 0:
                    counts["ternary_pair_even"] += 1
                    found.setdefault(canonical(row), dict(stage=stage, kind="pair", rows=[i, j], signs=[1, sign]))
    ordered = sorted(found, key=lambda v: (sum(x != 0 for x in v), v))
    summary = dict(stage=stage, seconds=time.monotonic() - started,
                   min_squared_norm=min(sum(x * x for x in row) for row in rows),
                   min_infinity_norm=min(max(abs(x) for x in row) for row in rows),
                   distinct_sign_classes=len(found), **counts)
    if ordered:
        summary["smallest_support"] = sum(x != 0 for x in ordered[0])
    dump(stage + "_basis.json", rows)
    dump(stage + "_summary.json", summary)
    print(json.dumps(summary), flush=True)
    return [(list(v), found[v]) for v in ordered[:16]], summary


lll_started = time.monotonic()
reduced = matrix.lll(delta=0.99, eta=0.51)
rows = [[int(reduced[i, j]) for j in range(127)] for i in range(127)]
assert abs(int(reduced.det())) == determinant
relations, lll_summary = inspect(rows, "lll")
stages = [lll_summary]

# A fixed, bounded BKZ ladder is permitted only while no ternary vector exists.
if not relations and time.monotonic() - started < 15:
    from fpylll import BKZ, IntegerMatrix
    B = IntegerMatrix.from_matrix(rows)
    for block_size, loops, seconds in [(20, 2, 10), (40, 4, 25), (50, 1, 15)]:
        if relations or time.monotonic() - started >= 45:
            break
        if block_size == 50 and stages[-1]["min_squared_norm"] >= 41:
            break  # no further work if BKZ40 showed no reduction
        seconds = min(seconds, max(1, int(48 - (time.monotonic() - started))))
        params = BKZ.Param(block_size=block_size, max_loops=loops, max_time=seconds,
                           flags=BKZ.MAX_LOOPS | BKZ.MAX_TIME)
        BKZ.reduction(B, params)
        rows = [[int(B[i, j]) for j in range(127)] for i in range(127)]
        assert abs(int(fmpz_mat(rows).det())) == determinant
        relations, bkz_summary = inspect(rows, "bkz" + str(block_size))
        stages.append(bkz_summary)


verified = []
for row, provenance in relations:
    assert check_vector(row)
    A, B = [], []
    for j, v in zip(indices, row):
        if v == 1:
            A.append(j)
            B.append(j + 128)
        elif v == -1:
            A.append(j + 128)
            B.append(j)
    A.sort()
    B.sort()
    assert A and len(A) == len(B) and len(A) % 2 == 0
    assert not (set(A) & set(B)) and 0 not in A + B and 128 not in A + B
    assert sorted((a + 128) % 256 for a in A) == B
    residues = [(sum(pow(zeta, k * a, p) for a in A) -
                 sum(pow(zeta, k * b, p) for b in B)) % p for k in range(1, 7)]
    product_a = math.prod(pow(zeta, a, p) for a in A) % p
    product_b = math.prod(pow(zeta, b, p) for b in B) % p
    assert residues == [0] * 6 and product_a == product_b
    assert (sum(A) - sum(B)) % 256 == 0
    assert any(((j in A) != ((j + 64) % 256 in A)) for j in range(256))
    coeffs = [0] + row
    relation = fmpz_poly(coeffs)
    phi = fmpz_poly([1] + [0] * 127 + [1])
    norm = int(relation.resultant(phi))
    assert norm != 0
    vp, rest = 0, abs(norm)
    while rest % p == 0:
        rest //= p
        vp += 1
    assert vp >= 3
    verified.append(dict(provenance=provenance, d=row, support=len(A),
                         sum_d=sum(row), A_exponents=A, B_exponents=B,
                         six_moment_differences=residues,
                         product_exponent_difference=(sum(A) - sum(B)) % 256,
                         product_a=product_a, product_b=product_b,
                         cyclotomic_norm=str(norm), prime_valuation=vp,
                         genuinely_cross_partial_pattern=True))

result = dict(p=p, zeta=zeta, root_order=256, coordinate_indices=indices,
              lattice_rank=127, lattice_determinant=str(determinant),
              parity_in_basis=False, parity_checked_on_candidates=True,
              stages=stages, verified_relations=verified,
              seconds=time.monotonic() - started,
              status="relation_found" if verified else "bounded_pilot_no_ternary_relation",
              scope="modular exchange building blocks only; no fiber amplification count")
dump("result.json", result)
dump("sha256.json", {name: hashlib.sha256((D / name).read_bytes()).hexdigest()
                     for name in ["basis.json", "result.json", "pilot.py"]})
print(json.dumps({"status": result["status"], "verified": len(verified),
                  "support": verified[0]["support"] if verified else None,
                  "seconds": result["seconds"]}), flush=True)
