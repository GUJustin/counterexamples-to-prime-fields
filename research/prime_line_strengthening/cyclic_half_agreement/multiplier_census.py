import itertools,json,time
from pathlib import Path
out=[]
for q in (31,127):
 start=time.monotonic();unseen=set(range(1,q));orbits=[]
 while unseen:
  a=min(unseen);O=[];x=a
  while x not in O:O.append(x);x=2*x%q
  unseen.difference_update(O);orbits.append(O)
 r=(q-1)//2;lam=(q-3)//4;good=[]
 for chosen in itertools.combinations(range(len(orbits)),r//len(orbits[0])):
  D={x for i in chosen for x in orbits[i]}
  if all(sum((x+d)%q in D for x in D)==lam for d in range(1,(q+1)//2)):
   good.append(sorted(D))
 sets=set(map(tuple,good));classes=[]
 while sets:
  D=min(sets);orb={tuple(sorted(a*x%q for x in D)) for a in range(1,q)};assert orb<=set(map(tuple,good));classes.append({'representative':list(D),'rotation_classes':len(orb)});sets-=orb
 rec={'unit_equivalence_classes':classes,'q':q,'doubling_orbits':orbits,'normalized_difference_sets':good,'count':len(good),'seconds':time.monotonic()-start};out.append(rec);print(json.dumps({'q':q,'count':len(good),'seconds':rec['seconds']}),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
