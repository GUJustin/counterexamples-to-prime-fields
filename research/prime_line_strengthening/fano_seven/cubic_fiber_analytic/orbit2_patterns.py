from pathlib import Path
from itertools import product
from collections import Counter
import json,time
root=Path(__file__).resolve().parent;entry=json.loads((root.parent/'design_orbits.jsonl').read_text().splitlines()[2])
T=entry['T'];Q=[[i for i in range(1,8) if i not in c] for c in entry['C']]
def records(blocks):
 out={}
 for v in product(range(4),repeat=7):
  f=v.count(3);d=v.count(2)
  if f>2 or d+3*f>9:continue
  s=sum(v);inc=tuple(sum(v[j] for j,b in enumerate(blocks) if i in b) for i in range(1,8))
  out.setdefault(s,[]).append((v,f,d,inc))
 return out
a=records(T);b=records(Q);hits=[]
for total,arr in a.items():
 if total<14:continue
 for tv,tf,td,ti in arr:
  for qv,qf,qd,qi in b.get(21-total,[]):
   f=tf+qf;d=td+qd
   if f>2 or d+3*f>9 or (f==2 and d>3):continue
   if any(x+y>10 for x,y in zip(ti,qi)):continue
   hits.append(dict(triple=list(tv),quad=list(qv),full=f,double=d,intersections=[x+y for x,y in zip(ti,qi)]))
out=dict(orbit=2,T=T,Q=Q,patterns=hits,count=len(hits),by_full=dict(Counter(x['full'] for x in hits)))
(root/'orbit2_patterns.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
