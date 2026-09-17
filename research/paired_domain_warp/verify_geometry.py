"""Exact finite checks for paired-domain collision and padding identities."""
from itertools import combinations, product
from math import prod, isqrt, comb
from fractions import Fraction
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def curve(p):
 rows=[]
 for x in range(1,p):
  hist=[0]*p
  for a,b in product(range(p),repeat=2):
   hist[((x*x-a*a)*(x*x-b*b))%p]+=1
  upper=p+6*(isqrt(p)+1)+768
  assert max(hist[1:])<=upper
  rows.append(max(hist[1:]))
 return dict(p=p,curves=(p-1)**2,max_points=max(rows),upper=upper)

def domains(p,m,D):
 reps=range(1,(p+1)//2);L=comb(m,D);R=(p-1)//2-m
 total_collisions=0;number=0;max_collisions=0
 for seed in combinations(reps,m):
  supports=list(combinations(seed,D));outside=set(reps)-set(seed)
  core={a%p for a in seed}|{-a%p for a in seed}
  vals=lambda I,x:prod((x*x-a*a)%p for a in I)%p
  collisions=0
  for I,J in combinations(supports,2):
   u=len(set(I)-set(J))
   count=sum(vals(I,x)==vals(J,x) for x in outside)
   if u==1:assert count==0
   collisions+=count
  total_collisions+=collisions;number+=1;max_collisions=max(max_collisions,collisions)
  w=supports[0]
  for I in supports:
   # Leading term and odd terms cancel. Exact root agreement is 2D.
   assert sum(vals(I,x)==0 for x in core)==2*D
   assert all(vals(I,x)!=0 for x in outside)
   for x in outside:assert vals(I,x)==vals(I,-x)
 # Symmetry under seed relabeling makes this the uniform support-pair average.
 B=Fraction((p-1)*(p+6*(isqrt(p)+1)+768),2*p*(p-m*m)) if p>m*m else None
 if B is not None:assert Fraction(total_collisions,number)<=comb(L,2)*B
 return dict(p=p,m=m,D=D,L=L,domains=number,total_collisions=total_collisions,max_collisions=max_collisions,collision_bound=str(B))

if __name__=='__main__':
 start=time.monotonic()
 out=dict(status='passed',curves=[curve(p) for p in [37,41,43]],domains=[domains(17,4,2),domains(29,4,2),domains(23,5,3)],seconds=time.monotonic()-start,scope='Finite curve counts, pair symmetry, support collisions and exact root identities. Absolute irreducibility and the general averaging theorem require the written proof.')
 (BASE/'geometry_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
