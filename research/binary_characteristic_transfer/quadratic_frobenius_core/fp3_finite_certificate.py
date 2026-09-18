"""Exact finite first-order certificate for the Fp^3 CA-only family."""
import json
from math import isqrt
from pathlib import Path


def certificate(p):
    root = isqrt(16*p)
    ceiling = root + (root*root < 16*p)
    N, A = 2*p*p-p-1, 2*p-ceiling-2
    B, H = 3*A, 120*A
    G, R = 4*B*B-2*B, 62
    conservative = (H-B+1)*G-(H+1)*N*R
    assert A*A < 2*N
    assert A > p + 2*isqrt(p) + 4  # stronger integer check below
    assert (A-p-2)**2 > 4*p
    assert 5*B >= 29*p
    assert 39*G > 40*N*R
    assert conservative > 0
    return dict(p=p, N=N, K=3, A=A, B=B, H=H, G=G, R=R,
                conservative_margin=conservative, below_exact_Johnson=True,
                characteristic_guard=p>3)


if __name__ == '__main__':
    rows = [certificate(p) for p in (4099, 8191, 65537, 2130706433)]
    # The final prime is only an arithmetic check, NOT the fixed benchmark.
    Path(__file__).with_suffix('.json').write_text(json.dumps(rows, indent=2)+'\n')
    print(json.dumps(rows, indent=2))
