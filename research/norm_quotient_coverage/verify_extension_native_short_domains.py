"""Exact finite seed/completion certificates for four selected-domain cases.

Uses integer Proth witnesses, rational square-root upper bounds, and upward
dyadic rounding of the proved recurrence. No field or domain is enumerated.
"""
import json
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path

PRECISION = 512
SCALE = 1 << PRECISION


def ceil_scaled(x):
    return (x.numerator*SCALE+x.denominator-1)//x.denominator


def strict_power_two_upper(x):
    exponent = x.numerator.bit_length()-x.denominator.bit_length()
    while x >= Fraction(2)**exponent:
        exponent += 1
    assert x < Fraction(2)**exponent
    return exponent


def proth_certificate(p, witness):
    odd, exponent = p-1, 0
    while odd % 2 == 0:
        odd //= 2
        exponent += 1
    assert odd % 2 == 1 and odd < 1 << exponent
    residue = pow(witness, (p-1)//2, p)
    assert residue == p-1
    return {"odd_factor": odd, "two_exponent": exponent,
            "witness": witness, "half_power_residue": residue}


cases = [
    ("Goldilocks_cubic", 2**64-2**32+1, 3, 1024, 255, 129, 4, 7),
    ("BabyBear_quartic", 2013265921, 4, 1024, 255, 129, 6, 11),
    ("BabyBear_quintic", 2013265921, 5, 1024, 255, 129, 22, 11),
    ("KoalaBear_sextic", 2130706433, 6, 512, 511, 257, 0, 3),
]
receipts = []
for name, p, d, m, s, r, t, proth_witness in cases:
    prime_certificate = proth_certificate(p, proth_witness)
    assert (p-1) % m == 0
    P = (p-1)//m-1
    M = p**d-1
    root_upper = isqrt(p)+1
    assert (root_upper-1)**2 < p < root_upper**2
    bias_numerator = d*root_upper+1
    epsilon = Fraction(bias_numerator, P)
    s0, r0 = s-2*t, r-t
    assert 0 < r0 < s0 and s <= P
    distinct_probability_lower = 1-Fraction(comb(s0, 2), P)
    assert distinct_probability_lower > 0
    seed_majorant = (Fraction(M-1, comb(s0, r0))
                     * (1+epsilon)**s0 / distinct_probability_lower)
    h_integer = ceil_scaled(seed_majorant)
    h_upper = Fraction(h_integer, SCALE)
    assert h_upper >= seed_majorant
    initial_integer = h_integer
    trace = [{"step": 0, "dyadic_numerator": h_integer,
              "strict_power_two_exponent": strict_power_two_upper(h_upper)}]
    for j in range(t):
        remaining = P-s0-2*j
        assert remaining >= 2
        gamma = Fraction(bias_numerator+s0+2*j, remaining)
        next_majorant = ((h_upper*h_upper+gamma*gamma*h_upper)
                         / (1-Fraction(1, remaining)))
        h_integer = ceil_scaled(next_majorant)
        h_upper = Fraction(h_integer, SCALE)
        assert h_upper >= next_majorant
        trace.append({"step": j+1, "remaining_population": remaining,
                      "gamma_numerator": gamma.numerator,
                      "gamma_denominator": gamma.denominator,
                      "dyadic_numerator": h_integer,
                      "strict_power_two_exponent": strict_power_two_upper(h_upper)})
    assert M*h_integer < SCALE
    n = (s+1)*m
    J = 131072
    w = J-1-(r-2)*m
    assert n == 262144 and 0 <= w < m and w == m-1
    A, T = w+(r-1)*m, w+r*m
    assert A == J+m-1 and T == J+2*m-1 < n
    assert w+(r-2)*m == J-1
    assert n <= p-1 and J < p
    receipts.append({
        "name": name, "status": "PASS_FINITE_EXISTENCE_CRITERION",
        "p": p, "extension_degree": d, "proth_certificate": prime_certificate,
        "m": m, "s": s, "r": r, "completion_pairs": t,
        "seed_size": s0, "seed_weight": r0,
        "population_size": P, "target_group_order": M,
        "sqrt_upper": root_upper,
        "bias_numerator": bias_numerator, "bias_denominator": P,
        "seed_binomial": comb(s0, r0),
        "distinctness_lower": {"numerator": distinct_probability_lower.numerator,
                              "denominator": distinct_probability_lower.denominator},
        "seed_bound_uses": "(1+epsilon)^s0, an upper bound on the exact moment polynomial",
        "dyadic_precision": PRECISION, "seed_dyadic_numerator": initial_integer,
        "recurrence_trace": trace,
        "final_Mh_strict_power_two_exponent": strict_power_two_upper(M*h_upper),
        "exact_final_positive_margin": SCALE-M*h_integer,
        "n": n, "J": J, "w": w, "max_witness_degree": J-1,
        "exact_source_and_common_agreement": A,
        "exact_nonzero_native_pencil_agreement": T,
        "capacity_margin": {"numerator": 2*m-1, "denominator": n},
        "source_common_loss": {"numerator": m, "denominator": n},
        "nonzero_native_labels": M,
        "domain": "Existential selected union of m-point fibers over F_p; not a prescribed NTT subgroup",
    })

result = {"status": "ALL_FOUR_PASS", "arithmetic": "Integers and exact Fractions only",
          "case_count": len(receipts), "cases": receipts,
          "scope": "Finite existence proofs for selected domains; no explicit tag lists, no prescribed-domain or benchmark claim"}
path = Path(__file__).with_name("extension_native_short_domains_verified.json")
path.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({"status": result["status"], "cases": [
    {"name": x["name"], "completion_pairs": x["completion_pairs"],
     "Mh_upper_power_two": x["final_Mh_strict_power_two_exponent"],
     "source_agreement": x["exact_source_and_common_agreement"],
     "near_agreement": x["exact_nonzero_native_pencil_agreement"]}
    for x in receipts]}, indent=2))
