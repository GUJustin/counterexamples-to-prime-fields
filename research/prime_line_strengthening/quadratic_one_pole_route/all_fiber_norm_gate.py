import json,itertools
from pathlib import Path
P=Path(__file__).parent;D=json.loads((P/'fiber_patterns.json').read_text());p=29;xs=D['base'];ys=D['word']
def interp(F,x):
 val=0
 for j in F:
  num=den=1
  for k in F:
   if k!=j:num=num*(x-xs[k])%p;den=den*(xs[j]-xs[k])%p
  val=(val+ys[j]*num*pow(den,-1,p))%p
 return val

def rr(M):
 M=[r[:] for r in M];nc=len(M[0]);rank=0;piv=[];order=list(range(len(M)));chosen=[]
 for c in range(nc):
  k=next((k for k in range(rank,len(M)) if M[k][c]),None)
  if k is None:continue
  M[k],M[rank]=M[rank],M[k];order[k],order[rank]=order[rank],order[k];chosen.append(order[rank])
  z=pow(M[rank][c],-1,p);M[rank]=[v*z%p for v in M[rank]]
  for k in range(len(M)):
   if k!=rank:
    z=M[k][c];M[k]=[(a-z*b)%p for a,b in zip(M[k],M[rank])]
  piv.append(c);rank+=1
 K=[]
 for j in range(nc):
  if j not in piv:
   v=[0]*nc;v[j]=1
   for i,c in enumerate(piv):v[c]=-M[i][j]%p
   K.append(v)
 return rank,chosen,piv,K
out=[]
for pat in D['patterns']:
 F=pat['full'];E=pat['empty'];f=len(F); singles=[j for j in range(14) if j not in F and j not in E];vs=[]
 for j in singles:
  q=1
  for k in F:q=q*(xs[j]-xs[k])%p
  vs.append((ys[j]-interp(F,xs[j]))*pow(q,-1,p)%p)
 M=[[(v*v*pow(x,k,p))%p for k in range(2)]+[(v*pow(x,k,p))%p for k in range(5-f)]+[pow(x,k,p) for k in range(8-2*f)] for j,v in zip(singles,vs) for x in [xs[j]]]
 rank,rows,cols,K=rr(M)
 out.append(dict(full=F,empty=E,singles=singles,coordinates=vs,rank=rank,columns=len(M[0]),independent_rows=rows,independent_columns=cols,kernel=K,matrix=M))
(P/'all_fiber_norm_gate.json').write_text(json.dumps(out,indent=2));print({f:{r:sum(len(x['full'])==f and x['rank']==r for x in out) for r in set(x['rank'] for x in out if len(x['full'])==f)} for f in range(4)});print('nontrivial kernels',[(x['full'],x['empty'],x['kernel']) for x in out if x['kernel']])
