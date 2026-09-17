"""Exact subset-sum and complete-list fixtures for prime-degree lifts."""
from pathlib import Path
from itertools import combinations
import json
import sympy as s

BASE=Path(__file__).resolve().parent
qs=[3,5,7,11,13]
x=s.Symbol('x')
def require(ok,message):
    if not ok:raise AssertionError(message)
def locator(nodes,p):
    out=[1]
    for a in nodes:
        nxt=[0]*(len(out)+1)
        for j,c in enumerate(out):nxt[j]=(nxt[j]-a*c)%p;nxt[j+1]=(nxt[j+1]+c)%p
        out=nxt
    return out

def fixture(B):
    m=len(qs);n=m*B;signatures=(2**B-1)**m
    start=100*signatures**2
    p=start+(1-start)%B
    attempts=0
    while True:
        while not (s.isprime(p) and all(pow(q,(p-1)//B,p)==1 for q in qs)):
            p+=B
        fibers=[]
        for q in qs:
            factors=s.factor_list(s.Poly(x**B-q,x,modulus=p))[1]
            require(all(f.degree()==1 and multiplicity==1 for f,multiplicity in factors),'complete splitting')
            fibers.append(sorted(-int(f.all_coeffs()[1])*pow(int(f.all_coeffs()[0]),-1,p)%p for f,_ in factors))
        nodes=[a for fiber in fibers for a in fiber]
        require(len(set(nodes))==n,'distinct domain')
        seen={};total=0;previous=0;zero_masks=[];collision=False
        for index in range(1<<n):
            mask=index^(index>>1)
            if index:
                change=mask^previous;j=change.bit_length()-1
                total=(total+(nodes[j] if mask&change else -nodes[j]))%p
            signature=[]
            for i in range(m):
                part=(mask>>(i*B))&((1<<B)-1)
                signature.append(0 if part in (0,(1<<B)-1) else part)
            signature=tuple(signature)
            if total in seen and seen[total]!=signature:
                collision=True;break
            seen[total]=signature
            if total==0:zero_masks.append(mask)
            previous=mask
        attempts+=1
        if not collision:break
        p+=B
        require(attempts<20,'fixture search budget')
    require(len(seen)==signatures,'all partial-fiber signatures distinct')
    require(len(zero_masks)==2**m,'only full-fiber zero sums')
    W=[0]*(2*B+1);W[2*B]=1;W[B]=-16%p
    candidates=[]
    for chosen in combinations(range(n),2*B):
        # Every candidate locator must have its first root moment zero.
        if sum(nodes[j] for j in chosen)%p:continue
        F=locator([nodes[j] for j in chosen],p)
        P=[(a-b)%p for a,b in zip(W,F)]
        if any(P[B:]):continue
        candidates.append(P[:B])
    require(sorted(candidates)==sorted([[(-39)%p]+[0]*(B-1),[(-55)%p]+[0]*(B-1)]),'exact composed list')
    return dict(B=B,p=p,n=n,k=B,agreement=2*B,seed_primes=qs,fibers=fibers,
                subset_checks=2**n,distinct_partial_signatures=len(seen),
                zero_sum_subsets=len(zero_masks),exact_list=candidates,split_primes_tried=attempts)

if __name__=='__main__':
    result=dict(status='PASS',fixtures=[fixture(2),fixture(3)])
    (BASE/'prime_fiber_rigidity_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
