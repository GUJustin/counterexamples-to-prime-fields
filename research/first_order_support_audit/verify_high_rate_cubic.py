"""Symbolic identities and rational root isolation for the high-rate curve."""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as s


def main():
    p,B,x,r,a=s.symbols('p B x r a')
    delta=1-p;rho=(1+p*p)/2;agr=(1+p)/2+delta**2*B/2;c=agr/rho-1
    total=(agr*agr/(2*rho)-s.Rational(1,2))*B+(1-agr)*B*B/2-(2-rho)*B**3/6+rho*(B-c)**3/(6*(2*rho-1))
    Q=x**3-3*delta*x+delta**2*(1+p)*(2-p)/(1+p*p)
    den=(1+p*p)*x-delta**2;bstar=p*delta/den
    assert s.factor(total.subs(B,bstar)+p*delta**3*(1+p*p)*Q/(12*den**3))==0
    half=(1-p*p)/(1+p*p)
    assert s.factor(Q.subs(x,half)+p*p*(1-p)**2*(1+p)**2*(p*p+3)/(1+p*p)**3)==0
    Fpoly=(8-r)*a*a-6*r*a+r*(4*r-5)
    T=r*(7-2*r)/(4+r)
    assert s.factor(Fpoly.subs(a,T)+4*r*(r-2)*(r-1)*(r*r-16*r+10)/(r+4)**2)==0
    records=[]
    for pp in (F(3,5),F(2,3),F(4,5),F(9,10),F(99,100),F(999,1000)):
        dd=1-pp;rr=(1+pp*pp)/2
        assert rr*rr-16*rr+10<0
        q=lambda xx:xx**3-3*dd*xx+dd*dd*(1+pp)*(2-pp)/(1+pp*pp)
        lo=(1-pp*pp)/(1+pp*pp);hi=F(2)
        assert q(lo)<0<q(hi)
        for _ in range(100):
            mid=(lo+hi)/2
            if q(mid)<0:lo=mid
            else:hi=mid
        def params(xx):
            BB=pp*dd/((1+pp*pp)*xx-dd*dd)
            aa=(1+pp)/2+dd*dd*BB/2
            cc=aa/rr-1;d=(aa-rr)/(1-rr)
            val=(aa*aa/(2*rr)-F(1,2))*BB+(1-aa)*BB*BB/2-(2-rr)*BB**3/6+rr*(BB-cc)**3/(6*(2*rr-1))
            assert 0<cc<BB<d<F(1,2)
            assert rr<aa and aa*aa<rr
            assert (8-rr)*aa*aa-6*rr*aa+rr*(4*rr-5)<0
            return aa,BB,val
        upper= params(lo);lower=params(hi)
        assert upper[2]>0>lower[2]
        assert lower[0]<upper[0] and upper[0]-lower[0]<F(1,10**28)
        records.append(dict(rate=str(rr),agreement_lower=str(lower[0]),agreement_upper=str(upper[0]),agreement_display=float((lower[0]+upper[0])/2),width_display=float((lower[1]+upper[1])/2)))
    out=dict(status='passed',symbolic_identities=3,rational_root_isolations=records,scope='Exact algebra and branch-admissible rational isolation; the proof establishes the global continuum threshold, not finite-multiplicity optimality at high rates.')
    Path(__file__).with_name('high_rate_cubic_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='passed',symbolic_identities=3,root_intervals=len(records),display=[{k:v for k,v in x.items() if 'display' in k or k=='rate'} for x in records]),indent=2))

if __name__=='__main__':main()
