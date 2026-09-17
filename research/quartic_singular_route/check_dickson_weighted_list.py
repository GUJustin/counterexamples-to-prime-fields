"""Verify endpoint derivatives and all pairwise weighted multiplicity budgets."""
from check_dickson_cubic import ev
from math import comb
from itertools import combinations
from pathlib import Path
import json,random

def check(p):
 k=(p-1)//4;n=p-1;D=k-1;e=2*k+1
 ts=sorted({a*a%p for a in range(p)})
 gs={t:[comb(e,2*j+1)*pow(t,k-j,p)%p for j in range(k+1)] for t in ts}
 vals={t:{x:ev(g,x,p) for x in range(1,p)} for t,g in gs.items()}
 endpoint=0;regular=0
 for t,g in gs.items():
  der=[j*g[j]%p for j in range(1,k+1)]
  for x in range(1,p):
   h=vals[t][x];q=pow(x,2*k,p)
   if q==1 and h in [1,p-1]:
    expected=(-3*h*pow(8*x,-1,p) if t==x else -h*pow(4*x,-1,p))%p
    assert ev(der,x,p)==expected
    endpoint+=t==x;regular+=t!=x
 pairs=0
 for t,u in combinations(ts,2):
  weight=0
  for x in range(1,p):
   h=vals[t][x]
   if h!=vals[u][x]:continue
   if pow(x,2*k,p)==1:
    assert h in [1,p-1]
    if t!=x and u!=x:weight+=2
   else:
    assert h==0;weight+=1
  assert weight<=D,(p,t,u,weight,D)
  pairs+=1
 rng=random.Random(p)
 words=[[((1+pow(x,2*k,p))*pow(2,-1,p))%p for x in range(1,p)]]
 words += [[rng.randrange(p) for x in range(n)] for _ in range(20)]
 for word in words:
  counts=[sum(vals[t][x]==word[x-1] for x in range(1,p)) for t in ts]
  for A in range(1,n+1):
   delta4=4*A*A-3*n*D
   if delta4<=0:continue
   L=sum(c>=A for c in counts)
   # B/Delta = (16An+9n²−6nD)/(8A²−6nD).
   assert L*(8*A*A-6*n*D)<16*A*n+9*n*n-6*n*D
 return dict(p=p,bank=len(ts),pair_budgets=pairs,endpoint_derivatives=endpoint,regular_derivatives=regular,words=len(words))
if __name__=='__main__':
 result=[check(p) for p in [13,17,29,41,73,97]]
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))
