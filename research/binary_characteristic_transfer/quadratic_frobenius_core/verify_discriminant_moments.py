"""Bounded identity replay, not a search for constructions.

Check exact character moments and root-budget inequalities on small prime
fields, including degenerate differences and the removed zero fiber.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path
import json

rows = []
for p in (11, 17, 31, 47):
    def chi(x):
        v = pow(x % p, (p-1)//2, p)
        return -1 if v == p-1 else v

    for n in sorted({p-1, (p-1)//2}):
        D = [x for x in range(1, p) if pow(x, n, p) == 1]
        assert len(D) == n
        exponents = coefficients = moment_tests = 0
        for e in range(3, n):
            if gcd(e-1, n) != 1:
                continue
            exponents += 1
            L0, C0 = gcd(e-2, n)-1, gcd(e, n)-1
            B0 = gcd(gcd(e, e-2), n)-1
            values = []
            for t in D:
                if t == 1:
                    continue
                den = (pow(t, e-1, p)-1)**2 % p
                v = (4-4*pow(t, e-2, p)*(t-1)**2*pow(den, -1, p)) % p
                values.append(v)
            assert values.count(0) == L0+C0-B0
            counts = Counter(v for v in values if v)
            mp = sum(counts.values())
            energy = sum(c*c for c in counts.values())
            H = [sum(c*chi(beta-v) for v,c in counts.items()) for beta in range(p)]
            J = [chi(beta)*H[beta] for beta in range(p)]
            S2 = sum(x*x for x in J)
            assert sum(Hb*Hb for Hb in H) == p*energy-mp*mp
            assert sum(J) == -mp
            assert S2 == p*energy-mp*mp-H[0]*H[0]
            for threshold in range(1, n+1):
                upper = Fraction((p-1)*S2-mp*mp, S2+(p-1)*threshold**2+2*threshold*mp)
                assert sum(x >= threshold for x in J) <= upper
                moment_tests += 1
            for a,b,c in product((1,2,3), repeat=3):
                beta = b*b*pow(a*c, -1, p) % p
                A = sum((a*x*x+b*x+c-pow(x,e,p)) % p == 0 for x in D)
                assert A*(A-1) <= 2*(n-1)-L0-C0
                ds = sum(chi((b*b-4*a*c)*(pow(t,e-1,p)-1)**2
                             +4*a*c*pow(t,e-2,p)*(t-1)**2)
                         for t in D if t != 1)
                assert ds >= A*(A-2)-(n-1)+L0+C0
                if beta not in (0,4):
                    assert J[beta] >= A*(A-2)-(n-1)+B0+counts[beta]
                coefficients += 1
        rows.append(dict(p=p,n=n,exponents_checked=exponents,
                         coefficient_examples_checked=coefficients,
                         one_sided_thresholds_checked=moment_tests,passed=True))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
