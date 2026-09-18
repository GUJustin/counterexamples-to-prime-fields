#!/usr/bin/env python3
"""Exact existence certificate for selected M31 circle power fibers.

This verifies the arithmetic hypotheses of fixed_weight_completion.tex.
It does not enumerate the existential tag set or assert Circle-STARK equivalence.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from math import comb
from pathlib import Path
import json
import resource
import time

started = time.monotonic()
getcontext().prec = 70
prime_exponent = 31
assert all(prime_exponent % d for d in range(2, 6))
p = 2**prime_exponent-1
ll = 4
lucas_lehmer = [ll]
for _ in range(prime_exponent-2):
    ll = (ll*ll-2) % p
    lucas_lehmer.append(ll)
assert ll == 0  # Lucas--Lehmer primality certificate for the Mersenne number.
assert 46340**2 < p < 46341**2

fiber, n, dimension = 1024, 262144, 131072
circle_order = p+1
image_size = circle_order//fiber
population = image_size-1  # Reserve tag1 before choosing the other tags.
q = p**4
group_order = q-1
s, r, t = 255, 129, 6
s0, r0 = s-2*t, r-t
assert (s+1)*fiber == n
assert image_size*fiber == circle_order
assert 0 < r0 < s0 and s <= population

# Character lemma gives 4 sqrt(p) on the image subgroup; removing1 costs1.
character_numerator = 4*46341+1
epsilon = Fraction(character_numerator, population)
distinct_probability_lower = 1-Fraction(comb(s0, 2), population)
assert distinct_probability_lower > 0
support_count = comb(s0, r0)
overlap_sum = sum(Fraction(comb(r0,u)*comb(s0-r0,u))*epsilon**(2*u)
                  for u in range(min(r0,s0-r0)+1))
seed_bound = (group_order-1)*overlap_sum/(distinct_probability_lower*support_count)

# Upward dyadic rounding keeps every recurrence comparison exact and compact.
grid = 2**256
def rounded_up(value):
    numerator = (value.numerator*grid+value.denominator-1)//value.denominator
    result = Fraction(numerator, grid)
    assert result >= value
    return numerator, result

seed_numerator, h = rounded_up(seed_bound)
def decimal(value):
    value = Fraction(value)
    return str(Decimal(value.numerator)/Decimal(value.denominator))
def log2(value):
    value = Fraction(value)
    return str((Decimal(value.numerator).ln()-Decimal(value.denominator).ln())/Decimal(2).ln())

steps = []
for j in range(t):
    unused = population-s0-2*j
    gamma = Fraction(character_numerator+s0+2*j, unused)
    conditional_upper = (h*h+gamma*gamma*h)/(1-Fraction(1,unused))
    numerator, h = rounded_up(conditional_upper)
    steps.append({"step": j+1, "remaining_population": unused,
                  "gamma_numerator": gamma.numerator,"gamma_denominator":gamma.denominator,
                  "hole_numerator_over_2_to_256": numerator,
                  "log2_hole_bound_display":log2(h),
                  "group_order_times_hole_bound_display":decimal(group_order*h)})
assert group_order*h < 1
assert group_order*steps[-1]["hole_numerator_over_2_to_256"] < grid

w = dimension-1-(r-2)*fiber
assert w == fiber-1 == 1023
source_agreement = (r-1)*fiber+w
near_agreement = r*fiber+w
assert source_agreement == dimension+fiber-1 == 132095
assert near_agreement == dimension+2*fiber-1 == 133119

receipt = {
    "status":"PASS_EXACT_EXISTENCE_CERTIFICATE_SELECTED_DOMAIN",
    "p":p,"primality_method":"Lucas-Lehmer, prime exponent31,29 iterations",
    "lucas_lehmer_residues":lucas_lehmer,
    "extension_degree":4,"alphabet_and_challenge_field_size":q,
    "product_group_order":group_order,
    "circle_order":circle_order,"power_fiber_size":fiber,"power_image_size":image_size,
    "reserved_tag":1,"population_size":population,
    "uniform_character_sum_bound":"4*sqrt(p), all nontrivial extension characters and all circle twists",
    "rational_character_bias_numerator":character_numerator,
    "rational_character_bias_denominator":population,
    "rational_character_bias_display":decimal(epsilon),
    "final_tag_count":s,"product_cardinality":r,"completion_pairs":t,
    "seed_tag_count":s0,"seed_product_cardinality":r0,"seed_support_count":support_count,
    "distinct_probability_lower_numerator":distinct_probability_lower.numerator,
    "distinct_probability_lower_denominator":distinct_probability_lower.denominator,
    "rounding_denominator":grid,
    "seed_hole_numerator_over_2_to_256":seed_numerator,
    "seed_log2_hole_bound_display":log2(Fraction(seed_numerator,grid)),
    "completion_steps":steps,
    "final_exact_integer_left":group_order*steps[-1]["hole_numerator_over_2_to_256"],
    "final_exact_integer_right":grid,
    "final_strict_inequality_slack":grid-group_order*steps[-1]["hole_numerator_over_2_to_256"],
    "domain_length":n,"strict_degree_bound":dimension,"maximum_witness_degree":dimension-1,
    "core_degree":w,"exact_both_source_and_common_agreement":source_agreement,
    "exact_nonzero_pencil_agreement":near_agreement,"nonzero_near_labels":group_order,
    "source_to_near_gap":near_agreement-source_agreement,
    "capacity_margin":str(Fraction(near_agreement-dimension,n)),
    "domain_scope":"existentially selected union of256 complete power fibers inside the norm-one circle",
    "code_scope":"ordinary univariate Reed-Solomon over F_(p^4); no Circle-STARK equivalence asserted",
    "elapsed_seconds":time.monotonic()-started,
    "peak_rss_platform_units":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
}
path=Path(__file__).with_name("receipt.json")
path.write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({"status":receipt["status"],"receipt":str(path),
                  "final_group_order_times_hole_bound":decimal(group_order*h),
                  "source_agreement":source_agreement,"near_agreement":near_agreement}))
