"""Search the shared-zero class for the cyclic word on mu_(12r).

Enumerate zero subsets of size2r inside mu_(3r), modulo rotation, and
interpolate the residual degree<r polynomial on r nonzero-word nodes.
All candidates are first over a specified split prime; characteristic-zero
lifts are a separate verification step. No unrestricted list claim.
"""
from pathlib import Path
from itertools import combinations,islice
from math import comb
import argparse,json,time
import numpy as np
import sympy as s


def scan(r,batch):
    start=time.monotonic();k=3*r;n=12*r;A=4*r
    q=((1000000+n-1)//n)*n+1
    while not s.isprime(q):q+=n
    root=pow(int(s.primitive_root(q)),(q-1)//n,q)
    xs=np.array([pow(root,i,q) for i in range(n)],dtype=np.int64)
    word=np.array([(pow(int(x),k,q)-1)**2*pow(2,-1,q)%q for x in xs],dtype=np.int64)
    inv=np.array([0]+[pow(i,-1,q) for i in range(1,q)],dtype=np.int64)
    nonzero=np.array([i for i in range(n) if word[i]!=0],dtype=np.int64)
    assert len(nonzero)==9*r
    zpatterns=set()
    for S in combinations(range(k),2*r):
        zpatterns.add(min(tuple(sorted((i+t)%k for i in S)) for t in range(k)))
    allsupport=np.array(list(combinations(nonzero,r)),dtype=np.int64)
    bank={};total=0;best=0
    for pattern in sorted(zpatterns):
        Z=tuple(4*i for i in pattern)
        divisor=np.ones(n,dtype=np.int64)
        for i in Z:divisor=divisor*(xs-xs[i])%q
        quotient_word=word*inv[divisor]%q
        for offset in range(0,len(allsupport),batch):
            I=allsupport[offset:offset+batch];B=len(I)
            x=xs[I];y=quotient_word[I]
            den=np.ones((B,r),dtype=np.int64)
            for j in range(r):
                diff=(x-x[:,j,None])%q;diff[:,j]=1
                den=den*diff%q
            weights=y*inv[den]%q
            prod=np.ones((B,n),dtype=np.int64);acc=np.zeros((B,n),dtype=np.int64)
            for j in range(r):
                diff=(xs[None,:]-x[:,j,None])%q
                prod=prod*diff%q;acc=(acc+weights[:,j,None]*inv[diff])%q
            values=prod*acc%q
            values[np.arange(B)[:,None],I]=y
            values=values*divisor[None,:]%q
            agreements=(values==word[None,:]).sum(axis=1)
            best=max(best,int(agreements.max()))
            for row in np.flatnonzero(agreements>=A):
                # Normalize the full evaluation vector under x->root^4*x.
                v=tuple(int(t) for t in values[row])
                canonical=min(v[4*t:]+v[:4*t] for t in range(k))
                if canonical not in bank:
                    bank[canonical]=dict(zero_exponents=Z,determining_exponents=[int(t) for t in I[row]],
                                         finite_field_agreements=int(agreements[row]),
                                         finite_field_support=[int(t) for t in np.flatnonzero(values[row]==word)],
                                         finite_field_orbit_size=len({v[4*t:]+v[:4*t] for t in range(k)}))
            total+=B
    assert total==len(zpatterns)*comb(9*r,r)
    return dict(r=r,n=n,k=k,A=A,split_prime=q,primitive_nth_root=root,
                zero_pattern_orbits=len(zpatterns),residual_interpolations=total,
                finite_field_candidate_orbits=len(bank),finite_field_orbit_size_sum=sum(v['finite_field_orbit_size'] for v in bank.values()),
                maximum_seen_agreement=best,candidates=list(bank.values()),seconds=time.monotonic()-start,
                scope='Specified shared-zero class over the split prime only. Exact characteristic-zero lifting is separate; no full-list or growing-family conclusion.')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--r',nargs='+',type=int,default=[1,2,3,4]);ap.add_argument('--batch',type=int,default=2048)
    ap.add_argument('--output',default='research/cyclotomic_dickson_word/structured_search.json')
    args=ap.parse_args();out={'fixtures':[]}
    for r in args.r:
        row=scan(r,args.batch);out['fixtures'].append(row)
        Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:v for k,v in row.items() if k!='candidates'}),flush=True)


if __name__=='__main__':main()
