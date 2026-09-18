"""Independent certificates using one fixed contraction bound per field."""
from fractions import Fraction as F
from math import comb, isqrt
from pathlib import Path
import json

cases = [
    ("Goldilocks", 2**64-2**32+1, 3, 1024, 4, 48, 2**38, 7),
    ("BabyBear", 2013265921, 4, 1024, 6, 84, 119, 11),
    ("BabyBear", 2013265921, 5, 1024, 22, 19, 76, 11),
    ("KoalaBear", 2130706433, 6, 512, 0, 272, 1, 3),
]
receipts = []
for name, p, d, m, t, exponent, contraction, primality_witness in cases:
    odd, power = p-1, 0
    while odd % 2 == 0:
        odd //= 2
        power += 1
    assert odd < 2**power and pow(primality_witness, (p-1)//2, p) == p-1
    # These are the hypotheses and witness of Proth's primality criterion.
    n, J = 262144, 131072
    assert (p-1) % m == 0 and n % m == 0
    s, r = n//m-1, (J-1)//m+2
    w = J-1-(r-2)*m
    assert 0 <= w < m
    P, M = (p-1)//m-1, p**d-1
    s0, r0 = s-2*t, r-t
    epsilon = F(d*(isqrt(p)+1)+1, P)
    distinct = 1-F(comb(s0, 2), P)
    assert 0 < r0 < s0 and distinct > 0 and s <= P
    seed = F(M-1, comb(s0, r0))*(1+epsilon)**s0/distinct
    cap = F(1, 2**exponent)
    assert seed < cap
    if t:
        # This bounds every remaining population, even after all s deletions.
        gamma = (P*epsilon+s)/(P-s)
        factor = (cap+gamma*gamma)/(1-F(1, P-s))
        assert factor < F(1, contraction)
        # Since contraction>1, the same cap applies at every later step.
        assert contraction > 1
    assert M < 2**exponent * contraction**t
    receipts.append({
        "field": name, "prime": p, "extension_degree": d,
        "n": n, "J": J, "m": m, "s": s, "r": r, "w": w,
        "completion_pairs": t, "seed_bound": f"h0 < 2^-{exponent}",
        "uniform_contraction_denominator": contraction,
        "final_integer_comparison": "M < 2^exponent * contraction^t",
        "exact_source_and_common_agreement": J+m-1,
        "exact_nonzero_native_agreement": J+2*m-1,
        "status": "PASS_EXISTENCE_ON_SELECTED_FIBERS",
    })
result = {"method": "exact fractions plus a uniform contraction; no dyadic iteration",
          "scope": "Katz bound and the proved compiler are mathematical inputs; no selected tag set is enumerated",
          "cases": receipts}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({"status": "PASS", "cases": len(receipts), "receipt": str(out)}))
