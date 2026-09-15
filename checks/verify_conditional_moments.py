#!/usr/bin/env python3
"""Sharper integer-moment list bounds with exact small-instance checks.

Counts subsets by their first moment and computes the exact range of their
second binomial moment, without enumerating the joint moment distribution.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, log2
from pathlib import Path
import json
import time


def conditional_counts(n, t):
    # Each record is (count, min, max, sum of second moments, sum of squares).
    rows = [dict() for _ in range(t+1)]
    rows[0][0] = (1, 0, 0, 0, 0)
    updates = 0
    for j in range(n):
        second = comb(j, 2)
        for k in range(min(t, j+1), 0, -1):
            for q, (count, low, high, total, squared) in rows[k-1].items():
                target = q+j
                old = rows[k].get(target)
                candidate = (count, low+second, high+second,
                             total+count*second,
                             squared+2*second*total+count*second*second)
                if old is None:
                    rows[k][target] = candidate
                else:
                    rows[k][target] = (old[0]+count, min(old[1], candidate[1]),
                                       max(old[2], candidate[2]),
                                       old[3]+candidate[3], old[4]+candidate[4])
                updates += 1
    assert sum(record[0] for record in rows[t].values()) == comb(n, t)
    weights = [comb(j, 2) for j in range(n)]
    weight_sum, squared_sum = sum(weights), sum(w*w for w in weights)
    assert sum(record[3] for record in rows[t].values()) == comb(n-1, t-1)*weight_sum
    assert sum(record[4] for record in rows[t].values()) == (
        comb(n-1, t-1)*squared_sum+comb(n-2, t-2)*(weight_sum*weight_sum-squared_sum))
    return rows[t], updates


def ceil_div(numerator, denominator):
    return (numerator+denominator-1)//denominator


def certify(n, t):
    start = time.perf_counter()
    rows, updates = conditional_counts(n, t)
    bounds = {q: ceil_div(count, high-low+1)
              for q, (count, low, high, _, _) in rows.items()}
    best_q = max(bounds, key=lambda q: (bounds[q], -q))
    count, low, high, _, _ = rows[best_q]
    R1 = comb(n, 2)-comb(n-t, 2)-comb(t, 2)+1
    R2 = comb(n, 3)-comb(n-t, 3)-comb(t, 3)+1
    original = ceil_div(comb(n, t), R1*R2)
    # Reflection a -> n-1-a independently checks every count and envelope.
    for q, (number, lo, hi, total, squared) in rows.items():
        reflected_q = t*(n-1)-q
        shift = t*comb(n-1, 2)-(n-2)*q
        assert rows[reflected_q] == (number, lo+shift, hi+shift,
            total+number*shift, squared+2*shift*total+number*shift*shift)
    # Integer Chebyshev counting: outside [center-radius,center+radius],
    # every second moment contributes at least (radius+1)^2 squared deviation.
    concentration = None
    for q, (number, lo, hi, total, squared) in rows.items():
        center = (2*total+number)//(2*number)
        deviation = squared-2*center*total+number*center*center
        for radius in range(max(center-lo, hi-center)+1):
            width = min(hi, center+radius)-max(lo, center-radius)+1
            retained = max(0, number-deviation//((radius+1)**2))
            bound = ceil_div(retained, width)
            candidate = dict(first_moment=q, center=center, radius=radius,
                subset_count=number, sum_second_moments=total,
                sum_squared_second_moments=squared, squared_deviation=deviation,
                retained_subset_lower_bound=retained, interval_width=width,
                list_lower_bound=bound, lower_bound_log2=log2(max(1,bound)))
            if concentration is None or bound > concentration['list_lower_bound']:
                concentration = candidate
    return dict(n=n, t=t, k=t-2, first_moment=best_q,
                conditioned_subset_count=count, second_moment_min=low,
                second_moment_max=high, second_moment_width=high-low+1,
                list_lower_bound=bounds[best_q],
                original_list_lower_bound=original,
                improvement_ratio=bounds[best_q]/original,
                lower_bound_log2=log2(bounds[best_q]),
                dp_updates=updates, elapsed_seconds=time.perf_counter()-start,
                concentration=concentration,
                first_moment_classes=[dict(first_moment=q, count=number,
                    second_min=lo, second_max=hi, sum_second_moments=total,
                    sum_squared_second_moments=squared)
                    for q,(number,lo,hi,total,squared) in sorted(rows.items())])


checked_cases = checked_subsets = 0
for n in range(4, 15):
    for t in range(3, n):
        actual = defaultdict(Counter)
        for support in combinations(range(n), t):
            actual[sum(support)][sum(comb(j, 2) for j in support)] += 1
            checked_subsets += 1
        rows, _ = conditional_counts(n, t)
        assert set(rows) == set(actual)
        for q, histogram in actual.items():
            assert rows[q] == (sum(histogram.values()), min(histogram), max(histogram),
                sum(v*c for v,c in histogram.items()), sum(v*v*c for v,c in histogram.items()))
            count, low, high, total, squared = rows[q]
            assert ceil_div(count, high-low+1) <= max(histogram.values())
            center = (2*total+count)//(2*count)
            deviation = squared-2*center*total+count*center*center
            for radius in range(max(center-low, high-center)+1):
                retained = max(0, count-deviation//((radius+1)**2))
                width = min(high, center+radius)-max(low, center-radius)+1
                assert retained <= sum(c for v,c in histogram.items() if abs(v-center)<=radius)
                assert ceil_div(retained, width) <= max(histogram.values())
        checked_cases += 1

certificate = certify(64, 34)
L = certificate['list_lower_bound']
p = 2**127-1
assert p**2 > 2**64  # The original Elias certificate remains unchanged.
assert L > 2**39
# A separate two-variable generating-function computation for the selected
# first-moment count, using coefficient extraction by Gaussian binomials.
# [y^t] prod_(j=0)^(n-1)(1+y*x^j) = x^(t(t-1)/2) [n choose t]_x.
degree = certificate['first_moment']-comb(34, 2)
coefficients = [1]+[0]*degree
for j in range(1, 35):
    # Multiply by (1-x^(30+j)), then divide by (1-x^j), truncating.
    numerator_degree = 30+j
    for a in range(degree, numerator_degree-1, -1):
        coefficients[a] -= coefficients[a-numerator_degree]
    for a in range(j, degree+1):
        coefficients[a] += coefficients[a-j]
assert coefficients[degree] == certificate['conditioned_subset_count']
concentration = certificate['concentration']
degree2 = concentration['first_moment']-comb(34, 2)
coefficients2 = [1]+[0]*degree2
for j in range(1, 35):
    for a in range(degree2, 30+j-1, -1):
        coefficients2[a] -= coefficients2[a-30-j]
    for a in range(j, degree2+1):
        coefficients2[a] += coefficients2[a-j]
assert coefficients2[degree2] == concentration['subset_count']
assert concentration['list_lower_bound'] > 2**41
assert concentration['list_lower_bound'] > 622*2**32
assert concentration['list_lower_bound'] > 53*certificate['original_list_lower_bound']
line_count = concentration['subset_count']
assert line_count > 2**52
assert p > 64+32*comb(line_count, 2)

result = dict(status='passed', exhaustive_cases=checked_cases,
              exhaustive_subsets=checked_subsets,
              independent_gaussian_binomial_coefficient=coefficients[degree],
              independent_central_gaussian_binomial_coefficient=coefficients2[degree2],
              finite_line_distinct_parameter_count=line_count,
              finite_line_collision_free_pole_certificate=True,
              certificate=certificate,
              scope='An exact lower bound on an integer-moment class, not an enumeration of that class or an exact maximum list size.')
out = Path(__file__).with_name('conditional_moment_results.json')
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({**result, 'certificate':{k:v for k,v in certificate.items()
      if k != 'first_moment_classes'}}, indent=2))
