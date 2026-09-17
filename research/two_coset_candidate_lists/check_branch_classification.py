"""Exact coefficient classification of every radical sign branch for r<=8."""
from collections import Counter,defaultdict
from itertools import product
from math import comb,isqrt
from pathlib import Path
import json
BASE=Path(__file__).resolve().parent


def prime(p):return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def generator(p):
    return next(g for g in range(2,p) if len({pow(g,i,p) for i in range(p-1)})==p-1)

def multiply(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return c


def main():
    rows=[];patterns=0
    for r in range(2,9):
        k=next(k for k in range(10,100) if prime(2*r*k+1));p=2*r*k+1
        omega=pow(generator(p),(p-1)//r,p)
        for j in range(r):
            counts=Counter()
            for sigma in product((-1,1),repeat=r):
                patterns+=1
                lower=[sum(sigma[a]*pow(omega,a*(ell-j),p) for a in range(r))%p for ell in range(j)]
                if not any(lower):counts[sum(sigma)*pow(r,-1,p)%p]+=1
            assert max(counts.values(),default=0)<=comb(r,r//2)
            if (r,j)==(4,1):assert max(counts.values())==2
            for b in range(1,r):
                terms=[]
                for a in range(r):
                    mask=(1<<a)^(1<<((a+b)%r))
                    if j==0:
                        coeff=[1]
                        for aa in range(r):
                            if aa!=a:coeff=multiply(coeff,[1,pow(omega,aa,p)],p)
                    else:
                        coeff=[comb(j-1,t)*pow(omega,a*(t-j),p)%p for t in range(j)]
                    terms.append((mask,coeff))
                constants=0
                for sigma in product((-1,1),repeat=r):
                    patterns+=1
                    grouped=defaultdict(lambda:[0]*r)
                    for s,(mask,coeff) in zip(sigma,terms):
                        for t,x in enumerate(coeff):grouped[mask][t]=(grouped[mask][t]+s*x)%p
                    if not any(any(v) for v in grouped.values()):constants+=1
                expected=2**(r//2) if r%2==0 and b==r//2 and j==1 else 0
                assert constants==expected,(r,j,b,constants,expected)
            rows.append(dict(r=r,j=j,p=p,constant_value_multiplicities=dict(counts),order_two_constant_signs=2**(r//2) if r%2==0 and j==1 else 0))
    out=dict(status='passed',rows=rows,sign_patterns_checked=patterns,
             scope='Exact coefficient cancellation in square-class character spaces for every section and Frobenius class at r2 through8. Universal classification follows from the written square-class proof.')
    (BASE/'branch_classification_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='passed',rows=len(rows),sign_patterns_checked=patterns)))

if __name__=='__main__':main()
