"""Independent analytic Jacobian for the 25-equation pointed system."""
import itertools,json
from pathlib import Path
root=Path(__file__).parent
h=json.loads((root/'hits.jsonl').read_text().splitlines()[0]); p=h['p'];a=h['a'];alpha=h['first_pole'];b=h['new_pole'];c=h['critical']
N=[34,54,93,0,84,3,56,70]
e1=sum(a)%p;e3=sum(__import__('math').prod(s) for s in itertools.combinations(a,3))%p;e4=__import__('math').prod(a)%p
rows=[];row=[0]*27
for i in range(4):
 other=[a[j] for j in range(4) if j!=i]
 de3=sum(x*y for x,y in itertools.combinations(other,2))
 de4=__import__('math').prod(other)
 row[i]=(alpha*de3-e4-e1*de4)%p
row[4]=e3;rows.append(row)
for l,(t,y,W) in enumerate(zip(h['nodes'],h['base_nodes'],h['values'])):
 dy=[0]*5;dw=[0]*5
 if y==alpha:dy[4]=1
 else:
  matches=[(i,j,s) for i,j in itertools.combinations(range(4),2) for s in (1,-1) if s*a[i]*a[j]%p==y]
  assert len(matches)==1
  i,j,s=matches[0];dy[i]=s*a[j];dy[j]=s*a[i]
  v=(a[i]**2+a[j]**2)%p
  assert W==(y-alpha)*v%p
  for k in range(4):dw[k]=dy[k]*v+(y-alpha)*(2*a[k] if k in (i,j) else 0)
  dw[4]=-v
 row=[0]*27
 for k in range(5):row[k]=-dy[k]%p
 row[5]=1;row[15+l]=2*t%p;rows.append(row)
 row=[0]*27
 for k in range(5):row[k]=-(t-b)*dw[k]%p
 row[6]=W
 for k in range(8):row[7+k]=pow(t,k,p)
 row[15+l]=(sum(k*N[k]*pow(t,k-1,p) for k in range(1,8))-W)%p
 rows.append(row)
 assert sum(N[k]*pow(t,k,p) for k in range(8))%p==(t-b)*W%p
A=[r[:] for r in rows];piv=[];rank=0
for j in range(27):
 ii=next((i for i in range(rank,25) if A[i][j]),None)
 if ii is None:continue
 A[rank],A[ii]=A[ii],A[rank];v=pow(A[rank][j],-1,p);A[rank]=[x*v%p for x in A[rank]]
 for i in range(25):
  if i!=rank:
   v=A[i][j];A[i]=[(x-v*y)%p for x,y in zip(A[i],A[rank])]
 piv.append(j);rank+=1
 if rank==25:break
assert rank==25
M=[[r[j] for j in piv] for r in rows];det=1
for j in range(25):
 i=next(i for i in range(j,25) if M[i][j]);
 if i!=j:M[i],M[j]=M[j],M[i];det=-det
 v=M[j][j];det=det*v%p;iv=pow(v,-1,p)
 for i in range(j+1,25):
  fac=M[i][j]*iv%p
  for k in range(j,25):M[i][k]=(M[i][k]-fac*M[j][k])%p
out={'prime':p,'rank':rank,'equations':25,'variables':27,'pivot_columns':piv,'minor_determinant':det%p,'jacobian':rows}
(root/'pointed_jacobian_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='jacobian'})
