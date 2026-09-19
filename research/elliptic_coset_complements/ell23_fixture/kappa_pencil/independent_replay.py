"""Independent stdlib group-law reconstruction and reverse-column rank audit."""
import json,hashlib,time
from pathlib import Path
r=Path(__file__).resolve().parent
start=time.monotonic()
f=json.loads((r.parent/'fixture.json').read_text()); cert=json.loads((r/'selected_supports.json').read_text())
p=1657

def add(P,Q):
 if P is None:return Q
 if Q is None:return P
 x,y=P;u,v=Q
 if x==u and (y+v)%p==0:return None
 m=((v-y)*pow((u-x)%p,-1,p) if x!=u else (3*x*x)*pow(2*y%p,-1,p))%p
 z=(m*m-x-u)%p
 return (z,(m*(x-z)-y)%p)
def mul(a,P):
 Q=None
 while a:
  if a&1:Q=add(Q,P)
  P=add(P,P);a//=2
 return Q
def ev(c,x):
 v=0
 for a in reversed(c):v=(v*x+a)%p
 return v
def loc(xs):
 c=[1]
 for x in xs:
  z=[0]*(len(c)+1)
  for i,a in enumerate(c):z[i]=(z[i]-x*a)%p;z[i+1]=(z[i+1]+a)%p
  c=z
 return c
basis=[tuple(x) for x in f['torsion_basis']]
rows=[]
for rec in cert['records']:
 h=f['subgroups'][rec['subgroup']];generator=tuple(h['generator'])
 H=[mul(j,generator) for j in range(23)]
 assert len(set(H))==23 and H[0] is None
 K=loc(sorted({Q[0] for Q in H[1:]}));assert K==h['K']
 a,c=rec['torsion_coordinates'];P=add(mul(a,basis[0]),mul(c,basis[1]))
 assert list(P)==rec['point'] and mul(23,P) is None and P not in H
 extras=sorted(mul(j,P)[0] for j in [1,2,4,5,6]);assert extras==rec['extra_x']
 fibers=[];tags=[]
 for j in [3,7]:
  A=mul(j,P);fiber=sorted({add(A,Q)[0] for Q in H})
  assert len(fiber)==23
  tag=(A[0]+sum(add(A,Q)[0]-Q[0] for Q in H[1:]))%p
  assert tag==ev(h['N'],A[0])*pow(ev(h['B'],A[0]),-1,p)%p
  fibers.append(fiber);tags.append(tag)
 assert tags==rec['tags_3_and_7']
 support=sorted(set(extras+fibers[0]+fibers[1]));assert len(support)==51 and support==rec['full_support']
 u=loc(support);assert u==rec['locator_coefficients_ascending']
 label=1
 for x in extras:label=label*ev(K,x)%p
 assert label==rec['label_kappa']
 for shift in range(40):
  left=[0]*91;left[shift:shift+52]=u
  rows.append(left+[label*x%p for x in left])
indices=[]
for item in cert['independent_rows']:
 assert item['stacked_row']==40*item['support_index']+item['recurrence_shift']
 indices.append(item['stacked_row'])
A=[rows[i] for i in indices]
mhash=hashlib.sha256(json.dumps(A,separators=(',',':')).encode()).hexdigest()
assert mhash==cert['independent_matrix_sha256']
# Different elimination order from producer; no FLINT imports.
rank=0
for col in reversed(range(182)):
 pivot=next((i for i in range(rank,182) if A[i][col]),None)
 if pivot is None:continue
 A[rank],A[pivot]=A[pivot],A[rank]
 inv=pow(A[rank][col],-1,p)
 A[rank]=[x*inv%p for x in A[rank]]
 for i in range(rank+1,182):
  v=A[i][col]
  if v:A[i]=[(x-v*y)%p for x,y in zip(A[i],A[rank])]
 rank+=1
assert rank==182
receipt={'status':'PASS','rank':rank,'supports_rebuilt':len(cert['records']),'matrix_sha256':mhash,'method':'Actual elliptic group law, Velu sum for tags, direct locator multiplication, pure-Python reverse-column elimination; no producer imports or FLINT','elapsed_seconds':time.monotonic()-start,'files':{x:hashlib.sha256((r/x).read_bytes()).hexdigest() for x in ['verify.py','selected_supports.json','receipt.json','independent_replay.py']}}
(r/'independent_replay.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
