from pathlib import Path
from math import comb
from collections import Counter
from itertools import product
import json

folder=Path(__file__).resolve().parent
reports=[]
for path in sorted(folder.glob('p*d*.log')):
 z=json.loads(path.read_text().splitlines()[0]);p=z['p'];D=z['D'];n=p+1;m=n//2;nu=z['nu'];a=z['torus_a'];b=z['torus_b']
 assert pow(nu,(p-1)//2,p)==p-1 and (a*a-nu*b*b)%p==1
 points=[(x,1) for x in range(p)]+[(1,0)]
 q=[(x*x-nu*y*y)%p for x,y in points];assert all(q)
 groups=[[i for i in range(n) if pow(q[i],(p-1)//2,p)==sign] for sign in (1,p-1)]
 assert [len(g) for g in groups]==[m,m]
 inv=[pow(pow(t,D//2,p),-1,p) for t in q]
 def evaluate(coeff,pts):
  return tuple(sum(c*pow(x,j,p)*pow(y,D-j,p) for j,c in enumerate(coeff))%p*inv[i]%p for i,(x,y) in enumerate(pts))
 def nextpoints(pts):return [((a*x+nu*b*y)%p,(b*x+a*y)%p) for x,y in pts]
 cases=sum(comb(D,s)*(p-1)**(s-1) for s in range(1,z['max_terms']+1))
 assert z['cases']==cases==sum(r['count'] for r in z['rows'])
 witness=[]
 for row in z['rows']:
  coeff=row['coefficients'];assert len(coeff)==D+1 and coeff[-1]==0
  vals=evaluate(coeff,points);word=[0]*n
  for group in groups:
   hist=Counter(vals[i] for i in group);mode=min(hist,key=lambda v:(-hist[v],v))
   for i in group:word[i]=mode
  pts=points;orbit=set();agreements=[];affine=[]
  for j in range(m):
   vals=evaluate(coeff,pts);orbit.add(vals)
   agreements.append(sum(v==w for v,w in zip(vals,word)))
   affine.append(sum(vals[i]==word[i] for i in range(p)))
   pts=nextpoints(pts)
  assert len(orbit)==row['orbit'] and set(agreements)=={row['maximum_agreement']}
  assert min(affine)==row['maximum_agreement']-1
  K=D+1;M=min(affine)
  F=(8*p-K)*M*M-6*K*M*p+K*(4*K-5*p)*p
  witness.append(dict(orbit=row['orbit'],projective_agreement=row['maximum_agreement'],affine_minimum=M,affine_first_order_polynomial=F))
 if p==11:
  # Independent full enumeration in a different projective normalization:
  # fix the highest nonzero coefficient to one and allow every lower coefficient.
  counts=Counter();best={};above=Counter()
  perm=[]
  for x,y in nextpoints(points):perm.append(x*pow(y,-1,p)%p if y else p)
  for top in range(D):
   for lower in product(range(p),repeat=top):
    coeff=list(lower)+[1]+[0]*(D-top);vals=evaluate(coeff,points)
    M=sum(max(Counter(vals[i] for i in group).values()) for group in groups)
    v=vals;L=0
    while True:
     L+=1;v=tuple(v[perm[i]] for i in range(n))
     if v==vals:break
     assert L<=m
    counts[L]+=1;best[L]=max(best.get(L,0),M)
    K=D+1;F=(8*n-K)*M*M-6*K*M*n+K*(4*K-5*n)*n
    above[L]+=F>0
  for row in z['rows']:
   L=row['orbit'];assert (counts[L],best[L],above[L])==(row['count'],row['maximum_agreement'],row['above_curve'])
 reports.append(dict(p=p,D=D,cases=cases,complete_polynomial_space=z['max_terms']==D,witnesses=witness))
out=dict(status='passed',total_cases=sum(r['cases'] for r in reports),rows=reports,scope='All extremal witnesses replayed by homogeneous matrix substitution; case counts checked; full F11 search independently repeated. Other complete or sparse censuses rely on the audited C++ enumeration.')
folder.joinpath('verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
