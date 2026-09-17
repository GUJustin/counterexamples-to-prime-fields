"""Independent rational integration of the restored high-rate shape."""
from fractions import Fraction as F
from pathlib import Path
import json
from verify import clip,integrate


def integrated_shape(r,a,B):
    L=a/r
    poly=[(F(0),F(0)),(L,F(0)),(L,B),(B,B)]
    poly=clip(poly,-(2*r-1),-F(1),2*a-1)
    branches=[(-r,F(0),a),(1-r,F(0),a-1),(F(1,2)-r,-F(1,2),a-F(1,2))]
    total=F(0)
    for h,s,c in branches:
        region=poly[:]
        for hh,ss,cc in branches:
            if (h,s,c)!=(hh,ss,cc):region=clip(region,hh-h,ss-s,cc-c)
        total+=integrate(region,h,s,c)
    return total


def column(r,a,s,R):
    cuts=sorted({s,R}|{t for t in (1-s,1+s) if s<t<R})
    out=F(0)
    for l,h in zip(cuts,cuts[1:]):
        mid=(l+h)/2
        branches=[(-r,a),(1-r,a-1),(F(1,2)-r,a-F(1,2)-s/2)]
        slope,intercept=min(branches,key=lambda bc:bc[0]*mid+bc[1])
        out+=slope*(h*h-l*l)/2+intercept*(h-l)
    return out


def main():
    parameters=[(F(i,20),(3*F(i,20)+1)/4) for i in range(11,20)]
    parameters += [(F(3,4),F(43049,50000)),(F(9,10),F(47389,50000))]
    integrals=dominance=0;positive=[]
    for r,a in parameters:
        assert r<a and a*a<r
        c=a/r-1;d=(a-r)/(1-r);h0=1-d;L=a/r
        assert 0<c<d<F(1,2)
        for i in range(1,21):
            B=d*F(i,20)
            expected=(a*a/(2*r)-F(1,2))*B+(1-a)*B*B/2-(2-r)*B**3/6+r*max(F(0),B-c)**3/(6*(2*r-1))
            assert integrated_shape(r,a,B)==expected
            integrals+=1
        for i in range(21):
            s=d*F(i,20);star=min(L,(2*a-1-s)/(2*r-1))
            assert h0<=star<=L and star>s
            for j in range(21):
                R=s+(L-s)*F(j,20)
                value=column(r,a,s,R)
                if R<h0:assert value<=0
                else:assert value<=column(r,a,s,star)
                dominance+=1
    for r,a,B in [(F(3,4),F(43049,50000),F(173,1000)),(F(9,10),F(47389,50000),F(49,500))]:
        value=integrated_shape(r,a,B);assert value>0
        positive.append(dict(rate=str(r),agreement=str(a),width=str(B),surplus=str(value)))
    out=dict(status='passed',rational_polygon_integrals=integrals,column_endpoint_comparisons=dominance,positive_examples=positive,scope='Corroborates restored optimal high-rate shape formula; quantified optimality follows from the compression and endpoint proof. No practical benchmark gain.')
    Path(__file__).with_name('high_rate_shape_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
