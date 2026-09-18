"""Exact counting frontier of the reserved-full-fiber, all-label compiler."""
import json
from math import comb
from pathlib import Path

n, J = 262144, 131072
cases = [
    ("Goldilocks_cubic", 2**64-2**32+1, 3, 1024),
    ("BabyBear_quartic", 2013265921, 4, 1024),
    ("BabyBear_quintic", 2013265921, 5, 1024),
    ("KoalaBear_sextic", 2130706433, 6, 512),
]


def binomial_at_least(a, b, threshold):
    if b < 0 or b > a:
        return False
    b = min(b, a-b)
    v = 1
    for j in range(1, b+1):
        v = v*(a-b+j)//j
        # The partial products are increasing; avoid enormous unnecessary
        # binomials for the small-fiber cases.
        if v >= threshold:
            return True
    return v >= threshold


central_127 = comb(127, 63)
assert central_127 < 2013265921**4-1
receipts = []
for name, p, d, current_m in cases:
    M = p**d-1
    rows = []
    for exponent in range(19):
        m = 1 << exponent
        if n % m or (p-1) % m:
            continue
        s = n//m-1
        r_max = min(s, (J-1)//m+2)
        central_pass = binomial_at_least(s, s//2, M)
        row = {"m": m, "s": s, "central_binomial_passes": central_pass}
        if central_pass and r_max >= 2:
            r = r_max
            while r >= 2 and not binomial_at_least(s, r, M):
                r -= 1
            if r >= 2:
                w = min(m-1, J-1-(r-2)*m)
                assert 0 <= w < m and w+(r-2)*m <= J-1
                T = r*m+w
                row.update({"best_counting_permitted_r": r, "w": w,
                            "agreement": T, "margin_numerator": T-J})
        rows.append(row)
    passed = [row for row in rows if "agreement" in row]
    best = max(passed, key=lambda row: row["agreement"])
    assert max(row["m"] for row in passed) == 1024
    assert best["m"] == 1024 and best["agreement"] == 133119
    assert best["margin_numerator"] == 2047
    assert comb(255, 129) >= M
    receipts.append({
        "name": name, "p": p, "extension_degree": d, "native_nonzero_labels": M,
        "all_compatible_divisors": rows,
        "maximum_counting_permitted_m": 1024,
        "maximum_counting_permitted_agreement": 133119,
        "maximum_margin": {"numerator": 2047, "denominator": n},
        "current_certified_m": current_m,
        "current_certified_margin": {"numerator": 2*current_m-1, "denominator": n},
        "remaining_margin_numerator": 2047-(2*current_m-1),
        "next_fiber_central_binomial": central_127,
        "next_fiber_exact_deficit": M-central_127,
    })

# Outside the reserved-full-fiber model: no core, no reserved tag.
p = 2013265921
m, s, r, w = 2048, 128, 65, 0
assert n == s*m and w+(r-2)*m <= J-1
assert comb(s, r) >= p**4-1
assert r*m+w-J == 2048
caveat = {
    "scope": "No reserved tag and zero core; necessary count only, not a coverage proof",
    "field": "BabyBear_quartic", "m": m, "s": s, "r": r, "w": w,
    "bank_size": comb(s, r), "native_nonzero_labels": p**4-1,
    "witness_degree_upper": w+(r-2)*m,
    "margin": {"numerator": 2048, "denominator": n},
    "f_and_common_agreement": J,
    "g_root_count_upper": J+m-1,
    "near_agreement": J+m,
}
result = {"status": "PASS_EXACT_MODEL_SPECIFIC_CEILING", "n": n, "J": J,
          "model": "n=(s+1)m; one reserved full fiber; 0<=w<m; w+(r-2)m<=J-1; one label per r-subset",
          "central_127": central_127, "cases": receipts,
          "unreserved_zero_core_caveat": caveat,
          "scope_excludes": ["other support parametrizations", "a universal RS bound", "a sufficient coverage theorem at the counting ceiling"]}
path = Path(__file__).with_name("one_pole_counting_ceiling_verified.json")
path.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({"status": result["status"], "central_127": central_127,
                  "field_frontiers": [{"name": c["name"], "max_m": 1024,
                                       "certified_margin_numerator": c["current_certified_margin"]["numerator"],
                                       "ceiling_margin_numerator": 2047}
                                      for c in receipts],
                  "zero_core_caveat_margin_numerator": 2048}, indent=2))
