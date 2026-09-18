"""Independent capacity/conservation/cut proof replay, without an optimizer."""
import gzip, json, struct, sys
from pathlib import Path
P=Path(__file__).parent/'all_m_certificates'
def verify(m):
 r=json.loads((P/f'm{m}.json').read_text()); n,w,D=262144,131071,181275*m
 vertices=[(i,j) for j in range(36) for i in range(160-j) if D-w*i-(w-1)*j>0]
 ids={ij:k+2 for k,ij in enumerate(vertices)}
 benefits={ij:D-w*ij[0]-(w-1)*ij[1] for ij in vertices}; B=sum(benefits.values())
 path=P/f'm{m}.flowbin'
 data=path.read_bytes() if path.exists() else gzip.decompress(path.with_suffix('.flowbin.gz').read_bytes())
 assert len(data)%12==0
 flowiter=iter(struct.iter_unpack('<Iq',data)); current=next(flowiter,None)
 balances=[0]*r['nodes']; side=set(r['source_side']); assert 0 in side and 1 not in side
 eid=cut=used=0
 def edge(u,v,cap):
  nonlocal current,eid,cut,used
  assert current is None or current[0]>=eid
  amount=0
  if current is not None and current[0]==eid:
   amount=current[1]; assert amount>0; used+=1;current=next(flowiter,None)
  assert 0<=amount<=cap
  balances[u]-=amount;balances[v]+=amount
  if u in side and v not in side:cut+=cap
  eid+=1
 for ij in vertices:edge(0,ids[ij],benefits[ij])
 for i,j in vertices:
  if i:edge(ids[i,j],ids[i-1,j],B+1)
 nextnode=len(vertices)+2
 for q in range(160):
  for ell in range(min(m,D-(w-1)*q)):
   active=[ids[i,q-i] for i in range(max(0,q-35),min(q,ell)+1)]
   if not active:continue
   z=nextnode;nextnode+=1
   for x in active:edge(x,z,n)
   edge(z,1,n*(m-ell))
 assert current is None and used==r['nonzero_flows']
 assert nextnode==r['nodes'] and eid==r['edges'] and all(x==0 for x in balances[2:])
 assert -balances[0]==balances[1]==cut==r['flow']
 assert B==r['benefit_sum'] and B-cut==r['maximum_slope']
 chosen={ij for ij in vertices if ids[ij] in side};assert chosen==set(map(tuple,r['selected_support']))
 assert all(i==0 or (i-1,j) in chosen for i,j in chosen)
 rank=0
 for q in range(160):
  indices=[i for i,j in chosen if i+j==q]
  rank+=sum(min(m-ell,sum(i<=ell for i in indices)) for ell in range(max(0,min(m,D-(w-1)*q))))
 assert sum(benefits[ij] for ij in chosen)-n*rank==B-cut
 return {'m':m,'maximum_slope':B-cut,'edges':eid,'flow':cut,'selected':len(chosen)}
lo,hi=map(int,sys.argv[1:3]);results=[verify(m) for m in range(lo,hi+1)]
(P/f'verified_{lo}_{hi}.json').write_text(json.dumps({'status':'PASS','results':results},indent=2))
print(json.dumps({'status':'PASS','range':[lo,hi],'maximum_slope':max(r['maximum_slope'] for r in results)}))
