from pathlib import Path
from collections import defaultdict
import subprocess,json
p=Path(__file__).resolve().parent
out=[]
for q in [9,15,21]:
 r=(q-1)//2
 text=subprocess.check_output([str(p/'composite_census_independent'),str(q)],text=True)
 (p/f'composite_q{q}_all.txt').write_text(text)
 by=defaultdict(list)
 for line in text.splitlines():
  m,*v=map(int,line.split());by[tuple(v)].append(m)
 expected={}
 allowed=[]
 for v,ms in by.items():
  target=tuple(r-1-x for x in v)
  if target not in by:continue
  key=sum(x*(r+1)**i for i,x in enumerate(v));tk=sum(x*(r+1)**i for i,x in enumerate(target))
  expected[key]=(tk,sorted(ms))
  for m in ms:
   comp=((1<<q)-1)^m
   allowed.append(min(sum(1<<((i+s)%q) for i in range(q) if comp>>i&1) for s in range(q)))
 source=json.loads((p.parent/'cyclic_half_agreement'/f'profiles_q{q}.json').read_text())
 actual={x['key']:(x['target_key'],sorted(x['C_masks'])) for x in source['profiles']}
 assert actual==expected,(q,'profile mismatch')
 assert sorted(source['allowed_first_support_masks'])==sorted(allowed),(q,'support mismatch')
 pairs=sum(len(ms)*len(by[tuple(r-1-x for x in v)]) for v,ms in by.items() if tuple(r-1-x for x in v) in by)
 out.append(dict(q=q,all_rotation_classes=sum(map(len,by.values())),retained_classes=len(allowed),ordered_pairs=pairs,pass_all=True))
(p/'COMPOSITE_CENSUS_INDEPENDENT_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
