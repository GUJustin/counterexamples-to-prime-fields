"""Exact paired-domain certificates, using only standard-library integers."""
from math import comb,isqrt
from fractions import Fraction
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def prime(b):
 assert all(b%d for d in range(2,isqrt(b)+1))
 p=(1<<b)-1;s=4
 for _ in range(b-2):s=(s*s-2)%p
 assert s==0
 return p

def bounds(b,n,m):
 p=(1<<b)-1;assert n%4==2
 K=n//2;D=(K+1)//2;q=n//2-m;U=p-1;R=U//2-m;L=comb(m,D)
 assert 0<D<m and q>0 and p>max(32,m*m)
 B=Fraction(U*(p+6*(isqrt(p)+1)+768),2*p*(p-m*m))
 M=Fraction(L*R,1)/(R+(L-1)*B)
 assert 0<M<=U
 missing=1-M/U
 complete=U*missing.numerator**q<missing.denominator**q
 # Strict half-rate characteristic Elias sufficient condition: eta*log2p>1.
 # p>2^(b-1), so 3*(b-1)>n is a conservative integer certificate.
 elias=3*(b-1)>n
 # n*2^(n/3)/p <2^-k iff n^3*2^(n+3k)<p^3.
 k=0
 while n**3*(1<<(n+3*(k+1)))<p**3:k+=1
 delta=Fraction(U,L)+U*B/R-1
 best=None
 for d in range(1,33):
  failure=delta*(1<<d)+Fraction(U,((1<<d)+1)**q)
  if best is None or failure<best[0]:best=(failure,d)
 f,d=best;bits=0
 while f.numerator*(1<<(bits+1))<f.denominator:bits+=1
 return dict(b=b,n=n,K=K,m=m,D=D,q=q,eta_numerator=3,far_numerator=2,list_bits=L.bit_length(),complete=complete,strict_elias=elias,prescription_below_power_of_two=k,sampling_failure_below_power_of_two=bits,gamma_inverse_log2=d), f

if __name__=='__main__':
 start=time.monotonic();rows=[]
 for b,n,m in [(127,318,143),(521,1458,685),(521,1438,673)]:
  prime(b);row,f=bounds(b,n,m);assert row['complete'] and row['strict_elias'] and row['prescription_below_power_of_two']>0
  rows.append(row)
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,scope='Exact integer/rational sufficient certificates; geometry supplied by the written paired-domain argument.')
 (BASE/'finite_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
