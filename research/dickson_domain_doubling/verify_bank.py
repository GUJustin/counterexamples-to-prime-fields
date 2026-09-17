"""Replay all extension-field nearest words and identify every composition."""
from pathlib import Path
from itertools import combinations
from math import comb
import json
folder=Path(__file__).resolve().parent
r=json.loads((folder/'bank_scan.log').read_text().splitlines()[0])
def add(x,y):return ((x[0]+y[0])%17,(x[1]+y[1])%17)
def mul(x,y):return ((x[0]*y[0]+3*x[1]*y[1])%17,(x[0]*y[1]+x[1]*y[0])%17)
def neg(x):return (-x[0]%17,-x[1]%17)
def sub(x,y):return add(x,neg(y))
def power(x,e):
 z=(1,0)
 while e:
  if e&1:z=mul(z,x)
  x=mul(x,x);e//=2
 return z
def decode(a):return (a%17,a//17)
def evaluate(cs,x):
 z=(0,0)
 for c in reversed(cs):z=add(mul(z,x),c)
 return z
xs=[power(decode(r['domain_generator']),j) for j in range(32)]
word=[sub(mul((9,0),add((1,0),power(x,16))),power(x,8)) for x in xs]
bank={tuple(map(decode,v)) for v in r['values']};assert len(bank)==r['bank_size']==22
bases=set()
for values in bank:
 c=list(values[:8])
 for h in range(1,8):
  for j in range(7,h-1,-1):c[j]=mul(sub(c[j],c[j-1]),power(sub(xs[j],xs[j-h]),287))
 coeff=[c[7]]
 for j in range(6,-1,-1):
  nxt=[(0,0)]*(len(coeff)+1)
  for t,v in enumerate(coeff):nxt[t]=sub(nxt[t],mul(xs[j],v));nxt[t+1]=add(nxt[t+1],v)
  nxt[0]=add(nxt[0],c[j]);coeff=nxt
 assert tuple(evaluate(coeff,x) for x in xs)==values
 assert sum(a==b for a,b in zip(values,word))==12
 assert all(coeff[j]==(0,0) for j in (1,3,5,7))
 assert all(coeff[j][1]==0 for j in (0,2,4,6))
 q=tuple(coeff[j][0] for j in (0,2,4,6));bases.add(q)
 assert sum(sum(a*pow(x,j,17) for j,a in enumerate(q))%17==((1+pow(x,8,17))*9-pow(x,4,17))%17 for x in range(1,17))==6
assert len(bases)==22
remaining=set(bank);sizes=[]
while remaining:
 v=next(iter(remaining));orbit={tuple(v[(j+4*t)%32] for j in range(32)) for t in range(8)}
 assert orbit<=bank;remaining-=orbit;sizes.append(len(orbit))
patterns={frozenset(a) for a in combinations(range(8),3)};orbits=0
while patterns:
 a=next(iter(patterns));patterns-={frozenset((x+t)%8 for x in a) for t in range(8)};orbits+=1
assert orbits==7 and r['supports']==4*orbits*comb(24,5)==1190112
assert r['complete'] and r['maximum_agreement']==12
out=dict(status='passed',nearest_list_size=22,maximum_agreement=12,all_polynomials_composed_from_base_field=True,base_coefficients=sorted(bases),orbit_sizes=sorted(sizes),support_count=r['supports'],scope='All 22 extension-field witnesses independently interpolated, identified as Q(X^2) with Q over F17 and verified on both domains. Completeness depends on the documented anchor cover and completed C++ enumeration. No general composition-preservation theorem.')
(folder/'bank_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='base_coefficients'},indent=2))
