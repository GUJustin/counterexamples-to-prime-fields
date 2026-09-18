"""Exact ceiling on collisions generated inside opposite-pair sectors."""
import json
import math
from fractions import Fraction
from pathlib import Path


def ceiling(tags, points, weight):
    total = math.comb(points, weight)
    upper = total
    relaxed = 0
    terms = []
    max_h = min(tags // 2, weight // 2, (points - weight) // 2)
    for h in range(max_h + 1):
        contexts = math.comb(points - 4 * h, weight - 2 * h)
        choices_a = math.comb(tags, h)
        relaxed += choices_a * math.comb(tags - h, h) * contexts
        if h < 5:
            continue
        # A fixed (h-4)-subset leaves four roots uniquely determined
        # by three moments and the product (Newton identities).
        choices_b_upper = math.comb(tags - h, h - 4) // math.comb(h, 4)
        term = choices_a * choices_b_upper * contexts
        upper += term
        terms.append((term, h))
    return {
        "supports": total,
        "collision_upper": upper,
        "relaxed_pairs": relaxed,
        "max_h": max_h,
        "largest_upper_term_h": max(terms)[1],
        "average_collision_upper": float(Fraction(upper, total)),
    }


punctured = ceiling(127, 255, 136)
full = ceiling(128, 256, 136)
target = 274980728111395088
N = punctured["supports"]
sufficient_collision_target = N * (target - 1) + 1
rotations = math.gcd(136, 256)
rotated_upper = rotations * full["collision_upper"]
assert rotations == 8
assert 496 * punctured["collision_upper"] < sufficient_collision_target
assert 250 * rotated_upper < 13 * sufficient_collision_target
result = {
    "scope": "Upper bounds on a class of certified ordered collisions; not a global fiber upper bound",
    "prime": 2130706433,
    "target_fiber": target,
    "punctured": punctured,
    "full_domain_relaxation": full,
    "sufficient_collision_target": sufficient_collision_target,
    "punctured_upper_over_target": float(Fraction(punctured["collision_upper"], sufficient_collision_target)),
    "product_stabilizing_rotations": rotations,
    "with_rotations_collision_upper": rotated_upper,
    "with_rotations_average_upper": float(Fraction(rotated_upper, N)),
    "with_rotations_upper_over_target": float(Fraction(rotated_upper, sufficient_collision_target)),
    "exact_checks": ["496 E_punctured < N(target-1)+1", "250 (8 E_full) < 13 (N(target-1)+1)"],
}
Path(__file__).with_name("verified.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: result[k] for k in ["punctured_upper_over_target", "with_rotations_average_upper", "with_rotations_upper_over_target", "exact_checks"]}, indent=2))
