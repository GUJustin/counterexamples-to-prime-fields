"""Exhaust small orbit subset coefficients and sampled entire-line lists."""
from pathlib import Path
from itertools import combinations
from math import comb,isqrt,prod
import random,json,time,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'paired_domain_warp'))
from verify_extension_profile import interpolate,evaluate
BASE=Path(__file__).resolve().parent

def trial(p,d,m,D,c,rng):
 omega=next(pow(h,(p-1)//d,p) for h in range(2,p) if pow(h,(p-1)//d,p)!=1)
 mu=[pow(omega,j,p) for j in range(d)]
 assert len(set(mu))==d
 for mask in range(1,(1<<d)-1):assert sum(mu[j] for j in range(d) if mask>>j&1)%p
 while True:
  a=[rng.randrange(p) for _ in range(m)];extra=[rng.randrange(p) for _ in range(c)]
  core=[v*w%p for v in a for w in mu];domain=core+extra+mu
  if len(domain)==len(set(domain)):break
 xs=core+extra;total=0;old=0;forbidden=[]
 for t in range(1<<len(xs)):
  mask=t^(t>>1)
  if t:
   delta=mask^old;j=delta.bit_length()-1;total=(total+(xs[j] if delta&mask else -xs[j]))%p
  genuine=mask>>(d*m)==0 and all((mask>>(d*i))&((1<<d)-1) in [0,(1<<d)-1] for i in range(m))
  if not total and not genuine:forbidden.append(mask)
  old=mask
 labels={};n=len(domain);K=d*D-1
 def loc(I,x):return prod((pow(x,d,p)-pow(a[i],d,p))%p for i in I)%p
 ref=tuple(range(D));f=[loc(ref,x) for x in domain];g=[0]*len(xs)+[1]*d
 for I in combinations(range(m),D):
  z=-loc(I,1)%p;labels.setdefault(z,set()).add(tuple((v-loc(I,x))%p for v,x in zip(f,domain)))
 actual={}
 for I in combinations(range(n),K):
  xx=[domain[i] for i in I];A=interpolate(xx,[f[i] for i in I],p);B=interpolate(xx,[g[i] for i in I],p)
  av=[evaluate(A,x,p) for x in domain];bv=[evaluate(B,x,p) for x in domain];common=0;roots={}
  for v,u,aa,bb in zip(f,g,av,bv):
   if u==bb:common+=v==aa
   else:
    z=(aa-v)*pow(u-bb,-1,p)%p;roots[z]=roots.get(z,0)+1
  assert common<K+d+1
  for z,k in roots.items():
   if common+k>=K+d+1:actual.setdefault(z,set()).add(tuple((aa+z*bb)%p for aa,bb in zip(av,bv)))
 if not forbidden:assert actual==labels
 injective=len(labels)==comb(m,D)
 if not forbidden and injective:assert all(len(v)==1 for v in actual.values())
 return dict(p=p,d=d,m=m,D=D,c=c,n=n,K=K,forbidden_zero_sums=len(forbidden),
  product_injective=injective,nearby_parameters=len(actual),criterion_applies=not forbidden,
  all_nearby_unique=all(len(v)==1 for v in actual.values()))

if __name__=='__main__':
 start=time.monotonic();rng=random.Random(20260917)
 fixtures=[(1009,3,3,2,1),(2013265921,3,4,3,1),(65521,5,2,1,2)]
 for p,d,m,D,c in fixtures:
  assert all(p%q for q in range(2,isqrt(p)+1)) and p>d**(d-1) and (p-1)%d==0
 rows=[trial(*args,rng) for args in fixtures for _ in range(3)]
 assert any(row['criterion_applies'] for row in rows)
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,
  scope='Exhaustive subset sums and all interpolation pencils on nine small fixed random domains. This tests the sufficient geometry criterion, not asymptotic probability by simulation.')
 (BASE/'random_small_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
