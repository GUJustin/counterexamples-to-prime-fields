"""Independent Fraction arithmetic; no SymPy or source construction imported."""
from fractions import Fraction as F
import json
from pathlib import Path
class K:
 def __init__(self,a=0): self.a=a.a if isinstance(a,K) else tuple(map(F,a if isinstance(a,(tuple,list)) else (a,0,0)))
 def __add__(self,b): b=K(b);return K(tuple(x+y for x,y in zip(self.a,b.a)))
 __radd__=__add__
 def __neg__(self):return K(tuple(-x for x in self.a))
 def __sub__(self,b):return self+-K(b)
 def __rsub__(self,b):return K(b)+-self
 def __mul__(self,b):
  b=K(b);c=[F(0)]*5
  for i,x in enumerate(self.a):
   for j,y in enumerate(b.a):c[i+j]+=x*y
  for j in (4,3):
   c[j-1]-=2*c[j];c[j-2]+=c[j];c[j-3]+=c[j]
  return K(c[:3])
 __rmul__=__mul__
 def __pow__(self,n):
  assert n>=0;r=K(1)
  for _ in range(n):r=r*self
  return r
 def __bool__(self):return any(self.a)
 def __eq__(self,b):return self.a==K(b).a
 def inv(self):
  assert self
  cols=[(self*K([int(i==j) for i in range(3)])).a for j in range(3)]
  m=[[cols[j][i] for j in range(3)]+[F(i==0)] for i in range(3)]
  for j in range(3):
   q=next(i for i in range(j,3) if m[i][j]);m[j],m[q]=m[q],m[j];v=m[j][j];m[j]=[a/v for a in m[j]]
   for i in range(3):
    if i!=j:
     v=m[i][j];m[i]=[a-v*b for a,b in zip(m[i],m[j])]
  return K([m[i][3] for i in range(3)])
 def __truediv__(self,b):return self*K(b).inv()
 def __rtruediv__(self,b):return K(b)*self.inv()
 def out(self):return [str(a) for a in self.a]
w=K([0,1,0]);assert w**3+2*w**2-w-1==0
# The monic cubic has no rational root (+/-1), hence is irreducible.
coeffs=[['0','0','0','0'],['1','-3*w**2-6*w+2','2*w**2+5*w+1','4*w**2+5*w-9'],['1-w','-3*w**2-4*w+4','3*w**2+5*w-4','3*w**2+4*w-6'],['1','-2*w-3','3*w**2+7*w-1','-w-2'],['1','-w**2-3*w','6*w**2+10*w-9','3*w**2+4*w-6'],['w**2+w','-2*w**2-4*w','w**2+3*w+1','3*w**2+4*w-6'],['1','-w-3','6*w**2+10*w-8','3*w**2+4*w-6']]
P=[[K(eval(s,{'w':w})) for s in a] for a in coeffs]
def ev(P,x):
 if x is None:return P[3]
 r=K(0)
 for c in reversed(P):r=r*x+c
 return r
nodes=[None,K(0),K(1),w*w,w*w+w-1,w,w*w+w,1-w*w,w*w+2*w-1,w*w+2*w+1,w*w-1,-w*w-2*w+3,3*w*w-1,(3*w*w+4*w-1)/7]
masks=[[3,5,6,7],[2,4,5,7],[2,3,4,6],[1,4,5,6],[1,3,4,7],[1,2,6,7],[1,2,3,5],[1,2,3],[1,4,5],[1,6,7],[2,4,6],[2,5,7],[3,4,7],[3,5,6]]
for i in range(14):
 for j in range(i):assert nodes[i] is None or nodes[j] is None or nodes[i]!=nodes[j]
for x,S in zip(nodes,masks):
 target=ev(P[S[0]-1],x);assert [i+1 for i,q in enumerate(P) if ev(q,x)==target]==S
assert all(sum(i in S for S in masks)==7 for i in range(1,8))
# Explicit PGL map X=2+1/T; none of the original nodes is 2.
a=K(2);assert all(x is None or x!=a for x in nodes)
Q=[[q[3],q[2]+3*a*q[3],q[1]+2*a*q[2]+3*a*a*q[3],ev(q,a)] for q in P]
tnodes=[K(0) if x is None else 1/(x-a) for x in nodes]
word=[]
for t,S in zip(tnodes,masks):
 target=ev(Q[S[0]-1],t);word.append(target)
 assert [i+1 for i,q in enumerate(Q) if ev(q,t)==target]==S
assert len({tuple(q[3].a) for q in Q})==7
out={'verdict':'PASS','field_polynomial':'w^3+2w^2-w-1','arithmetic':'independent fractions in basis 1,w,w^2','affine_map':'X=2+1/T; Q_i(T)=T^3 P_i(2+1/T)','affine_nodes':[x.out() for x in tnodes],'affine_polynomials':[[x.out() for x in q] for q in Q],'affine_word':[x.out() for x in word],'agreement_masks':masks,'agreement_counts':[7]*7,'distinct_pair_count':91,'distinct_polynomial_leading_coefficients':7}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['affine_nodes','affine_polynomials','affine_word','agreement_masks']}))
