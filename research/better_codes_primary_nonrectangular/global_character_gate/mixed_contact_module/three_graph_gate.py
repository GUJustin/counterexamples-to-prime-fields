import json
from pathlib import Path
from flint import fmpq as Q,fmpq_mat
P=Path(__file__).parent;xs=list(map(Q,['1','2','3','4','-1','16/7']));ws=[Q(0)]*4+[Q(6),Q('18/49')]
cols=[(d,i,j) for j in range(2) for i in range(3-j) for d in range(8-2*i-j)];rows=[]
for x,y in zip(xs,ws):
 for typ in [('eval',0),('eval',1),('deriv',0),('deriv',1),('deriv',2)]:
  row=[]
  for d,i,j in cols:
   a=Q(0)
   if typ==('eval',j):a+=x**d*y**i
   if typ==('deriv',j) and d:a+=d*x**(d-1)*y**i
   if typ==('deriv',j+1) and i:a+=i*x**d*y**(i-1)
   row.append(a)
  rows.append(row)
A,r=fmpq_mat(rows).rref();piv=[next(j for j in range(len(cols)) if A[i,j]) for i in range(r)];free=[j for j in range(len(cols)) if j not in piv];basis=[]
for j in free:
 v=[Q(0)]*len(cols);v[j]=Q(1)
 for i,c in enumerate(piv):v[c]=-A[i,j]
 assert all(sum(a*b for a,b in zip(row,v))==0 for row in rows)
 basis.append([{'monomial':cols[i],'coefficient':str(a)} for i,a in enumerate(v) if a])
out={'nodes':list(map(str,xs)),'word':list(map(str,ws)),'columns':len(cols),'rows':len(rows),'rank':r,'nullity':len(free),'kernel':basis};(P/'three_graph_gate.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
