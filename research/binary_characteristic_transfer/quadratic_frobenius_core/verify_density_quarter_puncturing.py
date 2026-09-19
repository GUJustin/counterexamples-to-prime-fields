#!/usr/bin/env python3
"""Exact onset arithmetic for the quarter-density Frobenius-block audit.

No finite-field domain or random puncturing is constructed. The general
classification and analytic monotonicity proof are in the accompanying note.
"""
from fractions import Fraction
from hashlib import sha256
from math import factorial, isqrt
from pathlib import Path
import json


def rational(x):
    x = Fraction(x)
    return {"numerator": x.numerator, "denominator": x.denominator}


def main():
    p = 257
    assert all(p % a for a in range(2, isqrt(p) + 1))
    population = 2 * (p * p - 1)
    sample = (p * p + 3) // 2
    assert 2 * sample == p * p + 3
    n = population + sample
    assert 2 * n == 5 * p * p - 1
    retained_target = (p + 3) // 4
    failure_maximum = retained_target - 1
    support_checks = []
    for k in (2 * p - 2, 2 * p):
        mean = Fraction(k * sample, population)
        assert mean > Fraction(k, 4)
        assert failure_maximum <= Fraction(p - 1, 4) <= Fraction(k, 8)
        assert mean - failure_maximum > Fraction(k, 8)
        exponent_lower = Fraction(2, k) * Fraction(k, 8) ** 2
        assert exponent_lower == Fraction(k, 32) >= Fraction(p - 1, 16)
        support_checks.append({
            "support_size": k, "mean": rational(mean),
            "mean_minus_failure_maximum": rational(mean - failure_maximum),
            "hoeffding_exponent_lower": rational(exponent_lower),
        })

    support_count = p * (p + 1)
    exp_exponent = (p - 1) // 16
    assert exp_exponent == 16
    exp_lower = Fraction(16 ** 6, factorial(6)) + Fraction(16 ** 7, factorial(7))
    assert support_count < exp_lower
    derivative_upper = Fraction(2, p) - Fraction(1, 16)
    assert derivative_upper < 0

    A = 2 * p
    T = isqrt(5 * p * p - 2)
    worst_retained = 2 * p - 2 + retained_target
    assert worst_retained >= T > A
    assert p * p - 144 * p + 80 > 0
    assert p + 4 <= A and 8 <= p + 4

    B = (p + 1) * (p * p - 1)
    q = p ** 4
    assert q - (1 + B) == p * (p - 1) ** 2 * (p + 1) > 1
    assert n < q
    assert Fraction(15, 4) < Fraction(31, 16) ** 2
    assert Fraction(15, 16) < 1
    assert p > 256
    assert Fraction(p * p, 256) > p  # sqrt(p) < p/16.
    assert T * T < 5 * p * p - 1 <= (T + 1) ** 2
    assert 2 * n - T * T > 0
    assert (2 * p + 1) ** 2 <= 5 * p * p - 2

    base = Path(__file__).parent
    source_hashes = {
        name: sha256((base / name).read_bytes()).hexdigest()
        for name in ("density_quarter_puncturing.tex", "scaled_fiber_padding.tex")
    }
    receipt = {
        "arithmetic_status": "PASS",
        "scope": "Exact finite-onset arithmetic; no puncturing/domain enumeration",
        "onset_prime": p,
        "prime_trial_division_limit": isqrt(p),
        "parameters": {
            "field_order_q": q, "extension_degree": 4,
            "first_block_size": population, "second_block_population": population,
            "retained_second_block_size": sample, "length_n": n,
            "message_dimension": 3, "source_and_common_agreement_A": A,
            "tested_threshold_T": T, "singleton_parameter_count_B": B,
            "additional_parameter_list_size": p + 1,
            "outside_plane_union_parameter_count": q - (1 + B),
        },
        "hypergeometric": {
            "retained_target": retained_target,
            "strict_failure_integer_maximum": failure_maximum,
            "support_checks": support_checks,
            "number_of_supports": support_count,
            "exponential_exponent_at_onset": exp_exponent,
            "exponential_strict_lower_bound": rational(exp_lower),
            "lower_bound_minus_support_count": rational(exp_lower - support_count),
            "union_probability_strict_upper": rational(Fraction(support_count, 1) / exp_lower),
            "log_union_derivative_strict_upper_at_onset": rational(derivative_upper),
            "monotonicity_extension": "For x>=257, derivative<2/x-1/16<=2/257-1/16<0",
        },
        "classification_bounds": {
            "singly_canonical_agreement_max": 2 * p,
            "doubly_noncanonical_agreement_max": p + 4,
            "doubly_canonical_retained_agreement_min": worst_retained,
            "retained_agreement_minus_T": worst_retained - T,
            "support_squared_johnson_slack_lower": rational(Fraction(p*p - 144*p + 80, 16)),
        },
        "placement": {
            "first_order_sqrt_coefficient_square_slack": rational(Fraction(31, 16) ** 2 - Fraction(15, 4)),
            "fourth_root_coefficient_fourth_power": rational(Fraction(15, 16)),
            "first_order_final_square_slack_p2_over_256_minus_p": rational(Fraction(p * p, 256) - p),
            "johnson_slack_2n_minus_T_squared": 2 * n - T * T,
            "gap_over_capacity_margin": rational(Fraction(T - A, T - 3)),
            "limiting_gap_ratio": "1 - 2/sqrt(5)",
            "johnson_distance_strictly_positive_and_at_most_one": T*T < 2*n <= (T+1)**2,
        },
        "audited_source_sha256": source_hashes,
        "limitations": [
            "Alphabet is F_(p^4), not a prime field.",
            "Length is asymptotic to (5/2)*p^2, not fixed at a practical short-domain benchmark.",
            "Exact threshold lists are certified; nearby agreements need not equal T.",
        ],
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
