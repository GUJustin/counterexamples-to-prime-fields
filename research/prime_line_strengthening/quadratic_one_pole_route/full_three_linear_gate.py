import json,itertools
from pathlib import Path
P=Path(__file__).parent;D=json.loads((P/'fiber_patterns.json').read_text());p=29;xs=D['base'];ys=D['word']
def interpolate3(F,x):
 val=0
 for j in F:
  num=den=1
  for k in F:
   if k!=j:num=num*(x-xs[k])%p;den=den*(xs[j]-xs[k])%p
  val=(val+ys[j]*num*pow(den,-1,p))%p
 return val

def rref(M):
 M=[r[:] for r in M];rank=0;piv=[];order=list(range(len(M)));chosen=[];det=1
 for c in range(6):
  k=next((k for k in range(rank,len(M)) if M[k][c]),None)
  if k is None:continue
  M[k],M[rank]=M[rank],M[k];order[k],order[rank]=order[rank],order[k]
  chosen.append(order[rank]);det=det*M[rank][c]%p
  z=pow(M[rank][c],-1,p);M[rank]=[v*z%p for v in M[rank]]
  for k in range(len(M)):
   if k!=rank:
    z=M[k][c];M[k]=[(a-z*b)%p for a,b in zip(M[k],M[rank])]
  piv.append(c);rank+=1
 return rank,chosen,M
out=[]
for pat in D['patterns']:
 F=pat['full'];E=pat['empty']
 if len(F)!=3:continue
 singles=[j for j in range(14) if j not in F and j not in E];rs=[]
 for j in singles:
  q=1
  for k in F:q=q*(xs[j]-xs[k])%p
  rs.append((ys[j]-interpolate3(F,xs[j]))*pow(q,-1,p)%p)
 M=[[1,v,v*v%p,-xs[j]%p,-xs[j]*v%p,-xs[j]*v*v%p] for j,v in zip(singles,rs)]
 rank,piv,red=rref(M)
 out.append(dict(full=F,empty=E,singles=singles,coordinates=rs,rank=rank,independent_rows=piv,matrix=M))
(P/'full_three_linear_gate.json').write_text(json.dumps(out,indent=2))
print({r:sum(x['rank']==r for x in out) for r in range(7)})
print('rankdeficient',[(x['full'],x['empty'],x['rank']) for x in out if x['rank']<6])
