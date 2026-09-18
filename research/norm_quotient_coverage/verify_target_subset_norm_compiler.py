#!/usr/bin/env python3
"""Exact pointwise-product and norm-compiler ledger; no field enumeration.

All inequalities are rational/integer comparisons.  Displayed dyadic
upper bounds are rounded upwards, and decimal values are never used
to accept a case.  The mixed Katz bound is a mathematical input.
"""

from fractions import Fraction
from math import comb, isqrt
from pathlib import Path
import json


P_PRIME = 2130706433
N = 262144
J = 131072
SQRT_CEILING = isqrt(P_PRIME) + 1


def ceil_fraction(x):
    return -((-x.numerator) // x.denominator)


def floor_fraction(x):
    return x.numerator // x.denominator


def dyadic_upper(x, bits=128):
    numerator = ceil_fraction(x * (1 << bits))
    assert x <= Fraction(numerator, 1 << bits)
    return {"numerator": numerator, "denominator_power_of_two": bits}


def polynomial_at(coefficients, x):
    """Integer homogeneous Horner evaluation, followed by one reduction."""
    numerator, denominator = x.numerator, x.denominator
    value = coefficients[-1]
    denominator_power = denominator
    for coefficient in reversed(coefficients[:-1]):
        value = value * numerator + coefficient * denominator_power
        denominator_power *= denominator
    return Fraction(value, denominator ** (len(coefficients) - 1))


def moment(auxiliary_degree, norm_degree, fiber_size):
    assert auxiliary_degree % norm_degree == 0
    assert (P_PRIME - 1) % fiber_size == 0
    assert N % fiber_size == J % fiber_size == 0
    native_degree = auxiliary_degree // norm_degree
    population = (P_PRIME - 1) // fiber_size - 1
    s = N // fiber_size - 1
    r = J // fiber_size + norm_degree
    w = fiber_size - 1
    assert norm_degree + 1 <= r <= s <= population
    assert J == w + (r - norm_degree - 1) * fiber_size + 1
    a = 1 - Fraction(comb(s, 2), population)
    epsilon = Fraction(auxiliary_degree * SQRT_CEILING + 1, population)
    assert a > 0 and 0 < epsilon <= 1
    group_order = P_PRIME ** auxiliary_degree - 1
    targets = P_PRIME ** native_degree - 1
    subset_count = comb(s, r)
    coefficients = [comb(r, u) * comb(s - r, u)
                    for u in range(min(r, s - r) + 1)]
    assert sum(coefficients) == subset_count
    first_sum = polynomial_at(coefficients, epsilon * epsilon)
    second_sum = epsilon ** r * polynomial_at(coefficients, epsilon)
    first = Fraction(group_order - 1, subset_count) * first_sum
    second = Fraction((group_order - 1) * (group_order - 2), subset_count) * second_sum
    missing_bound = (first + second) / a
    missing_count = min(targets, floor_fraction(targets * missing_bound))
    guaranteed_labels = targets - missing_count
    near = J + (norm_degree + 1) * fiber_size - 1
    common = J + fiber_size - 1
    direction_upper = J + norm_degree * fiber_size - 1
    row = {
        "auxiliary_degree": auxiliary_degree,
        "native_degree": native_degree,
        "relative_norm_degree": norm_degree,
        "m": fiber_size, "s": s, "r": r, "w": w,
        "population_size": population,
        "epsilon": {"numerator": epsilon.numerator, "denominator": epsilon.denominator},
        "distinctness_lower_bound": {"numerator": a.numerator, "denominator": a.denominator},
        "subset_count": subset_count,
        "auxiliary_group_order": group_order,
        "native_nonzero_labels": targets,
        "missing_fraction_upper_bound": dyadic_upper(missing_bound),
        "first_moment_contribution_upper_bound": dyadic_upper(first / a),
        "offdiagonal_contribution_upper_bound": dyadic_upper(second / a),
        "guaranteed_missing_labels_at_most": missing_count,
        "guaranteed_nearby_labels_at_least": guaranteed_labels,
        "all_native_labels_certified": targets * missing_bound < 1,
        "positive_label_fraction_certified": missing_bound < 1,
        "exact_polynomial_source_and_common_agreement": common,
        "rational_direction_agreement_upper_bound": direction_upper,
        "exact_nearby_agreement": near,
        "capacity_margin_numerator": near - J,
        "common_agreement_loss_numerator": near - common,
        "minimum_endpoint_loss_numerator": near - direction_upper,
        "meets_139782_agreement": near >= 139782,
    }
    return row, missing_bound


def next_fiber_obstruction(auxiliary_degree, largest_fiber):
    """For this particular moment criterion, not for all constructions."""
    next_fiber = 2 * largest_fiber
    s = N // next_fiber - 1
    largest_binomial = comb(s, s // 2)
    M = P_PRIME ** auxiliary_degree - 1
    assert largest_binomial < M - 1
    # V/a >= (M-1)/binom(s,r) > 1, because the u=0 term is one.
    return {
        "auxiliary_degree": auxiliary_degree,
        "largest_certified_fiber": largest_fiber,
        "next_fiber": next_fiber,
        "remaining_nonreserved_tags": s,
        "largest_subset_count": largest_binomial,
        "auxiliary_group_order_minus_one": M - 1,
        "reason": "V/a >= (M-1)/binom(s,r) > 1 for every r; larger fibers only reduce s",
        "scope": "failure of this pointwise second-moment sufficient criterion only",
    }


def main():
    assert (SQRT_CEILING - 1) ** 2 < P_PRIME < SQRT_CEILING ** 2
    assert P_PRIME == 127 * (1 << 24) + 1
    assert 127 < 1 << 24
    assert pow(3, (P_PRIME - 1) // 2, P_PRIME) == P_PRIME - 1
    norm_rows = []
    smaller_fiber_rows = []
    for e in (1, 2, 3, 6):
        row, bound = moment(6, e, 1024)
        assert 0 < bound < Fraction(1, 1 << 22)
        row["uniform_strict_missing_fraction_cap"] = "2^-22"
        norm_rows.append(row)
        small, small_bound = moment(6, e, 512)
        assert small["all_native_labels_certified"]
        smaller_fiber_rows.append(small)

    matched_rows = []
    matched_obstructions = []
    for native_degree, m in ((1, 4096), (2, 2048), (3, 2048), (6, 1024)):
        row, bound = moment(native_degree, 1, m)
        assert bound < 1
        matched_rows.append(row)
        matched_obstructions.append(next_fiber_obstruction(native_degree, m))

    # Pairwise finite comparisons use the same native alphabet and exact n,J.
    by_native = {row["native_degree"]: row for row in matched_rows}
    comparisons = []
    for norm in norm_rows:
        ordinary = by_native[norm["native_degree"]]
        comparisons.append({
            "native_degree": norm["native_degree"],
            "norm_capacity_numerator": norm["capacity_margin_numerator"],
            "one_pole_capacity_numerator": ordinary["capacity_margin_numerator"],
            "norm_common_loss_numerator": norm["common_agreement_loss_numerator"],
            "one_pole_common_loss_numerator": ordinary["common_agreement_loss_numerator"],
            "norm_minimum_endpoint_loss_numerator": norm["minimum_endpoint_loss_numerator"],
            "one_pole_minimum_endpoint_loss_numerator": ordinary["minimum_endpoint_loss_numerator"],
        })

    receipt = {
        "status": "PASS_EXACT_RATIONAL",
        "scope": "Selected base-field fiber domains; native field K, auxiliary field E. No explicit tag set, prescribed NTT domain, or benchmark claim.",
        "prime": P_PRIME, "prime_certificate": {"type": "Proth", "k": 127, "power": 24, "base": 3},
        "n": N, "dimension": J, "sqrt_strict_upper_bound": SQRT_CEILING,
        "norm_degree_six_auxiliary_rows": norm_rows,
        "smaller_fiber_all_native_rows": smaller_fiber_rows,
        "matched_one_pole_rows": matched_rows,
        "norm_next_fiber_moment_obstruction": next_fiber_obstruction(6, 1024),
        "matched_one_pole_next_fiber_obstructions": matched_obstructions,
        "matched_comparisons": comparisons,
        "asymptotic_comparison": "A dimension-shifted one-pole compiler with m'=e*m and shift t=(e-1)*m has the identical source/common/near profile whenever its divisibility and coverage conditions hold.",
    }
    path = Path(__file__).with_name("target_subset_norm_compiler_verified.json")
    path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"status": receipt["status"], "receipt": str(path),
                      "norm_rows": len(norm_rows), "matched_rows": len(matched_rows)}))


if __name__ == "__main__":
    main()
