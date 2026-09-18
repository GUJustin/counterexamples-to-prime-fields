"""Exact rational certificate for the degree-five half-cardinality onset.

Only the endpoint inequalities require finite arithmetic. Monotonicity and
the character/coefficient argument are proved in the accompanying note.
"""

from fractions import Fraction
import json
from pathlib import Path

p = 181
sqrt_upper = Fraction(134537, 10000)
log_upper = Fraction(10397, 2000)
assert sqrt_upper ** 2 > p

# Every omitted term in exp(log_upper) is positive. Thus this rational partial
# sum greater than181 proves log(181)<log_upper without floating-point logs.
term = Fraction(1)
partial = term
terms = 40
for j in range(1, terms + 1):
    term = term * log_upper / j
    partial += term
assert partial > p

margin_lower = Fraction(p - 2, 4) - sqrt_upper - 6 * log_upper
assert margin_lower == Fraction(1053, 10000) > 0

# A deliberately coarse exact check shows the stronger sufficient inequality
# does not hold at179. This is not a non-surjectivity claim.
q = 179
sqrt_lower = Fraction(1337, 100)
log_lower = Fraction(259, 50)
assert sqrt_lower ** 2 < q
term2 = Fraction(1)
partial2 = term2
for j in range(1, terms + 1):
    term2 = term2 * log_lower / j
    partial2 += term2
next_term = term2 * log_lower / (terms + 1)
tail_upper = next_term / (1 - log_lower / (terms + 2))
assert partial2 + tail_upper < q
previous_margin_upper = Fraction(q - 2, 4) - sqrt_lower - 6 * log_lower
assert previous_margin_upper == Fraction(-1, 5) < 0

# Arbitrary-dimension compiler variant deletes both0 and one additional tag.
# At the two nearest-half cardinalities for s=p-2, the density product is
# c(p)=(1-1/(p-2)^2)/4. Its stronger endpoint bound uses p^6 again.
q2 = 191
sqrt_upper2 = Fraction(138203, 10000)
log_upper2 = Fraction(52523, 10000)
assert sqrt_upper2 ** 2 > q2
term3 = Fraction(1)
partial3 = term3
for j in range(1, terms + 1):
    term3 = term3 * log_upper2 / j
    partial3 += term3
assert partial3 > q2
c2 = Fraction(94 * 95, 189 ** 2)
margin_lower2 = c2 * (q2 - 4 - 4 * sqrt_upper2) - 6 * log_upper2
assert c2 > Fraction(6, 25)
assert margin_lower2 > 0
derivative_lower2 = Fraction(6, 25) * Fraction(11, 13) - Fraction(6, 191)
assert derivative_lower2 > 0

# Exact code dimension J=floor(p^5/2) uses r=(p+1)/2 after core padding,
# not a nearest-half subset of the p-2 remaining tags.
c3 = Fraction(96 * 93, 189 ** 2)
assert c3 == (1 - Fraction(9, 189 ** 2)) / 4
assert c3 > Fraction(6, 25)
margin_lower3 = c3 * (q2 - 4 - 4 * sqrt_upper2) - 6 * log_upper2
assert margin_lower3 > 0

out = dict(endpoint_prime=p, r=(p-1)//2,
           sqrt_upper=str(sqrt_upper), sqrt_square_excess=str(sqrt_upper**2-p),
           log_upper=str(log_upper), exp_series_last_degree=terms,
           exp_partial_sum_excess_over_prime=str(partial-p),
           H181_strict_lower_bound=str(margin_lower),
           derivative="H'(x)=(sqrt(x)-6)*(sqrt(x)+4)/(4*x)>0 for x>36",
           conclusion="all odd primes p>=181 satisfy the product-surjectivity sufficient inequality at r=(p-1)/2",
           previous_prime=179, previous_H_strict_upper_bound=str(previous_margin_upper),
           previous_check_scope="failure of sufficient inequality only, not failure of product surjectivity",
           two_deleted_tags=dict(endpoint_prime=q2, subset_sizes=[94,95],
                                 sqrt_upper=str(sqrt_upper2), log_upper=str(log_upper2),
                                 density_product=str(c2), H191_strict_lower_bound=str(margin_lower2),
                                 derivative_positive_lower_bound=str(derivative_lower2),
                                 conclusion="all odd primes p>=191 suffice at r=(p-3)/2 or (p-1)/2"),
           exact_half_code_dimension=dict(endpoint_prime=q2, subset_size=96, available_tags=189,
                                          density_product=str(c3), H191_strict_lower_bound=str(margin_lower3),
                                          derivative_positive_lower_bound=str(derivative_lower2),
                                          general_r="(p+1)/2", general_s="p-2",
                                          conclusion="all odd primes p>=191 suffice for the exact J=floor(p^5/2) padded compiler"))
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps({k:v for k,v in out.items() if k != "exp_partial_sum_excess_over_prime"},indent=2))
