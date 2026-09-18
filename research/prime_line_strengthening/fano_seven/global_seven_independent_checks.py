"""Independent final amplitude rank and explicit critical deletion isomorphism."""
import runpy,json,itertools
from pathlib import Path
r=Path(__file__).parent;s=runpy.run_path(str(r/'orbit7_independent_field_audit.py'));K=s['K'];w=s['w'];u=w*w;v=w*w+w-1;z=w*w+w
M=[[K(eval(a,{'u':u,'v':v,'w':w,'z':z})) for a in row] for row in json.loads((r/'orbit7_generic.json').read_text())['rows']]
amp=[K(1),3*w*w+4*w-5,3*w*w+4*w-6]
assert all(sum((a*b for a,b in zip(row,amp)),K(0))==0 for row in M)
minor=None
for i,j in itertools.combinations(range(7),2):
 for a,b in itertools.combinations(range(3),2):
  det=M[i][a]*M[j][b]-M[i][b]*M[j][a]
  if det:minor={'rows':[i,j],'columns':[a,b],'value':det.out()};break
 if minor:break
assert minor
assert v*w*(v-w)/((w-1)*(z-v))==u
reps=[json.loads(a) for a in (r/'design_orbits.jsonl').read_text().splitlines()];row=reps[2]
# Construct only the one necessary critical deletion directly.
blocks=[set(t)|{8} for t in row['T']]+[set(range(1,8))-set(c) for c in row['C']]
keep=[1,2,4,5,6,7,8];T=[b-{3} for b in blocks if 3 in b];C=[set(keep)-b for b in blocks if 3 not in b]
targetT={tuple(b) for b in reps[7]['T']};targetC={tuple(b) for b in reps[7]['C']};mapping=None
for p in itertools.permutations(range(1,8)):
 f=dict(zip(keep,p));tr=lambda bs:{tuple(sorted(f[i] for i in b)) for b in bs}
 if tr(T)==targetT and tr(C)==targetC:mapping=f;break
assert mapping
out={'pass':True,'rank_two_minor':minor,'unique_normalized_amplitude':[a.out() for a in amp],'orbit2_extension_delete_candidate':3,'old_to_orbit7_labels':mapping,'deleted_T':[sorted(b) for b in T],'deleted_C':[sorted(b) for b in C]}
(r/'global_seven_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
