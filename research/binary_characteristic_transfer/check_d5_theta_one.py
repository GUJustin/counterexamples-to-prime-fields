"""Bounded exact test of the named d=5, s=2, theta=1 all-label candidate."""
from flint import fq_default_ctx
from itertools import combinations, product
from collections import Counter
from pathlib import Path
import json
rows=[]
for p in (3,5,7,11):
 F=fq_default_ctx(p,5,'a'); counts=Counter()
 for i,j in combinations(range(5),2):
  slots=[(0,k) for k in range(i+1,5) if k!=j]+[(1,k) for k in range(j+1,5)]
  for vals in product(range(p),repeat=len(slots)):
   mat=[[0]*5 for _ in range(2)];mat[0][i]=mat[1][j]=1
   for (r,k),v in zip(slots,vals):mat[r][k]=v
   x,y=map(F,mat); X=[x];Y=[y]
   for k in range(4):X.append(X[-1]**p);Y.append(Y[-1]**p)
   def P(a,b):return X[a]*Y[b]-X[b]*Y[a]
   z=(P(2,4)-P(2,3))/P(3,4)
   counts[tuple(z.to_list())]+=1
 missing=[v for v in product(range(p),repeat=5) if v not in counts]
 expected=(p**5-1)*(p**4-1)//((p**2-1)*(p-1))
 assert sum(counts.values())==expected
 row=dict(p=p,field=str(F),theta=1,spaces=expected,labels=len(counts),alphabet=p**5,missing=missing,fiber_histogram=dict(sorted(Counter(counts.values()).items())))
 rows.append(row);print(json.dumps(row),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
