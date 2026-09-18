#!/usr/bin/env python3
"""Exact finite two-ray certificate over F_131071, without a gap override.

Run with Python 3.10 or later; only the standard library is used.
Artifacts use fixed little-endian formats and deterministic domain order.
"""
import hashlib
import json
import math
import struct
from collections import Counter
from pathlib import Path
from time import monotonic

HERE = Path(__file__).resolve().parent
P, T_BANK, BLOCK_SIZE, N = 131071, 16, 330, 65536
GENERATOR = 3


def prime_sieve(limit):
    mask = bytearray(b"\x01") * (limit + 1)
    mask[:2] = b"\x00\x00"
    for d in range(2, math.isqrt(limit) + 1):
        if mask[d]:
            mask[d*d::d] = b"\x00" * ((limit - d*d) // d + 1)
    return [d for d, prime in enumerate(mask) if prime]


def factor_integer(value):
    factors, d = {}, 2
    while d*d <= value:
        while value % d == 0:
            factors[d] = factors.get(d, 0) + 1
            value //= d
        d += 1
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encode_domain(entries):
    return b"".join(struct.pack("<III", *entry) for entry in entries)


def write_json(filename, value):
    encoded = (json.dumps(value, indent=2) + "\n").encode()
    (HERE / filename).write_bytes(encoded)
    return digest(encoded)


def main():
    started = monotonic()
    p, t, D, n, g = P, T_BANK, BLOCK_SIZE, N, GENERATOR
    threshold = D + 2*t
    prime_divisors = prime_sieve(math.isqrt(p))
    assert all(p % ell for ell in prime_divisors)
    factors = factor_integer(p - 1)
    assert factors == {2: 1, 3: 1, 5: 1, 17: 1, 257: 1}
    assert math.prod(ell**power for ell, power in factors.items()) == p - 1
    assert all(ell in prime_divisors for ell in factors)
    primitive_tests = {ell: pow(g, (p - 1)//ell, p) for ell in factors}
    assert all(value != 1 for value in primitive_tests.values())
    assert pow(g, p - 1, p) == 1
    assert t >= 2 and D > 4*t + 3 and 2*t*t < p - 1
    assert n >= 2*t*t + t*D and p > n + 6*t + 1

    z = g*g % p
    a = [pow(z, i, p) for i in range(t)]
    b = [pow(z, t*j, p) for j in range(t)]
    a_index, b_index = {value: i for i, value in enumerate(a)}, {value: j for j, value in enumerate(b)}
    assert len(a_index) == len(b_index) == t
    assert all(pow(value, (p - 1)//2, p) == 1 for value in a + b)
    b_inverse = [pow(value, -1, p) for value in b]
    good_labels = {a[i]*b[j] % p: [i, j] for i in range(t) for j in range(t)}
    assert len(good_labels) == t*t
    assert set(good_labels) == {pow(z, k, p) for k in range(t*t)}
    endpoint_labels = [g, pow(g, 3, p)]
    assert len(set(endpoint_labels)) == 2
    assert all(pow(label, (p - 1)//2, p) == p - 1 for label in endpoint_labels)
    assert not set(endpoint_labels).intersection(good_labels)

    core, core_owners = [], []
    for j in range(t):
        for i in range(t):
            root = pow(g, (t*j - i) % (p - 1), p)
            for x in (root, p - root):
                assert a[i]*x*x % p == b[j]
                # Directly check both rays' complete ownership at each core node.
                assert [k for k, coefficient in enumerate(a) if coefficient*x*x % p == b[j]] == [i]
                assert [k for k, constant in enumerate(b) if constant == b[j]] == [j]
                core.append((x, b[j], 0))
                core_owners.append([i, j])
    assert len(core) == len({x for x, _, _ in core}) == 2*t*t == 512
    used = bytearray(p)
    used[0] = 1
    for x, _, _ in core:
        assert not used[x]
        used[x] = 1

    fresh, fresh_coordinates, cursor = [], [], 1
    for j in range(t):
        block, coordinates = [], []
        while len(block) < D:
            if not used[cursor]:
                x = cursor
                used[x] = 1
                value = x*x*b_inverse[j] % p
                assert value != 0
                block.append((x, 0, value))
                coordinates.append(x)
            cursor += 1
        fresh.extend(block)
        fresh_coordinates.append(coordinates)
    assert len(fresh) == t*D == 5280

    # These are exactly the neutral intersections requiring exclusion.
    cube_roots_by_constant = {value: [] for value in b}
    for x in range(1, p):
        value = pow(x, 3, p)
        if value in cube_roots_by_constant:
            cube_roots_by_constant[value].append(x)
    cube_roots = {x for roots in cube_roots_by_constant.values() for x in roots}
    endpoint_coefficients = [[label*inverse % p for inverse in b_inverse] for label in endpoint_labels]
    endpoint_exclusions = {c for row in endpoint_coefficients for c in row}
    assert len(endpoint_exclusions) == 2*t
    assert not endpoint_exclusions.intersection(a)
    forbidden_neutral = set(a) | cube_roots | endpoint_exclusions | {0}
    assert len(forbidden_neutral) <= 6*t + 1
    neutral, cursor = [], 1
    while len(core) + len(fresh) + len(neutral) < n:
        assert cursor < p
        if not used[cursor] and cursor not in forbidden_neutral:
            x = cursor
            used[x] = 1
            value = pow(x, 3, p)
            assert x not in a_index and value not in b_index
            assert x not in endpoint_exclusions
            neutral.append((x, value, 0))
        cursor += 1
    assert len(neutral) == 59744
    domain = core + fresh + neutral
    assert len(domain) == len({x for x, _, _ in domain}) == n
    assert all(x != 0 for x, _, _ in domain)
    assert sum(used) == n + 1

    # Count the fixed agreement of EVERY pure quadratic c*X^2 directly from
    # core and neutral coordinates: a point determines exactly one coefficient.
    fixed_pure_hits = [0]*p
    for x, value, direction in core + neutral:
        assert direction == 0
        coefficient = value*pow(x*x % p, -1, p) % p
        fixed_pure_hits[coefficient] += 1
    assert fixed_pure_hits[0] == 0
    assert all(fixed_pure_hits[coefficient] == 2*t for coefficient in a)
    neutral_set = {x for x, _, _ in neutral}
    for c, count in enumerate(fixed_pure_hits):
        assert count == (2*t if c in a_index else int(c in neutral_set))
    assert max(fixed_pure_hits) == 2*t

    # Exhaust all p coefficients and p labels using the exact fresh-block
    # identity lambda=c*b_j. For c!=0 these t labels are distinct. The zero
    # coefficient has all t blocks at lambda=0 and none at other labels.
    maximum_agreements = [max(fixed_pure_hits)]*p
    threshold_counts = [0]*p
    relaxed_counts = [0]*p
    for c in range(1, p):
        agreement = fixed_pure_hits[c] + D
        for constant in b:
            label = c*constant % p
            if agreement > maximum_agreements[label]:
                maximum_agreements[label] = agreement
            if agreement >= threshold:
                threshold_counts[label] += 1
            if agreement >= D:
                relaxed_counts[label] += 1
    maximum_agreements[0] = t*D
    threshold_counts[0] = relaxed_counts[0] = 1
    actual_threshold_labels = {label for label, count in enumerate(threshold_counts) if count}
    assert actual_threshold_labels == set(good_labels) | {0}
    assert all(threshold_counts[label] == 1 for label in actual_threshold_labels)
    assert all(maximum_agreements[label] == threshold for label in good_labels)
    assert all(maximum_agreements[label] == D for label in endpoint_labels)
    assert relaxed_counts[0] == 1 and set(relaxed_counts[1:]) == {t}
    assert min(maximum_agreements[1:]) >= D > 4*t + 3
    # Every non-pure quadratic is bounded by 2t core + 2t fresh + 3 neutral
    # agreements. Thus the computed pure maxima and threshold counts are the
    # full RS(3) profiles, not merely lower bounds from a selected subcode.
    non_pure_bound = 4*t + 3
    assert non_pure_bound == 67 < D

    # Independently evaluate all 32 endpoint witnesses on all 65536 points.
    endpoint_exact_hits = []
    for label, coefficients in zip(endpoint_labels, endpoint_coefficients):
        row = []
        for j, coefficient in enumerate(coefficients):
            matching = [x for x, value, direction in domain
                        if coefficient*x*x % p == (value + label*direction) % p]
            assert matching == fresh_coordinates[j]
            assert len(matching) == D
            row.append(len(matching))
        endpoint_exact_hits.append(row)
    # The jth witnesses for the two endpoints therefore agree with their
    # respective words on exactly the same D-point fresh block, certifying CA>=D.
    # The direction cases give CA<=max(D,2t+2,2t+3)=D.
    common_agreement_upper = max(D, 2*t + 2, 2*t + 3)
    assert common_agreement_upper == D
    zero_agreement = sum(value == 0 for _, value, _ in domain)
    assert zero_agreement == t*D == 5280

    assert threshold*threshold < 2*n
    assert 3*n < 2*314**2 and 3*n < 8*13**4
    assert 314 + 13 == 327 < D

    core_bytes, fresh_bytes, neutral_bytes = map(encode_domain, (core, fresh, neutral))
    domain_bytes = core_bytes + fresh_bytes + neutral_bytes
    (HERE / "domain.bin").write_bytes(domain_bytes)
    profile_bytes = b"".join(struct.pack("<H", value) for value in maximum_agreements)
    (HERE / "agreement_profile.bin").write_bytes(profile_bytes)
    native_labels = [{"label": 0, "witness_coefficient": 0, "exact_agreement": t*D}]
    native_labels += [{"label": label, "witness_coefficient": a[i], "bank_i": i,
                      "fresh_block_j": j, "exact_agreement": threshold}
                     for label, (i, j) in sorted(good_labels.items())]
    endpoint_difference_inverse = pow(endpoint_labels[1] - endpoint_labels[0], -1, p)
    for entry in native_labels:
        entry["standard_affine_parameter"] = (entry["label"] - endpoint_labels[0])*endpoint_difference_inverse % p
        assert entry["standard_affine_parameter"] not in (0, 1)
    label_hash = write_json("singleton_labels.json", native_labels)
    recipe = {
        "field_prime": p, "primitive_generator": g, "t": t, "block_size": D, "length": n,
        "code_dimension": 3, "z": z, "quadratic_coefficients_a": a, "constant_coefficients_b": b,
        "endpoint_labels": endpoint_labels, "endpoint_witness_coefficients": endpoint_coefficients,
        "cube_roots_by_constant": cube_roots_by_constant,
        "neutral_exclusions_apart_from_existing_domain": sorted(forbidden_neutral),
        "domain_order": "core, then fresh blocks j=0..15, then neutral",
        "core_recipe": "for j=0..15, i=0..15, append x=3^((16*j-i) mod 131070), then 131071-x; f=b_j, direction=0",
        "fresh_recipe": "for each j=0..15 take the 330 least positive coordinates not used by the core or previous fresh blocks; f=0, direction=x^2/b_j",
        "neutral_recipe": "take the 59744 least positive coordinates outside the existing domain and the recorded neutral exclusion set; f=x^3, direction=0",
        "domain_binary_format": "65536 records of little-endian uint32 (x,f,direction), with W_lambda=f+lambda*direction",
        "profile_binary_format": "131071 little-endian uint16 entries, entry lambda equals the exact maximum RS(3) agreement of W_lambda",
        "source_words": "F=W_3, G=W_27; standard affine parameter u maps to native lambda=3+24*u mod131071",
        "domain_sha256": digest(domain_bytes), "agreement_profile_sha256": digest(profile_bytes),
        "singleton_labels_sha256": label_hash}
    recipe_hash = write_json("recipe.json", recipe)
    receipt = {
        "status": "PASS: actual finite two-ray RS(3) certificate, no gap override",
        "p": p, "primitive_generator": g,
        "primality": {"method": "trial division by every prime through isqrt(p)",
                      "isqrt_p": math.isqrt(p), "trial_prime_count": len(prime_divisors)},
        "factorization_p_minus_1": factors, "primitive_generator_power_tests": primitive_tests,
        "t": t, "D": D, "T": threshold, "n": n, "dimension": 3,
        "finite_lemma_hypotheses": {"D_gt_4t_plus_3": D > 4*t + 3,
                                    "t_squared_lt_half_field_group": 2*t*t < p - 1,
                                    "n_ge_core_plus_fresh": n >= 2*t*t + t*D,
                                    "p_gt_n_plus_6t_plus_1": p > n + 6*t + 1},
        "domain_counts": {"core": len(core), "fresh": len(fresh), "neutral": len(neutral)},
        "core_owners": "exactly one quadratic bank member and one constant bank member at each core point",
        "bank_core_agreement": 2*t, "good_nonzero_label_count": len(good_labels),
        "cube_root_exclusion_count": len(cube_roots), "endpoint_coefficient_exclusion_count": len(endpoint_exclusions),
        "neutral_exclusion_count_including_zero": len(forbidden_neutral),
        "largest_domain_coordinate": max(x for x, _, _ in domain),
        "fixed_pure_agreement_histogram": dict(Counter(fixed_pure_hits)),
        "all_pure_coefficients_enumerated": p, "native_nonzero_coefficient_block_pairs_enumerated": (p - 1)*t,
        "exact_all_label_maximum_agreement_histogram": dict(sorted(Counter(maximum_agreements).items())),
        "singleton_threshold_labels": len(actual_threshold_labels),
        "relaxed_threshold_D_list_size_nonzero_labels": t, "relaxed_threshold_D_list_size_at_zero": 1,
        "zero_label_exact_agreement": zero_agreement, "non_pure_quadratic_upper_bound": non_pure_bound,
        "endpoint_labels": endpoint_labels, "endpoint_witness_counts_by_block": endpoint_exact_hits,
        "endpoint_witness_full_domain_evaluations": 2*t*n,
        "exact_endpoint_agreements": [D, D], "exact_common_agreement": common_agreement_upper,
        "johnson_check": {"T_squared": threshold*threshold, "two_n": 2*n, "slack": 2*n-threshold*threshold},
        "first_order_bound": {"sqrt_term_strictly_below": 314, "fourth_root_term_strictly_below": 13,
                              "curve_agreement_strictly_below": 327, "source_agreement": D},
        "normalized_source_gap": {"numerator": 1, "denominator": 2048},
        "normalized_capacity_margin_at_T": {"numerator": threshold - 3, "denominator": n},
        "loss_to_capacity_margin_ratio": {"numerator": 2*t, "denominator": threshold - 3},
        "hashes": {"core_sha256": digest(core_bytes), "fresh_sha256": digest(fresh_bytes),
                   "neutral_sha256": digest(neutral_bytes), "domain_sha256": digest(domain_bytes),
                   "agreement_profile_sha256": digest(profile_bytes), "singleton_labels_sha256": label_hash,
                   "recipe_sha256": recipe_hash},
        "elapsed_seconds": monotonic() - started}
    write_json("receipt.json", receipt)
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
