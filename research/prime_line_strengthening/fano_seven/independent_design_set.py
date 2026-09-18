"""Independent vertex-by-vertex hypergraph enumeration and literal set equality."""
import itertools,json,time,hashlib
from pathlib import Path
start=time.time();root=Path(__file__).parent
pairs=list(itertools.combinations(range(7),2));pairidx={p:i for i,p in enumerate(pairs)}
bymin=[[] for _ in range(7)]
for tri in itertools.combinations(range(7),3):
 mask=sum(1<<i for i in tri); ps=tuple(pairidx[p] for p in itertools.combinations(tri,2))
 bymin[tri[0]].append((mask,tri,ps))
deg=[0]*7;pc=[0]*21;blocks=[];halves={};calls=0

def vertex(v):
 global calls
 calls+=1
 if v==7:
  assert deg==[3]*7 and len(blocks)==7
  half=tuple(sorted(blocks));key=bytes(pc)
  halves.setdefault(key,[]).append(half)
  return
 need=3-deg[v]
 if need<0:return
 choices=bymin[v]
 if need and not choices:return
 def fill(left,lo):
  if not left:
   vertex(v+1);return
  for idx in range(lo,len(choices)):
   mask,tri,ps=choices[idx]
   if any(deg[t]>=3 for t in tri) or any(pc[q]>=2 for q in ps):continue
   for t in tri:deg[t]+=1
   for q in ps:pc[q]+=1
   blocks.append(mask);fill(left-1,idx);blocks.pop()
   for q in ps:pc[q]-=1
   for t in tri:deg[t]-=1
 fill(need,0)
vertex(0)
numhalves=sum(map(len,halves.values()));assert numhalves==12780
allhalves=[h for hs in halves.values() for h in hs];assert len(set(allhalves))==numhalves
print('independent halves',numhalves,'seconds',time.time()-start,flush=True)
labelled=set()
for key,Ts in halves.items():
 Cs=halves.get(bytes(2-x for x in key),())
 for T in Ts:
  for C in Cs:labelled.add((T,C))
assert len(labelled)==6150
reps=[json.loads(s) for s in (root/'design_orbits.jsonl').read_text().splitlines()]
expanded=set();orbitsets=[]
for row in reps:
 T=[tuple(x-1 for x in b) for b in row['T']];C=[tuple(x-1 for x in b) for b in row['C']]
 orb=set()
 for perm in itertools.permutations(range(7)):
  tt=tuple(sorted(sum(1<<perm[i] for i in b) for b in T))
  cc=tuple(sorted(sum(1<<perm[i] for i in b) for b in C))
  orb.add((tt,cc))
 assert not (expanded & orb), 'published representatives overlap'
 expanded.update(orb);orbitsets.append(len(orb))
assert labelled==expanded, {'missing':len(labelled-expanded),'extra':len(expanded-labelled)}
raw=json.dumps(sorted(labelled),separators=(',',':')).encode()
result={'algorithm':'fill all blocks by their least vertex; no lexicographic35-triple recursion','regular_halves':numhalves,'vertex_states':calls,'ordered_labelled_pairs':len(labelled),'expanded_representative_pairs':len(expanded),'orbit_sizes':orbitsets,'orbits_disjoint':True,'literal_set_equality':True,'ordered_pair_sha256':hashlib.sha256(raw).hexdigest(),'seconds':time.time()-start}
(root/'independent_design_set.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
