#!/usr/bin/env python3
"""One specified finite-field fixture; no codeword or challenge-field scan."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import signal
import time

import numpy as np
from flint import fmpz_mod_poly_ctx, fq_default_ctx

started = time.monotonic()
signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(
    TimeoutError("The authorized 60-second computation cap expired")))
signal.alarm(60)

p, h = 97, 5
Q, L = p*p+1, p*p-1
N = h*L
m = N//2
r, remainder = divmod(m, L)
n, k = N+m, h+1
T = isqrt(h*n-1)
common = h*p
noncanonical_upper = max(p,h*h)+(2*h-1)*h
assert p>=h*h and noncanonical_upper<common
source_upper = common
modulus = [5, 80, 6, 0, 1]
ctx = fq_default_ctx(
    modulus=fmpz_mod_poly_ctx(p)(modulus), var="a", fq_type="FQ_NMOD")
one, zero, s = ctx(1), ctx(0), ctx.gen()
order = p**4-1
assert order == 2**7 * 3 * 5 * 7**2 * 941
assert s**order == one
assert all(s**(order//q) != one for q in [2, 3, 5, 7, 941])
z, eta = s**Q, s**h
assert z**L == one and z**(p-1) != one
assert eta**(p*p) != eta
assert Q % h == 0 and h % 2 == 1 and h-1 < Q//h
assert source_upper < T <= (h+r)*(p-1)
assert T*T < h*n <= (T+1)**2

def coefficients(x):
    return [int(c) for c in x.to_list()]

def encode(x):
    return sum(int(c)*p**i for i, c in enumerate(x.to_list()))

def ceil_root_ratio(a, b, power):
    target = (a+b-1)//b
    q = isqrt(target) if power == 2 else isqrt(isqrt(target))
    q += q**power < target
    assert q**power*b >= a
    assert q == 0 or (q-1)**power*b < a
    return q

first_upper = ceil_root_ratio(k*n, 2, 2) + ceil_root_ratio(k**3*n, 72, 4)
assert Fraction(k, n) < Fraction(1, 100)
assert first_upper < common

# Ordered B* and its Frobenius values. Only 9408 field elements are used.
base = []
value = one
for _ in range(L):
    base.append(value)
    value *= z
assert value == one and len(set(base)) == L
assert all(y**(p*p) == y for y in base)
base_p = [y**p for y in base]
base_hp = [y**(h*p) for y in base]

# A prefix on fresh branch r has normalized tag z^(r+h*t).
extra = np.zeros(L, dtype=np.int64)
for t in range(remainder):
    extra[(r+h*t) % L] += 1
assert int(extra.max()) == 1 and int(extra.sum()) == remainder
fresh_weights = extra+r
assert int(fresh_weights.sum()) == m

# All 98 directions and all 97 intercepts: actual finite-field counts.
norm_generator = z**(p-1)
a = one
directions = []
all_image_values = set()
fresh_histogram = Counter()
nonzero_label_supports = Counter()
zero_label_supports = []
per_direction = []
for direction_index in range(p+1):
    assert a**(p+1) == one
    directions.append(a)
    unweighted = Counter()
    fresh = Counter()
    for y, yp, weight in zip(base, base_p, fresh_weights):
        intercept = yp-a*y
        unweighted[intercept] += 1
        fresh[intercept] += int(weight)
    assert len(unweighted) == p and len(fresh) == p
    assert unweighted[zero] == p-1
    assert all(count == p for b, count in unweighted.items() if b != zero)
    image_generator = one-a if a != one else z**p-z
    exact_image = {ctx(t)*image_generator for t in range(p)}
    assert set(unweighted) == exact_image
    all_image_values.update(exact_image)
    assert sum(fresh.values()) == m
    assert fresh[zero] >= r*(p-1)
    assert min(fresh.values()) >= r*(p-1)
    for v, count in fresh.items():
        fresh_histogram[count] += 1
        # For b!=0 there are p-1 different nonzero labels.
        nonzero_label_supports[h*p+count] += p-1
        # b=0,v!=0 is also a nonzero label; b=v=0 is the shared zero.
        if v != zero:
            nonzero_label_supports[h*(p-1)+count] += 1
    zero_label_supports.append(h*(p-1)+fresh[zero])
    per_direction.append({
        "a": coefficients(a),
        "fresh_zero": fresh[zero],
        "fresh_min": min(fresh.values()),
        "fresh_max": max(fresh.values()),
    })
    a *= norm_generator
assert a == one and len(set(directions)) == p+1
# Every nonzero value lies on exactly one image line; hence the lines differ.
assert len(all_image_values) == p*p
assert sum(nonzero_label_supports.values()) == (p+1)*(p*p-1)
assert min(nonzero_label_supports) >= T
assert min(zero_label_supports) >= T and len(zero_label_supports) == p+1

# Explicit endpoints outside all planes I_a + eta I_a:
# their B components are (1,z) and (1,z+1), respectively.
endpoint0 = one+eta*z
endpoint1 = one+eta*(z+one)
assert z**p != z and (z+one)**p != z+one
assert endpoint1-endpoint0 == eta
for a in directions:
    image_generator = one-a if a != one else z**p-z
    image = {ctx(t)*image_generator for t in range(p)}
    assert not (one in image and z in image)
    assert not (one in image and z+one in image)

# Instantiate every coordinate and both endpoint words. Each row stores
# x, f, g, f+endpoint0*g, f+endpoint1*g in the base-p coefficient encoding.
rows = np.empty((n, 5), dtype="<u4")
row = 0
domain_exponents = set()
for block, branch_count in [(0, h), (1, r+1)]:
    for j in range(branch_count):
        branch_size = L if block == 0 or j < r else remainder
        alpha = s**((Q//h)*j)
        coordinate_scale = alpha if block == 0 else s*alpha
        received_scale = alpha**(h*p)
        if block == 1:
            received_scale *= eta
        for t in range(branch_size):
            x = coordinate_scale*base[t]
            f = received_scale*base_hp[t]
            g = block
            if block == 0:
                assert x**h == z**((j+h*t) % L)
            else:
                assert x**h == eta*z**((j+h*t) % L)
            e = (block+(Q//h)*j+Q*t) % order
            assert e not in domain_exponents
            domain_exponents.add(e)
            rows[row] = [
                encode(x), encode(f), g,
                encode(f+endpoint0*g), encode(f+endpoint1*g)]
            row += 1
assert row == n and len(domain_exponents) == n
assert len(set(map(int, rows[:, 0]))) == n
assert int(rows[:, 2].sum()) == m

output = Path(__file__).resolve().parent
np.savez_compressed(output/"domain_and_sources.npz", rows=rows)
receipt = {
    "PASS": True,
    "scope": "One explicit domain and all canonical supports; other-codeword exclusion and exact common agreement use the proved algebraic bounds, not enumeration",
    "p": p, "extension_degree": 4, "modulus_ascending": modulus,
    "primitive_element": coefficients(s),
    "h": h, "full_core": N, "retained_fresh": m,
    "whole_fresh_branches": r, "prefix_fresh_coordinates": remainder,
    "n": n, "k": k, "threshold": T,
    "common_agreement_exact": common,
    "endpoint_agreement_interval": [common, source_upper],
    "endpoint_agreement_exact": common,
    "noncanonical_agreement_upper": noncanonical_upper,
    "first_order_agreement_upper": first_upper,
    "minimum_canonical_guarantee": (h+r)*(p-1),
    "minimum_nonzero_label_actual_canonical_agreement": min(nonzero_label_supports),
    "maximum_nonzero_label_actual_canonical_agreement": max(nonzero_label_supports),
    "singleton_labels": sum(nonzero_label_supports.values()),
    "extra_label_list_size": p+1,
    "zero_label_actual_agreement_range": [min(zero_label_supports), max(zero_label_supports)],
    "endpoint0": coefficients(endpoint0), "endpoint1": coefficients(endpoint1),
    "endpoint_gap_over_capacity_margin_lower": [T-source_upper, T-k],
    "row_encoding": "uint32 little-endian; field element=sum(c_i*97^i); columns x,f,g,endpoint0_word,endpoint1_word",
    "rows_sha256": sha256(rows.tobytes()).hexdigest(),
    "nonzero_canonical_agreement_histogram": dict(sorted(nonzero_label_supports.items())),
    "fresh_line_agreement_histogram": dict(sorted(fresh_histogram.items())),
    "zero_label_agreements": zero_label_supports,
    "per_direction": per_direction,
    "elapsed_seconds": time.monotonic()-started,
    "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
}
(output/"receipt.json").write_text(json.dumps(receipt, indent=2)+"\n")
signal.alarm(0)
print(json.dumps({key: value for key, value in receipt.items()
                 if key not in ["per_direction", "zero_label_agreements"]}, indent=2))
