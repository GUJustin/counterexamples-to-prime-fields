"""Exact cyclotomic moment classes, compared with finite-field classes."""
from itertools import combinations
from collections import Counter
from math import comb
from pathlib import Path
from fractions import Fraction
import json
import time


def check(n,A,s,p=None):
    ell=next(d for d in range(2,n+1) if n%d==0)
    rem=n
    while rem%ell==0:
        rem//=ell
    assert rem==1
    phi=n-n//ell
    basis=[]
    for exponent in range(n):
        vector=[0]*phi
        if exponent<phi:
            vector[exponent]=1
        else:
            for j in range(ell-1):
                vector[exponent-phi+j*(n//ell)]=-1
        basis.append(vector)
    h=1
    while h<=s:
        h*=ell
    q=n//h
    d=1;exponents=[]
    while d<=s:
        R=s//d-s//(ell*d)
        exponents.append(Fraction((n//d)-(n//d)//ell,R))
        d*=ell
    E=max(exponents)
    assert E<=Fraction(2*n,s)
    if p:
        assert p**E.denominator>n**E.numerator
        root=next(x for x in range(2,p) if pow(x,n,p)==1 and pow(x,n//ell,p)!=1)
    classes=Counter();signatures={}
    for subset in combinations(range(n),A):
        moments=[]
        for j in range(1,s+1):
            vector=[0]*phi
            for r in subset:
                exponent=r*j%n
                for index,c in enumerate(basis[exponent]):
                    vector[index]+=c
            moments.extend(vector)
        key=tuple(moments) if p is None else tuple(
            sum(pow(root,r*j,p) for r in subset)%p for j in range(1,s+1))
        mask=sum(1<<r for r in subset)
        mixed=[];full=0
        for r in range(q):
            bits=sum(((mask>>(r+q*l))&1)<<l for l in range(h))
            if bits==(1<<h)-1:
                full+=1
            elif bits:
                mixed.append((r,bits))
        signature=(tuple(mixed),full)
        assert key not in signatures or signatures[key]==signature
        signatures[key]=signature;classes[key]+=1
    assert len(set(signatures.values()))==len(signatures)
    for key,size in classes.items():
        mixed,b=signatures[key]
        assert size==comb(q-len(mixed),b)
    return dict(n=n,A=A,s=s,q=q,h=h,p=p,transfer_exponent=str(E),subsets=comb(n,A),
                moment_classes=len(classes),maximum_list=max(classes.values()),
                central_binomial_upper=comb(q,q//2))


def finite_field(n,A,s,p):
    root=next(x for x in range(2,p) if pow(x,n,p)==1 and pow(x,n//2,p)!=1)
    nodes=[pow(root,r,p) for r in range(n)]
    powers=[[pow(x,j,p) for j in range(1,s+1)] for x in nodes]
    classes=Counter(tuple(sum(powers[r][j] for r in subset)%p for j in range(s))
                    for subset in combinations(range(n),A))
    return dict(p=p,root=root,maximum_list=max(classes.values()),
                zero_moment_list=classes[(0,)*s])


def main():
    start=time.monotonic()
    rows=[check(n,A,s) for n,A in ((8,4),(16,4),(16,8),(16,12),(9,4),(25,5))
          for s in range(1,min(A,8))]
    finite=[finite_field(16,8,1,p) for p in (17,97,113,1009,65537)]
    transfer=[check(8,4,1,65537),check(16,8,3,65537),check(16,8,7,1009)]
    assert max(row['maximum_list'] for row in finite)>comb(8,4)
    result=dict(status='PASS',characteristic_zero=rows,finite_characteristic=finite,
                exact_transfer_checks=transfer,
                seconds=time.monotonic()-start,
                scope='Complete moment-class enumerations; finite-characteristic examples test the necessity of the transfer qualification.')
    Path(__file__).with_name('power_two_boundary_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
