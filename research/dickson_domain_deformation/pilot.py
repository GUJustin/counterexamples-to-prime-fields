from math import comb
from pathlib import Path
import json
import numpy as np
BASE=Path(__file__).resolve().parent

def ev(c,x,m):
 y=0
 for a in reversed(c):y=(y*x+a)%m
 return y

def run(p):
 n=p-1;k=n//4;L=n//2;e=(p+1)//2
 nodes=list(range(1,p))
 polys=[[comb(e,2*j+1)*pow(a,e-2*j-1,p)%p for j in range(k)] for a in range(1,L+1)]
 word=[((1+(1 if pow(x,n//2,p)==1 else -1))//2-pow(x,k,p))%p for x in nodes]
 supports=[[i for i,x in enumerate(nodes) if ev(c,x,p)==word[i]] for c in polys]
 assert all(len(s)==3*n//8 for s in supports)
 assert len({tuple(c) for c in polys})==L
 equations=[];rows=[];rhs=[];v=n+L*k
 for u,x in enumerate(nodes):
  incident=[i for i,s in enumerate(supports) if u in s]
  if not incident:continue
  ref=incident[0]
  for i in incident[1:]:
   row=[0]*v
   row[u]=(sum(t*(polys[i][t]-polys[ref][t])*pow(x,t-1,p) for t in range(1,k)))%p
   for t in range(k):
    row[n+i*k+t]=pow(x,t,p)
    row[n+ref*k+t]=-pow(x,t,p)%p
   residual=(ev(polys[i],x,p*p)-ev(polys[ref],x,p*p))%(p*p)
   assert residual%p==0
   rows.append(row);rhs.append(-residual//p%p);equations.append([u,i,ref])
 J=np.array(rows,dtype=np.int64);b=np.array(rhs,dtype=np.int64)
 mat=np.column_stack((J,b));ops=np.eye(len(rows),dtype=np.int64);pivot=[];rank=0
 for col in range(v):
  eligible=np.flatnonzero(mat[rank:,col])
  if not len(eligible):continue
  q=rank+int(eligible[0]);mat[[rank,q]]=mat[[q,rank]];ops[[rank,q]]=ops[[q,rank]]
  inv=pow(int(mat[rank,col]),-1,p);mat[rank]=mat[rank]*inv%p;ops[rank]=ops[rank]*inv%p
  for rr in range(len(rows)):
   if rr!=rank and mat[rr,col]:
    f=int(mat[rr,col]);mat[rr]=(mat[rr]-f*mat[rank])%p;ops[rr]=(ops[rr]-f*ops[rank])%p
  pivot.append(col);rank+=1
  if rank==len(rows):break
 bad=next((r for r in range(rank,len(rows)) if mat[r,-1]),None)
 out=dict(p=p,n=n,k=k,L=L,A=3*n//8,variables=v,equations=equations,nodes=nodes,polynomials=polys,rank=rank,row_count=len(rows),full_row_rank=rank==len(rows))
 if bad is not None:
  witness=ops[bad];assert np.all(witness@J%p==0) and int(witness@b%p)!=0
  out.update(status='obstructed_mod_p_squared',left_kernel=witness.tolist(),obstruction=int(witness@b%p))
 else:
  solution=np.zeros(v,dtype=np.int64)
  for r,col in enumerate(pivot):solution[col]=mat[r,-1]
  assert np.all(J@solution%p==b)
  newnodes=[(x+p*int(solution[u]))%(p*p) for u,x in enumerate(nodes)]
  newpolys=[[(a+p*int(solution[n+i*k+t]))%(p*p) for t,a in enumerate(c)] for i,c in enumerate(polys)]
  assert all(ev(newpolys[i],newnodes[u],p*p)==ev(newpolys[ref],newnodes[u],p*p) for u,i,ref in equations)
  out.update(status='first_correction_exists',correction=solution.tolist(),lifted_nodes=newnodes,lifted_polynomials=newpolys,pivot_columns=pivot)
 return out

if __name__=='__main__':
 rows=[]
 for p in (17,41):
  result=run(p);rows.append(result)
  print({key:result[key] for key in ('p','row_count','variables','rank','full_row_rank','status')},flush=True)
  (BASE/'pilot.json').write_text(json.dumps(dict(status='complete' if p==41 else 'running',fixtures=rows),indent=2)+'\n')
