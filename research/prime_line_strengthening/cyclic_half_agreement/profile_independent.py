"""Validate all retained profiles by set intersections; independent small census."""
from pathlib import Path
import json,itertools,math
r=Path(__file__).parent;out=[]
for q in [7,11,13,17,19,23]:
 d=json.loads((r/f'profiles_q{q}.json').read_text());h=(q-1)//2
 def bits(m):return {i for i in range(q) if m>>i&1}
 def key(S):return sum(len(S & {(x+a)%q for x in S})*(h+1)**(a-1) for a in range(1,h+1))
 def canonical(S):return min(sum(1<<((x+a)%q) for x in S) for a in range(q))
 P={a['key']:a for a in d['profiles']};allowed=[];pairs=0
 for k,row in P.items():
  assert row['target_key'] in P
  target=P[row['target_key']];pairs+=len(row['C_masks'])*len(target['C_masks'])
  kval=k;tval=row['target_key']
  for _ in range(h):assert kval%(h+1)+tval%(h+1)==h-1;kval//=h+1;tval//=h+1
  for m in row['C_masks']:
   S=bits(m);assert len(S)==h and key(S)==k and canonical(S)==m
   allowed.append(canonical(set(range(q))-S))
 assert sorted(allowed)==d['allowed_first_support_masks'] and len(set(allowed))==len(allowed)
 exhaustive=False
 if q<=13:
  allprofiles={}
  for S in itertools.combinations(range(q),h):
   m=sum(1<<i for i in S)
   if canonical(S)!=m:continue
   allprofiles.setdefault(key(set(S)),[]).append(m)
  assert sum(map(len,allprofiles.values()))==math.comb(q,h)//q
  def comp(k):
   ans=0
   for i in range(h):ans+=(h-1-k%(h+1))*(h+1)**i;k//=h+1
   return ans
  good={k:sorted(v) for k,v in allprofiles.items() if comp(k) in allprofiles}
  assert good=={k:sorted(a['C_masks']) for k,a in P.items()};exhaustive=True
 out.append({'q':q,'all_retained_masks_validated':True,'compatible_first_supports':len(allowed),'ordered_profile_pairs':pairs,'independent_exhaustive_census':exhaustive})
assert json.loads((r/'profiles_q7.json').read_text())['allowed_first_support_masks']==[23,29]
(r/'profile_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
