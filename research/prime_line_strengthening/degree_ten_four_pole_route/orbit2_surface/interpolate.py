"""Full (non-equivariant) degree62 interpolation over F83 from Frobenius orbits."""
import json,time,hashlib
from pathlib import Path
from flint import nmod_mat
P=Path(__file__).resolve().parent;raw=(P/'gauss_samples.json').read_bytes();d=json.loads(raw);assert d['field_modulus']==[80,82,0,1]
p=83;zero=(0,0,0);one=(1,0,0)
def mul(a,b):
 a0,a1,a2=a;b0,b1,b2=b;d3=a1*b2+a2*b1;d4=a2*b2
 return ((a0*b0+3*d3)%p,(a0*b1+a1*b0+d3+3*d4)%p,(a0*b2+a1*b1+a2*b0+d4)%p)
def power(a,n):
 v=one
 while n:
  if n&1:v=mul(v,a)
  a=mul(a,a);n//=2
 return v
def powers(a,n):
 v=[one]
 for _ in range(n):v.append(mul(v[-1],a))
 return v
points=[tuple(tuple(c) for c in z) for z in d['image_points']];assert len(set(points))==len(points)>3844
seen=set();reps=[]
for z in points:
 if z in seen:continue
 reps.append(z)
 for k in range(3):seen.add(tuple(power(c,p**k) for c in z))
cols=[(62-b-c,b,c) for b in range(63) for c in range(63-b)]
start=time.time();rows=[]
for z in reps[:760]:
 A,B,C=[powers(a,62) for a in z];triples=[mul(mul(A[a],B[b]),C[c]) for a,b,c in cols]
 rows.extend([[v[k] for v in triples] for k in range(3)])
print('matrix',len(rows),len(cols),'seconds',time.time()-start,flush=True)
M=nmod_mat(rows,p);del rows;R,rank=M.rref();del M
print('rank',rank,'seconds',time.time()-start,flush=True)
assert rank==2015
piv=[]
for i in range(rank):piv.append(next(j for j in range(2016) if int(R[i,j])))
free=next(j for j in range(2016) if j not in set(piv));v=[0]*2016;v[free]=1
for i,j in enumerate(piv):v[j]=-int(R[i,free])%p
del R
H=[(cols[j],a) for j,a in enumerate(v) if a]
# Every point independently evaluated with tuple arithmetic, not field-library substitution.
for z in points:
 A,B,C=[powers(a,62) for a in z];out=[0,0,0]
 for (a,b,c),v in H:
  val=mul(mul(A[a],B[b]),C[c])
  for k in range(3):out[k]+=v*val[k]
 assert all(t%p==0 for t in out)
receipt=dict(status='PASS',input_sha256=hashlib.sha256(raw).hexdigest(),prime=p,field_modulus=d['field_modulus'],distinct_points=len(points),Frobenius_orbits=len(reps),used_orbits=min(760,len(reps)),matrix_rows=3*min(760,len(reps)),matrix_columns=2016,rank=rank,kernel_dimension=1,pivot_columns=piv,free_column=free,image_degree=62,image_terms=H,all_points_directly_verified=True,seconds=time.time()-start)
(P/'gauss_image_interpolation.json').write_text(json.dumps(receipt,indent=2)+'\n');print('PASS',len(H),'terms',time.time()-start,flush=True)
