"""Independent exact F_(p^2) replay of the fixed-gap quadratic MCA corollary."""
from math import comb, ceil
from fractions import Fraction
from pathlib import Path
import json
import random


class QuadraticField:
    def __init__(self, p):
        self.p=p
        self.d=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
        self.zero=(0,0)
        self.one=(1,0)
    def add(self,x,y):
        p=self.p
        return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def neg(self,x):
        return (-x[0]%self.p,-x[1]%self.p)
    def sub(self,x,y):
        return self.add(x,self.neg(y))
    def mul(self,x,y):
        p=self.p
        return ((x[0]*y[0]+self.d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def inv(self,x):
        p=self.p
        norm=(x[0]*x[0]-self.d*x[1]*x[1])%p
        assert norm
        z=pow(norm,-1,p)
        return (x[0]*z%p,-x[1]*z%p)
    def evaluate(self,coeff,x):
        y=self.zero
        for c in reversed(coeff):
            y=self.add(self.mul(y,x),(c,0))
        return y


def replay(p):
    F=QuadraticField(p)
    N=p-1; k=N//4; A=3*N//8; L=N//2; Q=p*p
    chi=lambda x: 0 if x%p==0 else (1 if pow(x%p,N//2,p)==1 else -1)
    old=list(range(1,p))
    word={x:((1+chi(x))//2-pow(x,k,p))%p for x in old}
    coeffs=[[comb(2*k+1,2*j+1)*pow(a,2*k-2*j,p)%p for j in range(k)] for a in range(1,L+1)]
    assert len(set(map(tuple,coeffs)))==L
    supports=[[x for x in old if F.evaluate(c,(x,0))==(word[x],0)] for c in coeffs]
    assert all(len(S)==A for S in supports)
    anchor=max(old,key=lambda x:sum(x in S for S in supports))
    selected=[c for c,S in zip(coeffs,supports) if anchor in S]
    assert len(selected)*N>=A*L
    quotients=[]
    for c in selected:
        # Synthetic division of P(X)-w(anchor) by X-anchor.
        q=[0]*(k-1)
        q[-1]=c[-1]
        for j in range(k-2,0,-1):
            q[j-1]=(c[j]+anchor*q[j])%p
        assert (c[0]-word[anchor]+anchor*q[0])%p==0
        quotients.append(q)
    old.remove(anchor)
    f_old={x:(word[x]-word[anchor])*pow(x-anchor,-1,p)%p for x in old}
    for q in quotients:
        assert sum(F.evaluate(q,(x,0))==(f_old[x],0) for x in old)==A-1
    universe=[(a,b) for b in range(p) for a in range(p)]
    for x in universe:
        if x!=F.zero:
            assert F.mul(x,F.inv(x))==F.one
    unused=[x for x in universe if not(x[1]==0 and x[0]!=0)]
    values={x:[F.evaluate(q,x) for q in quotients] for x in unused}
    pads=sorted(unused,key=lambda x:len(set(values[x])),reverse=True)[:N+1]
    bound=ceil(Fraction(Q*A*L,Q+3*A*L))
    rng=random.Random(p)
    witness={}
    for attempt in range(32):
        f_pad={x:universe[rng.randrange(Q)] for x in pads}
        witness={}
        for x in pads:
            for i,y in enumerate(values[x]):
                witness[F.sub(y,f_pad[x])]=(i,x)
        if len(witness)>=bound:
            break
    assert len(witness)>=bound>=ceil(Fraction(3*(2*N)**2,100))
    agreement_counts=[]
    for z,(i,x0) in witness.items():
        q=quotients[i]
        zeros=[x for x in old if F.evaluate(q,(x,0))==(f_old[x],0)]
        ones=[x for x in pads if F.evaluate(q,x)==F.add(f_pad[x],z)]
        assert x0 in ones and len(zeros)>=k and len(zeros)+len(ones)>=A
        # A degree<k direction polynomial matching g=0 on these >=k
        # distinct old points is zero, and cannot match g=1 on x0.
        agreement_counts.append(len(zeros)+len(ones))
    return dict(p=p,quadratic_nonresidue=F.d,n=2*N,k=k,A=A,
                source_list=L,anchor=anchor,anchored_candidates=len(quotients),
                padding_points=[list(x) for x in pads],
                padding_values=[list(f_pad[x]) for x in pads],
                exceptional_labels=[list(z) for z in sorted(witness)],
                exceptional_count=len(witness),compiler_bound=bound,
                claimed_quadratic_bound=ceil(Fraction(3*(2*N)**2,100)),
                minimum_witness_agreements=min(agreement_counts),
                inverse_checks=Q-1,translation_trials=attempt+1)


def main():
    fixtures=[replay(p) for p in (17,41)]
    result=dict(status='passed',fixtures=fixtures,
                scope='Exact finite-field replay and root-count exclusion of full-support direction witnesses. Does not assert ordinary CA failure or prime ambient fields.')
    Path(__file__).with_name('quadratic_extension_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='passed',fixtures=[{k:v for k,v in x.items() if k not in ('padding_points','padding_values','exceptional_labels')} for x in fixtures]),indent=2))


if __name__=='__main__':
    main()
