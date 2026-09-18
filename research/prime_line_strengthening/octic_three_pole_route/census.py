import json,itertools
from fractions import Fraction as Q
from math import lcm,isqrt
from pathlib import Path
P=Path(__file__).parent;out={}
for name,file in [('paley','fiber_patterns.json'),('orbit2','orbit2_bank83.json')]:
 D=json.loads((P.parent/'quadratic_one_pole_route'/file).read_text());masks=D['masks'];A=[[int(i in masks[j]) for j in range(7)] for i in range(7)];T=[[int(i in masks[j+7]) for j in range(7)] for i in range(7)]
 E=[[Q(x) for x in row]+[Q(i==j) for j in range(7)] for i,row in enumerate(A)]
 for j in range(7):
  k=next(k for k in range(j,7) if E[k][j]);E[j],E[k]=E[k],E[j];z=E[j][j];E[j]=[x/z for x in E[j]]
  for k in range(7):
   if k!=j:
    z=E[k][j];E[k]=[x-z*y for x,y in zip(E[k],E[j])]
 den=lcm(*(x.denominator for row in E for x in row[7:]));inv=[[int(x*den) for x in row[7:]] for row in E]
 patterns=[]
 def vectors(pos,sm,norm,bound,vec):
  if pos==7:
   if sm==target:yield tuple(vec)
   return
  for v in range(-min(5,isqrt(bound-norm)),min(3,isqrt(bound-norm))+1):
   left=6-pos;rem=target-sm-v
   if rem < -5*left or rem>3*left or (left and rem*rem>left*(bound-norm-v*v)):continue
   if not left and rem:continue
   yield from vectors(pos+1,sm+v,norm+v*v,bound,vec+[v])
 for target in range(3):
  B=14-4*target
  slacks=[]
  for inds in itertools.combinations_with_replacement(range(7),target):slacks.append([inds.count(i) for i in range(7)])
  for u in vectors(0,0,0,B,[]):
   rhs=[sum(T[i][j]*u[j] for j in range(7)) for i in range(7)]
   for d in slacks:
    twice=[-sum(inv[j][i]*(rhs[i]+d[i]) for i in range(7)) for j in range(7)]
    if any(v%den for v in twice):continue
    v=[x//den for x in twice]
    if any(x< -3 or x>5 for x in v):continue
    if sum(x*x for x in u)+sum(x*x for x in v)>B:continue
    mult=[3+x for x in v]+[5+x for x in u]
    assert sum(mult)==56 and sum(x*(x-1)//2 for x in mult)<=98
    assert all(sum(mult[j] for j in range(14) if i in masks[j])==27-d[i] for i in range(7))
    patterns.append(dict(multiplicities=mult,T=35+target,genus=sum(x*(x-1)//2 for x in mult),slack=d))
 out[name]=dict(p=D['p'],base=D['base'],word=D['word'],masks=masks,patterns=patterns)
 print(name,len(patterns),{s:sum(x['T']==s for x in patterns) for s in (35,36,37)})
(P/'census.json').write_text(json.dumps(out,indent=2))
