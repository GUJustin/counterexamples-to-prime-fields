"""Independent orbit closure, brute root lifting, and Newton interpolation modulo17²."""
import json,itertools
from fractions import Fraction as F
from pathlib import Path
D=Path(__file__).parent;s=json.loads((D.parent/'local_search.json').read_text());rational=json.loads((D.parent/'rational_seed.json').read_text())
def add(a,b,m):return ((a[0]+b[0])%m,(a[1]+b[1])%m)
def sub(a,b,m):return ((a[0]-b[0])%m,(a[1]-b[1])%m)
def mul(a,b,m):return ((a[0]*b[0]+7*a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)
def inv(a,m):
 n=pow((a[0]*a[0]-7*a[1]*a[1])%m,-1,m);return(a[0]*n%m,-a[1]*n%m)
def pw(a,n,m):
 b=(1,0)
 for _ in range(n):b=mul(b,a,m)
 return b
def ev(c,x,m):
 a=(0,0)
 for b in reversed(c):a=add(mul(a,x,m),b,m)
 return a
dec=lambda a:(a%17,a//17)
enc=lambda a:a[0]+17*a[1]
zeta=dec(59)
def orbit(hits):
 out=set()
 for c in hits:
  c=list(map(dec,c))
  for conjugate in [False,True]:
   cc=[(a,-b%17) if conjugate else(a,b) for a,b in c]
   for r in range(3):out.add(tuple(mul(a,pw(zeta,r*j,17),17) for j,a in enumerate(cc)))
 return out
orig=json.loads((D/'full15.json').read_text());other=json.loads((D/'independent15.json').read_text())
expected=orbit([h['coefficients'] for h in orig['hits']]);actual=orbit(other['hits']);assert actual==expected and len(actual)==9
nodes=[mul((pow(y,11,17),0),pw(zeta,j,17),17) for y in range(1,17) for j in range(3)]
word=[(w,0) for w in s['word'] for _ in range(3)]
def rat(q,m):
 q=F(q);return(q.numerator*pow(q.denominator,-1,m)%m,0)
U=[rat(u,289) for u in rational['affine_nodes']];W=[rat(w,289) for w in rational['affine_word']]
lift=[]
for i,x in enumerate(nodes):
 target=sub((11,0),mul((3,0),U[i//3],289),289)
 options=[]
 for a,b in itertools.product(range(17),repeat=2):
  xx=(x[0]+17*a,x[1]+17*b)
  if pw(xx,3,289)==target:options.append(xx)
 assert len(options)==1;lift.append(options[0])
assert len(set(lift))==48
records=[]
for c in sorted(actual):
 support=[i for i,x in enumerate(nodes) if ev(c,x,17)==word[i]];assert len(support)==15
 normalized=[mul((10,0),a,17) for a in c]
 for j,a in enumerate(s['polynomials'][3]):normalized[3*j]=sub(normalized[3*j],(10*a%17,0),17)
 # Use LAST ten support nodes, unlike original first-ten Gaussian elimination.
 inds=support[-10:];xs=[lift[i] for i in inds];dd=[W[i//3] for i in inds]
 for k in range(1,10):
  for j in range(9,k-1,-1):dd[j]=mul(sub(dd[j],dd[j-1],289),inv(sub(xs[j],xs[j-k],289),289),289)
 poly=[dd[9]]
 for k in range(8,-1,-1):
  q=[(0,0)]*(len(poly)+1)
  for j,a in enumerate(poly):q[j]=sub(q[j],mul(xs[k],a,289),289);q[j+1]=add(q[j+1],a,289)
  q[0]=add(q[0],dd[k],289);poly=q
 assert [(a%17,b%17) for a,b in poly]==normalized
 residual=[sub(ev(poly,lift[i],289),W[i//3],289) for i in support]
 assert any(a!=(0,0) for a in residual) and all(a%17==b%17==0 for a,b in residual)
 records.append(dict(coefficients=list(map(enc,c)),support=support,interpolation_indices=inds,residual_div17=[[a//17,b//17] for a,b in residual]))
# Exact rational base has only16 candidates at threshold5 (proved by old census).
base=json.loads((D.parent/'ten_cubic_certificate.verified.json').read_text());assert base['old_ge5_count']==16
out=dict(pass_all=True,independent_canonical_hits=len(other['hits']),full_orbit_candidates=9,orbit_set_equality=True,fixed_cover_mod289_survivors=0,records=records)
(D/'lift15.independent.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='records'})
