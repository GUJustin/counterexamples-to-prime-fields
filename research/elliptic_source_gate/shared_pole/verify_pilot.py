"""Independent pointwise rational-identity and bucket replay; stdlib only."""
import json
from pathlib import Path
from collections import Counter
from math import prod
P=Path(__file__).parent
j=json.loads((P/'pilot.json').read_text());p=211
assert (j['p'],j['ell'],j['curve_A'],j['curve_B'])==(211,5,0,16)
lab={tuple(k):None if v is None else tuple(v) for k,v in j['torsion_label_points']}
assert len(lab)==25 and len(set(lab.values()))==25
pts=[(x,y) for x in range(p) for y in range(p) if (y*y-x*x*x-16)%p==0]
assert len(pts)+1==225

def add(a,b):
 if a is None:return b
 if b is None:return a
 x,y=a;u,v=b
 if x==u and (y+v)%p==0:return None
 m=((v-y)*pow(u-x,p-2,p) if x!=u else 3*x*x*pow(2*y,p-2,p))%p
 z=(m*m-x-u)%p
 return z,(m*(x-z)-y)%p
for a,A in lab.items():
 assert A is None or A in pts
 for b,B in lab.items():assert add(A,B)==lab[((a[0]+b[0])%5,(a[1]+b[1])%5)]

def c(a):
 n=(a[0]*a[0]-2*a[1]*a[1])%5
 return 0 if n==0 else (1 if n in (1,4) else -1)
def pm(a,b):return ((a[0]-b[0])%5,(a[1]-b[1])%5)
def pp(a,b):return ((a[0]+b[0])%5,(a[1]+b[1])%5)
for a in lab:assert sum(c(b)*c(pm(a,b)) for b in lab)==(24 if a==(0,0) else -1)
reps=[tuple(a) for a in j['labels']]
assert set(reps)=={a for a in lab if a<=((-a[0])%5,(-a[1])%5)}
polys=j['coefficients'];assert len(set(map(tuple,polys)))==13
assert all(len(f)<=26 for f in polys)
def ev(f,x):return sum(v*pow(x,k,p) for k,v in enumerate(f))%p
poles={lab[a][0] for a in reps if a!=(0,0)};assert len(poles)==12
# Compare with the rational formula at all 199 nonpoles. After clearing,
# these are polynomial identities of degree at most 25, so this certifies
# every coefficient without reproducing the generator's multiplication.
for x in set(range(p))-poles:
 D=prod((x-t)**2 for t in poles)%p
 for a,f in zip(reps,polys):
  value=2*c(a)*x
  for b in reps:
   if b==(0,0):continue
   t=lab[b][0]
   R=2*(t*x*x+t*t*x+32)*pow((x-t)**2,p-2,p)
   value+=(c(pm(b,a))+c(pp(b,a)))*R
  assert ev(f,x)==D*value%p
# Independent direct group-action check at all finite elliptic nonpoles.
for x,y in pts:
 if x in poles:continue
 D=prod((x-t)**2 for t in poles)%p
 for a,f in zip(reps,polys):
  val=0
  for b in lab:
   for shift in (pp(b,a),pm(b,a)):
    z=add((x,y),lab[shift]);assert z is not None
    val+=c(b)*z[0]
  assert ev(f,x)==D*val%p
buckets=[max(Counter(ev(f,x) for f in polys).values()) for x in range(p)]
assert sum(sorted(buckets,reverse=True)[:100])==227==j['all_field_top100_incidence_sum']
assert sum(buckets)==338==j['all_field_total_incidence_sum']
for rec in j['records']:
 assert rec['values']==[ev(f,rec['x']) for f in polys]
 assert rec['max_bucket']==buckets[rec['x']]
out={'pass':True,'distinct_polynomials':13,'degrees':[max(k for k,v in enumerate(f) if v) for f in polys], 'all_field_bucket_histogram':dict(sorted(Counter(buckets).items())), 'all_field_top100_incidence_sum':227,'minimum_agreement_upper_bound':227//13,'rational_identity_test_points':199,'scope':'This fixed bank over F211, arbitrary 100 distinct affine coordinates and arbitrary word.'}
(P/'pilot.independent.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
