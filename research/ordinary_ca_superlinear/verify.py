"""Complete p17 nearest census, orbit descent, and one/two-anchor CA replay."""
from itertools import product
from fractions import Fraction
from math import ceil
from pathlib import Path
from functools import reduce
import json,random
p=17;d=3;N=16;k=4;Q=p*p
add=lambda a,b:((a[0]+b[0])%p,(a[1]+b[1])%p)
sub=lambda a,b:((a[0]-b[0])%p,(a[1]-b[1])%p)
mul=lambda a,b:((a[0]*b[0]+d*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def ev(c,x):
 v=(0,0)
 for a in reversed(c):v=add(mul(v,x),(a,0))
 return v
def base_ev(c,x):
 v=0
 for a in reversed(c):v=(v*x+a)%p
 return v
word={x:(pow(x,2*k,p)+1-2*pow(x,k,p))*pow(2,-1,p)%p for x in range(1,p)}
M=-1;bank=[]
for c in product(range(p),repeat=k):
 S=[x for x in word if base_ev(c,x)==word[x]]
 if len(S)>M:M=len(S);bank=[(c,S)]
 elif len(S)==M:bank.append((c,S))
assert M==6 and len(bank)==22
# Orbit descent checked against an independent complete quotient census.
H=[x for x in range(1,p) if pow(x,k,p)==1]
profiles={};orbit_rows=[]
for c,S in bank:
 orbit={tuple(a*pow(h,j,p)%p for j,a in enumerate(c)) for h in H}
 r=len(orbit);dd=k//r
 assert k%r==0 and all(not a or j%dd==0 for j,a in enumerate(c))
 v=c[::dd];domain=sorted({pow(x,dd,p) for x in word})
 assert len(domain)==4*r
 wr={x:(pow(x,2*r,p)+1-2*pow(x,r,p))*pow(2,-1,p)%p for x in domain}
 m=sum(base_ev(v,x)==wr[x] for x in domain)
 assert dd*m==M
 if r not in profiles:
  maxq=max(sum(base_ev(a,x)==wr[x] for x in domain) for a in product(range(p),repeat=r))
  assert maxq==m
  profiles[r]=dict(orbit_size=r,fiber_size=dd,quotient_length=4*r,quotient_maximum=m,enumerated=p**r)
 orbit_rows.append(dict(coefficients=c,orbit_size=r,quotient_coefficients=v))

def replay(t):
 current=dict(word);cs=[list(c) for c,S in bank];anchors=[]
 for j in range(t):
  anchor=max(current,key=lambda x:sum(base_ev(c,x)==current[x] for c in cs))
  selected=[c for c in cs if base_ev(c,anchor)==current[anchor]]
  new=[]
  for c in selected:
   qq=[0]*(len(c)-1);qq[-1]=c[-1]
   for h in range(len(c)-2,0,-1):qq[h-1]=(c[h]+anchor*qq[h])%p
   assert (c[0]-current[anchor]+anchor*qq[0])%p==0
   new.append(qq)
  current={x:(w-current[anchor])*pow(x-anchor,-1,p)%p for x,w in current.items() if x!=anchor}
  cs=new;anchors.append(anchor)
  assert all(sum(base_ev(c,x)==w for x,w in current.items())==M-j-1 for c in cs)
 K=k-t;T=M-t+1;qpad=M-k+1
 oldmax=max(sum(base_ev(c,x)==w for x,w in current.items()) for c in product(range(p),repeat=K))
 assert oldmax==T-1
 universe=list(product(range(p),repeat=2))
 unused=[x for x in universe if x not in [(a,0) for a in word]]
 values={x:[ev(c,x) for c in cs] for x in unused}
 pads=sorted(unused,key=lambda x:len(set(values[x])),reverse=True)[:qpad]
 expectation=Q*(1-reduce(lambda a,x:a*(1-Fraction(len(set(values[x])),Q)),pads,Fraction(1)))
 rng=random.Random(20260917+t)
 for attempt in range(100):
  fp={x:rng.choice(universe) for x in pads};witness={}
  for x in pads:
   for i,v in enumerate(values[x]):witness[sub(v,fp[x])]=(i,x)
  if len(witness)>=ceil(expectation):break
 assert len(witness)>=ceil(expectation)
 for z,(i,x0) in witness.items():
  c=cs[i]
  count=sum(ev(c,(x,0))==(w,0) for x,w in current.items())+sum(ev(c,x)==add(fp[x],z) for x in pads)
  assert count>=T and ev(c,x0)==add(fp[x0],z)
 assert K-1+qpad==T-1
 return dict(anchors=anchors,n=len(current)+qpad,dimension=K,threshold=T,anchored_candidates=len(cs),old_polynomials_enumerated=p**K,old_maximum=oldmax,padding_points=pads,padding_values=[fp[x] for x in pads],exceptional_labels=sorted(witness),exceptional_count=len(witness),expected_union_ceiling=ceil(expectation),nonzero_direction_agreement_upper=K-1+qpad)
fixtures=[replay(t) for t in (1,2)]
parameter_cases=0
for r in range(41,10001):
 if r%3==0:continue
 t=r%3;qpad=(r-10*t)//3;n=4*r-t+qpad
 assert 3*n==13*(r-t) and Fraction(r,6)<=qpad<=Fraction(r,3)
 assert Fraction(Fraction(r,2)+1,n)>Fraction(3,26)
 for j in range(t):assert Fraction(Fraction(3*r,2)-j,4*r-j)>=Fraction(1,3)
 assert Fraction(qpad*r,36)>=Fraction(r*r,216)>=Fraction(n*n,4056)>Fraction(n*n,4096)
 parameter_cases+=1
result=dict(status='passed',source_polynomials_enumerated=p**k,source_maximum=M,nearest_list=len(bank),descent_profiles=list(profiles.values()),orbit_rows=orbit_rows,fixtures=fixtures,parameter_cases=parameter_cases,scope='Complete small-field nearest and quotient censuses; exact one/two-anchor witness replay. Ordinary-CA exclusion over the extension also uses interpolation and polynomial root counting. No numerical assertion of asymptotic prime selection or Elias for these small fixtures.')
Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({**{k:v for k,v in result.items() if k not in ('orbit_rows','fixtures')},'fixtures':[{k:v for k,v in row.items() if k not in ('padding_points','padding_values','exceptional_labels')} for row in fixtures]},indent=2))
