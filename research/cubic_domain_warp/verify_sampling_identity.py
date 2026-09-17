"""Exhaust the distinct-coordinate/nonzero-direction averaging identity."""
from fractions import Fraction as F
from itertools import combinations,combinations_with_replacement,product
from math import comb,prod
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent
start=time.monotonic();p=7;U=p-1
images=[{1},{1,2},{1,3,5},{1,2,4,6},set(range(1,p))];R=len(images)
rows=[]
for q in range(1,R+1):
 total=0;missing=0;failures=0
 for selected in combinations(range(R),q):
  for directions in product(range(1,p),repeat=q):
   labels=set()
   for j,g in zip(selected,directions):labels.update(v*pow(g,-1,p)%p for v in images[j])
   miss=U-len(labels);missing+=miss;failures+=miss>0;total+=1
 exact=F(U,comb(R,q))*sum((prod(F(U-len(images[j]),U) for j in selected) for selected in combinations(range(R),q)),F(0))
 upper=U*(sum((F(U-len(S),U) for S in images),F(0))/R)**q
 assert F(missing,total)==exact<=upper
 assert F(failures,total)<=exact
 rows.append(dict(q=q,choices=total,expected_missing=str(exact),mean_bound=str(upper),failure_probability=str(F(failures,total))))
identities=0
for R0 in range(1,11):
 for values in combinations_with_replacement(range(4),R0):
  es=[1]+[0]*R0
  for x in values:
   for j in range(R0,0,-1):es[j]+=x*es[j-1]
  for q in range(1,R0+1):
   assert es[q]*R0**q<=comb(R0,q)*sum(values)**q;identities+=1
out=dict(status='passed',direction_coordinate_choices=sum(r['choices'] for r in rows),
         rows=rows,elementary_symmetric_inequalities=identities,seconds=time.monotonic()-start,
         scope='Exhaustive finite identity and probability checks; the uniform inequality is proved by pairwise averaging.')
(BASE/'sampling_identity_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
