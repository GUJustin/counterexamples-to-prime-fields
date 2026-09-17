"""Exhaustive base-two product decoding and small Kummer line geometry."""
from pathlib import Path
from math import comb,prod,isqrt
from itertools import combinations
import json,time,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'paired_domain_warp'))
from verify_extension_profile import interpolate,evaluate
BASE=Path(__file__).resolve().parent

def decode_integer(t,m):
 if t==1:return []
 s=t.bit_length();I=[]
 for i in range(2,m+2):
  if (t<<i)<=((1<<i)-1)*(1<<s):
   if t%((1<<i)-1):return None
   t//= (1<<i)-1;s-=i;I.append(i)
   if s<0:return None
 return I if t==1 and s==0 else None

def setup(b,d,m,c):
 assert all(b%q for q in range(2,isqrt(b)+1));p=(1<<b)-1;s=4
 for _ in range(b-2):s=(s*s-2)%p
 assert s==0 and (p-1)%d==0
 alpha=pow(2,pow(d,-1,b),p);omega=next(pow(h,(p-1)//d,p) for h in range(2,100) if pow(h,(p-1)//d,p)!=1)
 assert pow(alpha,d,p)==2 and pow(omega,d,p)==1 and omega!=1
 n=d*(m+1)+c;A=n*(1<<((m+c+d)//d));assert p>A**(d*(d-1))
 mu=[pow(omega,j,p) for j in range(d)];core=[pow(alpha,i,p)*w%p for i in range(2,m+2) for w in mu];extra=[pow(alpha,i,p) for i in range(m+2,m+c+2)];domain=core+extra+mu
 assert len(domain)==len(set(domain))==n
 return p,core,extra,domain

def sums(b,d,m,c):
 p,core,extra,domain=setup(b,d,m,c);xs=core+extra;total=old=hits=0
 for t in range(1<<len(xs)):
  mask=t^(t>>1)
  if t:
   change=mask^old;j=change.bit_length()-1;total=(total+(xs[j] if mask&change else -xs[j]))%p
  if total==0:
   assert mask>>(d*m)==0 and all((mask>>(d*i))&((1<<d)-1) in [0,(1<<d)-1] for i in range(m));hits+=1
  old=mask
 assert hits==1<<m
 return dict(b=b,d=d,m=m,c=c,subsets_checked=1<<len(xs),zero_sum_subsets=hits)

def lists(b,d,m,D,c):
 p,core,extra,domain=setup(b,d,m,c);n=len(domain);K=d*D-1;assert p>1<<(D*(2*m-D+3)//2)
 def loc(I,x):return prod((pow(x,d,p)-(1<<i))%p for i in I)%p
 ref=tuple(range(2,D+2));f=[loc(ref,x) for x in domain];g=[0]*(d*m+c)+[1]*d;expected={}
 for I in combinations(range(2,m+2),D):
  z=-loc(I,1)%p;expected[z]=tuple((v-loc(I,x))%p for v,x in zip(f,domain))
 assert len(expected)==comb(m,D)
 actual={};zero=0
 for I in combinations(range(n),K):
  xs=[domain[i] for i in I];A=interpolate(xs,[f[i] for i in I],p);B=interpolate(xs,[g[i] for i in I],p)
  av=[evaluate(A,x,p) for x in domain];bv=[evaluate(B,x,p) for x in domain];common=0;roots={}
  for aa,bb,v,u in zip(av,bv,f,g):
   if bb==u:common+=aa==v
   else:
    z=(v-aa)*pow(bb-u,-1,p)%p;roots[z]=roots.get(z,0)+1
  assert common<K+d+1;zero=max(zero,common+roots.get(0,0))
  for z,q in roots.items():
   if common+q>=K+d+1:actual.setdefault(z,set()).add(tuple((aa+z*bb)%p for aa,bb in zip(av,bv)))
 assert zero==K+1 and set(actual)==set(expected)
 assert all(actual[z]=={v} for z,v in expected.items())
 return dict(b=b,d=d,m=m,D=D,c=c,n=n,K=K,interpolation_pencils=comb(n,K),nearby_count=len(actual),every_nearby_unique=True)

if __name__=='__main__':
 start=time.monotonic();decoded=0
 for m in range(1,15):
  seen=set()
  for mask in range(1<<m):
   I=[i+2 for i in range(m) if mask>>i&1];T=prod((1<<i)-1 for i in I)
   assert T not in seen and decode_integer(T,m)==I;seen.add(T);decoded+=1
 rootrows=[sums(61,3,3,1),sums(521,5,2,2),sums(1279,7,2,5)]
 listrows=[lists(61,2,3,2,0),lists(61,3,3,2,1),lists(61,3,4,3,1),lists(521,5,2,1,2)]
 out=dict(status='passed',decoded_subsets=decoded,root_sum_rows=rootrows,line_rows=listrows,seconds=time.monotonic()-start,scope='Exhaustive integer product decoding, all subset sums on small Kummer domains, and every potentially nearby codeword via interpolation pencils.')
 (BASE/'kummer_small_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
