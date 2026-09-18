import json
from pathlib import Path
P=Path(__file__).parent;D=json.loads((P.parent/'quadratic_one_pole_route/orbit2_bank83.json').read_text());out=[]
def det(A):
 A=[r[:] for r in A];prev=1;sgn=1
 for k in range(len(A)-1):
  if not A[k][k]:
   j=next(j for j in range(k+1,len(A)) if A[j][k]);A[j],A[k]=A[k],A[j];sgn=-sgn
  t=A[k][k]
  for i in range(k+1,len(A)):
   for j in range(k+1,len(A)):A[i][j]=(A[i][j]*t-A[i][k]*A[k][j])//prev
  for i in range(k+1,len(A)):A[i][k]=0
  prev=t
 return sgn*A[-1][-1]
for rec in json.loads((P/'orbit2_gate.json').read_text()):
 M=[];f=rec['full'];xs=D['base'];ys=D['word']
 for i,dx,dv in rec['conditions']:
  x=xs[i];v=ys[i] if f is None else (ys[i]-ys[f+7])*pow(xs[i]-xs[f+7],-1,83)%83
  M.append([(k if dx else 1)*(l if dv else 1)*x**(k-dx)*v**(l-dv)%83 if k>=dx and l>=dv else 0 for k,l in rec['columns']])
 assert M==rec['matrix'];A=[[M[i][j] for j in rec['pivot_columns']] for i in rec['pivot_rows']];z=det(A)%83
 assert z and len(A)==len(rec['columns']);out.append(dict(full=f,minor_mod83=z,size=len(A)))
(P/'orbit2_verification.json').write_text(json.dumps(dict(pass_all=True,minors=out),indent=2));print(out)
