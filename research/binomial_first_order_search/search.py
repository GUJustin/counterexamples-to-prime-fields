"""Bounded exploratory search; no asymptotic or family-wide conclusion."""
from math import comb,sqrt
from pathlib import Path
import json,time
import numpy as np


def curve(r):
    if r>=11-3*sqrt(13):return (3*r+2*sqrt(r*(5-r)*(2-r)))/(8-r)
    t=sqrt(r/2);lo=0.;hi=1.
    for _ in range(60):
        u=(lo+hi)/2
        if u*u*(u+3)<t:lo=u
        else:hi=u
    return t*(1+(lo+hi)/2)


def main():
    reports=[];start=time.monotonic()
    for p in (17,41,73,89,97,113,137):
        n=p-1;L=n//2;xs=np.arange(1,p,dtype=np.int64);aa=np.arange(1,L+1,dtype=np.int64)
        powers=np.ones((p,L),dtype=np.int64)
        for i in range(1,p):powers[i]=powers[i-1]*aa%p
        for e in range(3,p,2):
            k=(e-1)//2
            values=np.zeros((L,n),dtype=np.int64)
            for j in reversed(range(k)):
                coeff=(comb(e,2*j+1)%p)*powers[e-2*j-1]%p
                values=(values*xs[None,:]+coeff[:,None])%p
            word=[];maxcounts=[]
            for u in range(n):
                hist=np.bincount(values[:,u],minlength=p)
                word.append(int(np.argmax(hist)));maxcounts.append(int(hist.max()))
            agreements=np.sum(values==np.array(word)[None,:],axis=1)
            a1=curve(k/n)
            reports.append(dict(p=p,n=n,k=k,e=e,L=L,first_order_curve_display=a1,modal_average_agreement=sum(maxcounts)/(L*n),minimum_agreement=int(agreements.min()),maximum_agreement=int(agreements.max()),above_curve_candidates=int(np.sum(agreements/n>a1)),modal_average_margin=sum(maxcounts)/(L*n)-a1,word=word,agreement_counts=agreements.tolist()))
    best=sorted(reports,key=lambda x:x['modal_average_margin'],reverse=True)[:20]
    hits=[r for r in reports if r['above_curve_candidates']>=3]
    out=dict(status='completed',configurations=len(reports),seconds=time.monotonic()-start,best_by_full_bank_average=best,at_least_three_above_curve=hits,all_configurations=reports,scope='Finite modal-word search over odd binomial exponents and seven primes. The modal average is maximal for the complete candidate bank, but this does not optimize subbanks, prove an asymptotic bound, or test other polynomial families.')
    Path(__file__).with_name('search.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(configurations=len(reports),seconds=out['seconds'],best=[{k:v for k,v in r.items() if k not in ('word','agreement_counts')} for r in best[:10]],hit_count=len(hits)),indent=2))

if __name__=='__main__':main()
