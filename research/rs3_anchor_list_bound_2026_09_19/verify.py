#!/usr/bin/env python3
"""Exact symbolic certificates for the RS_3 one-anchor list bound.

Uses SymPy for polynomial arithmetic; no floating point or parameter sweep.
Run with the existing research-toolchain Python. Writes receipt.json beside
this script. This certifies arithmetic, not the independent combinatorial
proof reproduced in README.md.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
SQRT3 = sp.sqrt(3)
p, v, z, M = sp.symbols("p v z M", real=True)
c = sp.symbols("c", positive=True)
epsilon = sp.symbols("epsilon", real=True)


def sign_qsqrt3(expression):
    """Return sign(a+b*sqrt(3)) using rational comparisons only."""
    expression = sp.expand(expression)
    b = expression.coeff(SQRT3)
    a = sp.expand(expression - b * SQRT3)
    assert a.is_Rational and b.is_Rational, (a, b)
    if b == 0:
        return 1 if a > 0 else -1 if a < 0 else 0
    if a == 0:
        return 1 if b > 0 else -1 if b < 0 else 0
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    if b > 0:
        difference = 3 * b * b - a * a
    else:
        difference = a * a - 3 * b * b
    assert difference != 0  # sqrt(3) is irrational.
    return 1 if difference > 0 else -1


def positive_shift_certificate(polynomial, onset):
    shifted = sp.Poly(sp.expand(polynomial.subs(p, v + onset)), v)
    coefficients = list(reversed(shifted.all_coeffs()))
    signs = [sign_qsqrt3(value) for value in coefficients]
    assert all(sign > 0 for sign in signs), (polynomial, coefficients)
    return {
        "shift": f"p={onset}+v, v>=0",
        "coefficients_ascending": [str(value) for value in coefficients],
        "coefficient_signs_exact": signs,
    }


def main():
    # U/N = M*(z-1)/((z+1)*(z^2-M)), z=T-1, M=N-1.
    ratio = M * (z - 1) / ((z + 1) * (z * z - M))
    derivative = (
        -2 * M * ((z - 1) ** 2 * (z + 1) + M - 1)
        / ((z + 1) ** 2 * (z * z - M) ** 2)
    )
    assert sp.cancel(sp.diff(ratio, z) - derivative) == 0

    norm_M = 2 * p * p + 2 * p + 1
    cases = [
        {
            "name": "nineteen_tenths_p",
            "threshold_lower_bound": sp.Rational(19, 10) * p,
            "onset": 53,
            "A": 4,
            "B": 3,
            "expected_slack": (
                209 * p**3 - 10870 * p**2 + 1575 * p + 1500
            ) / 250,
        },
        {
            "name": "sqrt_three_p_original_onset",
            "threshold_lower_bound": SQRT3 * p,
            "onset": 401,
            "A": 21,
            "B": 10,
            "expected_slack": (
                SQRT3 * p**3 - (86 + 62 * SQRT3) * p**2
                + (40 - 10 * SQRT3) * p + 20
            ),
        },
        {
            "name": "sqrt_three_p_improved_onset",
            "threshold_lower_bound": SQRT3 * p,
            "onset": 53,
            "A": 9,
            "B": 4,
            "expected_slack": (
                SQRT3 * p**3 - (38 + 26 * SQRT3) * p**2
                + (16 - 4 * SQRT3) * p + 8
            ),
        },
    ]
    certificates = []
    for case in cases:
        T0 = case["threshold_lower_bound"]
        denominator_gap = sp.expand((T0 - 1) ** 2 - norm_M)
        slack = sp.expand(
            case["A"] * T0 * denominator_gap
            - case["B"] * norm_M * (T0 - 2)
        )
        assert sp.expand(slack - case["expected_slack"]) == 0
        certificates.append({
            "case": case["name"],
            "N": "2*(p^2+p+1)",
            "p_at_least": case["onset"],
            "threshold_lower_bound": str(T0),
            "bound_U_over_N": str(sp.Rational(case["A"], case["B"])),
            "denominator_gap": str(denominator_gap),
            "denominator_certificate": positive_shift_certificate(
                denominator_gap, case["onset"]
            ),
            "cross_multiplied_slack": str(slack),
            "slack_certificate": positive_shift_certificate(slack, case["onset"]),
        })

    # T=ceil(c*p)=c*p+epsilon with 0<=epsilon<1. The leading coefficients
    # do not depend on epsilon, so the ratio limit is uniform in rounding.
    T = c * p + epsilon
    numerator = sp.Poly(sp.expand(norm_M * (T - 2)), p)
    denominator = sp.Poly(sp.expand(T * ((T - 1) ** 2 - norm_M)), p)
    assert numerator.degree() == denominator.degree() == 3
    assert sp.expand(numerator.LC() - 2 * c) == 0
    assert sp.expand(denominator.LC() - c * (c * c - 2)) == 0
    limit = sp.cancel(numerator.LC() / denominator.LC())
    assert sp.cancel(limit - 2 / (c * c - 2)) == 0

    receipt = {
        "status": "PASS",
        "scope": "Exact arithmetic and monotonicity; no finite-field or codeword scan.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "sympy_version": sp.__version__,
        "anchor_bound": "N*(N-1)*(T-2)/(T*((T-1)^2-(N-1)))",
        "anchor_hypotheses": "N>=3, integer 3<=T<=N, (T-1)^2>N-1",
        "monotonicity": {
            "substitution": "z=T-1; M=N-1",
            "derivative_of_U_over_N": str(derivative),
            "sign": "strictly negative for M>=2 and z>sqrt(M)",
            "symbolic_identity_verified": True,
        },
        "finite_certificates": certificates,
        "rounded_threshold_asymptotic": {
            "range": "sqrt(2)<c<2 fixed, 0<=epsilon<1",
            "numerator_leading_coefficient": str(numerator.LC()),
            "denominator_leading_coefficient": str(denominator.LC()),
            "limit_U_over_N": str(limit),
            "limit_U_over_exhibited_N_over_2_list": str(2 * limit),
            "sufficient_denominator_onset": "p>=1 and p>(2*c+3)/(c^2-2)",
        },
    }
    output = HERE / "receipt.json"
    output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({
        "status": "PASS", "finite_certificates": len(certificates),
        "receipt": str(output), "script_sha256": receipt["script_sha256"],
    }, indent=2))


if __name__ == "__main__":
    main()
