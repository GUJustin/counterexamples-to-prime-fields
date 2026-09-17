"""Exhaust coefficient spaces for the strengthened far-input consequences."""
from pathlib import Path
from itertools import product
from math import prod
import json,time
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();linear=[];tensor=[];lines=[]
 for p in (3,5,7,11):
  for t in range(2,6):
   actual=sum(sum(v)%p==0 or all(v) for v in product(range(p),repeat=t))
   affine=((p-1)**t-(-1)**t)//p
   expected=p**(t-1)+(p-1)*affine
   assert actual==expected
   # Fixed t may be repeated over any equal-sized groups of directions.
   for r in (t,2*t,5*t):
    input_weight=r//t
    assert 2*(r-input_weight)*t==2*r*(t-1)
   linear.append(dict(p=p,t=t,nearby=actual,total=p**t))
  for ell in range(1,5):
   count=0;vertices=list(product((0,1),repeat=ell))
   for x in product(range(p),repeat=ell):
    coeff=[prod(xx if bit else 1-xx for bit,xx in zip(b,x))%p for b in vertices]
    assert sum(coeff)%p==1
    near=all(coeff);assert near==all(xx not in (0,1) for xx in x)
    count+=near
   assert count==(p-2)**ell
   tensor.append(dict(p=p,ell=ell,nearby=count,total=p**ell))
  # Every geometric line in the completed two-dimensional parameter space.
  valid=0;hist={};budgets={}
  families=[[(z,(s*z+b)%p) for z in range(p)] for s in range(p) for b in range(p)]
  families += [[(b,z) for z in range(p)] for b in range(p)]
  for points in families:
   deficits=[2*sum(x==0 for x in point) for point in points]
   if 0 not in deficits:continue
   valid+=1;budget=sum(deficits);assert budget<=4
   pattern=tuple(sorted(x for x in deficits if x));hist[pattern]=hist.get(pattern,0)+1
   budgets[budget]=budgets.get(budget,0)+1
  assert valid==p*(p+1)-2
  assert hist=={(2,):2*(p-1),(4,):p-1,(2,2):(p-1)**2}
  lines.append(dict(p=p,all_geometric_lines=p*(p+1),lines_with_nearby_points=valid,
   profiles={str(k):v for k,v in hist.items()},distance_budget_histogram=budgets))
 out=dict(status='passed',linear=linear,tensor=tensor,lines=lines,seconds=time.monotonic()-start,
  scope='Exact coefficient and affine-line enumeration. The RS realization is supplied by the separately verified completed affine profile; these counts add no field/domain claim.')
 (BASE/'far_mixtures_verification.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('linear','tensor','lines')})
