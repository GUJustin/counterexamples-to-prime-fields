#!/usr/bin/env python3
"""Exact threshold feasibility, without allocating length-n polynomial arrays."""
import json
from fractions import Fraction
from math import ceil, comb
from pathlib import Path


def dimensions(t, r, m):
    N = comb(m+t-1, t-1)
    J = comb(m+t-3, t-3)
    M = N-J
    alpha = Fraction((t-1)*J*m, M)
    beta = Fraction((t*r-1)*(M-1), 2)
    assert alpha == Fraction(4, m+3) if t == 3 else alpha == Fraction(18, m+5)
    return N, J, M, alpha, beta


def run():
    rows = []
    for r in (1, 2, 4):
        for a in (Fraction(2, 5), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
            b = a/3
            m3 = max(1, ceil(128/b**3-3))
            m4 = max(1, ceil(1152/a**4-5))
            N3, J3, M3, alpha3, beta3 = dimensions(3, r, m3)
            N4, J4, M4, alpha4, beta4 = dimensions(4, r, m4)
            emin = max(comb(N3-1, 2)*(3*r-1), comb(N4-1, 2)*(4*r-1))+1
            nmin = ceil(max(32*(beta3+3*r)/b**3,
                            64*(beta4+4*r)/a**4, 6*(r+1)/a, 3/a))
            e = max(emin, ceil(Fraction(nmin, 4*r)))
            D = r*e
            n = 4*D
            A = ceil(a*n)
            B = A//2
            assert D<A<=n and B>=b*n
            assert alpha3*D+beta3+3*r <= b**3*n/16
            assert alpha4*D+beta4+4*r <= a**4*n/32
            assert Fraction(n, B-r) <= 2/b
            T = n*(n-1)//((A-r)*(A-r-B+1))
            assert T <= 8/a**2
            assert A-r-1>0
            C3 = sum(comb((j+1)*r-1, r) for j in range(1, 3))
            C4 = sum(comb((j+1)*r-1, r) for j in range(1, 4))
            L0 = max(ceil(4/b), ceil(32*C3/b**4))
            L1 = max(ceil(6/a), ceil(256*C4/a**6))
            bound = L0*n+L0*(r+comb(n, 2)//(A-r-1))+L1+n
            assert bound <= L0*n+L0*(r+n/a)+L1+n
            rows.append({"r": r, "agreement_fraction": str(a), "rate": "1/4",
                         "m3": m3, "m4": m4, "e": e, "n": n, "A": A,
                         "characteristic_must_exceed": D*max(m3, m4),
                         "nonzero_family_plus_zero_label_bound": bound,
                         "bound_over_n": str(Fraction(bound, n))})
    result = {"status": "PASS", "fixtures": len(rows), "rows": rows,
              "scope": "Exact arithmetic feasibility only. No length-n polynomials or received lines are enumerated; the constants are not practically competitive."}
    Path(__file__).with_name("parameters_verification.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k != "rows"}, indent=2))


if __name__ == "__main__":
    run()
