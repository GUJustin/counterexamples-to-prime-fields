"""Independent Hasse matrix reconstruction and all 796 maximal-minor replays."""
import json,math,time
from pathlib import Path
import numpy as np
P=Path(__file__).parent;D=json.loads((P/'census.json').read_text());G=json.loads((P/'gate.json').read_text());reports=[];start=time.monotonic()
cols=[(k,8-j) for j in range(9) for k in range(3*j+4)]
for (name,d),g in zip(D.items(),G):
 p=d['p'];jets=[]
 for x,y in zip(d['base'],d['word']):
  jets.append([[(math.comb(k,a)*math.comb(l,b)*pow(x,k-a,p)*pow(y,l-b,p))%p if k>=a and l>=b else 0 for k,l in cols] for order in range(8) for a in range(order+1) for b in [order-a]])
 dets=[]
 for pat,cert in zip(d['patterns'],g['cases']):
  m=pat['multiplicities'];assert sum(m)==56 and sum(a*(a-1)//2 for a in m)<=98
  assert all(sum(m[j] for j in range(14) if i in d['masks'][j])<=27 for i in range(7))
  rows=[row for j,a in enumerate(m) for row in jets[j][:a*(a+1)//2]]
  assert cert['rank']==144 and cert['columns']==list(range(144))
  A=np.array([rows[j] for j in cert['rows']],dtype=np.int64);det=1
  for j in range(144):
   pivot=int(A[j,j]);assert pivot;det=det*pivot%p
   if j<143:
    factors=A[j+1:,j]*pow(pivot,-1,p)%p
    A[j+1:,j+1:]=(A[j+1:,j+1:]-factors[:,None]*A[j,j+1:][None,:])%p
  assert det==cert['pivot_product'] and det;dets.append(det)
 reports.append(dict(bank=name,count=len(dets),rank=144,determinants=dets))
(P/'verification.json').write_text(json.dumps(dict(pass_all=True,seconds=time.monotonic()-start,banks=reports),indent=2));print([(r['bank'],r['count'],r['rank']) for r in reports])
