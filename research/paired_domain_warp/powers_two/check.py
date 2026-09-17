"""Exact subset-product decoder tests and finite parameter search."""
from itertools import combinations
from math import comb,isqrt,prod
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def decode_integer(t,m,D):
 if t<1:return None
 original=t
 if t==1:s=0
 elif t.bit_length()%2:return None
 else:s=t.bit_length()//2
 if s>m*(m+1)//2:return None
 support=[]
 for i in range(1,m+1):
  if s<0:return None
  power=1<<(2*i);factor=power-1
  if t*power<=factor*(1<<(2*s)):
   if t%factor:return None
   t//=factor;s-=i;support.append(i)
 if t!=1 or s!=0 or len(support)!=D:return None
 if prod((1<<(2*i))-1 for i in support)!=original:return None
 return tuple(support)

def ll(b):
 assert all(b%d for d in range(2,isqrt(b)+1));p=(1<<b)-1;s=4
 for _ in range(b-2):s=(s*s-2)%p
 assert s==0

if __name__=='__main__':
 start=time.monotonic();tested=0
 for m in range(2,15):
  seen={}
  for D in range(1,m):
   for I in combinations(range(1,m+1),D):
    t=prod((1<<(2*i))-1 for i in I)
    assert t not in seen;seen[t]=I
    assert decode_integer(t,m,D)==I
    assert decode_integer(t,m,D+1) is None
    tested+=1
  # Exhaustive small integer nonbank inputs; final validation forbids errors.
  for t in range(1,1000):
   for D in [1,m//2,m-1]:
    got=decode_integer(t,m,D)
    assert (got is not None)==(t in seen and len(seen[t])==D)
 rows=[]
 for b in [127,521,1279,2203,9689]:
  ll(b);p=(1<<b)-1;best=None;best_ratio_num=0;best_ratio_den=1;half=None
  for m in range(2,min(b//2,200)+1):
   n=2*m+2
   for D in range(1,m):
    exponent=D*(2*m-D+1)
    if exponent>=b:continue
    K=2*D-1;J=comb(m,D);num=J**3*K**K*(n-K)**(n-K);den=n**(n+3)
    if num<=den:continue
    c=0
    while num>den*(1<<(3*(c+1))):c+=1
    row=dict(b=b,n=n,K=K,m=m,D=D,product_bit_bound=exponent,nearby_parameters=str(J),violation_factor_greater_than_power_two=c)
    if num*best_ratio_den>best_ratio_num*den:best=row;best_ratio_num=num;best_ratio_den=den
    if K*2==n:half=row
  rows.append(dict(b=b,best_scanned=best,last_half_rate=half))
 out=dict(status='passed',subset_decodings=tested,rows=rows,seconds=time.monotonic()-start,scope='Exact integer decoder tests and sufficient deterministic power-of-two parameters. Finite search is not an optimality claim.')
 (BASE/'verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
