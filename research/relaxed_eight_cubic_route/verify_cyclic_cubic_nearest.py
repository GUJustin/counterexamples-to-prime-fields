"""Independent FLINT matrix replay in reverse V/O/E coefficient order."""
import itertools,json,time,sys
from pathlib import Path
from fractions import Fraction as F
from flint import nmod_mat
D=Path(__file__).parent;seed=json.loads((D/'local_search.json').read_text());p=17;target=int(sys.argv[1]) if len(sys.argv)>1 else 18;start=time.monotonic();S=[];B=[]
for y,w in zip(seed['nodes'],seed['word']):
 t=next(t for t in range(17) if t**3%17==y);e=[pow(y,k,p) for k in range(4)];v=[pow(y,k,p) for k in range(3)]
 # Variables V2,V1,V0,O2,O1,O0,E3,E2,E1,E0.
 S.append([t*t*a%p for a in v[::-1]]+[t*a%p for a in v[::-1]]+e[::-1]+[w])
 B.append([[-t*a%p for a in v[::-1]]+v[::-1]+[0]*4+[0],[-t*t*a%p for a in v[::-1]]+[0]*3+e[::-1]+[w]])
def solve(rows):
 a,rank=nmod_mat(rows,17).rref();v=[0]*10;cnt=0
 for i in range(rank):
  j=next(j for j in range(11) if a[i,j]!=0)
  if j==10:return None,0
  v[j]=int(a[i,10]);cnt+=1
 return v,10-cnt
systems=0;unresolved=[];hits=[];byd={}
for d in range(1,8):
 count=0
 for I in itertools.combinations(range(16),d):
  rows=[r for j in I for r in B[j]];v,dim=solve(rows)
  if v is None:continue
  count+=1;m=target-2*d;prefix=16-m+dim
  if prefix>16:unresolved.append((I,dim));continue
  for J in itertools.combinations(range(prefix),dim):
   systems+=1;vv,dd=solve(rows+[S[j] for j in J])
   if vv is None:continue
   if dd:unresolved.append((I,J,dd));continue
   if not any(vv[:6]):continue
   valid=lambda row:sum(a*b for a,b in zip(row[:10],vv))%17==row[10]
   single=sum(map(valid,S));double=sum(all(map(valid,pair)) for pair in B)
   if single+2*double>=target:hits.append((vv,single,double))
 byd[d]=count
assert not hits and not unresolved
ref=json.loads((D/f'cyclic_cubic_nearest_gate_{target}.json').read_text());assert systems==ref['systems'] and {str(k):v for k,v in byd.items()}==ref['consistent_double_subsets']
# Confirm exact padded norms' J are never zero, independent of parity calculation.
nonzero={}
for label,disc in [('ten',17),('eleven',39)]:
 records=json.loads((D/f'{label}_quadratic_norm_independent.json').read_text())['records'];count=0
 def mul(a,b):return (a[0]*b[0]+disc*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
 for rec in records:
  E=[tuple(-F(t)/2 for t in a) for a in rec['B']];JJ=[tuple(-F(t) for t in a) for a in rec['C']]
  for i,a in enumerate(E):
   for j,b in enumerate(E):
    v=mul(a,b);JJ[i+j]=(JJ[i+j][0]+v[0],JJ[i+j][1]+v[1])
  assert any(a!=(0,0) for a in JJ);count+=1
 nonzero[label]=count
out=dict(pass_all=True,target=target,systems=systems,consistent_double_subsets=byd,hits=hits,unresolved=unresolved,nonzero_padded_J_counts=nonzero,scope='F17-coefficient degree<=9 candidates on full cubic fibers only',seconds=time.monotonic()-start)
(D/f'cyclic_cubic_nearest_gate_{target}.verified.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
