#!/usr/bin/env python3
"""Exact deterministic branch-prefix criteria; no random-domain assertion."""
from fractions import Fraction
from math import gcd,isqrt
from pathlib import Path
import hashlib,json
from flint import fmpz

def ceil_root_ratio(a,b,power):
    v=(a+b-1)//b
    r=isqrt(v) if power==2 else isqrt(isqrt(v))
    r+=r**power<v
    assert r**power*b>=a and (r==0 or (r-1)**power*b<a)
    return r

def check(p,h,num,den):
    assert p>=5 and fmpz(p).is_prime()
    M=p*p+1; ell=p*p-1
    assert h>1 and h%2 and M%h==0 and h<M
    assert gcd(h,ell)==1 and h-1<M//h
    N=h*ell;m=num*N//den;n=N+m;k=h+1
    R,tau=divmod(m,ell)
    assert 0<m<N and 0<=R<h and 0<=tau<ell
    T=isqrt(h*n-1);C=h*p
    assert p>=3*h-1
    divisors=[1]
    for prime,exponent in fmpz(h).factor():
        divisors=[d*int(prime)**j for d in divisors for j in range(exponent+1)]
    noncanonical=max((h//H)*max(p,H*H)+(2*h-h//H)*H for H in divisors if H>1)
    assert noncanonical<C
    U=C
    bank_min=(h+R)*(p-1)
    first=ceil_root_ratio(k*n,2,2)+ceil_root_ratio(k**3*n,72,4)
    assert Fraction(k,n)<Fraction(1,100)
    assert first<C<=U<T<=bank_min
    assert T*T<h*n<=(T+1)**2
    B=(p+1)*(p*p-1)
    ratio=Fraction(T-U,T-k)
    return {'p':p,'extension_degree':4,'h':h,'dimension':k,'length':n,
      'first_block_length':N,'second_block_length':m,
      'whole_second_branches':R,'partial_branch_length':tau,
      'threshold':T,'common_agreement':C,'source_agreement_upper':U,
      'source_agreement_exact':C,'noncanonical_agreement_upper':noncanonical,
      'canonical_agreement_lower':bank_min,'first_order_agreement_upper':first,
      'singleton_labels':B,'additional_label_list_size':p+1,
      'guaranteed_loss_over_capacity_margin':[ratio.numerator,ratio.denominator],
      'guaranteed_loss_over_capacity_margin_decimal':float(ratio)}

cases=[check(2013265921,12241,54,55),check(97,5,1,2),check(307,65,17,20)]
assert Fraction(*cases[0]['guaranteed_loss_over_capacity_margin'])>Fraction(28965,100000)
assert Fraction(*cases[1]['guaranteed_loss_over_capacity_margin'])>Fraction(18,100)
result={'PASS':True,'scope':'Exact finite parameters for explicitly specified branch-prefix domains; no coordinates enumerated by this checker',
 'domain_recipe':'For primitive xi in F_(p^4), M=p^2+1, alpha_j=xi^((M/h)*j), z0=xi^M: keep all D0, all xi*alpha_j*B* for j<R, and xi*alpha_R*z0^v for 0<=v<tau.',
 'endpoint_recipe':'lambda0=1+xi^h*z0 and lambda1=2+xi^h*z0; z0 not in F_p makes both labels outside every canonical plane.',
 'cases':cases,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
