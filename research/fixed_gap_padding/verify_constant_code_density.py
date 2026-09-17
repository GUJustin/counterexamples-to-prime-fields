"""Constant-code punctured lines: fiber averaging and exact large-field bounds."""
from fractions import Fraction as F
from math import comb,isqrt
from itertools import product
from collections import Counter
from pathlib import Path
import json,time
from verify_average_padding import h,c
from verify_vanishing_rate_density import root5,power_bound


def fiber_audit(p,D):
 total=maximum=0
 for middle in product(range(p),repeat=D-1):
  coeff=(0,)+middle+(1,)
  fibers=Counter(sum(a*pow(x,j,p) for j,a in enumerate(coeff))%p for x in range(p))
  count=sum(size==D for size in fibers.values())
  assert max(fibers.values())<=D
  total+=count;maximum=max(maximum,count)
 assert total==comb(p,D) and maximum*p**(D-1)>=total
 return dict(p=p,D=D,polynomials=p**(D-1),total_full_fibers=total,maximum=maximum)


def fixture(b):
 p=h.lucas_lehmer(b);n=root5(p**3);N=2*(n//4);L=N//2;q=n-N;U=p-1
 assert 2<N<n<p and 2*L==N
 # f=X²-(N+1)X, core1..N: pairs {x,N+1-x} give L distinct values.
 # All roots of each selected fiber are in the core, so outside images
 # have exactly L nonzero elements, without a collision estimate.
 scale=2**(2*b//5+80);x=F((F(L,U)*scale).__floor__(),scale)
 assert 0<x<=F(L,U)
 partial=sum((F(comb(q,j))*x**j for j in range(min(q,96)+1)),F(0))
 density=F(U,p)*(1-1/partial);J=h.ceil(p*density)
 assert p*p>n**3 # sufficient strict Elias at K1,A3
 bound=isqrt(3*n**3)+1
 assert bound**2>3*n**3 and J>bound
 if b>=61:assert J==U and F(U,partial)<1
 return dict(prime_exponent=b,n=n,K=1,A=3,core_length=N,list_size=L,
             far_separation_over_eta='1/2',exact_far_agreement=2,
             all_nonzero_parameters_nearby=(J==U),nearby_fraction_lower=c.decimal_lower(F(J,p),8),
             prescription_fraction_less_than_power_two=-power_bound(F(bound,p)),
             actual_global_maximum_list_size=n//3,strict_elias=True)


def main():
 start=time.monotonic()
 out=dict(status='passed',fiber_count_audits=[fiber_audit(p,D) for p,D in [(5,2),(5,3),(7,3),(11,4)]],
          certificates=[fixture(b) for b in [31,61,127,521]],seconds=time.monotonic()-start,
          scope='Elementary vanishing-rate constant-code examples; exact fiber counting and existence certificates. No fixed-positive-rate or actual-global-list separation.')
 Path(__file__).with_name('constant_code_density_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
