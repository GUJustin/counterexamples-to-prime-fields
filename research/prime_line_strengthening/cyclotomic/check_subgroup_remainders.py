"""Targeted exact divisibility certificates for small-degree split Dickson roots."""
from math import comb,gcd
from functools import reduce
from pathlib import Path
import json
import sympy as s
rows=[]
for e in [5,7,11,13,17,19]:
 d=(e-1)//2; coefficients=[comb(e,2*j+1) for j in range(d+1)]
 for c in [2,3,4]:
  N=c*d; rem=[1]+[0]*(d-1)
  for _ in range(N):
   top=rem[-1];rem=[0]+rem[:-1]
   rem=[x-top*y for x,y in zip(rem,coefficients)]
  g=reduce(gcd,rem[1:],0)
  factors=s.factorint(g)
  possible=[int(p) for p in factors if p>e and (p-1)%N==0 and (p-1)%e in (0,e-2)]
  # e | p+1 or p-1; then root set is in F_p.
  valid=[]
  for p in possible:
   roots=[x for x in range(1,p) if sum(a*pow(x,j,p) for j,a in enumerate(coefficients))%p==0] if p<100000 else None
   valid.append(dict(p=p,p_over_N=p/N,root_count=None if roots is None else len(roots),roots=roots))
  rows.append(dict(e=e,d=d,N=N,gcd_nonconstant_remainder=g,factors={str(p):int(a) for p,a in factors.items()},candidates=valid))
out={'scope':'Exact complete prime obstruction per listed e,N; not an asymptotic classification.','rows':rows}
Path(__file__).with_name('subgroup_remainders.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
