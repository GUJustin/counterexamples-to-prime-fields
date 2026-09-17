"""Exact low-rate robust-density certificates without n-digit integers."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,time
from verify_average_padding import h,c


def root5(v):
 lo=0;hi=1<<((v.bit_length()+4)//5)
 while hi-lo>1:
  mid=(lo+hi)//2
  if mid**5<=v:lo=mid
  else:hi=mid
 assert lo**5<=v<(lo+1)**5
 return lo


def power_bound(x):
 assert 0<x<1
 b=max(0,x.denominator.bit_length()-x.numerator.bit_length()-1)
 while x<F(1,2**(b+1)):b+=1
 assert x<F(1,2**b)
 return b


def fixture(b):
 p=h.lucas_lehmer(b);n=root5(p*p);N=2*n//3;q=n-N;U=p-1;R=p-N
 assert 4<N<n<p
 L=h.ceil(F(comb(N,3),3*N-8))
 # d=1; omit the favorable core collision subtraction for independence.
 M=F(L*R,R+L-1)
 scale=2**max(128,b//5+64);x=F((M/U*scale).__floor__(),scale)
 assert 0<x<=M/U<=1
 partial=sum((F(comb(q,j))*x**j for j in range(min(q,96)+1)),F(0))
 density=F(U,p)*(1-1/partial)
 # Sufficient strict Elias and upper bound on c1=c2=1 prescription.
 assert p*p*4**4>3**4*n**4
 prescription=F(3*n*n,2*p)
 assert density>prescription
 J=h.ceil(p*density)
 if b>=127:assert J==U and F(U,partial)<1
 return dict(prime_exponent=b,n=n,K=2,A=4,core_length=N,padding=q,
             list_lower=L,all_nonzero_parameters_nearby=(J==U),exact_far_agreement=3,far_separation_over_eta='1/2',
             nearby_fraction_lower=c.decimal_lower(density,8),
             missing_fraction_less_than_power_two=-power_bound(1-density),
             prescription_fraction_less_than_power_two=-power_bound(prescription),
             strict_elias=True)


def main():
 start=time.monotonic();rows=[fixture(b) for b in [31,61,127,521]]
 out=dict(status='passed',certificates=rows,seconds=time.monotonic()-start,
          scope='Vanishing-rate K2,eta2/n,half-gap far point; all field, integer-root, list, density, Elias and prescription inequalities exact. No fixed-positive-rate claim.')
 Path(__file__).with_name('vanishing_rate_density_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
