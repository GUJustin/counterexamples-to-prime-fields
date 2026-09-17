"""Exact search in the scalar/projective orbit of a Dickson candidate.

This enumerates PGL_2(F_p) and all nonzero scalar multiples via value
histograms, on the fixed full nonzero domain and its Dickson word.
It is not a search over all degree-<k candidates or over received words.
"""
from math import comb
from pathlib import Path
import argparse
import json
import time
import numpy as np


def search(p,affine_output=False):
    started=time.monotonic()
    assert p%8==1
    N=p-1; k=N//4; D=k-1; A=3*N//8
    xs=np.arange(1,p,dtype=np.int64)
    seed=[comb(2*k+1,2*j+1)%p for j in range(k)]
    vals=np.array([sum(c*pow(x,j,p) for j,c in enumerate(seed))%p for x in range(p)],dtype=np.int64)
    inv=np.array([0]+[pow(x,-1,p) for x in range(1,p)],dtype=np.int64)
    powers=np.array([pow(x,D,p) for x in range(p)],dtype=np.int64)
    word=np.array([((1+(1 if pow(int(x),N//2,p)==1 else -1))//2-pow(int(x),k,p))%p for x in xs],dtype=np.int64)
    bank={}; transformations=0; max_agreement=0; affine_survivors=0
    output_values=len(set(map(int,word)))

    def process(a,bs,c,d):
        nonlocal transformations,max_agreement,affine_survivors
        num=(a*xs[None,:]+bs[:,None])%p
        den=(c*xs+d)%p
        image=num*inv[den][None,:]%p
        candidate=vals[image]*powers[den][None,:]%p
        pole=(den==0)
        candidate[:,pole]=powers[num[:,pole]]*seed[-1]%p
        nz=candidate!=0
        ratios=word[None,:]*inv[candidate]%p
        rr=np.broadcast_to(np.arange(len(bs),dtype=np.int64)[:,None],candidate.shape)
        histogram=np.bincount((rr*p+ratios)[nz],minlength=len(bs)*p).reshape(len(bs),p)
        histogram+=((~nz)&(word[None,:]==0)).sum(axis=1)[:,None]
        histogram[:,0]=0  # scalar must be nonzero
        localmax=int(histogram.max())
        max_agreement=max(max_agreement,localmax)
        for row,scale in np.argwhere(histogram>=A):
            received=tuple(int(x) for x in candidate[row]*int(scale)%p)
            count=int(histogram[row,scale])
            assert sum(v==int(w) for v,w in zip(received,word))==count
            if received not in bank:
                bank[received]=dict(matrix=[int(a),int(bs[row]),int(c),int(d)],scale=int(scale),shift=0,agreements=count)
        if affine_output:
            fibers=np.bincount((rr*p+candidate).ravel(),minlength=len(bs)*p).reshape(len(bs),p)
            top=np.partition(fibers,p-output_values,axis=1)[:,-output_values:].sum(axis=1)
            for row in np.flatnonzero(top>=A):
                affine_survivors+=1
                scales=np.arange(1,p,dtype=np.int64)
                translated=(word[None,:]-scales[:,None]*candidate[row][None,:])%p
                ii=np.broadcast_to(np.arange(p-1,dtype=np.int64)[:,None],translated.shape)
                hh=np.bincount((ii*p+translated).ravel(),minlength=(p-1)*p).reshape(p-1,p)
                max_agreement=max(max_agreement,int(hh.max()))
                for si,shift in np.argwhere(hh>=A):
                    scale=int(scales[si]);shift=int(shift)
                    received=tuple(int(v) for v in (scale*candidate[row]+shift)%p)
                    count=int(hh[si,shift])
                    assert sum(v==int(w) for v,w in zip(received,word))==count
                    if received not in bank:
                        bank[received]=dict(matrix=[int(a),int(bs[row]),int(c),int(d)],scale=scale,shift=shift,agreements=count)
        transformations+=len(bs)

    all_b=np.arange(p,dtype=np.int64)
    for a in range(1,p):
        process(a,all_b,0,1)
    for d in range(p):
        for a in range(p):
            process(a,all_b[all_b!=(a*d)%p],1,d)
    assert transformations==p*(p*p-1)
    assert len(bank)>=N//2
    histogram={}
    for v in bank.values():
        key=str(v['agreements']);histogram[key]=histogram.get(key,0)+1
    first_order=sum(31*v['agreements']**2-6*N*v['agreements']-4*N*N>0 for v in bank.values())
    return dict(p=p,n=N,k=k,threshold=A,group_elements=transformations,
                distinct_candidates_at_threshold=len(bank),agreement_histogram=histogram,
                above_first_order=first_order,maximum_agreement=max_agreement,
                candidates=list(bank.values()),affine_output=affine_output,
                affine_survivors=affine_survivors,seconds=time.monotonic()-started)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--primes',nargs='+',type=int,default=[17,41,73])
    parser.add_argument('--output',default='research/projective_dickson_search/search.json')
    parser.add_argument('--affine-output',action='store_true')
    args=parser.parse_args()
    out={'scope':'Complete scalar/projective orbit of one seed on a fixed word, with all output translations if affine_output is true; not a complete RS list census.','fixtures':[]}
    for p in args.primes:
        result=search(p,args.affine_output)
        out['fixtures'].append(result)
        Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:v for k,v in result.items() if k!='candidates'}),flush=True)


if __name__=='__main__':
    main()
