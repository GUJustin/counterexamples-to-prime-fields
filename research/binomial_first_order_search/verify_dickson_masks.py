"""Exact replay of the r=2 character branches and orbit decomposition."""
from math import comb
from fractions import Fraction as F
from pathlib import Path
import json


def main():
    fixtures=[]
    for p in (17,41,73,89,97,113,137,257):
        k=(p-1)//4
        chi=lambda x:0 if x%p==0 else (1 if pow(x%p,(p-1)//2,p)==1 else -1)
        coeff=[comb(2*k+1,2*j+1)%p for j in range(k+1)]
        def G(x):
            out=0
            for c in reversed(coeff):out=(out*x+c)%p
            return out
        H=[h for h in range(1,p) if pow(h,k,p)==1]
        todo=set(range(1,p));cosets=[]
        while todo:
            h=min(todo);C={h*t%p for t in H};cosets.append(C);todo-=C
        residual=0;mask_total=0
        for C in cosets:
            fibers={}
            for x in C:
                value=G(x);constant=False
                if chi(x)==1:
                    t=next(t for t in range(1,p) if t*t%p==x)
                    cp,cm=chi(1+t),chi(1-t)
                    if cp==cm and cp:
                        assert value==cp%p;constant=True
                    elif cp*cm==-1:
                        assert value*value*x%p==1
                else:
                    if chi(1-x)==1:
                        assert value==0;constant=True
                    else:assert value*value*x%p==(1-x)%p
                if constant:mask_total+=1
                else:
                    fibers.setdefault(value,[]).append(x);residual+=1
            assert all(len(xs)<=9 for xs in fibers.values())
        for a in range(1,2*k+1):
            h=pow(a,-2,p);scale=pow(a,2*k,p)
            assert pow(h,k,p)==scale
            for x in range(1,p):
                direct=sum(coeff[j]*pow(a,2*k-2*j,p)*pow(x,j,p) for j in range(k))%p
                assert direct==(scale*G(h*x%p)-pow(x,k,p))%p
        fixtures.append(dict(p=p,k=k,constant_mask_points=mask_total,residual_points=residual,orbit_candidates=2*k))
    assert F(504,1400)+F(37,2**21)<F(3,8)
    assert 1400**2<2**21
    # a0>15/32: evaluate its increasing defining polynomial there.
    a=F(15,32);assert 31*a*a-6*a-4<0
    out=dict(status='passed',fixtures=fixtures,scope='Exact branch and orbit identities plus numerical constant checks. Fourier estimates rely on the stated character-sum argument, not on finite sampling.')
    Path(__file__).with_name('dickson_masks_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
