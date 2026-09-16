"""Rational logarithm, entropy and Stirling intervals for M31 searches."""
from fractions import Fraction as F
from functools import lru_cache
p=2**31-1
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(c,a):return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def div(a,b):
    assert b[0]>0
    vv=[x/y for x in a for y in b]
    return min(vv),max(vv)
def series(x,N=30):
    z=(x-1)/(x+1);v=z;s=F(0);z2=z*z
    for j in range(N):s+=2*v/(2*j+1);v*=z2
    tail=2*abs(v)/((2*N+1)*(1-z2))
    return s-tail,s+tail
ln2=series(F(2))
@lru_cache(None)
def ln(x):
    assert x>0
    e=x.numerator.bit_length()-x.denominator.bit_length();y=x/F(2)**e
    if y<1:y*=2;e-=1
    assert 1<=y<2
    return add(series(y),mul(e,ln2))
@lru_cache(None)
def entropy(t):return add(mul(-t,ln(t)),mul(t-1,ln(1-t)))
lp=ln(F(p));lpm=ln(F(p-1))
@lru_cache(None)
def raw_upper(m,h,r):
    t=F(h,m)
    v=add(mul(m,entropy(t)),mul(F(-1,2),ln(6*m*t*(1-t))))
    v=add(v,(F(1,12*m),F(1,12*m)))
    v=add(add(v,ln(t)),mul(-1,ln(F(m))))
    return div(add(v,mul(-2*r,lp)),ln2)[1]
def elias(rho,eta):
    t=1-rho-eta
    return add(add(mul(1-rho,lp),mul(-t,lpm)),mul(-1,entropy(t)))
