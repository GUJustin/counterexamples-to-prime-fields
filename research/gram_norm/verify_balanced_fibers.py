#!/usr/bin/env python3
"""Finite exact checks for balanced polynomial fibers and a rational escape."""
from collections import Counter
from itertools import product
import json
from pathlib import Path


def evaluate(c, x, p):
    y = 0
    for a in reversed(c):
        y = (y*x+a) % p
    return y


counts = dict(polynomials_checked=0, balanced_polynomials=0, domains=0)
for p in (5,7,11,13):
    for n in range(2,p):
        if (p-1) % n:
            continue
        D = [x for x in range(p) if pow(x,n,p)==1]
        assert len(D)==n
        counts['domains'] += 1
        for B in range(1,min(3,n)+1):
            if n % B:
                continue
            for low in product(range(p),repeat=B):
                for a in range(1,p):
                    c = low+(a,)
                    mult = Counter(evaluate(c,x,p) for x in D)
                    balanced = len(mult)==n//B and all(v==B for v in mult.values())
                    classified = all(c[i]==0 for i in range(1,B))
                    assert balanced == classified
                    counts['polynomials_checked'] += 1
                    counts['balanced_polynomials'] += balanced

p = 13
D = [x for x in range(p) if pow(x,6,p)==1]
U,V,H,W = [1,6,5,1],[-1,6,-5,1],[0,-1,0,2],[1,0,2,0,3]
fibers = {}
for x in D:
    den = evaluate(H,x,p)
    assert den != 0
    y = evaluate(U,x,p)*pow(den,-1,p)%p
    fibers.setdefault(y,[]).append(x)
assert fibers == {0:[1,3,4],1:[9,10,12]}
# Four simple critical points over the algebraic closure: factorization
# into quadratics x²±x+3, each discriminant 2, with no common root.
mul = [0]*5
for i,a in enumerate([3,1,1]):
    for j,b in enumerate([3,-1,1]):
        mul[i+j] = (mul[i+j]+3*a*b)%p
assert mul == W
assert (1-4*3)%p == 2
# The denominator has roots x=0 and x²=7. W is nonzero at either type.
assert W[0] != 0
assert (3*7**2+2*7+1)%p == 6

out = dict(status='all exact assertions passed', **counts,
           rational_example=dict(field=13,degree=3,domain=D,
                                 fibers=fibers,distinct_critical_points=4))
Path(__file__).with_name('balanced_fibers_verified.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
