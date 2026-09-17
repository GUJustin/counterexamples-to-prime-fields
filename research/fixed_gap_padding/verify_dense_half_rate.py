"""Exact half-rate finite density versus the numerical line prescription."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,time
from verify_average_padding import h,c


def certificate(b,n,K,A,m,s,bits):
 p=h.lucas_lehmer(b);N=m-1;q=n-N;gap=A-K
 assert 2*K==n and s==gap-1 and K+1<A<m<n<p
 L0,_,_=h.gram_bound(m,A,s);L=h.ceil(F(A*L0,m))
 T=(K-1)*comb(L,2)-h.pairs(L*(A-1),N)
 assert T>=0
 R=p-N;M=F(L*L*R,L*R+2*T)
 assert 0<M<=p
 assert p>2*q and 2*comb(n,A)<p**gap
 assert p**gap*A**A*(n-A)**(n-A)>n**n
 scale=2**128;x=F((M/p*scale).__floor__(),scale)
 assert 0<x<=M/p
 partial=sum((F(comb(q,j))*x**j for j in range(min(q,64)+1)),F(0))
 density=1-1/partial
 # Also exploit the exact union formula for the 31-bit fixture, where
 # ceil(J) can matter on the eighth decimal place.
 if b==31:
  exact=F(h.ceil(p*(1-(1-M/p)**q)),p)
  density=max(density,exact)
 J=h.ceil(p*density)
 assert n**gap*2**(n+bits*gap)<p**gap
 assert density>F(1,2**bits)
 return dict(prime_exponent=b,n=n,K=K,A=A,seed_length=m,moments=s,q=q,
             anchored_list_lower=L,nearby_fraction_lower=c.decimal_lower(density,8),
             prescription_fraction_less_than_power_two=-bits,
             label_lower_bound=J,strict_elias=True,direction_condition=True)


def main():
 start=time.monotonic()
 rows=[certificate(*r) for r in [(31,92,46,50,75,3,1),
                                (61,216,108,113,154,4,10),
                                (61,168,84,89,135,4,20),
                                (127,468,234,240,308,5,40),
                                (521,2800,1400,1411,1677,10,255)]]
 out=dict(status='passed',fixtures=rows,seconds=time.monotonic()-start,
          scope='Prime-field, exact half-rate, padded interval-domain existence certificates. The numerical prescription uses c1=c2=1 without an unspecified remainder. No prescribed subgroup, whole-line uniqueness or protocol-security claim.')
 Path(__file__).with_name('dense_half_rate_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
