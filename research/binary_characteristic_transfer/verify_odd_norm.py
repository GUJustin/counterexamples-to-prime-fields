#!/usr/bin/env python3
"""Exact small regression of the odd-characteristic two-pole norm compiler."""
import json,time,resource
from collections import Counter
start=time.monotonic();p=3
# F_81=F_3[z]/(z^4+z+2), irreducible (also verify by absence of factors).
def digs(a):return [(a//3**i)%3 for i in range(4)]
def enc(a):return sum((v%3)*3**i for i,v in enumerate(a))
def add(a,b):return enc([u+v for u,v in zip(digs(a),digs(b))])
def neg(a):return enc([-v for v in digs(a)])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 z=[0]*7
 for i,u in enumerate(digs(a)):
  for j,v in enumerate(digs(b)):z[i+j]=(z[i+j]+u*v)%3
 for k in range(6,3,-1):
  v=z[k];z[k]=0;z[k-4]=(z[k-4]-2*v)%3;z[k-3]=(z[k-3]-v)%3
 return enc(z[:4])
def power(a,n):
 b=1
 while n:
  if n&1:b=mul(b,a)
  a=mul(a,a);n//=2
 return b
def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def pa(a,b):
 c=a[:]+[0]*max(0,len(b)-len(a))
 for i,v in enumerate(b):c[i]=add(c[i],v)
 return trim(c)
def pn(a):return [neg(v) for v in a]
def pm(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):c[i+j]=add(c[i+j],mul(u,v))
 return trim(c)
def pp(a,n):
 b=[1]
 while n:
  if n&1:b=pm(b,a)
  a=pm(a,a);n//=2
 return b
def scale(a,c):return trim([mul(v,c) for v in a])
def ev(a,x):
 y=0
 for v in a[::-1]:y=add(mul(y,x),v)
 return y
def divide(a,b):
 c=a[:];q=[0]*max(1,len(a)-len(b)+1);ib=power(b[-1],79)
 while len(c)>=len(b) and c!=[0]:
  k=len(c)-len(b);v=mul(c[-1],ib);q[k]=v
  for j,u in enumerate(b):c[k+j]=sub(c[k+j],mul(v,u))
  trim(c)
 return trim(q),c
assert all(power(a,80)==1 for a in range(1,81))
B=[a for a in range(81) if power(a,9)==a];assert len(B)==9
pole=next(a for a in range(81) if a not in B)
N=9;b=3;s=3;d=4;r=1;K=3;T=5
Lam=[0]*10;Lam[1]=2;Lam[9]=1
head=[0]*7;head[6]=1
counts=Counter()
for t in B:
 for u in B:
  if t==u:continue
  G=pa(scale(pp([t,1],d),2),scale(pp([u,1],d),2))
  F=pa(scale(pp([t,1],r),2),scale(pp([u,1],r),2))
  der=[mul(G[i],i%3) for i in range(1,len(G))]
  assert trim(der)==pp(F,b)
  assert pa(pp(G,b),pn(G))==pm(Lam,pp(F,b))
  J,rem=divide(Lam,G);assert rem==[0]
  P=pm(F,J)
  assert pp(P,b)==pa(pp(Lam,b-1),pn(pp(J,b-1)))
  C=pa(P,pn(head));assert len(C)-1<=K
  assert sum(ev(P,x)==0 for x in B)==T
  assert len(G)-1==d and sum(ev(G,x)==0 for x in B)==d
  counts[ev(P,pole)]+=1
assert len(counts)*16>=72 and max(counts.values())<=16
out=dict(field_characteristic=3,field_modulus=[2,1,0,0,1],native_size=9,challenge_size=81,ordered_pairs=72,dimension=K,agreement=T,pole=pole,distinct_values=len(counts),maximum_multiplicity=max(counts.values()),proved_multiplicity_bound=16,identities_and_strict_degree_pass=True,seconds=time.monotonic()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print(json.dumps(out,indent=2))
