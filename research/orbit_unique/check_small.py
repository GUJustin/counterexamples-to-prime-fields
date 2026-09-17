"""Exhaustive root-sum rigidity and interpolation-pencil local-list fixtures."""
from pathlib import Path
from itertools import combinations
from math import comb,prod,isqrt
import sys,json,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'paired_domain_warp'))
from verify_extension_profile import interpolate,evaluate
BASE=Path(__file__).resolve().parent

def root(p,d):
 assert (p-1)%d==0
 for h in range(2,100):
  w=pow(h,(p-1)//d,p)
  if w!=1:assert pow(w,d,p)==1;return w
 raise AssertionError('no root found in fixture search')

def setup(p,d,m,c):
 A=(1<<(m+1))*(d+(1<<c));assert p>A**(d-1)
 w=root(p,d);powers=[pow(w,j,p) for j in range(d)]
 core=[(1<<i)*v%p for i in range(1,m+1) for v in powers];extra=[1<<(m+t) for t in range(1,c+1)];domain=core+extra+powers
 assert len(domain)==len(set(domain))==d*(m+1)+c
 return w,core,extra,domain

def sums(p,d,m,c):
 w,core,extra,domain=setup(p,d,m,c);xs=core+extra;count=0;hist={}
 # Gray order updates one summand, independently of the cyclotomic argument.
 total=0;previous=0
 for j in range(1<<len(xs)):
  mask=j^(j>>1)
  if j:
   diff=mask^previous;i=diff.bit_length()-1
   total=(total+(xs[i] if mask&diff else -xs[i]))%p
  if total==0:
   assert mask>>(d*m)==0
   for i in range(m):assert (mask>>(d*i))&((1<<d)-1) in [0,(1<<d)-1]
   count+=1;size=mask.bit_count();hist[size]=hist.get(size,0)+1
  previous=mask
 assert count==1<<m and hist=={d*j:comb(m,j) for j in range(m+1)}
 return dict(p_bits=p.bit_length(),d=d,m=m,c=c,subsets_checked=1<<len(xs),zero_sum_subsets=count)

def lists(p,d,m,D,c):
 omega,core,extra,domain=setup(p,d,m,c);n=len(domain);K=d*D-1;assert p>1<<(d*D*(2*m-D+1)//2)
 def loc(I,x):return prod((pow(x,d,p)-(1<<(d*i)))%p for i in I)%p
 ref=tuple(range(1,D+1));f=[loc(ref,x) for x in domain];g=[0]*(d*m+c)+[1]*d
 expected={}
 for I in combinations(range(1,m+1),D):
  z=-loc(I,1)%p;vals=tuple((v-loc(I,x))%p for v,x in zip(f,domain));expected[z]=vals
 assert len(expected)==comb(m,D)
 actual={};maxzero=0
 for I in combinations(range(n),K):
  xs=[domain[i] for i in I];A=interpolate(xs,[f[i] for i in I],p);B=interpolate(xs,[g[i] for i in I],p)
  av=[evaluate(A,x,p) for x in domain];bv=[evaluate(B,x,p) for x in domain]
  common=0;roots={}
  for a,b,v,u in zip(av,bv,f,g):
   if b==u:
    if a==v:common+=1
   else:
    z=(v-a)*pow(b-u,-1,p)%p;roots[z]=roots.get(z,0)+1
  assert common<K+d+1
  maxzero=max(maxzero,common+roots.get(0,0))
  for z,count in roots.items():
   if common+count>=K+d+1:actual.setdefault(z,set()).add(tuple((a+z*b)%p for a,b in zip(av,bv)))
 assert maxzero==K+1 and set(actual)==set(expected)
 for z,v in expected.items():assert actual[z]=={v}
 return dict(p=p,d=d,m=m,D=D,c=c,n=n,K=K,interpolation_pencils=comb(n,K),nearby_parameters=len(actual),all_nearby_unique=True)

if __name__=='__main__':
 start=time.monotonic()
 assert all(2013265921%q for q in range(2,isqrt(2013265921)+1))
 assert all(1279%q for q in range(2,isqrt(1279)+1))
 modulus=(1<<1279)-1; state=4
 for _ in range(1277):state=(state*state-2)%modulus
 assert state==0
 root_rows=[sums(2013265921,3,3,2),sums(2013265921,5,2,3),sums(2**1279-1,7,2,5)]
 list_rows=[lists(2013265921,3,3,2,0),lists(2013265921,3,4,3,1),lists(2013265921,5,2,1,3)]
 out=dict(status='passed',root_sum_rows=root_rows,list_rows=list_rows,seconds=time.monotonic()-start,
  scope='All subset sums in the root fixtures and every potentially nearby codeword on the test lines, via all interpolation pencils. Small fixtures test geometry, not numerical-bound violations.')
 (BASE/'small_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
