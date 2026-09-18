import json,math,time
from pathlib import Path
P=Path(__file__).parent
cols=[(k,6-j) for j in range(7) for k in range(3*j+3)]
out=[]
for name,filename,p in [('paley','fiber_patterns.json',29),('orbit2','orbit2_bank83.json',83)]:
 D=json.loads((P.parent/'quadratic_one_pole_route'/filename).read_text())
 M=[];conditions=[]
 for i,(x,y) in enumerate(zip(D['base'],D['word'])):
  mult=4 if i>=7 else 2
  for total in range(mult):
   for dx in range(total+1):
    dv=total-dx
    M.append([math.comb(k,dx)*math.comb(l,dv)*pow(x,k-dx,p)*pow(y,l-dv,p)%p if k>=dx and l>=dv else 0 for k,l in cols])
    conditions.append([i,dx,dv])
 A=[r[:] for r in M];ids=list(range(len(A)));piv=[];selected=[];rank=0
 for c in range(len(cols)):
  k=next((i for i in range(rank,len(A)) if A[i][c]),None)
  if k is None:continue
  A[k],A[rank]=A[rank],A[k];ids[k],ids[rank]=ids[rank],ids[k]
  selected.append(ids[rank]);piv.append(c);inv=pow(A[rank][c],-1,p)
  A[rank]=[a*inv%p for a in A[rank]]
  for i in range(len(A)):
   if i!=rank and A[i][c]:
    a=A[i][c];A[i]=[(x-a*y)%p for x,y in zip(A[i],A[rank])]
  rank+=1
 kernel=[]
 for c in range(len(cols)):
  if c not in piv:
   v=[0]*len(cols);v[c]=1
   for r,j in enumerate(piv):v[j]=-A[r][c]%p
   kernel.append(v)
 out.append(dict(bank=name,p=p,base=D['base'],word=D['word'],columns=cols,conditions=conditions,matrix=M,rank=rank,pivot_rows=selected,pivot_columns=piv,kernel=kernel))
 print(name,len(M),len(cols),rank,'kernel',len(kernel))
(P/'gate.json').write_text(json.dumps(out,indent=2))
