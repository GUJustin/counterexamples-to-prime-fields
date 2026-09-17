"""Exact dyadic certificates for completion of the entire product image."""
from math import comb,isqrt
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def floorlog_ratio(den,num):
 a=den.bit_length()-num.bit_length()
 if a<0:return -1
 if num*(1<<a)>den:a-=1
 assert a<0 or num*(1<<a)<=den<num*(1<<(a+1))
 return a

def data(b,r,n,t):
 p=2**b-1;assert n%4==2
 K=n//2;D=(K+1)//2;m0=n//2-r-2*t;D0=D-t
 assert 1<=D0<m0 and p>(n+1)**2 and p>(4*r+2)**2
 L=comb(m0,D0);C=4*r+2
 num=p**r*(p-2*m0*m0)+L*(C**(2*r+2)+2*m0*m0)
 den=L*(p-2*m0*m0)
 return p,K,D,m0,D0,L,C,num,den

def schedule(b,r,n,t,target=None):
 p,K,D,m0,D0,L,C,num,den=data(b,r,n,t)
 k=0 if target is None else target+(t+1).bit_length()
 a=floorlog_ratio(den,num)-k
 if a<0:return None
 seq=[a]
 for _ in range(t):
  num=p+C*C*(1<<a);den=(p-4)*(1<<(2*a))
  a=floorlog_ratio(den,num)-k
  if a<0:return None
  seq.append(a)
 if (1<<a)<=(p-1)**r:return None
 return dict(b=b,r=r,n=n,K=K,D=D,base_orbits=m0,base_support=D0,sprinkling_pairs=t,base_list_bits=L.bit_length(),dyadic_missing_exponents=seq,per_event_failure_exponent=k,failure_target=target,mode='existence' if target is None else 'randomized',direction_weight=2*r,affine_dimension=r,far_distance_numerator=n-K-1,nearby_distance_numerator=n-K-2*r-1)

def prime(b):
 assert all(b%j for j in range(2,isqrt(b)+1));p=2**b-1;s=4
 for _ in range(b-2):s=(s*s-2)%p
 assert s==0

if __name__=='__main__':
 start=time.monotonic();rows=[]
 for b,r,n in [(61,1,158),(127,1,294),(521,2,2518),(1279,3,8678),(1279,5,13782),(1279,10,26218)]:
  prime(b);best=None;first=None
  for t in range(1,2*r+25):
   ex=schedule(b,r,n,t)
   if ex and first is None:first=ex
   lo=0;hi=b//2
   while lo<hi:
    mid=(lo+hi+1)//2
    if schedule(b,r,n,t,mid):lo=mid
    else:hi=mid-1
   if lo and (best is None or lo>best['failure_target']):best=schedule(b,r,n,t,lo)
  assert first
  rows.append(dict(existence=first,best_randomized=best))
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,scope='Exact sufficient product-image completion bounds. Existence uses successive averaging; randomized certificates use separately budgeted conditional Markov events. Neither is an individual sample coverage check.')
 (BASE/'completion_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
