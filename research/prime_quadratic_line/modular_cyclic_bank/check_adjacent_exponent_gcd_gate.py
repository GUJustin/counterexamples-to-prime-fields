"""Small exact check of gcd bounds; native roots checked separately."""
from flint import nmod_poly
from itertools import product
import json
from math import isqrt
cases=[]
for p,h,r in [(19,6,3),(37,6,3),(73,12,6),(97,8,4),(97,4,8),(193,16,6),(193,6,16),(163,18,9)]:
 n=h*r
 assert n<p and (p-1)%n==0
 X=nmod_poly([0,1],p)
 D=[x for x in range(1,p) if pow(x,n,p)==1]
 data={}
 for tag in ('h','h_plus_2'):
  max_gcd=max_agreement=0; checks=0
  for a,b,c in product(range(1,6),range(6),range(1,6)):
   P=nmod_poly([c,b,a],p)
   F=X**h-P if tag=='h' else X**h*P-1
   G=P**r-1
   s=int(F.gcd(G).degree())
   K=min(h-2,2*r) if tag=='h' else min(h+2,2*r)
   bound=(h+2*r+2-K)//2 if tag=='h' else (h+2*r+4-K)//2
   assert s<=bound,(p,h,r,a,b,c,tag,s,bound)
   m=h if tag=='h' else -h
   T=sum(pow(x,m,p)==int(P(x)) for x in D)
   assert T<=s
   assert T<=isqrt(n)+2
   max_gcd=max(max_gcd,s); max_agreement=max(max_agreement,T); checks+=1
  data[tag]=dict(checks=checks,max_gcd=max_gcd,max_agreement=max_agreement,bound=bound)
 cases.append(dict(p=p,n=n,h=h,r=r,results=data))
print(json.dumps(dict(status='PASS',cases=cases,total=sum(v['checks'] for c in cases for v in c['results'].values())),indent=2))
