"""Check degree budgets, cyclic root allocation, and far-input interpolation."""
from pathlib import Path
from itertools import product
from math import prod
import json,time
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();fixtures=0;interpolation=[]
 for p in (7,11):
  for r in range(1,5):
   for e in range(1,5):
    for t in range(1,5):
     nodes=list(range(t))
     for counts in product(range(1,r+1),repeat=t):
      if sum(counts)>e*r:continue
      bins=[[] for _ in range(r)];offset=0
      for z,a in zip(nodes,counts):
       for j in range(a):bins[(offset+j)%r].append(z)
       offset+=a
      assert all(len(b)<=e and len(b)==len(set(b)) for b in bins)
      profile=[]
      for z in range(p):
       coeff=[prod((z-x)%p for x in b)%p for b in bins]
       zeros=sum(v==0 for v in coeff);profile.append(zeros)
       assert zeros==(counts[z] if z<t else 0)
      assert sum(profile)==sum(counts)<=e*r;fixtures+=1
  for t in range(2,6):
   r=3*t;nodes=list(range(t));profile=[]
   for z in range(p):
    coeff=[]
    for j in nodes:
     num=prod((z-i)%p for i in nodes if i!=j)%p
     den=prod((j-i)%p for i in nodes if i!=j)%p
     coeff.append(num*pow(den,-1,p)%p)
    assert sum(coeff)%p==1 and sum(x*a for x,a in zip(nodes,coeff))%p==z
    zeros=(r//t)*sum(a==0 for a in coeff);profile.append(zeros)
    assert zeros==(r*(t-1)//t if z<t else 0)
   assert sum(profile)==r*(t-1)
   interpolation.append(dict(p=p,t=t,r=r,zero_coordinate_profile=profile,nearby_parameters=p-t))
 out=dict(status='passed',allocation_fixtures=fixtures,interpolation=interpolation,seconds=time.monotonic()-start,
  scope='Exact polynomial-coordinate checks inside the separately proved completed affine space; no new domain or fixed-gap claim.')
 (BASE/'curve_profiles_verification.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='interpolation'})
