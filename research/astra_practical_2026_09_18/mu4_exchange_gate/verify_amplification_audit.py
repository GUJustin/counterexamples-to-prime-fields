#!/usr/bin/env python3
"""Independent finite audit of the whole-mu4 exchange amplification bounds."""

import collections
import itertools
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def ramanujan_two_power(d, s):
    if d == 1:
        return 1
    if s % d == 0:
        return d // 2
    if s % (d // 2) == 0:
        return -d // 2
    return 0


def product_count_audit():
    coefficients = {
        d: (-1) ** (34 + 34 // d) * math.comb(64 // d - 1, 34 // d)
        for d in [1, 2, 4, 8, 16, 32, 64]
    }
    counts = []
    for s in range(64):
        numerator = sum(value * ramanujan_two_power(d, s)
                        for d, value in coefficients.items())
        assert numerator % 64 == 0
        counts.append(numerator // 64)
    reference = json.loads((HERE / "sector_product_cap.json").read_text())
    assert counts == reference["product_class_counts"]
    assert sum(counts) == math.comb(63, 34)
    maximum = (math.comb(63, 34) + math.comb(31, 17)) // 64
    assert maximum == max(counts) == 11867343831270045
    assert [s for s in range(64) if counts[s] == maximum] == list(range(1, 64, 2))
    return {"character_coefficients": coefficients,
            "matches_every_root_dp_class": True,
            "maximum": maximum,
            "maximizing_classes": "all 32 odd exponents"}


def structural_pair_count(packet_count, packet_size, chosen):
    total_nodes = packet_count * packet_size - 1
    upper = min((packet_count - 1) // 2, chosen // packet_size,
                (total_nodes - chosen) // packet_size)
    terms = []
    for h in range(upper + 1):
        exchanges = (math.comb(packet_count - 1, h)
                     * math.comb(packet_count - 1 - h, h))
        completions = math.comb(total_nodes - 2 * packet_size * h,
                               chosen - packet_size * h)
        terms.append(exchanges * completions)
    return sum(terms), terms


def small_sector_audit():
    fixtures = []
    for M, b, chosen in [(8, 1, 4), (4, 2, 4), (4, 4, 8),
                         (8, 2, 8), (4, 3, 6)]:
        sectors = collections.Counter()
        for support in itertools.combinations(range(1, M * b), chosen):
            support = set(support)
            signature = []
            for j in range(M):
                occupied = tuple(i for i in range(b) if j + i * M in support)
                # The distinguished packet cannot be full, since node0 is omitted.
                signature.append(occupied if j == 0 or 0 < len(occupied) < b else None)
            sectors[tuple(signature)] += 1
        actual = sum(count * count for count in sectors.values())
        formula, _ = structural_pair_count(M, b, chosen)
        assert actual == formula
        fixtures.append({"packets": M, "packet_size": b, "chosen": chosen,
                         "subsets": sum(sectors.values()), "sectors": len(sectors),
                         "ordered_pairs": actual})
    return fixtures


def generator_audit():
    verified = json.loads((HERE / "verified5.json").read_text())
    pairs = verified["underlying_root_exponent_examples"]
    assert len(pairs) == 54
    for positive, negative in pairs:
        assert len(set(positive)) == len(set(negative)) == 20
        assert set(positive).isdisjoint(negative)
        assert 0 not in positive + negative
        delta = [int(i in positive) - int(i in negative) for i in range(256)]
        assert all(delta[i] == delta[(i + 64) % 256] for i in range(256))
    return {"audited_generators": len(pairs),
            "all_signed_differences_constant_on_mu4_packets": True}


if __name__ == "__main__":
    product = product_count_audit()
    pairs, terms = structural_pair_count(64, 4, 136)
    universe = math.comb(255, 136)
    required = 274980728111395088
    result = {"status": "PASS", "product_cap": product,
              "generators": generator_audit(), "small_exhaustive": small_sector_audit(),
              "minimum_sectors_for_required_count": (required - 1) // product["maximum"] + 1,
              "whole_packet_closure_upper": {
                  "ordered_pairs": str(pairs), "universe_count": str(universe),
                  "average_sector_size": pairs / universe,
                  "fraction_of_second_moment_target_log2":
                      math.log2(pairs) - math.log2(universe * (required - 1) + 1),
                  "h_range": [0, len(terms) - 1],
                  "ordered_pair_terms": [str(x) for x in terms],
                  "moments_and_product_ignored": True}}
    output = HERE / "amplification_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "product_cap": product["maximum"],
                      "minimum_sectors": result["minimum_sectors_for_required_count"],
                      "average_sector_size_upper": pairs / universe,
                      "small_exhaustive_subsets": sum(x["subsets"] for x in result["small_exhaustive"]),
                      "output": str(output)}))
