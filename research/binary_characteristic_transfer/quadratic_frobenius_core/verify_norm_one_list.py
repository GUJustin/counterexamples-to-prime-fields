"""Exact arithmetic replay for the matched norm-one list comparison.

These checks verify finite certificate arithmetic, not the symbolic theorem.
See NORM_ONE_DIRECT_LIST_AUDIT.md for the splitting and uniformity proofs.
"""
from fractions import Fraction
import json
from pathlib import Path

rows = []
for p in (53, 4099, 8191, 65537):
    N = 2 * (p*p + p + 1)
    T = (19*p+9)//10
    B, M = 3*T, 3
    H, G, R = 40*B, 4*B*B - 2*B, 62
    surplus = (H-B+1)*G - (H+1)*N*R
    lam = Fraction(N-2, T-2)
    upper = lam*(7*B-12) + 5*B-9
    assert upper == 21*N + 30*lam + 15*T - 51
    assert upper <= 22*N and surplus > 0 and p > 3
    assert T*T < 2*N and 10*B >= 57*p
    assert 39*G - 40*N*R >= Fraction(2711,25)*p*p-5428*p-4960 > 0
    A = 2*p+2
    assert Fraction(N*(A-2), A*A-2*N) == N//2
    rows.append(dict(p=p, N=N, T=T, B=B, list_lower=N//2,
                     upper_numerator=upper.numerator,
                     upper_denominator=upper.denominator,
                     upper_floor=upper.numerator//upper.denominator,
                     uniform_22N=22*N, graded_surplus=surplus))
out = Path(__file__).with_name('norm_one_list_counting_receipt.json')
out.write_text(json.dumps(rows, indent=2)+'\n')
print(json.dumps(rows, indent=2))
