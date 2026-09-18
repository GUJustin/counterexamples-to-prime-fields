"""Independent stdlib proof checker; performs no max-flow optimization."""
import json
from pathlib import Path
P=Path(__file__).parent;receipt=json.loads((P/'mincut.json').read_text())
flows={}
for line in (P/'mincut.flow').read_text().splitlines():
 k,v=map(int,line.split());assert k not in flows and v>0;flows[k]=v
n,w,D,L,m,Q,S=262144,131071,20846625,274277,115,159,35
assert D-(w-1)*Q>=m
vertices=[(i,j) for j in range(S+1) for i in range(Q-j+1)]
ids={ij:2+t for t,ij in enumerate(vertices)}
benefits={(i,j):(L-i-j+1)*(D-w*i-(w-1)*j) for i,j in vertices}
B=sum(benefits.values());balance=[0]*receipt['nodes'];cutset=set(receipt['source_side']);edge_count=cut=0
assert 0 in cutset and 1 not in cutset

def check_edge(u,v,capacity):
 global edge_count,cut
 amount=flows.pop(edge_count,0);assert 0<=amount<=capacity,(edge_count,amount,capacity)
 balance[u]-=amount;balance[v]+=amount
 if u in cutset and v not in cutset:cut+=capacity
 edge_count+=1
for ij in vertices:check_edge(0,ids[ij],benefits[ij])
for i,j in vertices:
 if i:check_edge(ids[i,j],ids[i-1,j],B+1)
nextnode=2+len(vertices)
for q in range(Q+1):
 for ell in range(m):
  active=[ids[i,q-i] for i in range(max(0,q-S),min(q,ell)+1)]
  if not active:continue
  z=nextnode;nextnode+=1;K=n*(L-q+1)
  for x in active:check_edge(x,z,K)
  check_edge(z,1,(m-ell)*K)
assert not flows
assert nextnode==receipt['nodes'] and edge_count==receipt['edges']
assert all(v==0 for v in balance[2:])
assert -balance[0]==balance[1]==receipt['flow']==cut==B==receipt['benefit_sum']
chosen={ij for ij in vertices if ids[ij] in cutset};assert chosen==set(map(tuple,receipt['selected_support']))
assert all(i==0 or(i-1,j)in chosen for i,j in chosen)
C=sum(benefits[ij] for ij in chosen)
R=sum((L-q+1)*sum(min(m-ell,sum(i<=ell for i,j in chosen if i+j==q)) for ell in range(m)) for q in range(Q+1))
assert C-n*R==B-cut==receipt['maximum_surplus']==0
out=dict(status='PASS',nodes=nextnode,edges=edge_count,flow=B,cut=cut,maximum_surplus=0,selected_support_size=len(chosen),saturation_margin=D-(w-1)*Q-m,scope='All Y-downward full-prefix subsets of the fixed m115,D20846625,L274277,j<=35,i+j<=159 primaryA shape')
(P/'verify_flow.json').write_text(json.dumps(out,indent=2));print(out)
