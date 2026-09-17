"""Exact arithmetic for cubic-warp full punctured-line certificates.

Uses the proved arrangement-irreducibility argument and Cafure–Matera
Corollary5.6 as mathematical inputs; this script does not prove them.
"""
from fractions import Fraction as F
from math import comb,isqrt
from pathlib import Path
import sys,json,time
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE.parent/'fixed_gap_padding'))
from verify_average_padding import h,c


def fixture(b,C,s,n=None,m=None):
 p=h.lucas_lehmer(b)
 if n is None:n=6*((C*b)//6)
 if m is None:m=2*n//3
 K=n//2;t=K+s+1
 assert n==2*K
 assert t<m<n<p and s>=1 and p>2*t*t
 L0,_,_=h.gram_bound(m,t,3*s);L=h.ceil(F(t*L0,m))
 assert L>1
 N=m-1;R=p-N;q=n-N;U=p-1
 sqrt_upper=isqrt(p)+1
 B=F(p+(t-1)*(t-2)*sqrt_upper+3*t**4,p-comb(m,2))
 assert B>1 and p>comb(m,2)
 M=F(L*R,1)/(R+(L-1)*B)
 assert 0<M<=R<=U
 # Large rows use a small exponent certificate; small rows can check
 # the exact rational power directly without creating huge integers.
 assert M>F(3*U,4)
 if 2*q>=b:
  assert U<2**(2*q)
  coverage_method='quarter-missing bound'
 else:
  assert q*p.bit_length()<100000
  assert U*(1-M/U)**q<1
  coverage_method='exact rational missing-label expectation'
 A=t;gap=A-K
 assert p**gap*A**A*(n-A)**(n-A)>n**n
 bits=b-((n+gap-1)//gap)-n.bit_length()
 assert bits>0 and n**gap*2**(n+bits*gap)<p**gap
 while n**gap*2**(n+(bits+1)*gap)<p**gap:bits+=1
 return dict(prime_exponent=b,n=n,K=K,m=m,threshold=A,seed_moments=3*s,
             transformed_moments=s,list_bits=L.bit_length(),padding=q,
             image_fraction_lower=c.decimal_lower(M/U,8),
             all_nonzero_parameters_nearby=True,coverage_method=coverage_method,far_coordinates=1,
             separation_fraction=str(F(1,gap)),strict_elias=True,
             prescription_fraction_less_than_power_two=-bits,
             list_lower_bound_sha256=c.digest_integer(L))

if __name__=='__main__':
 start=time.monotonic()
 rows=[fixture(127,None,1,n=214,m=202),fixture(1279,F(3),3),fixture(9689,F(15,8),1)]
 out=dict(status='passed',certificates=rows,seconds=time.monotonic()-start,
          scope='Exact finite arithmetic conditional on the written cubic-warp geometry and cited point-count theorem. Existence certificates; no coordinates or padding directions enumerated.')
 (BASE/'finite_certificates.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
