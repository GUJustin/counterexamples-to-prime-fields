"""Small exact test of a conditional sorting inequality, not an asymptotic proof."""
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import json
checked=0
for m in [4,6,8]:
 cache={}
 def data(h):
  if h in cache:return cache[h]
  Q=max((v+k-1 for v,k in enumerate(h) if k),default=-1); ds=[]
  for q in range(Q+1):
   us=[q-v for v,k in enumerate(h) if 0<=q-v<k]
   R=sum(min(sum(u<=ell for u in us),m-ell) for ell in range(m))
   ds.append((len(us),q*len(us)+4*R))
  cache[h]=ds;return ds
 for h in product(range(8),repeat=4):
  if not h[0] or h==tuple(sorted(h,reverse=True)):continue
  ds=data(h);ss=data(tuple(sorted(h,reverse=True)));Q=len(ds)-1
  nc=cc=0;lo=max(F(Q,4*m),F(47,100))
  for cnt,cost in reversed(ds):
   nc+=cnt;cc+=cost
   if nc:lo=max(lo,F(cc,4*m*nc))
  if lo>=1:continue
  for H in range(Q,Q+17):
   def threshold(d):return F(sum((H-q+1)*c for q,(n,c) in enumerate(d)),4*m*sum((H-q+1)*n for q,(n,c) in enumerate(d)))
   a=threshold(ds);b=threshold(ss);checked+=1
   assert max(lo,a)>=min(b,F(1)),(m,H,h,a,b,lo)
out={'model':'saturated leading coefficient rho=1/4','multiplicities':[4,6,8],'columns':4,'heights':'0..7','H':'maxdegree..maxdegree+16','agreement':'47/100..1','conditions':['all retained degrees active','min derivative exponent0','total surplus maximal among prefixes'],'comparisons':checked,'counterexamples':0,'scope':'finite exact check only'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
