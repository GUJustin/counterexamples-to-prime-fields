"""Sample determining supports for the full RS list around the Dickson word.

Every discovered candidate is an exact witness. Failure to discover a
candidate is not a nonexistence proof; sampling uses a seeded PRNG.
"""
from pathlib import Path
from math import comb
import argparse,json,time
import numpy as np


def run(p,samples,batch):
    start=time.monotonic();N=p-1;k=N//4;A=3*N//8
    xs=np.arange(1,p,dtype=np.int64)
    word=np.array([((1+(1 if pow(int(x),N//2,p)==1 else -1))//2-pow(int(x),k,p))%p for x in xs],dtype=np.int64)
    inv=np.array([0]+[pow(x,-1,p) for x in range(1,p)],dtype=np.int64)
    rng=np.random.default_rng(20260917+p)
    bank={};maximum=k;hist={};processed=0
    for offset in range(0,samples,batch):
        B=min(batch,samples-offset)
        # Ordering independent continuous keys yields uniform subsets in
        # the ideal model. Actual keys come from the stated finite PRNG.
        supports=np.argsort(rng.random((B,N)),axis=1)[:,:k]
        x=xs[supports];y=word[supports]
        denom=np.ones((B,k),dtype=np.int64)
        for j in range(k):
            diff=(x-x[:,j,None])%p
            diff[:,j]=1
            denom=denom*diff%p
        assert np.all(denom)
        weights=y*inv[denom]%p
        product=np.ones((B,N),dtype=np.int64)
        total=np.zeros((B,N),dtype=np.int64)
        for j in range(k):
            diff=(xs[None,:]-x[:,j,None])%p
            product=product*diff%p
            total=(total+weights[:,j,None]*inv[diff])%p
        values=product*total%p
        values[np.arange(B)[:,None],supports]=y
        agreements=(values==word[None,:]).sum(axis=1)
        maximum=max(maximum,int(agreements.max()))
        for aa,count in zip(*np.unique(agreements,return_counts=True)):
            hist[str(int(aa))]=hist.get(str(int(aa)),0)+int(count)
        for row in np.flatnonzero(agreements>=A):
            v=tuple(int(z) for z in values[row])
            if v not in bank:
                bank[v]=dict(determining_coordinates=[int(z) for z in x[row]],agreements=int(agreements[row]),hits=0)
            bank[v]['hits']+=1
        processed+=B
    first=next(a for a in range(k,N+1) if 31*a*a-6*N*a-4*N*N>0)
    return dict(p=p,n=N,k=k,agreement_threshold=A,samples=processed,
                maximum_sampled_agreement=maximum,distinct_candidates=len(bank),
                sample_agreement_histogram=hist,first_order_threshold=first,
                fixed_candidate_uniform_support_hit_probability=dict(numerator=comb(first,k),denominator=comb(N,k)),
                candidates=list(bank.values()),seconds=time.monotonic()-start,
                scope='Exact discovered witnesses only. No completeness or nonexistence claim; hit probability applies to one fixed candidate under ideal independent uniform sampling, not as a theorem about this PRNG.')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,default=41)
    ap.add_argument('--samples',type=int,default=1000000);ap.add_argument('--batch',type=int,default=1024)
    ap.add_argument('--output',default='research/projective_dickson_search/sampled_lists.json')
    args=ap.parse_args();out=run(args.prime,args.samples,args.batch)
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='candidates'},indent=2))


if __name__=='__main__':main()
