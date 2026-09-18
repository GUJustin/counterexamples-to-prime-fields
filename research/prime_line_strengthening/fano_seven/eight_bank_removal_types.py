"""Classify every deletion from the unique eight-bank incidence extension."""
import itertools,json,time
from pathlib import Path
r=Path(__file__).parent;start=time.monotonic();reps=[json.loads(s) for s in (r/'design_orbits.jsonl').read_text().splitlines()]
lookup={}
for oi,row in enumerate(reps):
 for perm in itertools.permutations(range(7)):
  key=tuple(tuple(sorted(sum(1<<perm[v-1] for v in b) for b in row[side])) for side in ['T','C'])
  if key in lookup:assert lookup[key]==oi
  lookup[key]=oi
assert len(lookup)==6150
out=[]
for oi,row in enumerate(reps):
 blocks=[set(t)|{8} for t in row['T']]+[set(range(1,8))-set(c) for c in row['C']]
 assert all(len(b)==4 for b in blocks)
 assert all(sum(i in b for b in blocks)==7 for i in range(1,9))
 assert all(sum(i in b and j in b for b in blocks)==3 for i,j in itertools.combinations(range(1,9),2))
 types=[];deletions=[]
 for drop in range(1,9):
  keep=[i for i in range(1,9) if i!=drop];pos={i:j for j,i in enumerate(keep)}
  T=[b-{drop} for b in blocks if drop in b]
  C=[set(keep)-b for b in blocks if drop not in b]
  key=tuple(tuple(sorted(sum(1<<pos[v] for v in b) for b in bs)) for bs in [T,C])
  typ=lookup[key];types.append(typ);deletions.append({'removed':drop,'orbit':typ,'T':[sorted(b) for b in T],'C':[sorted(b) for b in C]})
 out.append({'starting_orbit':oi,'removal_types':types,'has_excluded_removal':any(t in [0,1,3,4,5,6] for t in types),'deletions':deletions})
result={'rows':out,'seconds':time.monotonic()-start,'all_excluded_by_known_orbits':all(a['has_excluded_removal'] for a in out)}
(r/'eight_bank_removal_types.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'rows':[{k:v for k,v in a.items() if k!='deletions'} for a in out],'all_excluded':result['all_excluded_by_known_orbits'],'seconds':result['seconds']},indent=2))
