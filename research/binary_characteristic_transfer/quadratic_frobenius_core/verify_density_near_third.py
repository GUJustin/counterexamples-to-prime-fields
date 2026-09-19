#!/usr/bin/env python3
"""Exact finite arithmetic for the near-third density family.
The existence and all-prime proof are analytic, not an enumerated domain.
"""
from fractions import Fraction as F
from math import isqrt, factorial
from pathlib import Path
import json

def check(p):
    r=isqrt(p-1)+1
    n=8*p*(p-r)//3
    N=2*(p*p-1)
    m=n-N
    T=isqrt(2*n-1)
    A=2*p
    ell=T-A+2
    gamma=F(m,N)-F(ell-1,2*p-2)
    assert r*r>=p and (r-1)**2<p
    assert F(r,p)<F(1,60)
    assert 0<m<N and m>=2*p+3
    assert F(3*n,2)<(2*p-r)**2 and 2*p-r>0
    assert F(3*n,8)<p*p<=r**4
    assert T*T<2*n<=(T+1)**2 and T>A
    assert F(m,N)>=F(1,3)-F(4*r,3*p)>F(14,45)
    assert F(ell-1,2*p-2)<F(p+3,6*p-6)<=F(7,40)
    assert gamma>F(49,360)>F(1,8)
    assert 4*(p-1)*gamma**2>F(p-1,16)
    return dict(p=p,r=r,n=n,m=m,T=T,A=A,B=(p+1)*(p*p-1),
                gamma=str(gamma),loss_ratio=str(F(T-A,T-3)),
                johnson_squared_slack=2*n-T*T)

# Validate rounding over a finite interval; the proof covers all p>=4099.
for p in range(4099,100001):
    check(p)
# Old exact exponential-onset certificate also suffices here.
assert 257*258<F(16**6,factorial(6))+F(16**7,factorial(7))
assert F(2,257)-F(1,16)<0
receipt=dict(status="PASS",scope="Integer/rational arithmetic; no finite-field or puncture enumeration",
             integer_rounding_interval=[4099,100000],
             cases=[check(p) for p in [4099,2013265921,2147483647,18446744069414584321]],
             asymptotic_loss="1-sqrt(3)/2",
             limitations=["Alphabet F_(p^4)","Selected domain of order p^2", "Dimension three"])
Path(__file__).with_suffix('.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
