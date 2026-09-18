"""Independent exact audit and finite orbit ledger for the lattice pilot."""

from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import time

from flint import fmpz_mat, fmpz_poly

D = Path(__file__).parent
start = time.monotonic()
b = json.loads((D / "basis.json").read_text())
r = json.loads((D / "rotated_result.json").read_text())
p = 2130706433
zeta = pow(3, (p - 1) // 256, p)
assert p == b["p"] == r["p"]
assert zeta == b["zeta"] == r["zeta"] == 392596362
assert pow(zeta, 256, p) == 1 and pow(zeta, 128, p) == p - 1
assert b["indices"] == list(range(1, 128))
A = [[pow(zeta, k * j, p) for j in range(1, 128)] for k in (1, 3, 5)]
P = [[row[j] for j in range(3)] for row in A]
detmod = sum(P[0][i] * (P[1][(i+1)%3] * P[2][(i+2)%3] -
                       P[1][(i+2)%3] * P[2][(i+1)%3]) for i in range(3)) % p
assert detmod != 0 and detmod == b["pivot_determinant_mod_p"]
basis = b["basis"]
assert len(basis) == 127 and all(len(row) == 127 for row in basis)
assert all(sum(row[j] * a[j] for j in range(127)) % p == 0 for row in basis for a in A)
assert abs(int(fmpz_mat(basis).det())) == p ** 3

stages = []
for stage in ("lll", "bkz20", "bkz40", "bkz50"):
    path = D / (stage + "_basis.json")
    if path.exists():
        rows = json.loads(path.read_text())
        assert abs(int(fmpz_mat(rows).det())) == p ** 3
        assert all(sum(row[j] * a[j] for j in range(127)) % p == 0 for row in rows for a in A)
        stages.append(json.loads((D / (stage + "_summary.json")).read_text()))

tables = [[pow(zeta, k * j, p) for j in range(256)] for k in range(1, 7)]
histogram = Counter()
orbits = defaultdict(set)
canon = set()
for rel in r["verified_relations"]:
    d = rel["d"]
    assert len(d) == 128 and d[0] == 0 and any(d) and max(map(abs, d)) <= 1
    assert sum(d) % 2 == 0
    expected_a = sorted([j for j, c in enumerate(d) if c == 1] +
                        [j + 128 for j, c in enumerate(d) if c == -1])
    expected_b = sorted([j for j, c in enumerate(d) if c == -1] +
                        [j + 128 for j, c in enumerate(d) if c == 1])
    aa, bb = rel["A_exponents"], rel["B_exponents"]
    assert aa == expected_a and bb == expected_b
    assert 0 not in aa + bb and 128 not in aa + bb
    assert not set(aa) & set(bb)
    assert all((sum(tab[j] for j in aa) - sum(tab[j] for j in bb)) % p == 0 for tab in tables)
    assert (sum(aa) - sum(bb)) % 256 == 0
    assert pow(zeta, sum(aa), p) == pow(zeta, sum(bb), p)
    assert all(not (j in aa and (j + 128) % 256 in aa) for j in range(256))
    t = len(aa)
    assert t == len(bb) == rel["support"] and t % 2 == 0
    histogram[t] += 1
    orbit = []
    for s in range(256):
        x = tuple(sorted((j+s) % 256 for j in aa))
        y = tuple(sorted((j+s) % 256 for j in bb))
        key = tuple(sorted((x, y)))
        orbit.append(key)
        if 0 not in x + y:
            orbits[t].add(key)
    canon.add(min(orbit))

best = min(r["verified_relations"], key=lambda v: (v["support"], v["d"]))
f = fmpz_poly(best["d"])
phi = fmpz_poly([1] + [0]*127 + [1])
norm = int(f.resultant(phi))
assert norm != 0
vp, rest = 0, abs(norm)
while rest % p == 0:
    vp += 1
    rest //= p
assert vp >= 3

N = math.comb(255, 136)
required = 274980728111395088
target_collision = N * (required - 1) + 1
contribution = 0
ledger = []
for t, pairs in sorted(orbits.items()):
    ordered = 2 * len(pairs)
    contexts = math.comb(255 - 2*t, 136 - t)
    term = ordered * contexts
    contribution += term
    ledger.append(dict(t=t, unordered_disjoint_exchanges=len(pairs),
                       ordered_disjoint_exchanges=ordered,
                       common_136_subset_contexts=str(contexts),
                       exact_off_diagonal_collision_contribution=str(term)))

initial_resources = json.loads((D / "resources.json").read_text())
refinement_resources = json.loads((D / "refinement_resources.json").read_text())
out = dict(p=p, zeta=zeta, lattice_rank=127, lattice_determinant=str(p**3),
           verified_lattice_stages=stages, verified_input_exchange_count=len(r["verified_relations"]),
           support_histogram=dict(histogram), rotation_and_swap_orbits=len(canon),
           smallest_exchange=best,
           smallest_exchange_cyclotomic_norm=str(norm), smallest_exchange_norm_prime_valuation=vp,
           orbit_collision_ledger=ledger, total_off_diagonal_contribution=str(contribution),
           fraction_of_second_moment_target_log2=math.log2(contribution)-math.log2(target_collision),
           two_reduction_runs_total_watchdog_seconds=initial_resources["seconds"]+refinement_resources["seconds"],
           largest_sampled_rss_kib=max(initial_resources["peak_rss_kib"],refinement_resources["peak_rss_kib"]),
           final_reduction_status=refinement_resources["reason"],
           bkz50_completed=(D / "bkz50_basis.json").exists(),
           audit_seconds=time.monotonic()-start,
           scope="verified modular cross-pattern exchanges only; no benchmark count improvement")
(D / "verified.json").write_text(json.dumps(out, indent=2) + "\n")
sha_files = ["basis.json", "lll_basis.json", "bkz20_basis.json", "bkz40_basis.json",
             "rotated_result.json", "verified.json", "pilot.py", "rotate_ternary.py", "verify.py",
             "resources.json", "refinement_resources.json"]
(D / "sha256.json").write_text(json.dumps({name:hashlib.sha256((D/name).read_bytes()).hexdigest()
                                           for name in sha_files}, indent=2) + "\n")
print(json.dumps({k:v for k,v in out.items() if k not in ("smallest_exchange", "verified_lattice_stages")},indent=2))
