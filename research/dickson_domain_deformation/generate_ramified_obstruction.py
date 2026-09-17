"""Generate a finite certificate excluding all DVR lifts of the p41 seed."""
import json,numpy as np
from pathlib import Path
BASE=Path(__file__).resolve().parent
f=next(f for f in json.loads((BASE/'pilot.json').read_text())['fixtures'] if f['p']==41)
p=f['p'];n=f['n'];k=f['k'];v=f['variables'];eq=f['equations'];cs=f['polynomials'];xs=f['nodes'];E=len(eq)
J=np.zeros((E,v),dtype=np.int64);rhs=[];second=[]
for j,(u,i,r) in enumerate(eq):
 x=xs[u]
 deriv=sum(t*(cs[i][t]-cs[r][t])*pow(x,t-1,p) for t in range(1,k))%p
 J[j,u]=deriv
 for t in range(k):J[j,n+i*k+t]=pow(x,t,p);J[j,n+r*k+t]=-pow(x,t,p)%p
 residual=sum((cs[i][t]-cs[r][t])*pow(x,t,p*p) for t in range(k))%(p*p)
 rhs.append(-residual//p%p)
 second.append(sum(t*(t-1)//2*(cs[i][t]-cs[r][t])*pow(x,t-2,p) for t in range(2,k))%p)
def rref(A):
 A=A.copy()%p;O=np.eye(len(A),dtype=np.int64);rank=0;piv=[]
 for col in range(A.shape[1]):
  cand=np.flatnonzero(A[rank:,col])
  if not len(cand):continue
  z=rank+int(cand[0]);A[[rank,z]]=A[[z,rank]];O[[rank,z]]=O[[z,rank]]
  inv=pow(int(A[rank,col]),-1,p);A[rank]=A[rank]*inv%p;O[rank]=O[rank]*inv%p
  fac=A[:,col].copy();fac[rank]=0
  A=(A-fac[:,None]*A[rank])%p;O=(O-fac[:,None]*O[rank])%p
  piv.append(col);rank+=1
  if rank==len(A):break
 return A,O,piv
fixed=[0,1,2]+list(range(n,n+k))+[n+k+next(t for t in range(k) if (cs[1][t]-cs[0][t])%p)]
J=np.vstack((J,np.eye(v,dtype=np.int64)[fixed]));rhs += [0]*len(fixed)
R,O,piv=rref(J);rank=len(piv);free=[j for j in range(v) if j not in piv]
Z=np.zeros((v,len(free)),dtype=np.int64)
for a,j in enumerate(free):
 Z[j,a]=1
 for row,c in enumerate(piv):Z[c,a]=-R[row,j]%p
assert np.all(J@Z%p==0)
C=O[rank:];bbar=C@np.array(rhs)%p
quad=[]
for a in range(len(free)):
 for b in range(a,len(free)):
  vals=[]
  for j,(u,i,r) in enumerate(eq):
   x=xs[u];da=sum(t*(Z[n+i*k+t,a]-Z[n+r*k+t,a])*pow(x,t-1,p) for t in range(1,k))%p
   db=sum(t*(Z[n+i*k+t,b]-Z[n+r*k+t,b])*pow(x,t-1,p) for t in range(1,k))%p
   val=(Z[u,a]*db+Z[u,b]*da+2*second[j]*Z[u,a]*Z[u,b])%p
   if a==b:val=val*pow(2,-1,p)%p
   vals.append(val)
  quad.append(C@np.array(vals+[0]*len(fixed))%p)
M=np.array(quad,dtype=np.int64).T
RR,OO,pp=rref(M);trans=OO@bbar%p
bad=next((j for j in range(len(pp),len(C)) if trans[j]),None)
report=dict(quadratic_witness_rows=(OO[:len(pp)]@C%p).tolist(),gauge_fixed_columns=fixed,quadratic_forms=RR[:len(pp)].tolist(),jacobian_rank=rank,tangent_dimension=len(free),cokernel_dimension=len(C),quadratic_span_rank=len(pp),residual_outside_quadratic_span=bad is not None)
if bad is not None:
 witness=OO[bad]@C%p
 assert np.all(witness@J%p==0)
 report.update(p=p,kernel_basis=Z.T.tolist(),free_columns=free,jacobian_pivot_columns=piv,quadratic_left_witness=witness.tolist(),rhs_obstruction=int(witness@np.array(rhs)%p))
(BASE/'ramified_obstruction.json').write_text(json.dumps(report,indent=2)+'\n')
print({k:v for k,v in report.items() if not isinstance(v,list)})
