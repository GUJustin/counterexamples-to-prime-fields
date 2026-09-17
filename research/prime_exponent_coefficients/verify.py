"""Exact half-rate list certificates and bounds on the exponent coefficient."""
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path
BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('line_certificate',BASE.parent/'logarithmic_length_lines/verify.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)

def floor_log2(q):
    e=q.numerator.bit_length()-q.denominator.bit_length()
    power=F(2**e) if e>=0 else F(1,2**(-e))
    return e if q>=power else e-1

def narrow_log2(q):
    # Compress only outward before evaluating logarithms, keeping all
    # arctanh computations small even for a 14,000-bit list exponent.
    e=floor_log2(q)
    mant=q/(F(2**e) if e>=0 else F(1,2**(-e)))
    scale=2**96
    num=(mant*scale).__floor__()
    lo,hi=F(num,scale),F(num+1,scale)
    assert 1<=lo<=mant<hi<=2
    l,_=h.log2_bounds(lo);_,u=h.log2_bounds(hi)
    return F(e)+l,F(e)+u

def digest_integer(n):
    return hashlib.sha256(n.to_bytes((n.bit_length()+7)//8,'big')).hexdigest()

def decimal_lower(q,digits=5):
    scale=10**digits;a=(q*scale).__floor__()
    assert F(a,scale)<q
    return f'{a//scale}.{a%scale:0{digits}d}'

def main():
    def atan_interval(x,terms=20):
        s=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
        adjacent=s+(-1)**terms*x**(2*terms+1)/F(2*terms+1)
        return min(s,adjacent),max(s,adjacent)
    a0,a1=atan_interval(F(1,5));b0,b1=atan_interval(F(1,239))
    # Machin's identity and alternating-series bounds verify the pi upper bound.
    assert 16*a1-4*b0<F(355,113)
    rows=[]
    for b,m in [(31,5),(61,9),(127,17),(521,56)]:
        p=h.lucas_lehmer(b)
        n=2*((b*m)//2);k=n//2;t=k+m
        assert 0<k<t<n<p
        assert p**m*t**t*(n-t)**(n-t)>n**n  # strict sufficient Elias condition
        L,variances,den=h.gram_bound(n,t,m)
        independently_written=[F(t*(n-t),n-1)*F(comb(n-1,j)*comb(n+j,j),
                                  (2*j+1)*comb(2*j,j)**2) for j in range(1,m+1)]
        assert variances==independently_written
        ratio=F(comb(n,t))/den
        lo,hi=narrow_log2(ratio)
        K=floor_log2(ratio)
        assert ratio>2**K and L>2**K
        c_lo=F(m,n)*lo;c_hi=F(m,n)*hi
        assert (c_lo*10**5).__floor__()==(c_hi*10**5).__floor__()
        rows.append(dict(prime_exponent=b,n=n,k=k,m=m,t=t,
                         strict_log2_list_lower_bound=K,
                         log2_list_decimal_lower=decimal_lower(lo),
                         strict_forced_c2_decimal_lower=decimal_lower(c_lo),
                         list_lower_bound_sha256=digest_integer(L),
                         concentration_denominator_numerator_sha256=digest_integer(den.numerator),
                         concentration_denominator_denominator_sha256=digest_integer(den.denominator),
                         strict_elias_check=True))
    out=dict(status='PASS',fixtures=rows,
             scope='Half-rate interval domains over prime fields. Exact Gram smoothed-ellipsoid certificates, rational outward logarithm bounds, Lucas-Lehmer primality and integer Elias checks. Forced c2 comparisons assume c1=1. No optimality claim and no circle-domain assertion.')
    (BASE/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
