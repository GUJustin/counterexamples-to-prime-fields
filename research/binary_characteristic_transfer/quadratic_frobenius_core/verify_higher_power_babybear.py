#!/usr/bin/env python3
"""Exact parameter certificate, not an enumerated domain or counterexample scan."""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import hashlib
import json
from flint import fmpz

p, h = 2013265921, 12241
assert fmpz(p).is_prime()
assert (p*p+1) % h == 0 and 1 < h < p*p+1
k = h+1
N = h*(p*p-1)
m = 54*N//55
n = N+m
T = isqrt(h*n-1)
common = h*p
source_upper = common+h*h
support_min = h*(p-1)
required_retention = T-support_min
gamma = Fraction(m,N)-Fraction(required_retention-1,support_min)

def ceil_root_ratio(a,b,power):
    v=(a+b-1)//b
    r=isqrt(v) if power==2 else isqrt(isqrt(v))
    r += r**power < v
    assert r**power*b >= a
    assert r == 0 or (r-1)**power*b < a
    return r

# Low-rate first-order upper bound: sqrt(kn/2)+(k^3 n/72)^(1/4).
first_upper=ceil_root_ratio(k*n,2,2)+ceil_root_ratio(k**3*n,72,4)
assert Fraction(k,n)<Fraction(1,100)  # strictly inside the low-rate branch
assert first_upper < common <= source_upper < T
assert T*T<h*n and (T+1)**2>=h*n
assert (p*p+1)//h>h-1 and h<h*p
assert 0<required_retention<=support_min and gamma>0
# log(p(p+1)) < 2*bit_length(p)+1, so the union bound is strictly <1.
exponent=2*support_min*gamma*gamma
assert exponent>2*p.bit_length()+1
B=(p+1)*(p*p-1)
assert p**4-(p+1)*p*p>=2
ratio=Fraction(T-source_upper,T-k)
assert ratio>Fraction(28965,100000)
result={
 'PASS':True,'scope':'Exact finite hypotheses for the higher-power theorem; domain existence uses its probabilistic proof, not explicit enumeration',
 'p':p,'extension_degree':4,'h':h,'dimension':k,'full_first_block':N,
 'retained_second_block':m,'length':n,'threshold':T,
 'common_agreement':common,'source_agreement_upper':source_upper,
 'first_order_agreement_upper':first_upper,'singleton_labels':B,
 'additional_label_list_size':p+1,
 'guaranteed_loss_over_capacity_margin':[ratio.numerator,ratio.denominator],
 'guaranteed_loss_over_capacity_margin_decimal':float(ratio),
 'concentration_exponent_lower_bound':2*p.bit_length()+1,
 'practical_domain':False,'better_codes_improvement':False,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
