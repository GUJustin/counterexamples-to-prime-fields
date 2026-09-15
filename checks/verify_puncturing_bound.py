"""Exact coding-theory checks for the puncturing bound and its sharp endpoint."""
from itertools import combinations
from math import comb
from fractions import Fraction
from pathlib import Path
import json

identities=0
for n in range(4,101):
    for k in range(1,n-1):
        a=n-k
        for r in range((a+1)//2,a):
            s,d=a-r,2*r-a
            h=d+1
            assert n-d-k==2*s and n-d-s==n-r
            left=Fraction((n-d)*comb(n,d),comb(r,d))
            right=Fraction(s*comb(n,h),comb(r,h))
            assert left==right
            if d==0:
                assert left==n
            if r==a-1:
                assert left==comb(n,k+1)
            identities+=1

# Audit support extension, including errors of weight below the radius.
support_cases=0
for n in range(4,10):
    for r in range(1,n):
        for d in range(r):
            R=set(range(r))
            for weight in range(r+1):
                for E_tuple in combinations(range(r),weight):
                    E=set(E_tuple)
                    successes=sum(len(E-set(T))<=r-d for T in combinations(R,d))
                    assert successes==comb(r,d)
                    support_cases+=1

def affine_candidates(domain,word,p):
    candidates=set()
    for i,j in combinations(range(len(domain)),2):
        slope=(word[j]-word[i])*pow((domain[j]-domain[i])%p,-1,p)%p
        intercept=(word[i]-slope*domain[i])%p
        candidates.add((intercept,slope))
    return candidates

endpoints=[]
for n in range(4,9):
    p=257
    domain=[2**i for i in range(n)]
    direction=[-x*x%p for x in domain]
    assert max(sum((b+c*x)%p==y for x,y in zip(domain,direction))
               for b,c in affine_candidates(domain,direction,p))==2
    expected={sum(A)%p for A in combinations(domain,3)}
    assert len(expected)==comb(n,3)
    nearby=set()
    for z in range(p):
        word=[(x**3-z*x*x)%p for x in domain]
        witnesses=[(b,c) for b,c in affine_candidates(domain,word,p)
                   if sum((b+c*x)%p==y for x,y in zip(domain,word))>=3]
        if witnesses:
            assert len(witnesses)==1
            nearby.add(z)
    assert nearby==expected
    endpoints.append(dict(n=n,k=2,p=p,r=n-3,nearby_parameters=len(nearby),
                          upper_bound=comb(n,3),maximum_direction_agreement=2))

result=dict(status='passed',parameter_identities=identities,support_extension_cases=support_cases,
            exact_endpoint_lines=endpoints,
            scope='Finite arithmetic and exact affine-line enumeration; the general bound uses the cited unique-radius theorem.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
