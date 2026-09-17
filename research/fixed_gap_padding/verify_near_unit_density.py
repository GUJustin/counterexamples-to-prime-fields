"""Exact finite certificates for the density-to-one parameter regime."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,log2,sqrt,ceil,floor
import json,time
from verify_average_padding import h,c


def certificate(b,rho=F(1,2),C=2):
 p=h.lucas_lehmer(b);ell=log2(b);eps=sqrt(log2(ell)/ell)
 n=rho.denominator*round((sqrt(2)/C*b**1.5/sqrt(ell))/rho.denominator)
 K=int(rho*n);s=floor(C*n/b);missing=ceil((4+eps)*b/ell)
 k=K+1;A=k+s;m=A+missing;N=m-1;q=n-N;d=K-1
 assert 1<=k<A<m<n<p
 # Exact finite pigeonhole, using the full binomial-moment ranges.
 numerator=comb(m-1,missing);denominator=1
 for j in range(1,s+1):
  denominator*=comb(m,j+1)-comb(m-A,j+1)-comb(A,j+1)+1
 L=(numerator+denominator-1)//denominator
 box_L=L
 L0,_,_=h.gram_bound(m,A,s)
 L=max(L,h.ceil(F(A*L0,m)))
 assert L>p
 T=d*comb(L,2)-h.pairs(L*(A-1),N);assert T>=0
 M=F(L*L*(p-N),L*(p-N)+2*T)
 # Exact direction and Elias inequalities, without large p^q integers:
 # (p/(p-1))^q < 2 follows from Bernoulli and p>2q.
 assert p>2*q
 assert 2*comb(n,A)<p**(A-K)
 assert p**(A-K)*A**A*(n-A)**(n-A)>n**n
 # Avoid huge rational powers: (1-x)^q <=1/(1+q*x), an exact
 # Bernoulli consequence, provides a compact conservative density bound.
 U=p-1
 density=F(U,p)*F(q)*M/(U+F(q)*M)
 # A sharper rational exponential bound uses (1-x)^q <=(1+x)^(-q)
 # and truncates the positive binomial series at a fixed degree.
 scale=2**128
 x=F((M/U*scale).__floor__(),scale)
 assert 0<x<=M/U
 positive_sum=sum((F(comb(q,j))*x**j for j in range(min(q,32)+1)),F(0))
 density=max(density,F(U,p)*(1-1/positive_sum))
 J=h.ceil(p*density)
 assert 0<J<=p
 logL,_=c.narrow_log2(F(L))
 return dict(prime_exponent=b,n=n,K=K,A=A,q=q,seed_length=m,missing=missing,
             seed_moments=s,box_list_bits=box_L.bit_length(),list_log2_lower=c.decimal_lower(logL),
             density_decimal_lower=c.decimal_lower(density,8),
             exact_eta=str(F(A-K,n)),label_lower_bound_sha256=c.digest_integer(J),
             list_lower_bound_sha256=c.digest_integer(L),direction_condition=True,strict_elias=True,exact_far_agreement=A-1)


def main():
 start=time.monotonic();rows=[certificate(b) for b in (521,1279,2203,3217,4423)]
 out=dict(status='passed',fixtures=rows,seconds=time.monotonic()-start,
          scope='Far-point multiplicative-padding certificates with p-1 label universe. Exact finite prime-field certificates at rate1/2 and parameterC2. Floating choices only choose integer parameters; all mathematical inequalities, counts, primality and displayed density lower bounds are verified exactly. Not a convergence proof or a prescribed-domain result.')
 Path(__file__).with_name('near_unit_density_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
