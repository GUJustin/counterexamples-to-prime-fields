import json,time
from pathlib import Path
p=Path(__file__).with_name('doubling_profiles127.json');a=json.loads(p.read_text());q=127;start=time.monotonic();orbits=a['doubling_orbits'];allsets={};pairs=0
for c in a['unit_classes']:
 D=set(c['C']);assert len(D)==63 and {2*x%q for x in D}==D
 profile=[sum((x+d)%q in D for x in D) for d in range(1,q)]
 for om in c['compatible_T_orbit_masks']:
  T={x for j in range(18) if om>>j&1 for x in orbits[j]}
  assert all(profile[d-1]+sum((x+d)%q in T for x in T)==62 for d in range(1,q));pairs+=1
 for g in range(1,q):allsets[tuple(sorted(g*x%q for x in D))]=1
assert len(allsets)==a['retained_supports']
out={'all_38_representatives_all_126_differences_pass':True,'representative_pairs_checked':pairs,'unit_expansion_count':len(allsets),'seconds':time.monotonic()-start}
p.with_name('doubling_profiles127_verify.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
folder=p.with_name('doubling127_supports');folder.mkdir(exist_ok=True)
for i,c in enumerate(a['unit_classes']):(folder/f'class{i}.support').write_text(','.join(map(str,c['S']))+'\n')
