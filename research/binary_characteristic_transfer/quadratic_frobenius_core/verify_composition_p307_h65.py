#!/usr/bin/env python3
"""Exact parameters for the linear-characteristic source refinement.

This verifies the algebraic domain recipe and integer inequalities. It does
not enumerate the 11-million-coordinate domain or search over codewords.
"""
from fractions import Fraction
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import json


def prime_by_trial_division(value):
    return value >= 2 and all(value % divisor for divisor in range(2, isqrt(value) + 1))


def ceil_root_ratio(numerator, denominator, power):
    assert numerator >= 0 and denominator > 0 and power in (2, 4)
    rounded = (numerator + denominator - 1) // denominator
    root = isqrt(rounded) if power == 2 else isqrt(isqrt(rounded))
    root += root**power < rounded
    assert root**power * denominator >= numerator
    assert root == 0 or (root - 1)**power * denominator < numerator
    return root


p, h = 307, 65
assert prime_by_trial_division(p)
assert h > 1 and h % 2 == 1
L, quotient_order = p*p - 1, p*p + 1
assert quotient_order % h == 0 and h < quotient_order
assert gcd(h, p*L) == 1
assert p >= 3*h - 1 and p < h*h
assert h - 1 < quotient_order // h

divisor_bounds = []
for delta in range(1, h):
    if h % delta:
        continue
    reduced_degree = h // delta
    assert reduced_degree >= 3 and reduced_degree % 2 == 1
    bound = delta * (max(p, reduced_degree**2) + (2*reduced_degree - 1)*reduced_degree)
    if p >= reduced_degree**2:
        case = "p >= H^2"
        assert (reduced_degree - 1)*p > (2*reduced_degree - 1)*reduced_degree
    else:
        case = "p < H^2"
        assert bound == h*(3*reduced_degree - 1)
        assert p > 3*reduced_degree - 1
    assert bound < h*p
    divisor_bounds.append({
        "delta": delta,
        "H": reduced_degree,
        "case": case,
        "noncanonical_agreement_bound": bound,
    })
assert [item["delta"] for item in divisor_bounds] == [1, 5, 13]
noncanonical_maximum = max(item["noncanonical_agreement_bound"] for item in divisor_bounds)

N = h*L
m = 17*N // 20
r, prefix_length = divmod(m, L)
n, k = N + m, h + 1
T = isqrt(h*n - 1)
source = h*p
minimum_canonical = (h + r)*(p - 1)
assert 0 < m < N and 0 <= r < h and 0 <= prefix_length < L
assert m == r*L + prefix_length
assert noncanonical_maximum < source < T <= minimum_canonical
assert source + h*h < T  # even the older sufficient threshold guard passes
assert T*T < h*n <= (T + 1)**2

first_leading = ceil_root_ratio(k*n, 2, 2)
first_correction = ceil_root_ratio(k**3*n, 72, 4)
first_upper = first_leading + first_correction
assert 2*first_leading**2 > k*n  # the radical sum is strictly below its ceiling sum
assert Fraction(k, n) < Fraction(1, 100)
assert first_upper < source
singleton_labels = (p + 1)*L
outside_labels = p**4 - (1 + singleton_labels)
assert outside_labels >= 2
loss_ratio = Fraction(T - source, T - k)
assert loss_ratio > Fraction(265, 1000)

result = {
    "PASS": True,
    "scope": "Exact finite parameters for the deterministic algebraic branch-prefix domain; no domain enumeration or codeword scan",
    "p": p,
    "primality_certificate": "Trial division through floor(sqrt(307))=17",
    "extension_degree": 4,
    "alphabet_size": p**4,
    "h": h,
    "dimension": k,
    "linear_characteristic_threshold": 3*h - 1,
    "old_quadratic_characteristic_threshold": h*h,
    "old_quadratic_hypothesis_fails": p < h*h,
    "proper_composition_divisor_bounds": divisor_bounds,
    "noncanonical_agreement_bound": noncanonical_maximum,
    "source_agreement": source,
    "common_agreement": source,
    "full_first_block": N,
    "retained_second_block": m,
    "retention_fraction": [17, 20],
    "whole_fresh_branches": r,
    "next_branch_prefix_length": prefix_length,
    "length": n,
    "threshold": T,
    "minimum_canonical_agreement": minimum_canonical,
    "first_order_leading_ceiling": first_leading,
    "first_order_correction_ceiling": first_correction,
    "first_order_agreement_upper": first_upper,
    "first_order_certified_slack": source - first_upper,
    "johnson_squared_slack": h*n - T*T,
    "singleton_labels": singleton_labels,
    "additional_label_list_size": p + 1,
    "outside_canonical_labels": outside_labels,
    "rate": [k, n],
    "exact_loss_over_capacity_margin": [loss_ratio.numerator, loss_ratio.denominator],
    "exact_loss_over_capacity_margin_decimal": float(loss_ratio),
    "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
