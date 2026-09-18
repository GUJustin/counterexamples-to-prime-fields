#!/usr/bin/env python3
"""Exact arithmetic for the odd-fiber KKH r=2 quadratic enlargement.

This verifies a finite parameter-existence certificate. It does not construct
or enumerate its good tag set, pole, domain, or pair-label bank.
Uses only the Python standard library; all proof comparisons are integral.
"""

from fractions import Fraction
from hashlib import sha256
from math import comb, isqrt, prod
from pathlib import Path
import json


def integer_digest(value):
    blob = value.to_bytes((value.bit_length() + 7) // 8, "big")
    return {"bit_length": value.bit_length(), "sha256_big_endian": sha256(blob).hexdigest()}


def ratio(a, b):
    x = Fraction(a, b)
    return {"numerator": x.numerator, "denominator": x.denominator}


def main():
    p, m, s = 2147483647, 7161, 4680
    message_dimension = 3
    assert p % 2 == 1 and m > 1 and m % 2 == 1

    # Trial division, not a probable-prime test.
    trial_limit = isqrt(p)
    failed_divisors = [a for a in range(2, trial_limit + 1) if p % a == 0]
    assert not failed_divisors
    factorization = {2: 1, 3: 2, 7: 1, 11: 1, 31: 1, 151: 1, 331: 1}
    assert prod(ell ** power for ell, power in factorization.items()) == p - 1
    for ell in factorization:
        assert ell > 1 and all(ell % a for a in range(2, isqrt(ell) + 1))
    primitive_generator = 7
    generator_tests = {ell: pow(primitive_generator, (p - 1) // ell, p) for ell in factorization}
    assert all(value != 1 for value in generator_tests.values())

    assert (p - 1) % m == 0
    L = (p - 1) // m
    n = s * m
    assert 1 < s < m and s <= L and n < p
    d0, k = (m - 1) // 2, m - s
    assert 1 <= k <= min(s, d0)

    # Exact sampling-without-replacement union-bound criterion.
    union_numerator = L * comb(d0, k) * s ** k
    union_denominator = L ** k
    assert union_numerator < union_denominator
    safe_binary_slack = union_denominator.bit_length() - union_numerator.bit_length() - 1
    assert safe_binary_slack >= 0
    assert (union_numerator << safe_binary_slack) < union_denominator
    assert safe_binary_slack == 11692

    support_count = comb(s, 2)
    support_pair_count = comb(support_count, 2)
    allowed_poles = p - s
    collision_cap, collision_remainder = divmod(support_pair_count, allowed_poles)
    singleton_lower = support_count - 2 * collision_cap
    assert singleton_lower > 0
    assert support_count < p - 1  # A second far endpoint eta exists.
    assert 4 * singleton_lower > n

    A = m
    assert 8 * m % 7 == 0
    T = 8 * m // 7
    canonical_agreement = 2 * m
    assert A < T < canonical_agreement <= n
    johnson_slack = 2 * n - T * T
    assert johnson_slack > 0

    sqrt_upper, fourth_root_upper = 7091, 60
    first_sqrt_slack = 2 * sqrt_upper ** 2 - 3 * n
    first_fourth_slack = 8 * fourth_root_upper ** 4 - 3 * n
    assert first_sqrt_slack > 0 and first_fourth_slack > 0
    assert sqrt_upper + fourth_root_upper < A
    assert 64 * n < p < 65 * n
    assert 8 * (T - A) == T

    result = {
        "status": "PASS",
        "certificate_type": "finite parameter existence by exact counting; no tag or label enumeration",
        "construction": "KKH r=2 quotient with odd-fiber nonconstant-quadratic exclusion",
        "parameters": {
            "p": p, "m": m, "available_tags_L": L, "selected_tags_s": s,
            "length_n": n, "message_dimension": message_dimension,
            "source_agreement_A": A, "common_agreement_CA": A,
            "tested_threshold_T": T, "canonical_near_agreement": canonical_agreement,
        },
        "prime_certificate": {
            "method": "exhaustive trial division by every integer from 2 through floor(sqrt(p))",
            "trial_limit_inclusive": trial_limit,
            "trial_divisor_count": trial_limit - 1,
            "divisors_found": failed_divisors,
            "p_minus_1_factorization": factorization,
            "primitive_generator": primitive_generator,
            "generator_power_residues": generator_tests,
        },
        "tag_existence": {
            "C_m_size_upper_d0": d0,
            "forbidden_intersection_threshold_k": k,
            "permitted_intersection_maximum": k - 1,
            "union_numerator_formula": "L * binom(d0,k) * s^k",
            "union_denominator_formula": "L^k",
            "union_numerator": integer_digest(union_numerator),
            "union_denominator": integer_digest(union_denominator),
            "strict_union_bound_below_one": True,
            "strict_union_bound_below_two_to_minus": safe_binary_slack,
            "tag_set_enumerated": False,
        },
        "pole_averaging": {
            "canonical_support_count_N": support_count,
            "unordered_distinct_support_pairs": support_pair_count,
            "allowed_poles": allowed_poles,
            "collision_cap_floor": collision_cap,
            "division_remainder": collision_remainder,
            "singleton_label_lower_bound": singleton_lower,
            "singleton_fraction_of_n": ratio(singleton_lower, n),
            "singleton_lower_exceeds_n_over_4": True,
            "pole_enumerated": False,
        },
        "endpoint_choice": {
            "F": "W_0",
            "G": "W_eta, eta in F_p^* outside the canonical pair-label image",
            "existence_condition_N_less_than_p_minus_1": True,
            "standard_affine_native_label": "lambda=eta*u",
            "endpoint_enumerated": False,
        },
        "placement": {
            "first_order_bound_used": "n*a_1(3/n) <= sqrt(3n/2)+(3n/8)^(1/4)",
            "sqrt_term_strict_upper": sqrt_upper,
            "sqrt_term_integer_slack": first_sqrt_slack,
            "fourth_root_term_strict_upper": fourth_root_upper,
            "fourth_root_term_integer_slack": first_fourth_slack,
            "first_order_strict_upper": sqrt_upper + fourth_root_upper,
            "first_order_upper_less_than_A": True,
            "johnson_slack_2n_minus_T_squared": johnson_slack,
            "source_gap": T - A,
            "gap_over_tested_threshold": ratio(T - A, T),
            "gap_over_capacity_margin": ratio(T - A, T - message_dimension),
            "prime_over_length": ratio(p, n),
            "prime_strictly_between_64n_and_65n": True,
        },
        "limitations": [
            "Existence certificate, not an enumerated tag/pole/domain/label fixture.",
            "Singleton lower bound permits additional nonsingleton nearby labels.",
            "Canonical near agreement is 2m, not the tested threshold T.",
            "No infinite balanced-divisor prime family with p=Theta(n) is established.",
        ],
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
