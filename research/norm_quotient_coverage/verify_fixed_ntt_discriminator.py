#!/usr/bin/env python3
"""Exact collision-energy receipt for fixed KoalaBear NTT domains.

No subgroup elements or extension elements are enumerated.  All acceptance
checks are integer comparisons.  Polynomial root counting supplies the
mathematical bound evaluated here.
"""

from fractions import Fraction
from math import comb
from pathlib import Path
import json


def ceil_fraction(value):
    return -((-value.numerator) // value.denominator)


def main():
    p = 2130706433
    q = p ** 6
    full_degree_count = q - p ** 3 - p ** 2 + p
    n, J = 262144, 131072
    target_agreement = 139782
    target_labels = (q + 2 ** 128 - 1) // 2 ** 128
    assert target_labels == 274980728111395088
    assert (p - 1) % n == 0
    assert p == 127 * 2 ** 24 + 1 and 127 < 2 ** 24
    assert pow(3, (p - 1) // 2, p) == p - 1

    rows = []
    for m in (1024, 2048, 4096, 8192):
        s, r, w = n // m - 1, J // m + 1, m - 1
        assert 2 <= r <= s
        assert n == (s + 1) * m
        assert J == w + (r - 2) * m + 1
        L = comb(s, r)
        weights = [comb(r, u) * comb(s - r, u)
                   for u in range(min(r, s - r) + 1)]
        assert sum(weights) == L
        ordinary_sum = sum(weights[u] * (u - 1)
                           for u in range(1, len(weights)))
        orbit_sum = sum(weights[u] * (6 * ((u - 1) // 6))
                        for u in range(1, len(weights)))
        assert ordinary_sum == L * Fraction(r * (s - r), s) - L + 1
        assert 0 <= orbit_sum <= ordinary_sum
        image_bound = Fraction(L * full_degree_count, full_degree_count + orbit_sum)
        guaranteed = ceil_fraction(image_bound)
        assert 1 <= guaranteed <= L
        injective = L * orbit_sum < full_degree_count
        if injective:
            assert guaranteed == L
        A, T = J + m - 1, J + 2 * m - 1
        rows.append({
            "fiber_size": m, "nonreserved_tags": s,
            "subset_size": r, "core_size": w,
            "subset_count": L,
            "ordinary_pair_root_sum": ordinary_sum,
            "full_degree_orbit_pair_root_sum": orbit_sum,
            "raw_image_bound": {"numerator": image_bound.numerator,
                                "denominator": image_bound.denominator},
            "distinct_nonzero_labels_at_least": guaranteed,
            "all_subset_labels_distinct_certified": injective,
            "nonendpoint_affine_mixture_labels_at_least": guaranteed - 1,
            "exact_source_and_common_agreement": A,
            "exact_nearby_agreement": T,
            "capacity_margin_numerator": T - J,
            "source_and_common_gap_numerator": T - A,
            "enough_labels_at_2_to_minus_128": guaranteed - 1 >= target_labels,
            "reaches_required_agreement": T >= target_agreement,
        })

    next_fiber_unreserved_tags = n // 8192
    next_fiber_all_cardinality_max = comb(next_fiber_unreserved_tags,
                                         next_fiber_unreserved_tags // 2)
    assert next_fiber_all_cardinality_max == 601080390 < target_labels
    best = next(row for row in rows if row["fiber_size"] == 4096)
    assert best["all_subset_labels_distinct_certified"]
    assert best["subset_count"] == 860778005594247069
    assert best["enough_labels_at_2_to_minus_128"]
    assert target_agreement - best["exact_nearby_agreement"] == 519
    receipt = {
        "status": "PASS_EXACT_INTEGER",
        "scope": "Fixed domain mu_262144 in the KoalaBear prime field, native alphabet F_(p^6), existential full-degree pole. This is the prior quotient/discriminator mechanism with overlap and Frobenius-orbit root-count refinements.",
        "prime": p, "alphabet_size": q,
        "full_degree_six_poles": full_degree_count,
        "n": n, "dimension": J,
        "required_agreement": target_agreement,
        "required_label_count": target_labels,
        "cases": rows,
        "one_pole_counting_frontier": {
            "largest_possible_fiber_with_required_labels": 4096,
            "next_fiber": 8192,
            "number_of_fibers_even_without_reserve": next_fiber_unreserved_tags,
            "max_fixed_cardinality_bank_even_without_reserve": next_fiber_all_cardinality_max,
            "reserved_fiber_max_agreement": best["exact_nearby_agreement"],
            "agreement_shortfall": 519,
            "qualification": "Fixed-cardinality one-pole full-fiber compiler only, not a universal coding bound",
        },
    }
    path = Path(__file__).with_name("fixed_ntt_discriminator_verified.json")
    path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"status": receipt["status"], "receipt": str(path),
                      "best_agreement_with_required_labels": best["exact_nearby_agreement"],
                      "best_row_labels": best["subset_count"]}))


if __name__ == "__main__":
    main()
