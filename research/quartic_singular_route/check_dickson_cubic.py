"""Exact coefficient identities, full ordinary core, and existing list counts."""
from math import comb
from pathlib import Path
import json

def add(a,b,p):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return [x%p for x in c]
def scale(a,c,p):return [x*c%p for x in a]
def mul(a,b,p):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return c
def ev(a,x,p):
 v=0
 for c in reversed(a):v=(v*x+c)%p
 return v

def check(p):
 k=(p-1)//4;e=2*k+1;q=[0]*(2*k)+[1];S=add([1],q,p)
 bank=set(); counts=[]
 for a in range(p):
  G=[comb(e,2*j+1)*pow(a,2*k-2*j,p)%p for j in range(k+1)]
  der=[j*G[j]%p for j in range(1,len(G))]
  G2=mul(G,G,p)
  left=add(mul([0,4],mul(add(scale(G2,2,p),scale(S,-1,p),p),der,p),p),mul(G,add(add(scale(G2,4,p),[-1],p),scale(q,-3,p),p),p),p)
  assert all(c==0 for c in left),(p,a)
  assert add(scale(G2,2,p),scale(S,-1,p),p)[-1]==1
  if a:
   P=tuple(G[:-1]);bank.add(P)
   assert P[-1]==-a*a*pow(8,-1,p)%p
   if p%8==1:
    match=[x for x in range(1,p) if ev(G,x,p)==(1+pow(x,2*k,p))*pow(2,-1,p)%p]
    assert len(match)==3*k//2
    assert sum(pow(x,2*k,p)==1 for x in match)==k//2
    counts.append(len(match))
 for x in range(1,p):
  qx=pow(x,2*k,p);g=(1+qx)*pow(2,-1,p)%p
  assert 4*x*(2*g*g-1-qx)%p==0
  assert g*(4*g*g-1-3*qx)%p==0
 assert len(bank)==2*k
 return dict(p=p,D=k-1,all_parameter_identities=p,distinct_nonzero_bank=len(bank),ordinary_core=p-1,agreement=(3*k//2 if counts else None))
if __name__=='__main__':
 result=[check(p) for p in [13,17,29,41,73,97]]
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))
