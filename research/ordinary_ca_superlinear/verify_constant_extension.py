"""Exact support censuses and an essential-hypothesis negative control."""
from itertools import combinations,product
from math import comb
from fractions import Fraction
from pathlib import Path
import json

class Quadratic:
 def __init__(self,p,nu):self.p=p;self.nu=nu;self.zero=(0,0);self.one=(1,0)
 def scalar(self,x):return (x%self.p,0)
 def add(self,x,y):return ((x[0]+y[0])%self.p,(x[1]+y[1])%self.p)
 def sub(self,x,y):return ((x[0]-y[0])%self.p,(x[1]-y[1])%self.p)
 def mul(self,x,y):return ((x[0]*y[0]+self.nu*x[1]*y[1])%self.p,(x[0]*y[1]+x[1]*y[0])%self.p)
 def inv(self,x):
  t=pow((x[0]*x[0]-self.nu*x[1]*x[1])%self.p,-1,self.p)
  return (x[0]*t%self.p,-x[1]*t%self.p)
 def conj(self,x):return (x[0],-x[1]%self.p)
 def ev(self,c,x):
  z=self.zero
  for a in reversed(c):z=self.add(self.mul(z,x),a)
  return z

def census(F,xs,ys,K):
 inverses={(i,j):F.inv(F.sub(xs[i],xs[j])) for i in range(len(xs)) for j in range(len(xs)) if i!=j}
 best=-1;bank=set();hits=0
 for S in combinations(range(len(xs)),K):
  c=[ys[i] for i in S]
  for j in range(1,K):
   for i in range(K-1,j-1,-1):c[i]=F.mul(F.sub(c[i],c[i-1]),inverses[S[i],S[i-j]])
  poly=[c[-1]]
  for j in range(K-2,-1,-1):
   out=[F.zero]*(len(poly)+1)
   for t,v in enumerate(poly):out[t]=F.sub(out[t],F.mul(xs[S[j]],v));out[t+1]=F.add(out[t+1],v)
   out[0]=F.add(out[0],c[j]);poly=out
  coeff=tuple(poly);M=sum(F.ev(coeff,x)==y for x,y in zip(xs,ys))
  if M>best:best=M;bank=set();hits=0
  if M==best:bank.add(coeff);hits+=1
 assert hits==len(bank)*comb(best,K)
 return best,bank

F=Quadratic(7,3);theta=(0,1)
xs=[F.scalar(x) for x in range(7)]
ys=[F.scalar(pow((x*x-3)%7,-1,7)) for x in range(7)]
M,bank=census(F,xs,ys,2);assert M==3
positive=[]
for a,b in combinations(range(7),2):
 A=[(a,1),(b,1)];assert set(A).isdisjoint(F.conj(x) for x in A)
 def Z(x):return F.mul(F.sub(x,A[0]),F.sub(x,A[1]))
 newxs=xs+A;newys=[F.mul(Z(x),y) for x,y in zip(xs,ys)]+[F.zero]*2
 maximum,newbank=census(F,newxs,newys,4);assert maximum==M+2
 for P in bank:
  assert sum(F.mul(Z(x),F.ev(P,x))==y for x,y in zip(newxs,newys))==M+2
 positive.append(dict(roots=A,maximum=maximum,nearest_list=len(newbank)))
# Full conjugate pair: the denominator of the old rational word is canceled.
A=[theta,F.conj(theta)]
def Zbad(x):return F.mul(F.sub(x,A[0]),F.sub(x,A[1]))
badys=[F.mul(Zbad(x),y) for x,y in zip(xs,ys)]+[F.zero]*2
badmaximum,badbank=census(F,xs+A,badys,4)
assert badmaximum==7>M+2 and all(y==F.one for y in badys[:7])

# Exact census of every outside-base-field assignment for a two-coordinate
# noise block. The refined union bound is already below one in this fixture.
oldxs=[F.scalar(x) for x in (1,2,3,4)]
oldys=[F.scalar(pow(x,-1,7)) for x in (1,2,3,4)]
oldM,oldbank=census(F,oldxs,oldys,2);assert oldM==2
coords=oldxs+[F.scalar(0),F.scalar(5)]
outside=[(a,b) for a in range(7) for b in range(1,7)]
hist={};good_example=None
for noise in product(outside,repeat=2):
 mx,newbank=census(F,coords,oldys+list(noise),2)
 hist[mx]=hist.get(mx,0)+1
 if mx==oldM:
  assert oldbank.issubset(newbank)
  if good_example is None:good_example=noise
assert hist=={2:1596,3:168},hist
bound=sum(Fraction(comb(4,l)*comb(2,3-l)*49**(2-l),42**(3-l)) for l in range(2) if 0<=3-l<=2)
assert Fraction(hist[3],42**2)<=bound==Fraction(1,9)<1

out=dict(status='passed',field='F7[T]/(T^2-3)',source_dimension=2,source_maximum=M,source_nearest_list=len(bank),positive_zero_blocks=positive,conjugate_pair_negative_control=dict(maximum=badmaximum,preserved_target=M+2),noise=dict(assignments=42**2,maximum_histogram=hist,union_bound=str(bound),actual_failure_fraction=str(Fraction(hist[3],42**2)),example=good_example),scope='Complete determining-support censuses verify every zero-block fixture and all 1764 noise assignments; negative control shows why conjugate-pair avoidance is needed. General claims rely on the separate proofs.')
Path(__file__).with_name('constant_extension_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
