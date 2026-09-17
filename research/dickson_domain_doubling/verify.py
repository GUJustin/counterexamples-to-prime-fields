"""Independent tuple-field replay of the lower witness and search cover."""
from pathlib import Path
from itertools import combinations
from math import comb
import json
folder=Path(__file__).resolve().parent
r=json.loads((folder/'scan.log').read_text().splitlines()[0])
def add(x,y):return ((x[0]+y[0])%17,(x[1]+y[1])%17)
def mul(x,y):return ((x[0]*y[0]+3*x[1]*y[1])%17,(x[0]*y[1]+x[1]*y[0])%17)
def power(x,e):
 z=(1,0)
 while e:
  if e&1:z=mul(z,x)
  x=mul(x,x);e//=2
 return z
def neg(x):return (-x[0]%17,-x[1]%17)
assert pow(3,8,17)==16
for a in range(17):
 for b in range(17):
  if a or b:assert mul((a,b),power((a,b),287))==(1,0)
g=(r['domain_generator']%17,r['domain_generator']//17)
xs=[power(g,j) for j in range(32)];assert len(set(xs))==32 and power(g,32)==(1,0)
w=[add(mul((9,0),add((1,0),power(x,16))),neg(power(x,8))) for x in xs]
assert len(set(w))==4
for c in range(4):assert len(set(w[c::4]))==1
coeffs={0:9,2:16,4:7,6:2}
v=[]
for x in xs:
 value=(0,0)
 for e,c in coeffs.items():value=add(value,mul((c,0),power(x,e)))
 v.append(value)
assert sum(a==b for a,b in zip(v,w))==12
patterns={frozenset(a) for a in combinations(range(8),4)};sizes=[]
while patterns:
 a=next(iter(patterns));orb={frozenset((x+t)%8 for x in a) for t in range(8)};patterns-=orb;sizes.append(len(orb))
assert len(sizes)==10 and sum(sizes)==70
assert r['supports']==4*len(sizes)*comb(24,4)==425040
assert r['complete'] and r['successful_supports']==0 and r['maximum_agreement']==12
out=dict(status='passed',field='F17[T]/(T^2-3)',checked_inverses=288,domain_size=32,lower_witness_coefficients=coeffs,lower_witness_agreement=12,anchor_orbit_sizes=sorted(sizes),covered_supports=r['supports'],scope='Independent field arithmetic, lower witness, and anchor-cover replay. Upper bound uses the complete C++ determining-support enumeration; no general composition theorem.')
(folder/'verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
