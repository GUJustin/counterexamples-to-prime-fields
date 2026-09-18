#!/usr/bin/env python3
"""Two disjoint K4,4 collision-bank mechanism check, not an onset.

Uses only the Python standard library. Primality is proved by trial division
by every prime through isqrt(p); all subsequent checks use exact integers.
"""
import hashlib
import json
import math
from collections import Counter, defaultdict
from itertools import combinations_with_replacement
from pathlib import Path
from random import Random
from time import monotonic

HERE = Path(__file__).resolve().parent
H = 1500
P = 10125000000029
SEED = 2026091832
COMPONENT_SIZE = 4


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
    t = COMPONENT_SIZE
    assert len(prime_class) >= 4*t
    numerator_primes = prime_class[:t] + prime_class[2*t:3*t]
    denominator_primes = prime_class[t:2*t] + prime_class[3*t:4*t]
    assert not set(numerator_primes) & set(denominator_primes)
    reference_prime = prime_class[0]
    coherent_roots = {}
    for ell in numerator_primes + denominator_primes:
        ratio = ell * pow(reference_prime, -1, P) % P
        assert pow(ratio, (P-1)//4, P) == 1
        root = square_root(ratio)
        assert pow(root, (P-1)//2, P) == 1
        coherent_roots[ell] = root
    edges = [(i, j) for i in range(2*t) for j in range(2*t) if i//t == j//t]
    assert len(edges) == 2*t*t == 32

    banks = []
    for edge_id, (i, j) in enumerate(edges):
        a, b = numerator_primes[i], denominator_primes[j]
        ratio = a * pow(b, -1, P) % P
        assert pow(ratio, (P - 1) // 4, P) == 1
        alpha, beta = coherent_roots[a], coherent_roots[b]
        theta = alpha * pow(beta, -1, P) % P
        assert theta * theta % P == ratio
        assert pow(theta, (P - 1) // 2, P) == 1
        banks.append({"id": edge_id, "component": i//t,
                      "numerator_index": i, "denominator_index": j,
                      "alpha": alpha, "beta": beta,
                      "a": a, "b": b, "theta": theta,
                      "theta_inverse": pow(theta, -1, P)})
    L = len(banks)
    A = 2 * (L - 1) - (t-1)**2
    assert A == 3*t*t+2*t-3
    assert L == 32 and A == 53
    assert len({bank["theta"] for bank in banks}) == L
    products = defaultdict(list)
    for i, j in combinations_with_replacement(range(L), 2):
        product = banks[i]["theta"] * banks[j]["theta"] % P
        products[product].append([i,j])
    assert max(map(len, products.values())) == 2
    for representations in products.values():
        if any(i == j for i,j in representations):
            assert len(representations) == 1
        if len(representations) == 2:
            flat = [banks[i] for pair in representations for i in pair]
            assert len({bank["component"] for bank in flat}) == 1
            assert len({bank["numerator_index"] for bank in flat}) == 2
            assert len({bank["denominator_index"] for bank in flat}) == 2
            assert len({bank["id"] for bank in flat}) == 4

    core, core_squares = [], set()
    distinct_pair_groups = {square:pairs for square,pairs in products.items()
                            if all(i != j for i,j in pairs)}
    lost_coordinates = Counter()
    for square, pairs in sorted(distinct_pair_groups.items()):
        core_squares.add(square)
        root = square_root(square)
        if len(pairs) == 1:
            assignments = [(root,pairs[0]), (P-root,pairs[0])]
        else:
            assert len(pairs) == 2
            pairs.sort()
            assignments = [(root,pairs[0]), (P-root,pairs[1])]
            lost_coordinates.update(i for pair in pairs for i in pair)
            sums = [sum(banks[i]["theta"] for i in pair)%P for pair in pairs]
            assert sums[0] != sums[1]
        for x, (i,j) in assignments:
            value = (banks[i]["theta"] + banks[j]["theta"]) % P
            assert polynomial(banks[i], x) == polynomial(banks[j], x) == value
            core.append({"x": x, "f": value, "g": 0, "owners": [i, j]})
    assert len(core) == L*A//2 == t*t*A == 848
    assert len({entry["x"] for entry in core}) == 848
    assert set(lost_coordinates.values()) == {(t-1)**2} == {9}
    multiplicities = Counter(map(len,distinct_pair_groups.values()))
    assert multiplicities == {1:352, 2:72}
    core_hits = Counter()
    for entry in core:
        owners = [b["id"] for b in banks if polynomial(b, entry["x"]) == entry["f"]]
        assert owners == entry["owners"]
        core_hits.update(owners)
    assert set(core_hits.values()) == {A}

    M = L // 8
    assert M == 4
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
    assert n == 1459 and T * T < 2 * n
    # Low-rate DKT bound: n*a1(3/n) <= sqrt(3n/2)+(3n/8)^(1/4).
    # These strict rational bounds put it below 47+5=52<A=53.
    assert 3*n < 2*47**2 and 3*n < 8*5**4
    assert 47+5 < A
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
    assert nonbank_bound == 43 < A < T
    assert direction_nonzero_bound == 10 < A
    assert neutral_core_nonbank_bound == 35 < A
    exceptional_zero_agreement = sum((entry["f"] + exceptional_label*entry["g"])%P == 0
                                     for entry in domain)
    assert exceptional_zero_agreement == len(grid) == 8 < A
    assert cross_pairs == 0

    fixture = {
        "p": P, "H": H, "seed": SEED, "translation_trial": trial,
        "u0": u0, "v0": v0, "c0": c0, "endpoint_labels": endpoints,
        "exceptional_label": exceptional_label,
        "component_size": t, "reference_prime": reference_prime,
        "numerator_primes": numerator_primes, "denominator_primes": denominator_primes,
        "banks": banks, "raw_intervals": raw_intervals,
        "core": core, "grid": grid, "neutral": neutral,
        "singleton_threshold_labels": near_labels,
    }
    encoded = (json.dumps(fixture, indent=2) + "\n").encode()
    (HERE / "fixture.json").write_bytes(encoded)
    receipt = {
        "status": "PASS: exact two-K4,4 collision-bank mechanism check",
        "scope": "Toy d=1 override; p is not in the theorem's asymptotic field window. No constant-fraction, onset, or target-benchmark claim.",
        "p": P, "H": H,
        "primality": {"method": "trial division by every prime through isqrt(p)",
                      "trial_prime_count": len(all_small_primes), "isqrt_p": math.isqrt(P)},
        "quartic_class_sizes": {str(key): len(value) for key, value in sorted(classes.items())},
        "chosen_quartic_class": class_value,
        "L": L, "component_size": t, "two_biclique_edges": len(edges),
        "distinct_unordered_products_including_repetitions": len(products),
        "distinct_pair_product_multiplicities": dict(multiplicities),
        "lost_core_coordinates_per_bank": dict(Counter(lost_coordinates.values())),
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
        "exceptional_zero_polynomial_agreement": exceptional_zero_agreement,
        "complete_line_profile": {"labels_at_exact_agreement_54":len(near_labels),
                                  "all_other_labels_exact_agreement":A,
                                  "relaxed_threshold_53_list_size_everywhere":L},
        "nonzero_direction_bound": direction_nonzero_bound,
        "zero_direction_nonbank_bound": neutral_core_nonbank_bound,
        "exact_endpoint_agreements": [A, A], "exact_common_agreement": A,
        "johnson_integer_check": {"T_squared": T * T, "two_n": 2 * n},
        "first_order_integer_upper_bound": {"sqrt_term_less_than":47,
                                            "fourth_root_term_less_than":5,
                                            "curve_agreement_less_than":52,
                                            "source_agreement":A},
        "fixture_sha256": hashlib.sha256(encoded).hexdigest(),
        "elapsed_seconds": monotonic() - started,
    }
    (HERE / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
