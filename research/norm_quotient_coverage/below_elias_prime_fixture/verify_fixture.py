#!/usr/bin/env python3
"""Independent exact verification of the canonical 23-tag prime fixture.

Checks bitset DP, enumerates all fixed-size subsets by two half tables,
and verifies one saved support per nonzero field element by multiplication.
All computations use Python integers; no numerical Fourier transform.
"""
from pathlib import Path
import hashlib
import json
import math
import resource
import struct
import sys
import time

started = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (50, 50))
out = Path(__file__).resolve().parent
canonical = json.loads((out / "canonical_tags.json").read_text())
tags = canonical["tags"]
p, M, m, b, a0, s, r = 65537, 65536, 2, 3, 1, 23, 13
assert len(tags) == len(set(tags)) == s and a0 not in tags
assert all(p % a for a in range(2, math.isqrt(p) + 1))
assert M == 2**16 and pow(b, M // 2, p) == p - 1
assert all(pow(a, M // 2, p) == 1 for a in tags)

log_table = [-1] * p
value = 1
for exponent in range(M):
    assert log_table[value] == -1
    log_table[value] = exponent
    value = value * b % p
assert value == 1 and all(x >= 0 for x in log_table[1:])
factors = [(b - a) % p for a in tags]
assert len(set(factors)) == s and all(factors)
logs = [log_table[x] for x in factors]

# Method 1: exact Boolean cyclic subset-sum dynamic programming.
all_bits = (1 << M) - 1
dp = [0] * (r + 1)
dp[0] = 1
for index, exponent in enumerate(logs):
    for k in range(min(r, index + 1), 0, -1):
        old = dp[k - 1]
        rotated = ((old << exponent) & all_bits) | (old >> (M - exponent))
        dp[k] |= rotated
assert dp[r] == all_bits

# Method 2: independently enumerate the two halves by ordinary sums.
split = 11
def half_buckets(entries, bit_offset):
    length = 1 << len(entries)
    sums = [0] * length
    buckets = [[] for _ in range(len(entries) + 1)]
    for mask in range(length):
        if mask:
            low = mask & -mask
            sums[mask] = (sums[mask ^ low] + entries[low.bit_length() - 1]) % M
        buckets[mask.bit_count()].append((sums[mask], mask << bit_offset))
    return buckets

left = half_buckets(logs[:split], 0)
right = half_buckets(logs[split:], split)
counts = [0] * M
supports = [0] * M
enumerated = 0
for left_size, left_bucket in enumerate(left):
    right_size = r - left_size
    if not 0 <= right_size < len(right):
        continue
    for left_sum, left_mask in left_bucket:
        for right_sum, right_mask in right[right_size]:
            product_log = (left_sum + right_sum) % M
            counts[product_log] += 1
            if supports[product_log] == 0:
                supports[product_log] = left_mask | right_mask
            enumerated += 1
assert enumerated == math.comb(s, r) == 1144066
assert sum(counts) == enumerated and min(counts) >= 1

# Method 3: check every saved support by direct field multiplication.
target_product = 1
for product_log, mask in enumerate(supports):
    assert mask.bit_count() == r and mask < 1 << s
    product = 1
    remaining = mask
    while remaining:
        low = remaining & -remaining
        product = product * factors[low.bit_length() - 1] % p
        remaining ^= low
    assert product == target_product
    target_product = target_product * b % p
assert target_product == 1

# Explicit degree/source ledger, including actual polynomial coefficients.
domain_tags = set(tags) | {a0}
domain = [x for x in range(1, p) if x * x % p in domain_tags]
n, J, w = len(domain), 24, 1
assert n == 48 and J - 1 == (r - 2) * m + w
assert 1 in domain and p - 1 in domain
assert all((x * x - b) % p != 0 for x in domain)

def evaluate(coefficients, x):
    acc = 0
    for coefficient in reversed(coefficients):
        acc = (acc * x + coefficient) % p
    return acc

def locator(roots):
    coefficients = [1]
    for root in roots:
        nxt = [0] * (len(coefficients) + 1)
        for i, coefficient in enumerate(coefficients):
            nxt[i] = (nxt[i] - root * coefficient) % p
            nxt[i + 1] = (nxt[i + 1] + coefficient) % p
        coefficients = nxt
    return coefficients

def divide_by_y_minus_b(coefficients):
    quotient = [0] * (len(coefficients) - 1)
    quotient[-1] = coefficients[-1]
    for i in range(len(quotient) - 1, 0, -1):
        quotient[i - 1] = (coefficients[i] + b * quotient[i]) % p
    assert (coefficients[0] + b * quotient[0]) % p == 0
    return quotient

def lift_and_multiply_by_x_minus_one(coefficients):
    result = [0] * (2 * len(coefficients))
    for i, coefficient in enumerate(coefficients):
        result[2 * i] = (-coefficient) % p
        result[2 * i + 1] = coefficient
    while result and result[-1] == 0:
        result.pop()
    return result

F = [pow(b, r - 1 - i, p) for i in range(r)]
common_tags = tags[:r - 1]
V = locator(common_tags)
assert len(F) == len(V) == r and F[-1] == V[-1] == 1
Qf = [(a - c) % p for a, c in zip(F, V)]
assert Qf.pop() == 0
Vb_inverse = pow(evaluate(V, b), -1, p)
Qg_numerator = [coefficient * Vb_inverse % p for coefficient in V]
Qg_numerator[0] = (Qg_numerator[0] - 1) % p
Qg = divide_by_y_minus_b(Qg_numerator)
hf_coefficients = lift_and_multiply_by_x_minus_one(Qf)
hg_coefficients = lift_and_multiply_by_x_minus_one(Qg)
f_coefficients = lift_and_multiply_by_x_minus_one(F)
assert len(hf_coefficients) <= J and len(hg_coefficients) <= J
assert len(f_coefficients) - 1 == 25 and f_coefficients[-1] == 1
f_values = [evaluate(f_coefficients, x) for x in domain]
g_values = [-(x - 1) * pow((x * x - b) % p, -1, p) % p for x in domain]
hf_values = [evaluate(hf_coefficients, x) for x in domain]
hg_values = [evaluate(hg_coefficients, x) for x in domain]
f_matches = [x for x, u, v in zip(domain, f_values, hf_values) if u == v]
g_matches = [x for x, u, v in zip(domain, g_values, hg_values) if u == v]
assert f_matches == g_matches and len(f_matches) == 25
assert f_matches == [x for x in domain if x == 1 or x * x % p in common_tags]

# Exact entropy comparison: H_p(7/16)<1/2 iff this integer inequality holds.
entropy_left = (p - 1)**7 * 16**16
entropy_right = p**8 * 7**7 * 9**9
assert entropy_left < entropy_right

data = {
    "p": p, "primitive_generator": b, "pole": b, "m": m,
    "reserved_tag": a0, "core_points": [1],
    "sample_size": s, "subset_size": r,
    "sampled_tags": tags, "factor_logs_base_3": logs,
    "support_mask_bit_order": "bit i refers to sampled_tags[i]; entry t represents product 3^t, hence pencil label -3^t",
    "domain": domain,
    "f_values": f_values, "g_values": g_values,
    "f_polynomial_coefficients_ascending": f_coefficients,
    "common_witness_f_coefficients_ascending": hf_coefficients,
    "common_witness_g_coefficients_ascending": hg_coefficients,
    "common_match_coordinates": f_matches,
}
payload = (json.dumps(data, indent=2) + "\n").encode()
(out / "tags_domain_words.json").write_bytes(payload)
count_bytes = struct.pack("<" + "I" * M, *counts)
support_bytes = struct.pack("<" + "I" * M, *supports)
(out / "product_counts_u32le.bin").write_bytes(count_bytes)
(out / "witness_supports_u32le.bin").write_bytes(support_bytes)
usage = resource.getrusage(resource.RUSAGE_SELF)
peak_rss_bytes = int(usage.ru_maxrss if sys.platform == "darwin" else usage.ru_maxrss * 1024)
assert peak_rss_bytes <= 512 * 1024**2
receipt = {
    "status": "PASS",
    "p": p, "m": m, "pole": b, "sample_size": s, "subset_size": r,
    "canonical_discovery_seed": 2026091823, "canonical_discovery_trial": canonical["trial"],
    "independent_bitset_dp_product_coverage": dp[r].bit_count(),
    "meet_in_the_middle_enumerated_subsets": enumerated,
    "meet_in_the_middle_product_coverage": sum(count > 0 for count in counts),
    "minimum_product_multiplicity": min(counts),
    "maximum_product_multiplicity": max(counts),
    "direct_field_multiplication_verified_supports": M,
    "code": {
        "length": n, "strict_degree_bound": J, "maximum_witness_degree": J - 1,
        "rate": "1/2", "core_size": w,
        "exact_each_source_agreement": 25, "exact_common_agreement": 25,
        "exact_nonzero_pencil_agreement": 27,
        "near_pencil_labels": M, "near_affine_interpolation_labels": p - 2,
        "radius": "7/16", "source_gap": "1/24", "capacity_margin": "1/16",
    },
    "entropy_certificate": {
        "statement": "H_65537(7/16)<1/2",
        "integer_left": str(entropy_left), "integer_right": str(entropy_right),
        "positive_integer_slack": str(entropy_right - entropy_left),
        "equivalent_inequality": "(p-1)^7 * 16^16 < p^8 * 7^7 * 9^9",
    },
    "sha256": {
        "tags_domain_words.json": hashlib.sha256(payload).hexdigest(),
        "product_counts_u32le.bin": hashlib.sha256(count_bytes).hexdigest(),
        "witness_supports_u32le.bin": hashlib.sha256(support_bytes).hexdigest(),
    },
    "elapsed_seconds": time.monotonic() - started,
    "peak_rss_bytes": peak_rss_bytes,
    "scope": "all products and one valid support per nonzero pencil label explicitly verified; prescribed practical NTT-domain benchmark is different",
}
(out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
