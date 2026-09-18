"""Independent edge reconstruction and primal-dual replay; no optimization."""
from array import array
import argparse,gzip,json,struct
from pathlib import Path
P=Path(__file__).parent
ap=argparse.ArgumentParser();ap.add_argument('--stem',type=Path,default=P/'partial_prefix')
stem=ap.parse_args().stem
r=json.loads(stem.with_suffix('.json').read_text())
m,n,w,D=r['m'],262144,131071,r['D']
assert 115<=m<=371 and D==m*181275
def node(x,i,j):return 2+m*(160*j-j*(j-1)//2+i)+x
pairs=[(i,j) for j in range(36) for i in range(160-j)]
height=lambda i,j:D-w*i-(w-1)*j
B=sum(height(i,j) for i,j in pairs)
path=stem.with_suffix('.flowbin')
data=path.read_bytes() if path.exists() else gzip.decompress(stem.with_suffix('.flowbin.gz').read_bytes())
assert len(data)%12==0
it=iter(struct.iter_unpack('<Iq',data));item=next(it,None)
balance=array('q',[0])*r['nodes'];side=bytearray(r['nodes'])
for v in r['source_side']:side[v]=1
assert side[0] and not side[1]
eid=cut=used=0
def edge(u,v,cap):
 global item,eid,cut,used
 assert item is None or item[0]>=eid
 amount=0
 if item is not None and item[0]==eid:
  amount=item[1];assert amount>0;used+=1;item=next(it,None)
 assert 0<=amount<=cap
 balance[u]-=amount;balance[v]+=amount
 if side[u] and not side[v]:cut+=cap
 eid+=1
for i,j in pairs:
 for x in range(m):edge(0,node(x,i,j),1 if x<m-1 else height(i,j)-m+1)
for i,j in pairs:
 for x in range(m):
  if x:edge(node(x,i,j),node(x-1,i,j),B+1)
  if i:edge(node(x,i,j),node(x,i-1,j),B+1)
nextnode=2+len(pairs)*m
for q in range(160):
 for ell in range(m):
  inds=list(range(max(0,q-35),min(q,ell)+1))
  if not inds:continue
  z=nextnode;nextnode+=1
  for i in inds:edge(node(ell-i,i,q-i),z,n)
  edge(z,1,n*(m-ell))
assert item is None and used==r['nonzero_flows']
assert eid==r['edges'] and nextnode==r['nodes'] and not any(balance[2:])
assert -balance[0]==balance[1]==r['flow']==cut
assert B==r['benefit_sum'] and B-cut==r['maximum_slope']
hs={}
for i,j in pairs:
 selected=[x for x in range(m) if side[node(x,i,j)]]
 assert selected==list(range(len(selected)))
 h=len(selected);hs[i,j]=height(i,j) if h==m else h
 if i:assert hs[i-1,j]>=hs[i,j]
assert {(i,j):h for i,j,h in r['selected_heights']}=={ij:h for ij,h in hs.items() if h}
rank=sum(min(m-ell,sum(hs[i,q-i]>ell-i for i in range(max(0,q-35),min(q,ell)+1))) for q in range(160) for ell in range(m))
assert sum(hs.values())-n*rank==B-cut
out=dict(status='PASS',maximum_slope=B-cut,flow=cut,nodes=nextnode,edges=eid,rank=rank,dimension=sum(hs.values()))
stem.with_suffix('.verified.json').write_text(json.dumps(out,indent=2));print(out)
