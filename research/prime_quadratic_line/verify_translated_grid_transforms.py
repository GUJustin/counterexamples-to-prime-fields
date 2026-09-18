#!/usr/bin/env python3
"""Small exact ledger for TRANSLATED_GRID_RS_TRANSFORM_AUDIT.md."""
from fractions import Fraction
from pathlib import Path
import json

n, k, A, T, B, p = 1405, 3, 52, 53, 486, 10125000000029
d = T - A
ratio = Fraction(d, T-k)
assert ratio == Fraction(1, 50)
m = 64
composition = (m*n, m*(k-1)+1, m*A, m*T)
assert composition == (89920, 129, 3328, 3392)
composition_ratio = Fraction(m*d, composition[3]-composition[1])
assert composition_ratio == Fraction(64, 3263) < ratio
assert composition[3]**2 < (composition[1]-1)*composition[0]

s = n - 2*k
padding = (n+s, k+s, A+s, T+s)
assert s == 1399 and padding == (2804, 1402, 1451, 1452)
assert 2*padding[1] == padding[0]
assert Fraction(padding[3]-padding[2], padding[3]-padding[1]) == ratio
assert Fraction(padding[3], padding[0]) < Fraction(2, 3)
# a1(1/2)=(1+sqrt6)/5 > 2/3, using sqrt6 > 7/3.
assert Fraction(49, 9) < 6
block = A-k+1
blocks = (s+block-1)//block
assert block == 50 and blocks == 28

field = 7
old_domain = [1, 2, 3]
old_word = [pow(x, -1, field) for x in old_domain]
old_max = max(sum(value == c for value in old_word) for c in range(field))
new_domain = [0] + old_domain
new_word = [0, 1, 1, 1]
new_max = max(sum((a+b*x)%field == value for x, value in zip(new_domain,new_word))
              for a in range(field) for b in range(field))
assert old_max == 1 and new_max == 3 > old_max+1

receipt = {
    "status": "PASS: exact transform arithmetic and full F7 negative control",
    "seed": [n,k,A,T,B,p],
    "seed_loss_capacity_ratio": str(ratio),
    "composition_degree": m,
    "composition_n_k_A_T": composition,
    "composition_loss_capacity_ratio": str(composition_ratio),
    "ideal_half_rate_padding_roots": s,
    "ideal_half_rate_n_k_A_T": padding,
    "ideal_half_rate_loss_capacity_ratio": str(ratio),
    "half_rate_agreement_below_two_thirds": True,
    "DKT_half_rate_curve_above_two_thirds": True,
    "quadratic_extension_block_limit": block,
    "required_blocks_for_half_rate": blocks,
    "resulting_extension_degree": 2**blocks,
    "F7_root_padding_negative_control": {"old_max":old_max,"new_max":new_max},
    "scope": "No new construction or finite fixed-rate benchmark certificate.",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
