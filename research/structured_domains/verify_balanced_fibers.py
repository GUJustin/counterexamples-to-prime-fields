"""Exact small-field checks of balanced polynomial/rational fiber lemmas."""
from itertools import product
from collections import Counter
from pathlib import Path
import json


def primes(limit):
    return [p for p in range(3, limit+1)
            if all(p % d for d in range(2, int(p**.5)+1))]


def order(g,p):
    x=1
    for n in range(1,p):
        x=x*g%p
        if x==1:
            return n


def ev(poly,x,p):
    acc=0
    for a in reversed(poly):
        acc=(acc*x+a)%p
    return acc


def mul(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]=(out[i+j]+x*y)%p
    return out


def power(poly,j,p):
    out=[1]
    for _ in range(j):
        out=mul(out,poly,p)
    return out


counts=dict(normalized_polynomials=0,balanced_polynomials=0,
            boundary_degrees=0,rational_maps=0,scaled_pullbacks=0,
            extension_field_polynomials=0)
for p in primes(101):
    g=next(g for g in range(2,p) if order(g,p)==p-1)
    for n in range(1,p):
        if (p-1)%n:
            continue
        h=pow(g,(p-1)//n,p)
        D=sorted(pow(h,j,p) for j in range(n))
        for B in range(1,n+1):
            if n%B:
                continue
            if p<=19 and B<=4:
                for middle in product(range(p),repeat=B-1):
                    poly=[0]+list(middle)+[1]
                    hist=Counter(ev(poly,x,p) for x in D)
                    balanced=len(hist)==n//B and set(hist.values())=={B}
                    assert balanced == all(c==0 for c in middle)
                    counts['normalized_polynomials']+=1
                    counts['balanced_polynomials']+=balanced
            if B in {1,n}:
                for a in range(1,p):
                    hist=Counter((a*pow(x,B,p)+2)%p for x in D)
                    assert len(hist)==n//B and set(hist.values())=={B}
                    counts['boundary_degrees']+=1
        for d in range(1,n//2+1):
            if n%(2*d):
                continue
            M=n//d
            c=pow(h,d,p)  # Generator, hence nonsquare in even-order image.
            image={pow(x,d,p) for x in D}
            assert c in image and all(y*y%p!=c for y in image)
            B=2*d
            A=[c]+[0]*(2*d-1)+[1]
            C=[0]*d+[1]
            labels=[ev(A,x,p)*pow(ev(C,x,p),-1,p)%p for x in D]
            hist=Counter(labels)
            assert len(hist)==n//B and set(hist.values())=={B}
            counts['rational_maps']+=1
            for k in range(1,min(4,len(hist))+1):
                # Explicitly expand denominator-cleared polynomials and
                # compare with composed values at every domain coordinate.
                for coeffs in product(range(2),repeat=k):
                    out=[0]*(B*(k-1)+1)
                    for j,a in enumerate(coeffs):
                        term=mul(power(A,j,p),power(C,k-1-j,p),p)
                        for idx,b in enumerate(term):
                            out[idx]=(out[idx]+a*b)%p
                    for x,y in zip(D,labels):
                        assert ev(out,x,p)==pow(ev(C,x,p),k-1,p)*ev(coeffs,y,p)%p
                    counts['scaled_pullbacks']+=1

# Exercise the stronger characteristic hypothesis using F_4 and F_9.
# Encode a+b*z as a+p*b, with z^2+r1*z+r0=0.
for p,r0,r1 in [(2,1,1),(3,1,0)]:
    q=p*p
    def add(x,y):
        return ((x%p+y%p)%p)+p*((x//p+y//p)%p)
    def times(x,y):
        a,b=x%p,x//p
        c,d=y%p,y//p
        return (a*c-r0*b*d)%p+p*((a*d+b*c-r1*b*d)%p)
    def exp(x,j):
        out=1
        for _ in range(j):
            out=times(out,x)
        return out
    def evaluate(poly,x):
        out=0
        for a in reversed(poly):
            out=add(times(out,x),a)
        return out
    primitive=next(x for x in range(1,q)
                   if len({exp(x,j) for j in range(q-1)})==q-1)
    for n in range(1,q):
        if (q-1)%n or n<=p:
            continue
        h=exp(primitive,(q-1)//n)
        D=[exp(h,j) for j in range(n)]
        assert len(set(D))==n
        for B in range(1,min(n,4)+1):
            if n%B:
                continue
            for middle in product(range(q),repeat=B-1):
                poly=[0]+list(middle)+[1]
                hist=Counter(evaluate(poly,x) for x in D)
                balanced=len(hist)==n//B and set(hist.values())=={B}
                assert balanced==all(c==0 for c in middle)
                counts['extension_field_polynomials']+=1

assert {x:(x*x+x)%7 for x in [1,2,4,5]}=={1:2,2:6,4:6,5:2}
result=dict(status='all exact assertions passed',counts=counts,
            scope='coding theory; prime fields at most 101 and F_4,F_9')
Path(__file__).with_name('balanced_fiber_verification.json').write_text(
    json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
