import json,math,time
from pathlib import Path
from flint import nmod_mat
P=Path(__file__).parent
cols=[(k,10-j) for j in range(11) for k in range(3*j+5)]
outs=[]
for name,fn,p in [('paley','fiber_patterns.json',29),('orbit2','orbit2_bank83.json',83)]:
 D=json.loads((P.parent/'quadratic_one_pole_route'/fn).read_text());M=[];conds=[]
 for i,(x,y) in enumerate(zip(D['base'],D['word'])):
  mult=6 if i>=7 else 4
  for total in range(mult):
   for dx in range(total+1):
    dv=total-dx
    M.append([math.comb(k,dx)*math.comb(l,dv)*pow(x,k-dx,p)*pow(y,l-dv,p)%p if k>=dx and l>=dv else 0 for k,l in cols]);conds.append([i,dx,dv])
 A=nmod_mat(M,p);R,rank=A.rref();rows=[[int(R[i,j]) for j in range(len(cols))] for i in range(rank)]
 piv=[next(j for j,x in enumerate(row) if x) for row in rows];free=[j for j in range(len(cols)) if j not in piv];K=[]
 for f in free:
  v=[0]*len(cols);v[f]=1
  for row,c in zip(rows,piv):v[c]=-row[f]%p
  assert all(sum(x*y for x,y in zip(row,v))%p==0 for row in M)
  K.append(v)
 lead=[[v[j] for j,(k,l) in enumerate(cols) if l==10] for v in K]
 lr=nmod_mat(lead,p).rank() if lead else 0
 out=dict(bank=name,p=p,columns=cols,conditions=conds,matrix=M,rank=rank,pivots=piv,free_columns=free,kernel=K,leading_Y10=lead,leading_projection_rank=lr,base=D['base'],word=D['word'])
 outs.append(out);print(name,'shape',len(M),len(cols),'rank',rank,'nullity',len(K),'leading rank',lr,flush=True)
(P/'gate.json').write_text(json.dumps(outs,indent=2))
