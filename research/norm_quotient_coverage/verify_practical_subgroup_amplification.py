#!/usr/bin/env python3
"""Exact arithmetic for a CONDITIONAL analytic gate, not a moment certificate."""
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
import json

getcontext().prec = 70
p, n, index, r = 2130706433, 262144, 8128, 139782
assert p - 1 == n * index
q = p**6
sqrt_p = Decimal(p).sqrt()
def dec(x):
    x = Fraction(x)
    return str(Decimal(x.numerator) / Decimal(x.denominator))

rows = []
for k, sufficient_moment in ((5, 130), (6, 4182)):
    strict_threshold = Fraction(n**(2*k-1), p**k)
    deficit_threshold = Fraction((n-570)**(2*k), n*p**k)
    assert sufficient_moment < deficit_threshold < strict_threshold
    # These exact powers establish B < n-570 via Holder IF the moment bound holds.
    left, right = sufficient_moment*n*p**k, (n-570)**(2*k)
    assert left < right
    dimension, generic_rank_bound = 6**(2*k), 2*k*6**(2*k-1)
    rows.append({
        "moment_order": 2*k,
        "unproved_sufficient_uniform_moment_bound": sufficient_moment,
        "strict_bias_threshold": dec(strict_threshold),
        "deficit_570_threshold": dec(deficit_threshold),
        "exact_power_inequality_left": left,
        "exact_power_inequality_right": right,
        "general_convolution_rank_bound": generic_rank_bound,
        "tensor_dimension": dimension,
        "general_remark_7_5_error_bound_decimal": str(
            (1+1/sqrt_p)*Decimal(generic_rank_bound+dimension)/sqrt_p),
    })

theta_product = Fraction(r*(n-r), n*n)
u = theta_product*570
prefactor = (q-2)*(n+1)
term = partial = Fraction(1)
for degree in range(1, 1000):
    term *= u / degree
    partial += term
    if partial > prefactor:
        break
else:
    raise AssertionError("Taylor positivity check failed")
assert partial > prefactor  # exp(u) > this positive Taylor partial sum.

receipt = {
    "status": "CONDITIONAL_IMPLICATION_ONLY_NO_CHARACTER_MOMENT_BOUND_PROVED",
    "p": p, "extension_degree": 6, "subgroup_size": n, "index": index,
    "product_cardinality": r,
    "sqrt_p": str(sqrt_p),
    "subgroup_size_over_sqrt_p": str(Decimal(n)/sqrt_p),
    "restricted_second_moment_threshold_over_p": dec(Fraction(n*n,p)),
    "full_parseval_bound": str((Decimal(p-1)*n).sqrt()),
    "generic_centered_correlation_bound_epsilon_zero": str(
        (Decimal(p-n+1)+10*(n-1)*sqrt_p).sqrt()),
    "coverage_deficit_decimal": str(
        Decimal(prefactor).ln()/Decimal(theta_product.numerator)*theta_product.denominator),
    "moment_implications": rows,
    "cauchy_exponent_rational": {"numerator":u.numerator,"denominator":u.denominator},
    "cauchy_prefactor": prefactor,
    "taylor_degree": degree,
    "taylor_partial_sum_numerator": partial.numerator,
    "taylor_partial_sum_denominator": partial.denominator,
    "exact_positive_numerator": partial.numerator-prefactor*partial.denominator,
    "compiler_still_capped_at_agreement": 131073,
    "benchmark_target_agreement": 139782,
}
output = Path(__file__).with_name("practical_subgroup_amplification.json")
output.write_text(json.dumps(receipt, indent=2)+"\n")
print(json.dumps({"receipt":str(output),"status":receipt["status"],
                  "taylor_degree":degree,"candidate_moment_bounds":[130,4182]}))
