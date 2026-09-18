import itertools,json
from pathlib import Path
def rot(m,j):return ((m<<j)|(m>>(8-j)))&255
def canon(m):return min(rot(m,j) for j in range(8))
def profile(m):return tuple((m&rot(m,d)).bit_count() for d in range(1,5))
def unit(m,g):return sum(1<<(g*j%8) for j in range(8) if m>>j&1)
reps=sorted({canon(sum(1<<j for j in S)) for S in itertools.combinations(range(8),4)})
target=(7,7,7,6);valid=[]
for Q in itertools.combinations_with_replacement(reps,4):
 if tuple(sum(profile(m)[j] for m in Q) for j in range(4))==target:valid.append(Q)
classes=[];remaining=set(valid)
while remaining:
 Q=min(remaining);orb={tuple(sorted(canon(unit(m,g)) for m in Q)) for g in (1,3,5,7)};assert orb<=set(valid);classes.append({'supports':Q,'profiles':[profile(m) for m in Q],'unit_orbit_size':len(orb)});remaining-=orb
out={'rotation_representatives':reps,'skew_representatives':[m for m in reps if profile(m)[3]==0],'compatible_unordered_quadruples':len(valid),'simultaneous_unit_classes':classes}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
