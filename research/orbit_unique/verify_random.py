"""Exact finite union-bound certificates for logarithmic-length orbit lines.

These certify the generator's success probability, not the combinatorial
properties of a particular sampled domain.
"""
from pathlib import Path
from math import comb,isqrt
from fractions import Fraction
import json,time
BASE=Path(__file__).resolve().parent

def prime_mersenne(b):
 assert all(b%q for q in range(2,isqrt(b)+1));p=(1<<b)-1;s=4
 for _ in range(b-2):s=(s*s-2)%p
 assert s==0;return p

def certificate(b,d,D):
 p=prime_mersenne(b);assert all(d%q for q in range(2,isqrt(d)+1))
 assert (p-1)%d==0 and p>d**(d-1)
 m=2*D-2;c=d-2;K=d*D-1;n=2*K;J=comb(m,D)
 assert n==d*(m+1)+c and 1<=D<m
 invalid=comb(n,2);roots=1<<(n-d);products=d*D*comb(J,2)
 # Conditional on a valid, resampled domain. This also includes the
 # invalid-domain term in the numerator, a conservative extra allowance.
 B=Fraction(invalid+roots+products,p-invalid)
 assert B<1 and (d+1)*(b-1)>n
 q=0
 while B<(Fraction(1,1<<(q+1))):q+=1
 r=-1
 while J**(d+1)>n**(d+1)*(1<<(n+(r+1)*(d+1))):r+=1
 assert r>=0
 return dict(b=b,d=d,n=n,K=K,m=m,D=D,extra_coordinates=c,nearby_count=str(J),
  probability_failure_less_than_power_two_minus=q,ratio_greater_than_power_two=r,
  separation_fraction=f'{d}/{d+1}',root_subset_bound_bits=n-d,
  product_collision_numerator_bits=products.bit_length(),
  far_distance_numerator=n-K-1,nearby_distance_numerator=n-K-d-1)

if __name__=='__main__':
 start=time.monotonic()
 rows=[certificate(521,3,78),certificate(521,5,47),certificate(1279,7,82)]
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,
  scope='Exact union-bound success certificates for random valid domains, not deterministic classification certificates for specific samples. No witness recovery claim.')
 (BASE/'random_parameters.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
