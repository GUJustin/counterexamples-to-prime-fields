#!/usr/bin/env python3
"""Independent check of conditional single-variable collision bounds."""
from pathlib import Path
import json, random
rng=random.Random(912026);p=37
conditional_cases=free_values=gap_two_cases=collision_cases=0
for q in range(1,11):
 for trial in range(20):
  x=rng.sample(range(p),q+4)
  A,B,z0,C=x[:4];z=[z0]+x[4:]
  def slopes(zz):
   out=[None];c=pow((z0-A)%p,-1,p)
   for j in range(1,q+1):
    out.append(c)
    if j<q:
     aa=A if j%2 else B;bb=B if j%2 else A
     c=c*(zz[j]-aa)*pow((zz[j]-bb)%p,-1,p)%p
   return out
  eligible=0
  for i in range(1,q+1):
   for j in range(i+2,q+1,2):
    others=set(x);others.remove(z[i]);solutions=[]
    for t in range(p):
     if t in others:continue
     zz=z.copy();zz[i]=t;c=slopes(zz)
     if c[i]==c[j]:solutions.append(t)
     free_values+=1
    assert len(solutions)<=1
    if j-i==2:
     assert not solutions;gap_two_cases+=1
    else:eligible+=1
    collision_cases+=bool(solutions);conditional_cases+=1
  assert eligible==max(q-3,0)**2//4
out={'status':'passed','prime':p,'conditional_pairs':conditional_cases,
     'free_variable_values':free_values,'gap_two_pairs_proved_collision_free_in_fixtures':gap_two_cases,
     'pairs_with_one_admissible_collision':collision_cases}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
