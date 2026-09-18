#!/usr/bin/env python3
"""Exact arithmetic receipt for PARTIAL_PACKET_DENOMINATOR_CODIMENSION.md."""
import json
from math import comb
from pathlib import Path

p, B, J, A = 2130706433, 512, 131072, 139782
target = 274980728111395088


def ceildiv(x, y):
    return -((-x) // y)


def guarantee(pool, chosen, heads):
    return ceildiv(comb(pool, chosen), B * p**heads)


band = A - (1031 + J - 1)
assert band == 7680
assert 2 * (A - 266 * B) == 7180 < band
assert 2 * (A - 511 - 265 * B) == 7182 < band
assert 2 * (A - 265 * B) >= band
assert 2 * (A - 511 - 264 * B) >= band

# For each possible partial remainder and denominator residue, check the
# floor/ceiling step used in the denominator-independent proof. Integer
# B-shifts of d cancel from the left side, so one period covers all d.
for u in range(-B, B):
    for v in range(B):
        assert (u + v) // B - ceildiv(v, B) <= u // B

profiles = []
for h in range(266, 274):
    c = A - h * B
    kernel_bound = max(0, (J - 1 - c) // B + 1)
    codimension = h - (kernel_bound + 1)
    assert codimension == 16
    profiles.append(dict(h=h, c=c, kernel_bound=kernel_bound,
                         affine_codimension=codimension))

old_A, old_h, old_c = 139775, 272, 511
old_kernel = (J - 1 - old_c) // B + 1
assert old_h - (old_kernel + 1) == 15
assert old_h * B + old_c == old_A

assert 519 + B == 1031
assert 519 + 505 == 2 * B
assert 518 + 505 + 254 * B == J - 1
assert 518 + 272 * B == A
assert 6 + 273 * B == A

counts = {
    "incumbent": guarantee(511, 272, 14),
    "fixed_518_core_extra_denominator": guarantee(510, 272, 15),
    "273_packets_6_core": guarantee(511, 273, 15),
}
assert counts == {
    "incumbent": 4009245024241067461,
    "fixed_518_core_extra_denominator": 880067499,
    "273_packets_6_core": 1647305831,
}
assert counts["incumbent"] > target
assert counts["273_packets_6_core"] * 166_000_000 < target

receipt = {
    "status": "PASS: exact arithmetic; algebraic proof is in companion note",
    "field_prime": p,
    "packet_size": B,
    "code_dimension": J,
    "target_agreement": A,
    "required_distinct_labels": target,
    "denominator_degree_for_partial_rigidity": 1031,
    "common_top_band_including_leading": band,
    "common_nonleading_coefficients": band - 1,
    "arbitrary_core_max_partial_degree": A - 266 * B,
    "fixed_511_core_max_added_partial_degree": A - 511 - 265 * B,
    "profiles": profiles,
    "incumbent_affine_codimension": 15,
    "new_affine_codimension": 16,
    "generic_pigeonhole_guarantees": counts,
    "scope": "No upper bound on exceptional combinatorial fiber sizes; no improved certificate.",
}
path = Path(__file__).with_name("partial_packet_denominator_verified.json")
path.write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
