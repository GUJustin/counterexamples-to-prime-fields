"""Streaming capacity/conservation replay plus independent Pascal rank count."""
import json,sys,bisect
from pathlib import Path
P=Path(__file__).parent;name=sys.argv[1];d=json.loads((P/(name+'.json')).read_text());m,L,Q,S=(d[k]for k in ['m','L','Q','S']);n=262144;w=131071;D=d.get("D",m*181275)
assert D>(m-1)+(w-1)*Q
vs=[(i,j)for j in range(S+1)for i in range(Q-j+1)];ids={v:i+2 for i,v in enumerate(vs)}
weight=lambda q:1 if L<0 else L-q+1
benef={v:weight(sum(v))*(D-w*v[0]-(w-1)*v[1])for v in vs};B=sum(benef.values());bal=[0]*d['nodes'];side=set(d['source_side']);assert 0 in side and 1 not in side
f=iter(open(P/(name+'.flow')))
def nxt():
 try:return tuple(map(int,next(f).split()))
 except StopIteration:return None
cur=nxt();idx=0;cut=0

def edge(u,v,c):
 global idx,cut,cur
 z=0
 if cur is not None:
  assert cur[0]>=idx
  if cur[0]==idx:z=cur[1];cur=nxt()
 assert 0<=z<=c
 bal[u]-=z;bal[v]+=z
 if u in side and v not in side:cut+=c
 idx+=1
for v in vs:edge(0,ids[v],benef[v])
for i,j in vs:
 if i:edge(ids[i,j],ids[i-1,j],B+1)
z=2+len(vs)
for q in range(Q+1):
 for ell in range(m):
  aa=range(max(0,q-S),min(q,ell)+1)
  if not aa:continue
  for i in aa:edge(ids[i,q-i],z,n*weight(q))
  edge(z,1,(m-ell)*n*weight(q));z+=1
assert cur is None and idx==d['edges']and z==d['nodes']
assert all(a==0 for a in bal[2:]);assert -bal[0]==bal[1]==cut==d['flow'];assert B==d['benefit_sum']
chosen={v for v in vs if ids[v]in side};assert chosen==set(map(tuple,d['selected_support']));assert all(i==0 or(i-1,j)in chosen for i,j in chosen)
qs=[sorted(i for i,j in chosen if i+j==q)for q in range(Q+1)]
rank=sum(weight(q)*sum(min(m-ell,bisect.bisect_right(qs[q],ell))for ell in range(m))for q in range(Q+1));C=sum(benef[v]for v in chosen)
assert C-n*rank==B-cut==d['maximum_surplus']
out=dict(status='PASS',name=name,m=m,L=L,Q=Q,S=S,edges=idx,flow=cut,coefficient_count=C,local_rank=rank,maximum_surplus=B-cut,selected_support_size=len(chosen))
(P/(name+'.verified.json')).write_text(json.dumps(out,indent=2));print(out)
