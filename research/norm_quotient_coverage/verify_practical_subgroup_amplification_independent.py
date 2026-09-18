"""Independent exact test of the conditional moment-to-coverage gate.

No import of, or execution of, the original verifier. No moments are computed.
The exponential test uses a smaller half-integer exponent and a fixed-degree
integer polynomial instead of the original adaptive Fraction Taylor loop.
"""
import hashlib
import json
from math import factorial, gcd
from pathlib import Path

p = 2130706433
N = 262144
r = 139782
index = 8128
q = p**6
assert p - 1 == N * index
assert 0 < r < N

moment_checks = []
for k, moment_cap in [(5, 130), (6, 4182)]:
    lhs = N * p**k * moment_cap
    rhs = (N - 570)**(2*k)
    assert lhs < rhs
    moment_checks.append({
        "order": 2*k,
        "assumed_uniform_moment_cap": moment_cap,
        "lhs": lhs,
        "rhs": rhs,
        "exact_positive_difference": rhs - lhs,
    })

# u = theta(1-theta)*570 is strictly larger than 283/2.
u_num = 570 * r * (N - r)
u_den = N*N
assert 2*u_num > 283*u_den
common = gcd(u_num, u_den)
prefactor = (q - 2)*(N + 1)

# P_160(283/2) = numerator/denominator < exp(283/2) < exp(u).
degree = 160
fac = factorial(degree)
numerator = sum(
    283**j * 2**(degree-j) * (fac // factorial(j))
    for j in range(degree+1)
)
denominator = 2**degree * fac
margin = numerator - prefactor*denominator
assert margin > 0

receipt = {
    "status": "PASS_CONDITIONAL_IMPLICATION_ONLY",
    "unproved": "Neither uniform character-moment hypothesis is certified",
    "p": p,
    "extension_degree": 6,
    "subgroup_size": N,
    "annihilator_size": index,
    "fixed_cardinality": r,
    "uniform_character_sum_upper": N - 570,
    "character_sum_bound_is_strict": True,
    "moment_power_checks": moment_checks,
    "cauchy_prefactor": prefactor,
    "cauchy_exponent": {"numerator": u_num//common, "denominator": u_den//common},
    "exponent_lower_bound": "283/2",
    "exponent_cross_product_margin": 2*u_num - 283*u_den,
    "fixed_taylor_degree": degree,
    "taylor_denominator": denominator,
    "taylor_numerator": numerator,
    "exact_positive_taylor_margin": margin,
    "taylor_margin_sha256": hashlib.sha256(str(margin).encode()).hexdigest(),
    "conclusion": "Every element of F_(p^6)^* is a product of exactly 139782 distinct factors b-a, conditional on either stated uniform moment hypothesis",
    "scope_excludes": ["proof of either moment bound", "literature applicability", "a degree-admissible coding compiler", "a practical benchmark certificate"],
}
path = Path(__file__).with_name("practical_subgroup_amplification_independent.json")
path.write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps({
    "status": receipt["status"],
    "moment_orders": [row["order"] for row in moment_checks],
    "strict_character_bound": f"B < {N-570}",
    "fixed_taylor_degree": degree,
    "positive_integer_margin_digits": len(str(margin)),
    "receipt": str(path),
}))
