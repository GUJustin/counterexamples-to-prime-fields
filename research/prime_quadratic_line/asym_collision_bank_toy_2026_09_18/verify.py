#!/usr/bin/env python3
"""Exact asymmetric collision-bank toy; no asymptotic-onset assertion.

Only the Python standard library is used. Run with Python 3.10 or later.
The generated fixture records every bank and every domain coordinate.
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
P = 10125000000029
H, K = 600, 1500
RICH_SIZE, FILLER_SIZE = 2, 4
SEED = 2026091834


def prime_sieve(limit):
    mask = bytearray(b"\x01") * (limit + 1)
    mask[0:2] = b"\x00\x00"
    for k in range(2, math.isqrt(limit) + 1):
        if mask[k]:
            start = k * k
            mask[start::k] = b"\x00" * ((limit - start) // k + 1)
    return [i for i, flag in enumerate(mask) if flag]


def square_root(a):
    """Tonelli--Shanks, with the smaller root chosen canonically."""
    a %= P
    if not a:
        return 0
    assert pow(a, (P - 1) // 2, P) == 1
    q, exponent = P - 1, 0
    while q % 2 == 0:
        q //= 2
        exponent += 1
    z = 2
    while pow(z, (P - 1) // 2, P) != P - 1:
        z += 1
    m, c = exponent, pow(z, q, P)
    t, root = pow(a, q, P), pow(a, (q + 1) // 2, P)
    while t != 1:
        i, probe = 0, t
        while probe != 1:
            probe = probe * probe % P
            i += 1
        assert i < m
        b = pow(c, 1 << (m - i - 1), P)
        root = root * b % P
        c = b * b % P
        t = t * c % P
        m = i
    assert root * root % P == a
    return min(root, P - root)


def polynomial(bank, x):
    return (bank["theta"] + x * x * bank["theta_inverse"]) % P


def main():
    started = monotonic()
    assert H < K // 2 and P % 4 == 1 and K**4 < P
    trial_primes = prime_sieve(math.isqrt(P))
    assert all(P % ell for ell in trial_primes)
    banks, components = [], []
    used_vertex_primes = set()
    for component_id, (width, size) in enumerate(((H, RICH_SIZE), (K, FILLER_SIZE))):
        candidates = [ell for ell in trial_primes if width // 2 <= ell <= width]
        classes = defaultdict(list)
        for ell in candidates:
            classes[pow(ell, (P - 1) // 4, P)].append(ell)
        class_value, prime_class = max(classes.items(), key=lambda item: (len(item[1]), -item[0]))
        assert len(prime_class) >= 2 * size
        numerators, denominators = prime_class[:size], prime_class[size:2 * size]
        vertices = numerators + denominators
        assert not used_vertex_primes.intersection(vertices)
        used_vertex_primes.update(vertices)
        reference = vertices[0]
        roots = {}
        for ell in vertices:
            ratio = ell * pow(reference, -1, P) % P
            assert pow(ratio, (P - 1) // 4, P) == 1
            roots[ell] = square_root(ratio)
            assert pow(roots[ell], (P - 1) // 2, P) == 1
        for i, a in enumerate(numerators):
            for j, b in enumerate(denominators):
                theta = roots[a] * pow(roots[b], -1, P) % P
                assert theta * theta % P == a * pow(b, -1, P) % P
                assert pow(theta, (P - 1) // 2, P) == 1
                banks.append({"id": len(banks), "component": component_id,
                              "numerator_index": i, "denominator_index": j,
                              "a": a, "b": b, "alpha": roots[a], "beta": roots[b],
                              "theta": theta, "theta_inverse": pow(theta, -1, P)})
        components.append({"id": component_id, "width": width, "size": size,
                           "candidate_prime_count": len(candidates),
                           "quartic_class_sizes": {str(k): len(v) for k, v in sorted(classes.items())},
                           "chosen_quartic_class": class_value, "reference_prime": reference,
                           "numerator_primes": numerators, "denominator_primes": denominators})

    t, s = RICH_SIZE, FILLER_SIZE
    R, L = t * t, len(banks)
    assert R == 4 and L == t * t + s * s == 20
    assert len({bank["theta"] for bank in banks}) == L
    A = 2 * (L - 1) - (t - 1)**2
    A_filler = 2 * (L - 1) - (s - 1)**2
    assert A == 37 and A_filler == 29
    products = defaultdict(list)
    for i, j in combinations_with_replacement(range(L), 2):
        products[banks[i]["theta"] * banks[j]["theta"] % P].append([i, j])
    assert max(map(len, products.values())) == 2
    for pairs in products.values():
        if any(i == j for i, j in pairs):
            assert len(pairs) == 1
        if len(pairs) == 2:
            flat = [banks[i] for pair in pairs for i in pair]
            assert len({bank["component"] for bank in flat}) == 1
            assert len({bank["numerator_index"] for bank in flat}) == 2
            assert len({bank["denominator_index"] for bank in flat}) == 2
            assert len({bank["id"] for bank in flat}) == 4

    core, core_squares, lost = [], set(), Counter()
    pair_groups = {square: pairs for square, pairs in products.items()
                   if all(i != j for i, j in pairs)}
    for square, pairs in sorted(pair_groups.items()):
        core_squares.add(square)
        root = square_root(square)
        pairs.sort()
        if len(pairs) == 1:
            assignments = [(root, pairs[0]), (P - root, pairs[0])]
        else:
            assignments = [(root, pairs[0]), (P - root, pairs[1])]
            lost.update(i for pair in pairs for i in pair)
            sums = [sum(banks[i]["theta"] for i in pair) % P for pair in pairs]
            assert sums[0] != sums[1]
        for x, owners in assignments:
            value = sum(banks[i]["theta"] for i in owners) % P
            actual = [bank["id"] for bank in banks if polynomial(bank, x) == value]
            assert actual == owners
            core.append({"x": x, "f": value, "g": 0, "owners": owners})
    assert len(core) == (R * A + s * s * A_filler) // 2 == 306
    assert len({entry["x"] for entry in core}) == len(core)
    core_hits = [sum(polynomial(bank, entry["x"]) == entry["f"] for entry in core)
                 for bank in banks]
    for bank, hits in zip(banks, core_hits):
        size = t if bank["component"] == 0 else s
        assert lost[bank["id"]] == (size - 1)**2
        assert hits == (A if bank["component"] == 0 else A_filler)
    multiplicities = Counter(map(len, pair_groups.values()))
    assert multiplicities == {1: 116, 2: 37}

    M = L // 8
    assert M == 2
    rng = Random(SEED)
    for trial in range(24):
        u0, v0 = rng.randrange(P), rng.randrange(P)
        grid, seen_slopes, deletions = [], set(), Counter()
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
                             "square": ratio, "x": square_root(ratio), "g": pow(U, -1, P)})
        if 4 * len(grid) >= M * M:
            break
    else:
        raise AssertionError("bounded translation pilot found no retained grid")

    intervals, raw_owners, cross_pairs = [], {}, 0
    for bank in banks:
        offset = (bank["theta"] * u0 + v0 * bank["theta_inverse"]) % P
        scale = pow(bank["b"] * bank["theta"] % P, -1, P)
        low, high = bank["a"] + bank["b"], M * (bank["a"] + bank["b"])
        width = H if bank["component"] == 0 else K
        assert high - low + 1 <= 3 * width * M < P
        interval = {"bank": bank["id"], "offset": offset, "scale": scale,
                    "low": low, "high": high, "screened": bank["component"] == 0}
        intervals.append(interval)
        if not interval["screened"]:
            continue
        for integer in range(low, high + 1):
            raw_label = (offset + integer * scale) % P
            previous = raw_owners.get(raw_label, 0)
            assert not (previous >> bank["id"]) & 1
            cross_pairs += previous.bit_count()
            raw_owners[raw_label] = previous | (1 << bank["id"])
    assert cross_pairs == 0
    c0 = 1
    while c0 in raw_owners:
        c0 += 1
    for entry in grid:
        entry["f"] = c0 * entry["g"] % P
    exceptional_label = -c0 % P
    endpoints, candidate = [], 0
    while len(endpoints) < 2:
        if (candidate + c0) % P not in raw_owners and candidate != exceptional_label:
            endpoints.append(candidate)
        candidate += 1
    assert endpoints == [0, 1]

    d = 1  # Explicit toy override: the asymptotic formula gives zero.
    assert M // (64 * H) == 0
    T, n = A + d, (A + d)**2 // 2 + 1
    assert T == 38 and n == 723 and T * T < 2 * n
    # Strict rational majorants for the two terms in the low-rate a_1 bound.
    assert 3 * n * 50**2 < 2 * 1647**2
    assert 3 * n * 50**4 < 8 * 203**4
    assert 1647 + 203 == 50 * A
    used = {entry["x"] for entry in core + grid}
    assert len(used) == len(core) + len(grid)
    neutral, skipped, x = [], 0, 1
    while len(core) + len(grid) + len(neutral) < n:
        if x not in used:
            value = pow(x, 3, P)
            if all(polynomial(bank, x) != value for bank in banks):
                neutral.append({"x": x, "f": value, "g": 0})
                used.add(x)
            else:
                skipped += 1
        x += 1
    domain = core + grid + neutral
    assert len(domain) == len(used) == n and 0 not in used

    grid_hits, native_checks, endpoint_bank_profiles = [], 0, []
    for bank, interval, expected_fixed in zip(banks, intervals, core_hits):
        hits = Counter()
        for entry in grid:
            native = (entry["U"] * polynomial(bank, entry["x"]) - c0) % P
            integer = bank["a"] * entry["u"] + bank["b"] * entry["v"]
            formula = (interval["offset"] + interval["scale"] * integer - c0) % P
            assert native == formula
            assert polynomial(bank, entry["x"]) == (entry["f"] + native * entry["g"]) % P
            if bank["component"] == 0:
                assert (raw_owners[(native + c0) % P] >> bank["id"]) & 1
            hits[native] += 1
            native_checks += 1
        grid_hits.append(hits)
        assert max(hits.values()) == 1
        fixed = sum(polynomial(bank, entry["x"]) == entry["f"] for entry in core + neutral)
        assert fixed == expected_fixed
        endpoint_profile = []
        for label in endpoints:
            exact = sum(polynomial(bank, entry["x"]) == (entry["f"] + label * entry["g"]) % P
                        for entry in domain)
            assert exact == expected_fixed + hits[label]
            assert exact == A if bank["component"] == 0 else exact < A
            endpoint_profile.append(exact)
        endpoint_bank_profiles.append(endpoint_profile)
    filler_maximum = max(core_hits[i] + max(grid_hits[i].values()) for i in range(R, L))
    assert filler_maximum == A_filler + 1 == 30 < A

    near_labels = []
    for i in range(R):
        for label, count in sorted(grid_hits[i].items()):
            assert label != exceptional_label and label not in endpoints
            assert raw_owners[(label + c0) % P].bit_count() == 1
            owners = [j for j in range(L) if core_hits[j] + grid_hits[j][label] >= T]
            assert owners == [i]
            near_labels.append({"label": label, "bank": i, "exact_bank_agreement": A + count})
    assert len({entry["label"] for entry in near_labels}) == len(near_labels) == R * len(grid)
    nonbank_bound, direction_bound, zero_direction_bound = L + 2 * M + 3, 2 * M + 2, L + 3
    assert nonbank_bound == 27 < A < T
    assert direction_bound == 6 < A and zero_direction_bound == 23 < A
    exceptional_zero_agreement = sum((entry["f"] + exceptional_label * entry["g"]) % P == 0
                                     for entry in domain)
    assert exceptional_zero_agreement == len(grid) < A

    fixture = {"p": P, "H": H, "K": K, "seed": SEED, "translation_trial": trial,
               "u0": u0, "v0": v0, "c0": c0, "endpoint_labels": endpoints,
               "exceptional_label": exceptional_label, "components": components,
               "banks": banks, "raw_intervals": intervals, "core": core, "grid": grid,
               "neutral": neutral, "singleton_threshold_labels": near_labels}
    encoded = (json.dumps(fixture, indent=2) + "\n").encode()
    (HERE / "fixture.json").write_bytes(encoded)
    receipt = {
        "status": "PASS: exact asymmetric K2,2 plus K4,4 collision-bank mechanism check",
        "scope": "Toy d=1 override. H,K,t,s and p do not certify the asymptotic parameter prescription, field window, onset, or constant exceptional fraction.",
        "p": P, "H": H, "K": K,
        "primality": {"method": "trial division by every prime through isqrt(p)",
                      "trial_prime_count": len(trial_primes), "isqrt_p": math.isqrt(P)},
        "components": components, "rich_bank_count": R, "filler_bank_count": L - R,
        "bank_count": L, "distinct_unordered_products_including_repetitions": len(products),
        "distinct_pair_product_multiplicities": dict(multiplicities),
        "core_nodes": len(core), "core_agreement_histogram": dict(Counter(core_hits)),
        "lost_core_coordinates_histogram": dict(Counter(lost.values())),
        "M": M, "grid_retained": len(grid), "grid_deletions": dict(deletions),
        "grid_affine_identities_checked": native_checks,
        "screened_rich_raw_interval_pairs": sum(v["high"] - v["low"] + 1 for v in intervals if v["screened"]),
        "rich_raw_label_union_size": len(raw_owners), "rich_raw_cross_bank_collision_pairs": cross_pairs,
        "c0": c0, "endpoint_labels": endpoints, "endpoint_bank_profiles": endpoint_bank_profiles,
        "exceptional_label": exceptional_label, "exceptional_zero_polynomial_agreement": exceptional_zero_agreement,
        "toy_d": d, "asymptotic_formula_d": M // (64 * H), "domain_size": n,
        "code_dimension": 3, "threshold": T, "neutral_nodes": len(neutral),
        "neutral_bank_roots_skipped": skipped, "maximum_filler_agreement_any_label": filler_maximum,
        "singleton_threshold_label_count": len(near_labels),
        "complete_line_profile": {"labels_at_exact_agreement_38": len(near_labels),
                                  "all_other_labels_exact_agreement": A,
                                  "relaxed_threshold_37_list_size_everywhere": R},
        "nonbank_bound_away_from_zero_exception": nonbank_bound,
        "nonzero_direction_bound": direction_bound, "zero_direction_nonbank_bound": zero_direction_bound,
        "exact_endpoint_agreements": [A, A], "exact_common_agreement": A,
        "johnson_integer_check": {"T_squared": T * T, "two_n": 2 * n},
        "first_order_integer_upper_bound": {"sqrt_term_less_than": "1647/50",
                                            "fourth_root_term_less_than": "203/50",
                                            "curve_agreement_less_than": A,
                                            "source_agreement": A},
        "fixture_sha256": hashlib.sha256(encoded).hexdigest(), "elapsed_seconds": monotonic() - started}
    (HERE / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
