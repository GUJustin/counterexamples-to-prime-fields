"""Find and replay small exact product-image/affine-profile fixtures."""
from itertools import combinations,product
from math import prod
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def fixture(p,r,D):
 padding=list(range(1,r+1));core=list(range(r+1,(p+1)//2));m=len(core)
 images={}
 for I in combinations(core,D):
  v=tuple(prod((x*x-a*a)%p for a in I)%p for x in padding)
  images.setdefault(v,I)
 complete=len(images)==(p-1)**r
 row=dict(p=p,r=r,m=m,D=D,n=2*(m+r),K=2*D-1,image_size=len(images),group_size=(p-1)**r,complete=complete)
 if not complete:return row
 ref=tuple(core[:D]);domain=[a for x in core+padding for a in [x,p-x]]
 H=lambda I,x:prod((x*x-a*a)%p for a in I)%p
 w=[H(ref,x) for x in domain];K=2*D-1;far=len(domain)-2*D
 assert sum(v==0 for v in w)==K+1
 profiles={};checked=0
 for zs in product(range(p),repeat=r):
  target=tuple(-z%p if z else 1 for z in zs)
  I=images[target]
  candidate=[(a-H(I,x))%p for a,x in zip(w,domain)]
  received=list(w)
  for j,z in enumerate(zs):received[2*m+2*j]=(received[2*m+2*j]+z)%p;received[2*m+2*j+1]=(received[2*m+2*j+1]+z)%p
  wt=sum(z!=0 for z in zs);distance=sum(a!=b for a,b in zip(received,candidate))
  assert distance==far-2*wt
  # Root bound gives dist(w,C)=far; changing2wt positions gives the
  # matching lower bound, independent of enumeration of the code.
  profiles[str(wt)]=distance;checked+=1
 row.update(affine_points_checked=checked,distance_by_parameter_weight=profiles,far_distance=far,scope='Exact finite geometry fixture; no below-Elias or numerical-prescription claim.')
 return row

if __name__=='__main__':
 start=time.monotonic();rows=[fixture(17,1,3),fixture(19,1,4),fixture(37,2,8)]
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start)
 (BASE/'small_completion_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
