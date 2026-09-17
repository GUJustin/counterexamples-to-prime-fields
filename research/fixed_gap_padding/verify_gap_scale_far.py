"""Exact constants and finite gap-scale far-point certificates."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,time
from verify_average_padding import h,c


def fixture(b,C,alpha,gap,denom):
 p=h.lucas_lehmer(b);n=denom*((C*b//denom));K=n//2;m=int(alpha*n)
 A=K+gap;s=gap-1;N=m-1;q=n-N;U=p-1
 assert n%2==0 and alpha*n==m and K<A<m<n<p
 L0,_,_=h.gram_bound(m,A,s);L=h.ceil(F(A*L0,m))
 T=(K-1)*comb(L,2)-h.pairs(L*(A-1),N);assert T>=0
 M=F(L*L*(p-N),L*(p-N)+2*T)
 scale=2**128;x=F((M/U*scale).__floor__(),scale)
 assert 0<x<=M/U
 series=sum((F(comb(q,j))*x**j for j in range(min(q,96)+1)),F(0))
 density=F(U,p)*(1-1/series)
 assert p**gap*A**A*(n-A)**(n-A)>n**n
 expected={(2203,2):(4128,2064,2066,F('0.93155073'),126),
           (4423,7):(26520,13260,13267,F('0.99999974'),619)}
 if (b,gap) in expected:
  nn,kk,aa,dd,bb=expected[(b,gap)]
  assert (n,K,A)==(nn,kk,aa) and density>dd
  assert n**gap*2**(n+bb*gap)<p**gap
 J=h.ceil(p*density)
 assert J**gap>n**gap*2**n
 bits=0
 while n**gap*2**(n+(bits+1)*gap)<p**gap:bits+=1
 return dict(prime_exponent=b,n=n,K=K,A=A,m=m,moments=s,
             far_separation_over_eta=str(F(1,gap)),exact_far_agreement=A-1,
             nearby_fraction_lower=c.decimal_lower(density,8),
             prescription_fraction_less_than_power_two=-bits,strict_elias=True,
             list_lower_bound_sha256=c.digest_integer(L),label_lower_bound_sha256=c.digest_integer(J))


def main():
 start=time.monotonic()
 # C*alpha*H2(beta)>1 without logarithmic approximations.
 assert 3**5<2**8 # H2(3/4)>4/5, C*alpha=5/4.
 assert 15**15<2**59 # H2(15/16)>5/16, C*alpha=16/5.
 # exp(224/15)>10^6 from a positive Taylor partial sum.
 x=F(224,15);term=F(1);total=term
 for j in range(1,70):term*=x/j;total+=term
 assert total>10**6
 rows=[fixture(b,F(15,8),F(2,3),2,6) for b in [521,2203,4423]]
 rows += [fixture(b,F(6),F(8,15),7,30) for b in [4423,9689]]
 out=dict(status='passed',certificates=rows,seconds=time.monotonic()-start,
          scope='Exact finite prime-field certificates and exact asymptotic constant inequalities. Arbitrary padded intervals; eta shrinks and the far separation is a fixed fraction of eta. No prescribed-domain result.')
 Path(__file__).with_name('gap_scale_far_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
