"""Exhaustive moment-vector and exact-list checks for composite fibers."""
from pathlib import Path
from itertools import combinations
import json
import time
import sympy as sym
from verify_prime_fiber_rigidity import locator, require


def fixture(B,seed,S,C,padding):
    x=sym.Symbol('x')
    p=10**10+(1-10**10)%B
    while not (sym.isprime(p) and all(pow(a,(p-1)//B,p)==1 for a in seed)):
        p+=B
    fibers=[]
    for a in seed:
        factors=sym.factor_list(sym.Poly(x**B-a,x,modulus=p))[1]
        require(all(f.degree()==1 and v==1 for f,v in factors),'split simple roots')
        fibers.append(sorted(-int(f.all_coeffs()[1])%p for f,_ in factors))
    nodes=[x for fiber in fibers for x in fiber]+list(range(1,padding+1))
    require(len(nodes)==len(set(nodes)),'domain distinctness')
    powers=[[pow(x,j,p) for j in range(1,B)] for x in nodes]
    totals=[0]*(B-1);previous=0;zero_masks=[]
    for index in range(1<<len(nodes)):
        mask=index^(index>>1)
        if index:
            bit=mask^previous;position=bit.bit_length()-1
            direction=1 if mask&bit else -1
            row=powers[position]
            for j in range(B-1):
                totals[j]=(totals[j]+direction*row[j])%p
        if not any(totals):
            zero_masks.append(mask)
        previous=mask
    whole=[]
    for subset in range(1<<len(seed)):
        whole.append(sum(((1<<B)-1)<<(i*B) for i in range(len(seed)) if subset>>i&1))
    require(sorted(zero_masks)==sorted(whole),'zero moment vectors iff whole fibers')
    W=[0]*(2*B+1);W[0]=C%p;W[B]=-S%p;W[2*B]=1
    lists={}
    for K in (B,B+1):
        actual=[]
        for mask in zero_masks:
            if mask.bit_count()!=2*B:
                continue
            F=locator([v for i,v in enumerate(nodes) if mask>>i&1],p)
            Q=[(u-v)%p for u,v in zip(W,F)]
            if not any(Q[K:]):
                require(all(not c for j,c in enumerate(Q) if j%B),'composed candidate')
                actual.append(Q[:K])
        expected=[]
        for a,b in combinations(seed,2):
            if K==B and (a+b-S)%p:
                continue
            Q=[0]*K;Q[0]=(C-a*b)%p
            if K>B:
                Q[B]=(a+b-S)%p
            expected.append(Q)
        require(sorted(actual)==sorted(expected),'entire decoding list')
        lists[str(K)]=actual
    return dict(B=B,p=p,seed=seed,domain=nodes,padding=padding,
                subset_checks=1<<len(nodes),zero_moment_subsets=len(zero_masks),
                agreement=2*B,exact_lists=lists)


def main():
    started=time.monotonic()
    c=3118905
    result=dict(status='PASS',fixtures=[
        fixture(4,[c+i for i in range(4)],2*c+3,c*c+3*c,2),
        fixture(6,[5,7,11],12,0,2)],
        scope='Exhaustive subset moment vectors and complete lists at K=B and K=B+1; infinitude and Kummer independence use the proof.')
    result['seconds']=time.monotonic()-started
    Path(__file__).with_name('composite_fiber_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({**result,'fixtures':[{k:v for k,v in row.items() if k not in {'domain','exact_lists'}} |
          {'exact_list_sizes':{k:len(v) for k,v in row['exact_lists'].items()}} for row in result['fixtures']]},indent=2))


if __name__=='__main__':
    main()
