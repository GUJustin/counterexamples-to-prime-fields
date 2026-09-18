"""Exhaustive quotient/product fixture in F_17^2; no asymptotic inference."""
from itertools import combinations
from pathlib import Path
import json
P=17; Q=P*P; S=P-1; R=8; M=18; J=(R-2)*M+1
# b^2=3; 3 is a quadratic nonresidue modulo17.
assert pow(3,(P-1)//2,P)==P-1
B=P

def add(x,y): return ((x%P+y%P)%P)+P*((x//P+y//P)%P)
def neg(x): return (-x%P)+P*((-(x//P))%P)
def sub(x,y): return add(x,neg(y))
def mul(x,y):
 a,c=x%P,x//P;d,e=y%P,y//P
 return (a*d+3*c*e)%P+P*((a*e+c*d)%P)
def power(x,n):
 z=1
 while n:
  if n&1:z=mul(z,x)
  x=mul(x,x);n//=2
 return z
def inv(x):
 assert x
 return power(x,Q-2)
def ev(c,x):
 y=0
 for a in reversed(c): y=add(mul(y,x),a)
 return y

def locator(tags):
 c=[1]
 for a in tags:
  d=[0]*(len(c)+1)
  for i,v in enumerate(c):
   d[i]=sub(d[i],mul(a,v));d[i+1]=add(d[i+1],v)
  c=d
 return c

bank={};count=0
for tags in combinations(range(1,P),R):
 v=locator(tags); z=ev(v,B)
 assert z
 bank.setdefault(z,(tags,v)); count+=1
assert len(bank)==Q-1
norms=[power(x,M) for x in range(Q)]
assert norms.count(0)==1
assert all(norms.count(a)==M for a in range(1,P))
f=[];g=[]
for y in norms:
 deninv=inv(sub(y,B))
 f.append(mul(sub(power(y,R),power(B,R)),deninv))
 g.append(neg(deninv))
checks=0
for product,(tags,v) in bank.items():
 lam=neg(product)
 # h(Y)=(p_S(Y)-p_S(b))/(Y-b), p_S(Y)=Y^r-V_S(Y).
 ps=[neg(a) for a in v[:-1]]
 numerator=ps[:];numerator[0]=sub(numerator[0],ev(ps,B))
 quotient=[0]*(len(numerator)-1)
 rem=numerator[:]
 for i in range(len(rem)-1,0,-1):
  quotient[i-1]=rem[i];rem[i-1]=add(rem[i-1],mul(B,rem[i]));rem[i]=0
 assert rem[0]==0 and len(quotient)-1==R-2
 matches=[]
 for x,y in enumerate(norms):
  residual=sub(add(f[x],mul(lam,g[x])),ev(quotient,y))
  assert residual==mul(ev(v,y),inv(sub(y,B)))
  if residual==0: matches.append(x)
 assert len(matches)==R*M and 0 not in matches
 checks+=1
def interpolate(tags, values):
 result=[0]*len(tags)
 for a,value in zip(tags,values):
  basis=locator([t for t in tags if t!=a])
  scale=mul(value,inv(ev(basis,a)))
  for i,c in enumerate(basis): result[i]=add(result[i],mul(scale,c))
 return result
tags=list(range(1,R))
fv=[mul(sub(power(a,R),power(B,R)),inv(sub(a,B))) for a in tags]
gv=[neg(inv(sub(a,B))) for a in tags]
wf=interpolate(tags,fv);wg=interpolate(tags,gv)
fmatch={x for x,y in enumerate(norms) if f[x]==ev(wf,y)}
gmatch={x for x,y in enumerate(norms) if g[x]==ev(wg,y)}
assert len(fmatch)==len(gmatch)==len(fmatch&gmatch)==(R-1)*M
out=dict(status='PASS',prime=P,extension_degree=2,irreducible='X^2-3',
 domain_size=Q,strict_degree_bound=J,norm_packet_size=M,
 subsets_enumerated=count,nonzero_products_covered=len(bank),
 labels_and_full_domain_residuals_checked=checks,
 canonical_agreements=R*M,source_agreement_bound=(R-1)*M,
 common_source_matches_attained=len(fmatch&gmatch),
 scope='Exhaustive toy product coverage and compiler; not a degree-five numerical check')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
