"""Independent standard-library direct syndrome replay of ONE saved pair."""
import json,hashlib,time
from pathlib import Path
root=Path(__file__).parent;start=time.monotonic()
raw=(root/'fixture.json').read_bytes();f=json.loads(raw)
p=f['p'];t=(f['ell']-1)//2;Z=[7,231,340,411,470];d=len(Z)
xs=[x for x in f['domain'] if x not in Z];k=f['k']+d;rows=len(xs)-k
assert (p,len(xs),k,rows)==(1657,259,178,81)
def ev(c,x):
 z=0
 for a in reversed(c):z=(z*x+a)%p
 return z
def rank(A):
 A=[r[:] for r in A];rank=0
 for j in range(len(A[0])):
  pivot=next((i for i in range(rank,len(A)) if A[i][j]),None)
  if pivot is None:continue
  A[rank],A[pivot]=A[pivot],A[rank]
  inv=pow(A[rank][j],-1,p)
  A[rank]=[v*inv%p for v in A[rank]]
  for i in range(rank+1,len(A)):
   c=A[i][j]
   if c:A[i]=[(a-c*b)%p for a,b in zip(A[i],A[rank])]
  rank+=1
 return rank
weights=[]
for x in xs:
 v=1
 for y in xs:
  if x!=y:v=v*(x-y)%p
 weights.append(pow(v,-1,p))
# Every parity/code product is a moment of degree at most len(xs)-2.
assert all(sum(w*pow(x,j,p) for w,x in zip(weights,xs))%p==0 for j in range(len(xs)-1))
S=[]
for index in (1,2):
 h=f['subgroups'][index];assert not(set(h['kernel_x'])&set(Z))
 values=[]
 for x in xs:
  K=ev(h['K'],x);N=ev(h['N'],x)
  row=[]
  for i in range(3):
   e=pow(N,t-3+i,p)*pow(pow(K,2*i+1,p),-1,p)%p if K else 0
   row.extend(e*pow(x,j,p)%p for j in range(d+1))
  values.append(row)
 A=[[sum(w*pow(x,i,p)*v[j] for w,x,v in zip(weights,xs,values))%p for j in range(18)] for i in range(rows)]
 assert rank(A)==18;S.append(A)
joined=[a+b for a,b in zip(*S)];actual=rank(joined);assert actual==36
arch=json.loads((root/'fixed_extra_intersections.json').read_text())
record=next(v for v in arch['pairs'] if (v['H'],v['H_prime'])==(1,2))
assert record['joined_rank']==actual and arch['Z']==Z
out={'status':'PASS','scope':'one pair only, independent stdlib direct parity-check construction','p':p,'Z':Z,'pair':[1,2],'matrix_shape':[81,36],'individual_ranks':[18,18],'joined_rank':actual,'intersection_dimension':0,'matches_saved_direct_census':True,'fixture_sha256':hashlib.sha256(raw).hexdigest(),'seconds':time.monotonic()-start}
(root/'independent_pair_1_2_syndrome.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
