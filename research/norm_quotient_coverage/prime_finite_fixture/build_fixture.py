#!/usr/bin/env python3
"""One deterministic sample and an exact sixth-moment certificate.

Run with the research interpreter under run_bounded.py.  No floating-point
Fourier transform, subset enumeration, or character enumeration is used.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import math
import random
import resource
import struct
import sys
import time

from flint import nmod_poly

started = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (50, 50))
out = Path(__file__).resolve().parent
p = 65537
M = p - 1
m = 2
b = 3
a0 = 1
s = 1420
seed = 20260918
ntt_prime = 998244353

# Trial division here is tiny and makes the field prerequisite independent.
assert all(p % a for a in range(2, math.isqrt(p) + 1))
assert pow(b, M, p) == 1 and pow(b, M // 2, p) == p - 1
# As M is a power of two, this proves that 3 generates F_p^*.
assert M == 2**16

logs = [-1] * p
value = 1
for exponent in range(M):
    assert logs[value] == -1
    logs[value] = exponent
    value = value * b % p
assert value == 1 and all(v >= 0 for v in logs[1:])
H = [a for a in range(1, p) if logs[a] % 2 == 0]
assert len(H) == M // m and b not in H and a0 in H
population = [a for a in H if a != a0]
G = sorted(random.Random(seed).sample(population, s))
assert len(G) == len(set(G)) == s and a0 not in G

factor_logs = sorted(logs[(b - a) % p] for a in G)
assert len(set(factor_logs)) == s and min(factor_logs) >= 0
indicator = [0] * M
for exponent in factor_logs:
    indicator[exponent] = 1
poly = nmod_poly(indicator, ntt_prime)
cube = poly**3
c3 = [0] * M
for j, coefficient in enumerate(cube):
    c3[j % M] = (c3[j % M] + int(coefficient)) % ntt_prime

# Each cyclic coefficient counts ordered triples, and is at most s^2:
# after choosing the first two logs there is at most one third log.
assert s * s < ntt_prime
assert max(c3) <= s * s
assert sum(c3) == s**3
energy = sum(value * value for value in c3)
nontrivial_sixth_moment = M * energy - s**6
assert nontrivial_sixth_moment >= 0
bias_threshold_sixth_power = Fraction(s, 2)**6
assert nontrivial_sixth_moment < bias_threshold_sixth_power

# All arithmetic for the exponential certificate is rational.
def exp_series_bounds(x, last_degree=100):
    term = Fraction(1)
    partial = term
    for j in range(1, last_degree + 1):
        term *= x / j
        partial += term
    next_term = term * x / (last_degree + 1)
    ratio_bound = x / (last_degree + 2)
    assert 0 <= ratio_bound < 1
    return partial, partial + next_term / (1 - ratio_bound)

_, exp_lower_endpoint_upper = exp_series_bounds(Fraction(s - 1, 128))
exp_upper_endpoint_lower, _ = exp_series_bounds(Fraction(s, 128))
assert exp_lower_endpoint_upper < p < exp_upper_endpoint_lower
# Therefore s=ceil(128 log p), with both inequalities strict.

domain_tags = set(G) | {a0}
domain = [x for x in range(1, p) if pow(x, m, p) in domain_tags]
n = len(domain)
assert n == m * (s + 1) == 2842
assert all((pow(x, m, p) - b) % p != 0 for x in domain)
J = n // 2
quotient, w = divmod(J - 1, m)
r = quotient + 2
assert (J, r, w) == (1421, 712, 0)
assert 0 < r < s
theta = Fraction(r, s)
exponent = theta * (1 - theta) * Fraction(s, 2)
fourier_prefactor = (p - 2) * (s + 1)
exp_lower_bound = exponent**5 / math.factorial(5)
assert exp_lower_bound > fourier_prefactor
error_upper = Fraction(fourier_prefactor, 1) / exp_lower_bound
assert error_upper < 1

tag_data = {
    "p": p, "primitive_generator": b, "m": m, "pole": b,
    "reserved_tag": a0, "seed": seed, "sample_size": s,
    "population_order": "increasing integer representatives of quadratic residues other than 1",
    "sampling": "Python random.Random(seed).sample(population, s), then sorted",
    "sampled_tags": G, "factor_logs_base_3": factor_logs,
    "domain": domain,
}
tags_bytes = (json.dumps(tag_data, indent=2) + "\n").encode()
(out / "tags_and_domain.json").write_bytes(tags_bytes)
convolution_bytes = struct.pack("<" + "I" * M, *c3)
(out / "cyclic_triple_convolution_u32le.bin").write_bytes(convolution_bytes)

usage = resource.getrusage(resource.RUSAGE_SELF)
peak_rss_bytes = int(usage.ru_maxrss if sys.platform == "darwin" else usage.ru_maxrss * 1024)
assert peak_rss_bytes <= 512 * 1024**2
receipt = {
    "status": "PASS",
    "p": p, "multiplicative_group_order": M, "m": m,
    "primitive_generator_and_pole": b,
    "primitive_order_half_power": pow(b, M // 2, p),
    "image_subgroup_size": len(H), "reserved_tag": a0,
    "sample_size": s, "seed": seed,
    "sample_count": 1,
    "convolution_modulus": ntt_prime,
    "cyclic_coefficient_integer_upper_bound": s * s,
    "cyclic_coefficient_observed_maximum": max(c3),
    "cyclic_coefficient_sum": sum(c3),
    "triple_additive_energy": energy,
    "nontrivial_character_sixth_moment": nontrivial_sixth_moment,
    "bias_threshold": str(Fraction(s, 2)),
    "bias_threshold_sixth_power": str(bias_threshold_sixth_power),
    "sixth_moment_ratio": str(Fraction(nontrivial_sixth_moment, bias_threshold_sixth_power)),
    "character_bias_conclusion": "every nontrivial character sum has absolute value strictly below 710",
    "log_sample_size_certificate": {
        "lower_log_endpoint": str(Fraction(s - 1, 128)),
        "upper_log_endpoint": str(Fraction(s, 128)),
        "Taylor_last_degree": 100,
        "conclusion": "exp(1419/128)<65537<exp(1420/128); sample size is exactly ceil(128 log 65537)",
    },
    "code": {
        "length": n, "strict_degree_bound": J,
        "maximum_witness_degree": J - 1, "rate": str(Fraction(J, n)),
        "subset_size": r, "core_size": w,
        "exact_each_source_agreement": J + m - 1,
        "exact_common_agreement": J + m - 1,
        "certified_near_agreement": J + 2 * m - 1,
        "near_pencil_labels": p - 1,
        "near_fraction_on_pencil": str(Fraction(p - 1, p)),
        "near_affine_interpolation_labels": p - 2,
        "near_fraction_between_two_far_sources": str(Fraction(p - 2, p)),
    },
    "cauchy_positivity": {
        "theta": str(theta), "exponent": str(exponent),
        "nontrivial_character_prefactor": fourier_prefactor,
        "exponential_lower_bound_used": "exp(exponent)>exponent^5/120",
        "exponential_rational_lower_bound": str(exp_lower_bound),
        "total_fourier_error_strict_upper_bound": str(error_upper),
        "conclusion": "every nonzero field element is a product of exactly 712 distinct factors b-a with a in sampled_tags",
    },
    "sha256": {
        "tags_and_domain.json": hashlib.sha256(tags_bytes).hexdigest(),
        "cyclic_triple_convolution_u32le.bin": hashlib.sha256(convolution_bytes).hexdigest(),
    },
    "elapsed_seconds": time.monotonic() - started,
    "peak_rss_bytes": peak_rss_bytes,
    "scope": "explicit finite existence certificate for witnesses via exact product counts; witnesses are not enumerated",
}
(out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
