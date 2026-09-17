"""Exact finite orbit parameters and fast Lucas-Lehmer certificates."""
from math import comb,isqrt
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def mersenne_prime(b):
 assert all(b%d for d in range(2,isqrt(b)+1));p=(1<<b)-1;s=4
 for _ in range(b-2):
  v=s*s-2;s=(v&p)+(v>>b)
  if s>=p:s-=p
  if s<0:s+=p
 assert s==0
 return p

if __name__=='__main__':
 start=time.monotonic()
 # Cross-check folding against ordinary reduction on several complete chains.
 for b in [3,5,7,13,17,19,31,61,127]:
  p=(1<<b)-1;a=c=4
  for _ in range(b-2):
   a=(a*a-2)%p;v=c*c-2;c=(v&p)+(v>>b)
   if c>=p:c-=p
   if c<0:c+=p
   assert a==c
 rows=[]
 for b,d in [(9689,3),(19937,5),(44497,7)]:
  t0=time.monotonic();p=mersenne_prime(b);assert (p-1)%d==0
  best=None
  for D in range(2,300):
   m=2*D-2;c=d-2;n=2*(d*D-1);K=n//2
   E=d*D*(2*m-D+1)//2;A=(1<<(m+1))*(d+(1<<c))
   if p<=1<<E or p<=A**(d-1):continue
   J=comb(m,D);w=-1
   while J**(d+1)>n**(d+1)*(1<<(n+(w+1)*(d+1))):w+=1
   if w<0:continue
   assert (d+1)*(b-1)>n
   best=dict(b=b,d=d,n=n,K=K,m=m,D=D,extra_coordinates=c,nearby_count=str(J),
    product_exponent=E,norm_bound_bits=(A**(d-1)).bit_length(),
    ratio_greater_than_power_two=w,far_distance_numerator=n-K-1,
    nearby_distance_numerator=n-K-d-1,separation_fraction=f'{d}/{d+1}')
  assert best is not None;best['seconds_including_primality']=time.monotonic()-t0;rows.append(best);print(json.dumps(best),flush=True)
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,
  scope='Exact parameter and primality certificates for the proposed prime-order orbit theorem. The mathematical norm/classification proof must be audited separately.')
 (BASE/'parameters.json').write_text(json.dumps(out,indent=2)+'\n')
