#!/usr/bin/env python3
"""Exact rational arithmetic for the bounded subgroup-twist audit.

This checks the numerical consequences of the proved character bound;
it does not enumerate characters or assume that the bound is attained.
"""
from fractions import Fraction
from decimal import Decimal, localcontext
from pathlib import Path
import json

p = 2130706433
n = 262144
d = 6
k = 131072
target_agreement = 139782
index = (p - 1) // n
assert index == 8128 and index * n == p - 1

sqrt_lower = Fraction(46159575745450694, 10**12)
sqrt_upper = Fraction(46159575745450695, 10**12)
assert sqrt_lower * sqrt_lower < p < sqrt_upper * sqrt_upper

def decimal_string(x):
    with localcontext() as ctx:
        ctx.prec = 45
        return str(Decimal(x.numerator) / Decimal(x.denominator))

cases = []
for epsilon in (0, 1):
    coefficient = Fraction(d) - Fraction(1 + epsilon, index)
    constant = Fraction(1 + epsilon, index)
    lower = coefficient * sqrt_lower + constant
    upper = coefficient * sqrt_upper + constant
    assert lower > n
    cases.append({
        "infinity_exception_present": bool(epsilon),
        "sqrt_coefficient": str(coefficient),
        "additive_boundary_bound": str(constant),
        "proved_bound_expression_strict_lower": str(lower),
        "proved_bound_expression_strict_upper": str(upper),
        "decimal_lower": decimal_string(lower),
        "decimal_upper": decimal_string(upper),
        "excess_over_domain_strict_lower": str(lower - n),
        "scope": "interval for the theorem bound, not for an actual character sum",
    })

receipt = {
    "p": p,
    "extension_degree": d,
    "domain_size": n,
    "subgroup_index": index,
    "sqrtp_strict_lower": str(sqrt_lower),
    "sqrtp_strict_upper": str(sqrt_upper),
    "cases": cases,
    "strict_code_degree_bound": k,
    "one_pole_maximum_agreement": k + 1,
    "target_agreement": target_agreement,
    "agreement_shortfall": target_agreement - (k + 1),
    "target_subset_generic_witness_degree": target_agreement - 2,
    "allowed_witness_degree": k - 1,
    "witness_degree_excess": (target_agreement - 2) - (k - 1),
    "scope": "no character search and no practical improvement certificate",
}
assert receipt["agreement_shortfall"] == 8709
assert receipt["witness_degree_excess"] == 8709
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
