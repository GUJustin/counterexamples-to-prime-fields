"""Target identity absorption and old-activation impact of auxiliary replacements."""
import json,re,hashlib
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parent;CACHE=ROOT.parents[1]/'tmp/current-lower-primary-cache'
manifest=json.loads((ROOT/'auxiliary_source_replacements.json').read_text())
a,b,c=sp.symbols('a b c');identity=[655365+262146*a,1310730+524292*a,2097170+524292*a+524292*b+262146*c]
checks=[]
for suffix in 'ABCD':
 p=ROOT/f'MovingFiberArithmetic6811{suffix}.lean'
 if not p.exists():p=CACHE/p.name
 for idx,body in re.findall(r'namespace ProximityPrize.SubmissionLower.MovingFiberArithmetic6811.G(\d+)\n(.*?)(?=\nend ProximityPrize|\Z)',p.read_text(),re.S):
  scale=int(re.search(r'def scale : ℕ := (\d+)',body)[1])
  for j in range(3):
   expr=re.search(r'def g'+str(j)+r' \(a b c : ℕ\) : ℕ :=\s*(.*?)(?=\ndef )',body,re.S)[1]
   assert re.fullmatch(r'[0-9abc*+^\s]+',expr)
   graph=sp.sympify(expr.replace('^','**').replace('\n',' '),locals={'a':a,'b':b,'c':c})
   slack=sp.Poly(50204*graph-scale*131073*80870*identity[j],a,b,c)
   coeffs=[int(x) for x in slack.coeffs()];assert min(coeffs)>=0
   checks.append(dict(group=int(idx),flag_coordinate=j,min_nonzero_coefficient=min(coeffs),terms=len(coeffs)))
assert len(checks)==48
assert all(all(v>=0 for v in x['flag_delta']) for x in manifest['sources'])
ns={'__file__':str(ROOT/'replay_ledger.py')};exec((ROOT/'replay_ledger.py').read_text().split('worst=[]')[0],ns)
usage={g:dict(intervals=0,rows=set(),lost_intervals=0,lost_rows=set(),lost_integer_z=0,examples=[]) for g in range(16)}
for (r,v),row in ns['rows'].items():
 lo=0
 for stop,who in row['singletons']:
  if 1<=who<=16:
   g=who-1;u=usage[g];u['intervals']+=1;u['rows'].add((r,v))
   cutoff=manifest['groups'][g]['new_source_limit']-r-v+1
   lost=max(0,min(stop,cutoff)-lo)
   if lost:
    u['lost_intervals']+=1;u['lost_rows'].add((r,v));u['lost_integer_z']+=lost
    if len(u['examples'])<3:u['examples'].append(dict(r=r,v=v,lo=lo,stop=stop,new_required_lo=cutoff))
  lo=stop
for u in usage.values():u['rows']=len(u['rows']);u['lost_rows']=len(u['lost_rows'])
out=dict(identity_target_pass=True,argument='All new budget flags dominate old ones; old graph coefficients already absorb target identity charge coefficientwise.',checks=checks,old_singleton_usage=usage,scope='Identity and activation only; updated root upper costs, own/packed sheets and new-target source theorem port still required.')
(ROOT/'auxiliary_geometry_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('48 target identity coefficient gates pass')
print('lost intervals',sum(x['lost_intervals'] for x in usage.values()),'lost z',sum(x['lost_integer_z'] for x in usage.values()))
print('groups',[(g,u['intervals'],u['lost_intervals']) for g,u in usage.items()])
