"""Exact failure bounds for multi-pair block sampling."""
from math import comb,isqrt
from fractions import Fraction
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def prime(b):
 assert all(b%d for d in range(2,isqrt(b)+1));p=(1<<b)-1;s=4
 for _ in range(b-2):s=(s*s-2)%p
 assert s==0;return p

def bound(b,r,n,m):
 p=(1<<b)-1;K=n//2;assert n%4==2
 D=(K+1)//2;assert (n//2-m)%r==0
 q=(n//2-m)//r;assert q>0 and D<m
 U=p-1;V=U**r;N=p-2*r-1;L=comb(m,D)
 a=Fraction(N-m*(m-1),N);lam=Fraction(2*r*(isqrt(p)+1)+2*r+1,N)
 assert a>0 and lam<1
 delta=Fraction(V,L)+(1+V*lam**(2*r+2))/a-1;assert delta>0
 best=None
 for d in range(1,129):
  f=q*delta*(1<<d)+Fraction(U,((1<<d)+1)**q)
  if best is None or f<best[0]:best=(f,d)
 f,d=best;bits=0
 while f.numerator*(1<<(bits+1))<f.denominator:bits+=1
 u=2*r+1;k=-1
 for kk in range(0,b):
  if n**u*(1<<(n+u*kk))<p**u:k=kk
  else:break
 assert u*(b-1)>n # conservative sufficient strict Elias for half rate
 return dict(b=b,r=r,n=n,K=K,m=m,D=D,blocks=q,L_bits=L.bit_length(),far_fraction=f'{2*r}/{2*r+1}',failure_below_power_of_two=bits,gamma_inverse_log2=d,prescription_below_power_of_two=k,success_bound=f<1),f

if __name__=='__main__':
 start=time.monotonic();rows=[]
 for b,r,n,m in [(521,1,1458,685),(521,2,2518,1211),(521,3,3518,1711),(1279,3,8678,4186),(1279,5,13782,6751),(1279,10,26218,12949)]:
  prime(b);row,f=bound(b,r,n,m);assert row['success_bound'];rows.append(row)
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,scope='Exact rational bound using ceil sqrt, Lucas-Lehmer primality, and integer Elias/prescription comparisons. General Fourier and sampling argument is supplied by the written proof.')
 (BASE/'multiblock_finite_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
