"""Replay the two-far-input consequence on a complete finite product image."""
from pathlib import Path
from itertools import combinations,product
from math import prod,comb
import json,time
BASE=Path(__file__).resolve().parent

if __name__=='__main__':
 start=time.monotonic();p=37;r=2;D=8;K=15;core=list(range(3,19));padding=[1,2];domain=[v for a in core+padding for v in (a,p-a)];n=len(domain)
 images={}
 for I in combinations(core,D):
  key=tuple(prod((x*x-a*a)%p for a in I)%p for x in padding);images.setdefault(key,I)
 assert len(images)==(p-1)**r
 def H(I,x):return prod((x*x-a*a)%p for a in I)%p
 ref=core[:D];f=[H(ref,x) for x in domain]
 distances=[]
 for z in range(p):
  zs=(1-z,z);target=tuple(-v%p if v%p else 1 for v in zs);I=images[target]
  Q=[(a-H(I,x))%p for a,x in zip(f,domain)];received=f.copy()
  for j,v in enumerate(zs):
   for k in [2*len(core)+2*j,2*len(core)+2*j+1]:received[k]=(received[k]+v)%p
  found=sum(a!=b for a,b in zip(received,Q));wt=sum(v%p!=0 for v in zs)
  assert found==n-K-1-2*wt
  distances.append(found)
 assert distances[:2]==[18,18] and distances[2:]==[16]*(p-2)
 counts=[]
 for q in [3,5,7,11]:
  for rr in range(2,6):
   actual=sum(all(v) and sum(v)%q==1 for v in product(range(q),repeat=rr))
   predicted=((q-1)**rr-(-1)**rr)//q
   assert actual==predicted and predicted<=q**(rr-1)
   counts.append(dict(p=q,r=rr,nearby_affine_coefficients=actual,total=q**(rr-1)))
 out=dict(status='passed',fixture=dict(p=p,n=n,K=K,r=r,exact_line_distances=distances,nearby_parameters=p-2,endpoint_separation_coordinates=2),affine_coefficient_counts=counts,seconds=time.monotonic()-start,scope='Explicit witnesses plus the degree/direction lower bound certify all field parameters of the toy line. The toy fixture is not a below-Elias numerical-bound violation; asymptotic and finite field guarantees come from completion certificates.')
 (BASE/'far_inputs_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
