"""Actual splitting-prime fixtures satisfying the conservative norm bound."""
from pathlib import Path
from math import comb,isqrt,prod,gcd
from fractions import Fraction
from itertools import combinations
import json,time,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'orbit_unique'))
from generate_roots import modpow
from verify_parameters import mersenne_prime
from check_exhaustive import replay_line
BASE=Path(__file__).resolve().parent

def decode(T,q,L,m,D,S):
 h=q.bit_length()-1;assert q==1<<h
 if T<=1 or T.bit_length()%h:return None
 s=T.bit_length()//h;u=Fraction(T,q**s);I=[]
 for i in range(L,L+m):
  f=1-Fraction(1,q**i)
  if u<=f:u/=f;I.append(i)
 if u!=1 or len(I)!=D or sum(I)!=S:return None
 return I

def parameters(p,b,d,m,D,c,q):
 M=m+c;L=1;n=d*(m+2)+c;assert q-1>3*d**(d-1) and q>4*(d*M)**(d-2)
 W=prod(q**i-1 for i in range(1,M+1));N=(d-1)*d**(M+1);B=(W*n*(q+1))**N
 Smax=D*(2*m-D+1)//2
 if not(p>B and p>q**Smax):return None
 values=[q]+[(q**(i+1)-1)*pow(q**i-1,-1,p)%p for i in range(1,M+1)]
 if any(modpow(x,(p-1)//d,p,b)!=1 for x in values):return None
 e=pow(d,-1,(p-1)//d)
 roots=[pow(x,e,p) for x in values];assert all(pow(a,d,p)==x for a,x in zip(roots,values))
 omega=next(pow(h,(p-1)//d,p) for h in range(2,100) if pow(h,(p-1)//d,p)!=1)
 replay=replay_line(p,d,m,D,c,q,roots[1:]+roots[:1],omega)
 S=replay['selected_sum'];supports=[I for I in combinations(range(1,m+1),D) if sum(I)==S]
 for I in supports:
  T=prod(q**i-1 for i in I);assert T<p and decode(T,q,1,m,D,S)==list(I)
  z=((-1)**(D+1)*(q-1)**D*pow(T,-1,p))%p
  lift=((-1)**(D+1)*(q-1)**D*pow(z,-1,p))%p
  assert lift==T
 return dict(b=b,d=d,m=m,D=D,c=c,q=q,n=n,K=d*D-1,norm_bound_bits=B.bit_length(),no_wrap_power_bits=(q**Smax).bit_length(),norm_field_degree_upper=N,decoded_supports=len(supports),line=replay)

if __name__=='__main__':
 start=time.monotonic();rows=[]
 for d,m,D,c,fields in [(2,4,2,0,[1279,2203,9689]),(3,2,1,0,[9689])]:
  found=None
  for b in fields:
   p=mersenne_prime(b);assert (p-1)%d==0 and gcd(d,(p-1)//d)==1
   for h in range(3 if d==2 else 5,44):
    q=1<<h
    found=parameters(p,b,d,m,D,c,q)
    if found:break
   if found:break
  assert found is not None,(d,m)
  rows.append(found);print({k:v for k,v in found.items() if k!='line'},flush=True)
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,scope='Actual fields and domains satisfy the universal splitting-prime norm and integer no-wrap bounds. Every nearby codeword is independently classified by interpolation pencils. Toy fixtures test the proof and decoder, not numerical-bound violations.')
 (BASE/'integer_verification.json').write_text(json.dumps(out,indent=2)+'\n');print('passed')
