"""Exact cyclotomic audit of modular five-point survivors."""
from pathlib import Path
import json,itertools,time
import sympy as s
start=time.monotonic();base=Path(__file__).parent;z=s.symbols('z');phi=sum(z**i for i in range(7))
def red(a):
 n,d=s.fraction(s.cancel(a));return s.rem(s.rem(n,phi,z)*s.invert(s.rem(d,phi,z),phi,z),phi,z).expand()
def mul(a,b):return s.rem(a*b,phi,z).expand()
def inv(a):return s.invert(a,phi,z).expand()
eta=z+z*z+z**4;alpha=(eta-1)/2;c=3*(eta+3)/4
nodes=[red(z**i) for i in range(7)]+[red(alpha*z**i) for i in range(7)]
word=[red(z**(5*i)) for i in range(7)]+[red(c*z**(5*i)) for i in range(7)]
d=json.loads((base/'five_old_point_gate.json').read_text());subsets=next(v for v in d['cases'] if v['bank']=='paley')['fresh_survivor_subsets']
def orbit(S):return {tuple(sorted((i//7)*7+(i%7+k)%7 for i in S)) for k in range(7)}
reps=sorted({min(orbit(S)) for S in subsets});assert len(set().union(*(orbit(S) for S in reps)))==len(subsets)
result=[]
for subset in reps:
 A=[[red(nodes[i]**j) for j in range(4)]+[word[i]] for i in subset];det=s.Integer(1)
 for j in range(5):
  pivot=next((i for i in range(j,5) if A[i][j]!=0),None)
  if pivot is None:det=s.Integer(0);break
  if pivot!=j:A[j],A[pivot]=A[pivot],A[j];det=-det
  v=A[j][j];det=mul(det,v);vi=inv(v)
  for i in range(j+1,5):
   factor=mul(A[i][j],vi)
   for k in range(j+1,5):A[i][k]=s.expand(A[i][k]-mul(factor,A[j][k]))
   A[i][j]=s.Integer(0)
 result.append({'representative':subset,'orbit_size':len(orbit(subset)),'exact_determinant':str(det),'vanishes':det==0})
out={'field':'Q(zeta7), phi7(z)=1+z+...+z^6','modular_prime':29,'records':result,'seconds':time.monotonic()-start}
(base/'paley_five_point_exact.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
