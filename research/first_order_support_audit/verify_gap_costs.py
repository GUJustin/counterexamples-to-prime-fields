"""Exact corroborating checks for the quarter-rate proof-ledger converse."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from verify import rank_formula
from verify_smaller_certificates import diagonal_rank


def main():
    # Rational isolation of the positive root, with no floating arithmetic.
    lower=F(4687923417635740609,10**19)
    upper=lower+F(1,10**19)
    poly=lambda a:31*a*a-6*a-4
    assert poly(lower)<0<poly(upper)
    assert upper+F(1,2000)<F(47,100)
    cap=lambda a,w:2*a*a-F(1,2)+(1-a)*w/2-F(7,24)*w*w
    assert cap(F(47,100),F(1,4))==-F(2443,240000)
    # The two partial derivatives are positive throughout the rectangle.
    assert 4*lower-F(1,8)>0
    assert (1-F(47,100))/2-F(7,12)*F(1,4)>0
    checks=0
    for m in range(1,9):
        for H in product(range(5),repeat=4):
            S=[(u,b) for b,h in enumerate(H) for u in range(h)]
            if not S or max(u+b for u,b in S)>=2*m:continue
            R=rank_formula(H,m);s=len(S);U=max(u for u,b in S)
            assert 8*R>=m*s
            if 2*U<m:assert R>=(m-2*U)*s
            # Critical-threshold surplus is nonpositive, checked using
            # an upper rational approximation (stronger for these fixtures).
            assert sum(m*upper-F(u+b,4) for u,b in S)<=R
            checks+=1
    fixtures=[]
    for m in (2048,4096,8192):
        a=F(469,1000); columns=(F(455,1000)*m).__floor__()+1
        qmax=(4*m*a).__ceil__()-1
        R=s=0;benefit=F(0)
        for q in range(qmax+1):
            k=min(q+1,columns)
            R+=diagonal_rank(q,k,m);s+=k
            benefit+=k*(m*a-F(q,4))
        delta=benefit-R; assert delta>0
        U=qmax;V=columns-1
        epslo=a-upper;epshi=a-lower
        assert m*epslo>(1-2*lower)/8
        assert 4*U>m and 4*(V+1)>m and 8*V>=m
        assert 8*epslo*R>=delta
        ell=(qmax*R/delta).__floor__()
        rec=(qmax-V)*V*(V+1)+V*(V+1)*(2*V+1)//6
        assert ell+1>qmax*R/delta
        assert ell>m/(32*epslo)-1
        assert 3*rec>=V**3
        fixtures.append(dict(m=m,monomials=s,rank=R,surplus=str(delta),U=U,V=V,challenge_degree=ell,reconstruction_budget=rec))
    report=dict(status='passed',arbitrary_support_checks=checks,cap_corner=str(cap(F(47,100),F(1,4))),positive_fixtures=fixtures,scope='Exact corroboration of a leading-coefficient proof-ledger converse; no intrinsic list or MCA lower bound.')
    Path(__file__).with_name('gap_costs_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
