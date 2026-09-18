import json
from pathlib import Path
P=Path(__file__).parent
D=json.loads((P.parent/'quadratic_one_pole_route/orbit2_bank83.json').read_text());p=83;xs=D['base'];ys=D['word']
def reduce(M):
 A=[r[:] for r in M];r=0;pv=[];ids=list(range(len(A)));rows=[]
 for c in range(len(A[0])):
  k=next((k for k in range(r,len(A)) if A[k][c]),None)
  if k is None:continue
  A[k],A[r]=A[r],A[k];ids[k],ids[r]=ids[r],ids[k];rows.append(ids[r]);z=pow(A[r][c],-1,p);A[r]=[v*z%p for v in A[r]]
  for k in range(len(A)):
   if k!=r:
    z=A[k][c];A[k]=[(v-z*u)%p for v,u in zip(A[k],A[r])]
  pv.append(c);r+=1
 K=[]
 for j in range(len(A[0])):
  if j not in pv:
   v=[0]*len(A[0]);v[j]=1
   for i,c in enumerate(pv):v[c]=-A[i][j]%p
   K.append(v)
 return r,rows,pv,K
out=[]
for f in [None,2]:
 cols=[(k,3-j) for j in range(4) for k in range(j*(3-(f is not None))+2)]
 M=[];pts=[]
 for i,(x,y) in enumerate(zip(xs,ys)):
  if f is not None and i in [4,f+7]:continue
  v=y if f is None else (y-ys[f+7])*pow(x-xs[f+7],-1,p)%p
  for dx,dv in ([(0,0),(1,0),(0,1)] if i>=7 else [(0,0)]):
   row=[(pow(x,k-dx,p)*pow(v,l-dv,p)*(k if dx else 1)*(l if dv else 1))%p if k>=dx and l>=dv else 0 for k,l in cols]
   M.append(row);pts.append([i,dx,dv])
 rank,rows,piv,K=reduce(M);out.append(dict(full=f,columns=cols,conditions=pts,rank=rank,matrix=M,pivot_rows=rows,pivot_columns=piv,kernel=K))
(P/'orbit2_gate.json').write_text(json.dumps(out,indent=2));print([(a['full'],len(a['matrix']),len(a['columns']),a['rank'],len(a['kernel'])) for a in out])
