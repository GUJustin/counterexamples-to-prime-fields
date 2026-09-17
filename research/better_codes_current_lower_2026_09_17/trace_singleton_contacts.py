"""Identify exact root/phase contacts creating the binding singleton allowance."""
import ast,json,textwrap
from pathlib import Path
import repaired_auxiliary_roots as roots
ROOT=Path(__file__).parent
for filename,names in [('base_packing_audit.py',{'mix','cost','safe'})]:
 tree=ast.parse((ROOT/filename).read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names],type_ignores=[]),filename,'exec'))
r,v=12,43;y=r+v;finish=9679-y
record=next(x for x in json.loads((ROOT/'regenerated_singletons_1_12.json').read_text())['rows'] if (x['r'],x['v'])==(r,v))
ts=record['threshold'];pot=json.loads((ROOT/'expanded_total_all_contexts.json').read_text())['potentials'];pot=pot[:7]+pot[-1:]
src=(ROOT/'regenerate_singletons.py').read_text();block=src[src.index('  segments=[]'):src.index('  own=[0]*8')];exec(textwrap.dedent(block))
contacts=[]
for z in points:
 value=min(a*z+b for lo,hi,a,b in segments if lo<=z<=hi)
 if value!=record['own'][0]:continue
 candidates=[]
 if r<=32 and y<=149 and y+z<=8121 and safe(r,y):candidates.append(('carrier',cost(r,v,z)))
 for j,(a,b,c) in enumerate(pot):
  if ts[j]<=z:candidates.append((f'phase{j}',a*(y+z)+b*y+c*r))
 for group in range(16):
  d=roots.root_domain(group,r,v)
  if d and d[0]<=z<=d[1]:candidates.append((f'root{group}',roots.root_upper(group,r,v,z)))
 contacts.append(dict(z=z,total=y+z,value=value,winners=[name for name,val in candidates if val==value],alternatives=sorted(candidates,key=lambda x:x[1])[:8]))
assert contacts
out=dict(r=r,v=v,sheet=0,slope=0,allowance=record['own'][0],contacts=sorted(contacts,key=lambda x:x['z']))
(ROOT/'binding_singleton_contacts.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
