"""Exhaust all small domains and all potentially optimal received symbols."""
from itertools import combinations,product
from pathlib import Path
import json,time

def fixture(p,k,L,n,coeff):
 g=next(g for g in range(1,p) if len({pow(g,i,p) for i in range(p-1)})==p-1)
 H=[pow(g,(p-1)//L*i,p) for i in range(L)]
 assert k%L==0 and n%L==0 and coeff[-1]==1 and coeff[1]!=0
 def G(x):return sum(a*pow(x,i,p) for i,a in enumerate(coeff))%p
 values={x:tuple((G(h*x%p)-pow(x,k,p))%p for h in H) for x in range(p)}
 modes=[]
 for i in range((p-1)//L):
  orbit=[G(pow(g,i,p)*h%p) for h in H]
  modes.append(max(orbit.count(v) for v in set(orbit)))
 target=sum(sorted(modes,reverse=True)[:n//L]);best=-1;words=0;domains=0
 for D in combinations(range(p),n):
  domains+=1
  # A symbol absent from every candidate has zero matches; replacing it
  # by any present symbol cannot reduce any candidate's agreements.
  for w in product(*(sorted(set(values[x])) for x in D)):
   counts=[sum(values[x][j]==v for x,v in zip(D,w)) for j in range(L)]
   low=min(counts);assert low<=target
   best=max(best,low);words+=1
 assert best==target
 return dict(p=p,k=k,L=L,n=n,coeff=coeff,optimal_agreement=target,
             domains=domains,received_words=words,includes_zero_domains=True)

if __name__=='__main__':
 start=time.monotonic()
 rows=[fixture(7,3,3,n,c) for n in (3,6) for c in ((0,1,1,1),(2,2,0,1))]
 rows += [fixture(13,4,2,4,(0,1,0,1,1))]
 out=dict(status='passed',fixtures=rows,seconds=time.monotonic()-start,
          scope='Exhausts all domains and every nondominated received word for the displayed orbit fixtures.')
 Path(__file__).with_name('orbit_domain_optimality_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
