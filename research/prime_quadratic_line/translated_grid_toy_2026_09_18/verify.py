#!/usr/bin/env python3
"""Deterministic translated-grid mechanism check, not an asymptotic onset.

Uses only the Python standard library. Primality is proved by trial division
by every prime through isqrt(p); all subsequent checks use exact integers.
"""
import hashlib
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from pathlib import Path
from random import Random
from time import monotonic

HERE = Path(__file__).resolve().parent
H = 1500
P = 10125000000029
SEED = 2026091827


def prime_sieve(limit):
    mask = bytearray(b"\x01") * (limit + 1)
    mask[0:2] = b"\x00\x00"
    for k in range(2, math.isqrt(limit) + 1):
        if mask[k]:
            start = k * k
            mask[start::k] = b"\x00" * (((limit - start) // k) + 1)
    return [i for i, flag in enumerate(mask) if flag]


def square_root(a, p=P):
    """Tonelli--Shanks, returning the smaller of the two roots."""
    a %= p
    if not a:
        return 0
    assert pow(a, (p - 1) // 2, p) == 1
    if p % 4 == 3:
        r = pow(a, (p + 1) // 4, p)
        return min(r, p - r)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c = s, pow(z, q, p)
    t, r = pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, probe = 0, t
        while probe != 1:
            probe = probe * probe % p
            i += 1
        assert i < m
        b = pow(c, 1 << (m - i - 1), p)
        r = r * b % p
        c = b * b % p
        t = t * c % p
        m = i
    assert r * r % p == a
    return min(r, p - r)


def polynomial(bank, x):
    return (bank["theta"] + x * x * bank["theta_inverse"]) % P


def integer_fiber_check():
    """A separate integer grid with d=2 and exactly one-quarter retention."""
    h, a, b, m = 6, 3, 5, 1024
    d = m // (64 * h)
    assert d == 2
    full = [0] * (m * (a + b) + 1)
    kept = [0] * len(full)
    for u in range(1, m + 1):
        for v in range(1, m + 1):
            k = a * u + b * v
            full[k] += 1
            if (u + v) % 4 == 0:
                kept[k] += 1

    # Independent Diophantine interval count: v=(k-3u)/5, u=2k mod5.
    inverse_a_mod_b = pow(a, -1, b)
    for k, observed in enumerate(full):
        lo = max(1, -((-(k - b * m)) // a))
        hi = min(m, (k - b) // a)
        residue = k * inverse_a_mod_b % b
        first = lo + (residue - lo) % b
        expected = 0 if first > hi else 1 + (hi - first) // b
        assert observed == expected

    x = sum(kept)
    k_exact = (m - 1) * (a + b) + 1
    k_bound = 3 * h * m
    dmax = max(full)
    rich = sum(c >= d for c in kept)
    light_points = sum(c for c in kept if c < d)
    assert x == m * m // 4
    assert k_exact <= k_bound
    assert dmax <= Fraction(1) + Fraction(2 * m, h)
    assert dmax <= Fraction(3 * m, h)
    assert light_points <= k_bound * (d - 1)
    assert rich >= Fraction(h * m, 16)
    assert rich * Fraction(3 * m, h) >= x - k_bound * (d - 1)
    return {
        "scope": "integer-fiber counting only; no finite-field bank or onset claim",
        "H": h, "a": a, "b": b, "M": m, "d": d,
        "retention_rule": "(u+v) mod4 = 0",
        "retained_points": x,
        "integer_interval_size": k_exact,
        "interval_bound_3HM": k_bound,
        "maximum_full_fiber": dmax,
        "maximum_retained_fiber": max(kept),
        "light_points": light_points,
        "rich_labels": rich,
        "required_rich_lower_bound_HM_over_16": h * m // 16,
        "independent_diophantine_counts_checked": len(full),
    }


def main():
    started = monotonic()
    assert P % 4 == 1 and 2 * H**4 < P < 4 * H**4
    all_small_primes = prime_sieve(math.isqrt(P))
    assert all(P % ell for ell in all_small_primes)
    candidates = [ell for ell in all_small_primes if H // 2 <= ell <= H]
    classes = defaultdict(list)
    for ell in candidates:
        classes[pow(ell, (P - 1) // 4, P)].append(ell)
    class_value, prime_class = max(classes.items(), key=lambda kv: (len(kv[1]), -kv[0]))
    assert len(prime_class) >= 18
    numerator_primes, denominator_primes = prime_class[:9], prime_class[9:18]
    assert not set(numerator_primes) & set(denominator_primes)

    points = [(x, y) for x in range(3) for y in range(3)]
    lines = [(s, t) for s in range(3) for t in range(3)]
    edges = [(i, j) for i, (x, y) in enumerate(points)
             for j, (s, t) in enumerate(lines) if (y - s * x - t) % 3 == 0]
    assert len(edges) == 27
    neighbors = [{j for i0, j in edges if i0 == i} for i in range(9)]
    assert all(len(neighbors[i] & neighbors[j]) <= 1 for i, j in combinations(range(9), 2))

    banks = []
    for edge_id, (i, j) in enumerate(edges):
        a, b = numerator_primes[i], denominator_primes[j]
        ratio = a * pow(b, -1, P) % P
        assert pow(ratio, (P - 1) // 4, P) == 1
        theta = square_root(ratio)
        assert theta * theta % P == ratio
        assert pow(theta, (P - 1) // 2, P) == 1
        banks.append({"id": edge_id, "point": points[i], "line": lines[j],
                      "a": a, "b": b, "theta": theta,
                      "theta_inverse": pow(theta, -1, P)})
    L = len(banks)
    A = 2 * (L - 1)
    assert L == 27 and A == 52
    products = {}
    for i, j in combinations_with_replacement(range(L), 2):
        product = banks[i]["theta"] * banks[j]["theta"] % P
        assert product not in products
        products[product] = [i, j]

    core, core_squares = [], set()
    for i, j in combinations(range(L), 2):
        square = banks[i]["theta"] * banks[j]["theta"] % P
        core_squares.add(square)
        root = square_root(square)
        for x in (root, P - root):
            value = (banks[i]["theta"] + banks[j]["theta"]) % P
            assert polynomial(banks[i], x) == polynomial(banks[j], x) == value
            core.append({"x": x, "f": value, "g": 0, "owners": [i, j]})
    assert len(core) == L * (L - 1) == 702
    assert len({entry["x"] for entry in core}) == 702
    core_hits = Counter()
    for entry in core:
        owners = [b["id"] for b in banks if polynomial(b, entry["x"]) == entry["f"]]
        assert owners == entry["owners"]
        core_hits.update(owners)
    assert set(core_hits.values()) == {A}

    M = L // 4
    assert M == 6
    rng = Random(SEED)
    for trial in range(24):
        u0, v0 = rng.randrange(P), rng.randrange(P)
        grid, seen_slopes = [], set()
        deletions = Counter()
        for u in range(1, M + 1):
            for v in range(1, M + 1):
                U, V = (u0 + u) % P, (v0 + v) % P
                if not U or not V:
                    deletions["zero_U_or_V"] += 1
                    continue
                ratio = V * pow(U, -1, P) % P
                if pow(ratio, (P - 1) // 2, P) != 1:
                    deletions["nonsquare"] += 1
                    continue
                if ratio in seen_slopes:
                    deletions["repeated_square_slope"] += 1
                    continue
                seen_slopes.add(ratio)
                if ratio in core_squares:
                    deletions["core_square_slope"] += 1
                    continue
                grid.append({"u": u, "v": v, "U": U, "V": V,
                             "square": ratio, "x": square_root(ratio),
                             "g": pow(U, -1, P)})
        if len(grid) >= M * M / 4:
            break
    else:
        raise AssertionError("bounded translation pilot found no retained grid")

    raw_owners = {}
    raw_intervals = []
    cross_pairs = 0
    for bank in banks:
        a, b, theta = bank["a"], bank["b"], bank["theta"]
        offset = (theta * u0 + v0 * bank["theta_inverse"]) % P
        scale = pow(b * theta % P, -1, P)
        low, high = a + b, M * (a + b)
        assert high - low + 1 <= 3 * H * M < P
        raw_intervals.append({"bank": bank["id"], "offset": offset,
                              "scale": scale, "low": low, "high": high})
        for integer in range(low, high + 1):
            raw_label = (offset + integer * scale) % P
            previous = raw_owners.get(raw_label, 0)
            assert not (previous >> bank["id"]) & 1
            cross_pairs += previous.bit_count()
            raw_owners[raw_label] = previous | (1 << bank["id"])

    c0 = 1
    while c0 in raw_owners:
        c0 += 1
    assert c0 != 0
    for entry in grid:
        entry["f"] = c0 * entry["g"] % P
    exceptional_label = -c0 % P
    endpoints = []
    candidate = 0
    while len(endpoints) < 2:
        if (candidate + c0) % P not in raw_owners and candidate != exceptional_label:
            endpoints.append(candidate)
        candidate += 1

    # d=1 is a deliberate toy override, not the asymptotic formula's value.
    d = 1
    asymptotic_d = M // (64 * H)
    assert asymptotic_d == 0
    T = A + d
    n = T * T // 2 + 1
    assert n == 1405 and T * T < 2 * n
    used = {entry["x"] for entry in core + grid}
    assert len(used) == len(core) + len(grid)
    neutral, skipped_neutral_bank_roots = [], 0
    x = 1
    while len(core) + len(grid) + len(neutral) < n:
        if x not in used:
            value = pow(x, 3, P)
            if all(polynomial(bank, x) != value for bank in banks):
                neutral.append({"x": x, "f": value, "g": 0})
                used.add(x)
            else:
                skipped_neutral_bank_roots += 1
        x += 1
    domain = core + grid + neutral
    assert len(domain) == len(used) == n and 0 not in used

    grid_hits = []
    all_bank_affine_checks = 0
    for bank, interval in zip(banks, raw_intervals):
        hits = Counter()
        for entry in grid:
            native = (entry["U"] * polynomial(bank, entry["x"]) - c0) % P
            integer = bank["a"] * entry["u"] + bank["b"] * entry["v"]
            formula = (interval["offset"] + interval["scale"] * integer - c0) % P
            assert native == formula
            assert (raw_owners[(native + c0) % P] >> bank["id"]) & 1
            assert (entry["f"] + native * entry["g"]) % P == polynomial(bank, entry["x"])
            hits[native] += 1
            all_bank_affine_checks += 1
        grid_hits.append(hits)
        # Exhaustive bank agreement classification at every coordinate.
        fixed_hits = sum(polynomial(bank, entry["x"]) == entry["f"]
                         for entry in core + neutral)
        assert fixed_hits == A
        for label in endpoints:
            exact = sum(polynomial(bank, entry["x"]) ==
                        (entry["f"] + label * entry["g"]) % P for entry in domain)
            assert exact == A

    near_labels = []
    for bank, hits in zip(banks, grid_hits):
        for label, hit_count in sorted(hits.items()):
            if hit_count < d or label == exceptional_label:
                continue
            if raw_owners[(label + c0) % P].bit_count() != 1:
                continue
            threshold_owners = [j for j, other_hits in enumerate(grid_hits)
                                if A + other_hits[label] >= T]
            assert threshold_owners == [bank["id"]]
            near_labels.append({"label": label, "bank": bank["id"],
                                "exact_bank_agreement": A + hit_count})
    assert len({entry["label"] for entry in near_labels}) == len(near_labels)
    assert near_labels
    nonbank_bound = L + 2 * M + 3
    direction_nonzero_bound = 2 * M + 2
    neutral_core_nonbank_bound = L + 3
    assert nonbank_bound == 42 < A < T
    assert direction_nonzero_bound == 14 < A
    assert neutral_core_nonbank_bound == 30 < A

    integer_receipt = integer_fiber_check()
    fixture = {
        "p": P, "H": H, "seed": SEED, "translation_trial": trial,
        "u0": u0, "v0": v0, "c0": c0, "endpoint_labels": endpoints,
        "exceptional_label": exceptional_label,
        "numerator_primes": numerator_primes, "denominator_primes": denominator_primes,
        "banks": banks, "raw_intervals": raw_intervals,
        "core": core, "grid": grid, "neutral": neutral,
        "singleton_threshold_labels": near_labels,
    }
    encoded = (json.dumps(fixture, indent=2) + "\n").encode()
    (HERE / "fixture.json").write_bytes(encoded)
    receipt = {
        "status": "PASS: exact translated-grid mechanism check",
        "scope": "Toy d=1 override; not a finite asymptotic onset or a target-benchmark certificate.",
        "p": P, "H": H,
        "primality": {"method": "trial division by every prime through isqrt(p)",
                      "trial_prime_count": len(all_small_primes), "isqrt_p": math.isqrt(P)},
        "quartic_class_sizes": {str(key): len(value) for key, value in sorted(classes.items())},
        "chosen_quartic_class": class_value,
        "L": L, "C4_free_graph_edges": len(edges),
        "distinct_unordered_products_including_repetitions": len(products),
        "core_nodes": len(core), "core_matches_per_bank": A,
        "M": M, "grid_retained": len(grid), "grid_deletions": dict(deletions),
        "grid_affine_identities_checked": all_bank_affine_checks,
        "full_raw_interval_pairs": sum(t["high"] - t["low"] + 1 for t in raw_intervals),
        "raw_label_union_size": len(raw_owners), "raw_cross_bank_collision_pairs": cross_pairs,
        "c0": c0, "endpoint_labels": endpoints, "exceptional_label": exceptional_label,
        "toy_d": d, "asymptotic_formula_d": asymptotic_d,
        "threshold": T, "domain_size": n, "code_dimension": 3,
        "neutral_nodes": len(neutral), "neutral_bank_roots_skipped": skipped_neutral_bank_roots,
        "singleton_threshold_label_count": len(near_labels),
        "bank_agreement_histogram_at_counted_labels": dict(Counter(t["exact_bank_agreement"] for t in near_labels)),
        "nonbank_bound_away_from_exception": nonbank_bound,
        "nonzero_direction_bound": direction_nonzero_bound,
        "zero_direction_nonbank_bound": neutral_core_nonbank_bound,
        "exact_endpoint_agreements": [A, A], "exact_common_agreement": A,
        "johnson_integer_check": {"T_squared": T * T, "two_n": 2 * n},
        "integer_fiber_toy": integer_receipt,
        "fixture_sha256": hashlib.sha256(encoded).hexdigest(),
        "elapsed_seconds": monotonic() - started,
    }
    (HERE / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
