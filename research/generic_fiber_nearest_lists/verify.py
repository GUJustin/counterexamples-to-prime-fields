"""Exact finite fixtures for generic-fiber nearest-list preservation.

Exhausts every determining support, not every polynomial in the field.
The general characteristic-zero claim is proved separately in PROOF.md.
"""
from itertools import combinations
from math import comb,isqrt
from pathlib import Path
import json
BASE=Path(__file__).resolve().parent

def evaluate(c,x,p):
 y=0
 for a in reversed(c): y=(y*x+a)%p
 return y

def interpolate(xs,ys,p):
 n=len(xs);c=[0]*n
 for i,x in enumerate(xs):
  f=[1];den=1
  for j,z in enumerate(xs):
   if i==j:continue
   nxt=[0]*(len(f)+1)
   for t,a in enumerate(f):nxt[t]=(nxt[t]-z*a)%p;nxt[t+1]=(nxt[t+1]+a)%p
   f=nxt;den=den*(x-z)%p
  scale=ys[i]*pow(den,-1,p)%p
  c=[(a+scale*b)%p for a,b in zip(c,f)]
 return tuple(c)

def maximum_list(xs,ys,k,p):
 seen=set();nearest=[];M=0
 for I in combinations(range(len(xs)),k):
  c=interpolate([xs[i] for i in I],[ys[i] for i in I],p)
  if c in seen:continue
  seen.add(c)
  a=sum(evaluate(c,x,p)==y for x,y in zip(xs,ys))
  if a>M:M=a;nearest=[c]
  elif a==M:nearest.append(c)
 return M,set(nearest),len(seen)

def main():
 results=[]
 for B,p in [(2,1009),(3,10009)]:
  assert all(p%d for d in range(2,isqrt(p)+1))
  source=[-2,-1,0,1,2];word=[2,1,0,1,2];k=2
  sm,sl,_=maximum_list([x%p for x in source],word,k,p)
  assert sm==3 and sl=={(0,1),(0,p-1)}
  fibers={}
  for x in range(1,p):fibers.setdefault(pow(x,B,p),[]).append(x)
  t=next(t for t in range(p) if all(len(fibers.get((t+a)%p,[]))==B for a in source))
  xs=[];ys=[]
  for a,y in zip(source,word):
   xs.extend(fibers[(t+a)%p]);ys.extend([y]*B)
  assert len(set(xs))==B*len(source)
  M,L,num=maximum_list(xs,ys,B*k,p)
  expected=set()
  for c in sl:
   row=[0]*(B*k);row[0]=(c[0]-t*c[1])%p;row[B]=c[1]
   expected.add(tuple(row))
  assert M==B*sm and L==expected,(B,p,t,M,len(L))
  # Noncomposed interpolants exist below the stated threshold.
  noncomposed=next(interpolate([xs[i] for i in I],[ys[i] for i in I],p)
      for I in combinations(range(len(xs)),B*k)
      if any(interpolate([xs[i] for i in I],[ys[i] for i in I],p)[j]
             for j in range(B*k) if j%B))
  a=sum(evaluate(noncomposed,x,p)==y for x,y in zip(xs,ys))
  assert B*k<=a<B*(k+1)
  results.append(dict(B=B,p=p,t=t,n=len(xs),dimension=B*k,maximum_agreement=M,
      complete_nearest_list=len(L),determining_supports=comb(len(xs),B*k),
      distinct_interpolants=num,nearest_polynomials=sorted(L),
      noncomposed_control_agreement=a))
 out=dict(status='passed',fixtures=results,scope='Complete finite-field nearest lists for two specializations. General generic-fiber theorem is a separate algebraic proof, not inferred from these fixtures.')
 (BASE/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))

if __name__=='__main__':main()
