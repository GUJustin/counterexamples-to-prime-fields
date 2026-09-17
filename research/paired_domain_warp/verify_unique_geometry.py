"""Exhaustive all-potential-codeword checks for the signed-relation criterion."""
from itertools import combinations,product
from math import prod,isqrt
from pathlib import Path
import json,time
from verify_extension_profile import interpolate,evaluate,mul
BASE=Path(__file__).resolve().parent

def check(p,reps,D,zero,xfactor):
 assert all(p%d for d in range(2,isqrt(p)+1));m=len(reps);K=2*D-1+xfactor
 for signs in product([-1,0,1],repeat=m):
  if not any(signs):continue
  total=sum(e*a for e,a in zip(signs,reps))%p
  ratio=prod(pow((1-a)*pow(1+a,-1,p)%p,e,p) for e,a in zip(signs,reps))%p
  assert total or ratio!=1
 domain=[x for a in reps+[1] for x in (a,p-a)]+([0] if zero else [])
 w=[1]
 for a in reps[:D]:w=mul(w,[-a*a,0,1],p)
 if xfactor:w=[0]+w
 f=[evaluate(w,x,p) for x in domain];g=[0]*(2*m)+([1,p-1] if xfactor else [1,1])+([0] if zero else [])
 expected={}
 for I in combinations(reps,D):
  H=[1]
  for a in I:H=mul(H,[-a*a,0,1],p)
  if xfactor:H=[0]+H
  q=tuple((a-b)%p for a,b in zip(w,H));assert q[K:]==(0,0)
  z=-prod((1-a*a)%p for a in I)%p
  expected.setdefault(z,set()).add(q[:K])
 actual={};maxima=[0]*p
 for I in combinations(range(len(domain)),K):
  xs=[domain[i] for i in I];A=interpolate(xs,[f[i] for i in I],p);B=interpolate(xs,[g[i] for i in I],p)
  av=[evaluate(A,x,p) for x in domain];bv=[evaluate(B,x,p) for x in domain]
  for z in range(p):
   agreement=sum((a+z*b-v-z*u)%p==0 for a,b,v,u in zip(av,bv,f,g))
   maxima[z]=max(maxima[z],agreement)
   if agreement>=K+3:actual.setdefault(z,set()).add(tuple((a+z*b)%p for a,b in zip(A,B)))
 assert actual==expected and all(len(v)==1 for v in actual.values())
 assert maxima[0]==K+1 and all(maxima[z]==K+3 for z in actual)
 return dict(p=p,n=len(domain),K=K,extra_zero=zero,X_factor=xfactor,nearby_parameters=len(actual),all_nearby_unique=True)

if __name__=='__main__':
 start=time.monotonic();rows=[]
 for p,reps in [(101,[2,3,5]),(1031,[2,4,8])]:
  for zero,xfactor in [(False,0),(True,0),(True,1)]:rows.append(check(p,reps,2,zero,xfactor))
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start)
 (BASE/'unique_geometry_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
