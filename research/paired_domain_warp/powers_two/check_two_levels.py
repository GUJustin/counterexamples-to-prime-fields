"""Exhaust every interpolation pencil to determine a whole finite-field line.

This enumerates K-coordinate supports, not field elements. Each additional
coordinate contributes either an identity or one explicitly solved parameter.
Thus it checks all field parameters even when p is large.
"""
from pathlib import Path
from itertools import combinations
from math import comb
import sys,json,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from verify_extension_profile import interpolate,evaluate,mul
BASE=Path(__file__).resolve().parent

def check(p,m,D,zero=False,xfactor=False):
 reps=[1<<i for i in range(1,m+1)];domain=[x for a in reps+[1] for x in (a,p-a)]+([0] if zero else [])
 K=2*D-1+int(xfactor);n=len(domain);w=[1]
 for a in reps[:D]:w=mul(w,[-a*a,0,1],p)
 if xfactor:w=[0]+w
 f=[evaluate(w,x,p) for x in domain];g=[0]*(2*m)+([1,p-1] if xfactor else [1,1])+([0] if zero else [])
 maxima={};near={};baseline=0
 for I in combinations(range(n),K):
  xs=[domain[i] for i in I];A=interpolate(xs,[f[i] for i in I],p);B=interpolate(xs,[g[i] for i in I],p)
  common=0;roots={}
  for x,v,u in zip(domain,f,g):
   a=evaluate(A,x,p);b=evaluate(B,x,p)
   if b==u:
    if a==v:common+=1
   else:
    z=(v-a)*pow(b-u,-1,p)%p;roots[z]=roots.get(z,0)+1
  baseline=max(baseline,common);assert common<K+3
  for z,c in roots.items():
   agreement=common+c;maxima[z]=max(maxima.get(z,0),agreement)
   if agreement>=K+3:near.setdefault(z,set()).add(tuple((a+z*b)%p for a,b in zip(A,B)))
 hist={n-baseline:p}
 for z,a in maxima.items():
  if a>baseline:hist[n-baseline]-=1;hist[n-a]=hist.get(n-a,0)+1
 assert sum(hist.values())==p and baseline==K+1
 assert len(near)==comb(m,D) and all(len(bank)==1 for bank in near.values())
 if not zero or xfactor:assert set(hist)=={n-K-1,n-K-3}
 else:assert hist.get(n-K-2,0)>0 # Deliberate negative control for parity scope.
 return dict(p=str(p),n=n,K=K,zero=zero,X_factor=xfactor,interpolation_pencils=comb(n,K),
  exact_distance_histogram={str(k):str(v) for k,v in sorted(hist.items())},nearby_parameters=len(near),all_nearby_unique=True)

if __name__=='__main__':
 start=time.monotonic();rows=[check(65537,3,2),check(65537,3,2,True),check(65537,3,2,True,True),check(2**61-1,4,2),check(2**61-1,6,3)]
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,
  scope='Exhaustive interpolation-pencil classification of every field parameter; the extra-zero odd-K case intentionally has an intermediate distance level.')
 (BASE/'two_level_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
