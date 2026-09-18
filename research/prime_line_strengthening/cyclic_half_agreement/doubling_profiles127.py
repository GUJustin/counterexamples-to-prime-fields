import itertools,json,time
from pathlib import Path
q=127;m=7;r=63;start=time.monotonic();full=(1<<q)-1
primitive=next(g for g in range(2,q) if all(pow(g,126//d,q)!=1 for d in (2,3,7)))
orbits=[sorted({pow(primitive,j,q)*pow(2,k,q)%q for k in range(7)}) for j in range(18)]
assert len(set(sum(orbits,[])))==126
orbitmasks=[sum(1<<x for x in o) for o in orbits]
dreps=[];covered=set()
for x in range(1,q):
 if x not in covered:
  dreps.append(x);covered.update(s*x*pow(2,k,q)%q for s in (-1,1) for k in range(7))
assert len(dreps)==9
profiles={};records={}
for inds in itertools.combinations(range(18),9):
 om=sum(1<<i for i in inds);mask=0
 for i in inds:mask|=orbitmasks[i]
 profile=tuple((mask&(((mask<<d)|(mask>>(q-d)))&full)).bit_count() for d in dreps)
 profiles.setdefault(profile,[]).append(om);records[om]=(mask,profile)
retained={om for profile,oms in profiles.items() if tuple(62-x for x in profile) in profiles for om in oms}
classes=[];remaining=set(retained);smallfull=(1<<18)-1
while remaining:
 om=min(remaining);unit={(om<<j|om>>(18-j))&smallfull for j in range(18)}
 assert unit<=retained
 mask,profile=records[om];classes.append({'orbit_mask':om,'C_mask':str(mask),'C':[i for i in range(q) if mask>>i&1],'S':[i for i in range(q) if not(mask>>i&1)],'profile':profile,'unit_orbit_size':len(unit),'compatible_T_orbit_masks':profiles[tuple(62-x for x in profile)]});remaining-=unit
pairs=sum(len(oms)*len(profiles.get(tuple(62-x for x in profile),[])) for profile,oms in profiles.items())
out={'q':q,'primitive_root':primitive,'doubling_orbits':orbits,'difference_representatives':dreps,'all_supports':len(records),'distinct_profiles':len(profiles),'retained_supports':len(retained),'ordered_pairs':pairs,'unit_classes':classes,'seconds':time.monotonic()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('doubling_orbits','unit_classes')}));print('unit_classes',len(classes),flush=True)
