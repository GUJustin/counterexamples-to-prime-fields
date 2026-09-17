"""Exhaustive interpolation replay, including all quadratic-extension parameters.

For each K-subset, interpolate f and g separately. At a base parameter the
candidate is A+zB. At every nonbase parameter, a coordinate agrees precisely
when both base coefficients agree. Thus this enumerates every codeword that
could have at least K agreements, without enumerating the whole extended code.
"""
from itertools import combinations
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def mul(a,b,p):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return c

def evaluate(c,x,p):
 y=0
 for a in reversed(c):y=(y*x+a)%p
 return y

def interpolate(xs,ys,p):
 out=[0]*len(xs)
 for i,(x,y) in enumerate(zip(xs,ys)):
  q=[1];den=1
  for j,v in enumerate(xs):
   if i!=j:q=mul(q,[-v,1],p);den=den*(x-v)%p
  scale=y*pow(den,-1,p)%p
  for j,c in enumerate(q):out[j]=(out[j]+scale*c)%p
 return out

if __name__=='__main__':
 start=time.monotonic();p=17;K=5;n=16;r=1
 core=list(range(2,9));domain=[v for a in core+[1] for v in (a,p-a)]
 w=[1]
 for a in core[:3]:w=mul(w,[-a*a,0,1],p)
 f=[evaluate(w,x,p) for x in domain];g=[0]*14+[1,1]
 assert len(w)-1==K+1 and sum(v==0 for v in f)==K+1
 maxima=[0]*p;lists=[set() for _ in range(p)];outside_max=0;subsets=0
 for I in combinations(range(n),K):
  xs=[domain[i] for i in I]
  A=interpolate(xs,[f[i] for i in I],p)
  B=interpolate(xs,[g[i] for i in I],p)
  av=[evaluate(A,x,p) for x in domain];bv=[evaluate(B,x,p) for x in domain]
  common=sum(a==v and b==u for a,b,v,u in zip(av,bv,f,g))
  outside_max=max(outside_max,common)
  for z in range(p):
   agreement=sum((a+z*b-v-z*u)%p==0 for a,b,v,u in zip(av,bv,f,g))
   maxima[z]=max(maxima[z],agreement)
   if agreement>=K+2*r+1:lists[z].add(tuple((a+z*b)%p for a,b in zip(A,B)))
  subsets+=1
 assert maxima==[K+1]+[K+3]*(p-1)
 assert outside_max==K+1
 assert not lists[0] and all(lists[z] for z in range(1,p))
 seen=set()
 for bank in lists:
  assert seen.isdisjoint(bank);seen.update(bank)
 # 3 is nonsquare modulo17, so F17[T]/(T^2-3) has 17^2 elements.
 assert pow(3,(p-1)//2,p)==p-1
 out=dict(status='passed',p=p,extension_size=p*p,n=n,K=K,interpolation_subsets=subsets,
   base_distances=[n-a for a in maxima],nonbase_parameters=p*p-p,
   exact_distance_at_every_nonbase_parameter=n-outside_max,
   base_list_sizes=[len(bank) for bank in lists],distinct_nearby_codewords=len(seen),
   scope='Exhaustive all-potential-witness interpolation; exact lists over both fields. Toy geometry, not a below-Elias certificate.',seconds=time.monotonic()-start)
 (BASE/'extension_profile_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
