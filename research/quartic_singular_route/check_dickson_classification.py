from math import comb
from itertools import product
from pathlib import Path
import json

def add(a,b,p):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]=(c[i]+x)%p
 for i,x in enumerate(b):c[i]=(c[i]+x)%p
 return c

def mul(a,b,p):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return c

def scale(a,c,p):return [(c*x)%p for x in a]
def residual(G,p):
 k=(p-1)//4;q=[0]*(2*k)+[1]
 G2=mul(G,G,p);Gp=[(i*G[i])%p for i in range(1,len(G))] or [0]
 A=add(add(scale(G2,2,p),[-1],p),scale(q,-1,p),p)
 B=add(add(scale(G2,4,p),[-1],p),scale(q,-3,p),p)
 return add([0]+scale(mul(A,Gp,p),4,p),mul(G,B,p),p)
rows=[]
for p in (5,13,17,29,41,73,97):
 k=(p-1)//4;e=2*k+1;good=[]
 for t in range(p):
  G=[comb(e,2*j+1)*pow(t,k-j,p)%p for j in range(k+1)]
  r=residual(G,p)
  assert all(r[j]==0 for j in range(2*k,3*k+1))
  ok=not any(r)
  assert ok==(t==0 or pow(t,2*k,p)==1)
  if ok:good.append(tuple(G))
 assert len(good)==2*k+1
 exhaustive=None
 if p in (5,13):
  allmonic=[tuple(c)+(1,) for c in product(range(p),repeat=k) if not any(residual(list(c)+[1],p))]
  assert set(allmonic)==set(good)
  exhaustive=p**k
 rows.append(dict(p=p,k=k,parameter_tests=p,exact_monic_count=len(good),exhaustive_monic_polynomials=exhaustive,status='passed'))
Path(__file__).with_name('dickson_classification_checks.json').write_text(json.dumps(rows,indent=2)+'\n')
print('Passed',len(rows),'prime fixtures;',sum(r['parameter_tests'] for r in rows),'parameter checks; exhaustive monic polynomials:',sum(r['exhaustive_monic_polynomials'] or 0 for r in rows))
