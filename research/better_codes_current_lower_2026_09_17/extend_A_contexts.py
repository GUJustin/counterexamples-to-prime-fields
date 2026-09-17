"""Build conditional new contexts for primary A box(r36,y163), total9275.

Old singleton and base receipts are deliberately frozen. New singleton bounds
use actual target phase source routes. Extends the eight Bellman tables exactly.
"""
import ast,json,re
from pathlib import Path
# Execute only initialization of the expanded old-slice diagnostic.
ROOT=Path(__file__).parent
exec((ROOT/'expanded_A_old_slice.py').read_text().split('def breakpoints')[0])
for filename,names in [('search_new_phase.py',{'channel','threshold'}),('repeat_phases.py',{'pieces','candidates'})]:
 tree=ast.parse((ROOT/filename).read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names],type_ignores=[]),filename,'exec'))
delta=A-w+1
unique=base_sources+[[new['L'],new['Y'],new['s'],new['gap']]]
unique_pot=q.POT[:7]+q.POT[-1:]
newkeys=[(r,v) for r in range(1,37) for v in range(164-r) if (r,v) not in q.rows]
assert len(newkeys)==268
thresholds={}
for r,v in newkeys:
 ts=[threshold(L,Y,S,g,r,v) for L,Y,S,g in unique]
 assert min(ts)==0,('no singleton route at zero',r,v,ts)
 thresholds[r,v]=ts

def own_bound(r,v,slope):
 ts=thresholds[r,v];finish=9276-r-v
 cuts=sorted({0,finish}|{t for t in ts if t<finish});answer=0
 for lo,stop in zip(cuts,cuts[1:]):
  hi=stop-1;lines=[(a,a*(r+v)+b*(r+v)+c*r) for j,(a,b,c) in enumerate(unique_pot) if ts[j]<=lo]
  points={lo,hi}
  for k,(a,b) in enumerate(lines):
   for aa,bb in lines[:k]:
    if a!=aa:
     cross=(bb-b)//(a-aa)
     points.update(x for x in [cross,cross+1] if lo<=x<=hi)
  for z in points:answer=max(answer,min(a*z+b for a,b in lines)-slope*z)
 return answer

sheets=[];new_own_count=0;packing_pairs=0
for j in range(8):
 text=(q.CACHE/f'MovingFiberPackingData6811S{j}.lean').read_text()
 slope=int(re.search(r'def slope : Nat := (\d+)',text)[1]);own={};packed={}
 for typ,r,nums in re.findall(r'def (own|packed)(\d+) : Array Nat := #\[([^\]]*)\]',text):
  (own if typ=='own' else packed)[int(r)]=[int(a) for a in nums.split(',')]
 for r in range(1,37):
  own.setdefault(r,[]);packed.setdefault(r,[])
  for v in range(len(own[r]),164-r):own[r].append(own_bound(r,v,slope));new_own_count+=1
 packed[0]+=[0]*(164-len(packed[0]))
 for r,v in newkeys:
  best=0
  for rr in range(1,r+1):
   for u in range(v+1):
    best=max(best,own[rr][u]+packed[r-rr][v-u]);packing_pairs+=1
  assert len(packed[r])==v
  packed[r].append(best)
 sheets.append((slope,own,packed))
 print('extended packing sheet',j,flush=True)

for r,v in newkeys:
 lines=[(slope,packed[r][v]) for slope,own,packed in sheets]
 finish=9276-r-v;breaks={3,finish}
 for k,(a,b) in enumerate(lines):
  for aa,bb in lines[:k]:
   if a!=aa:
    cross=(bb-b)//(a-aa)
    breaks.update(x for x in [cross,cross+1,cross+2] if 3<=x<finish)
 seg=[]
 for z in sorted(breaks-{finish}):
  a,b=min(lines,key=lambda ab:ab[0]*z+ab[1])
  if not seg or a!=seg[-1][2]:seg.append([z,a*z+b,a])
 ts=thresholds[r,v]
 q.rows[r,v]=dict(base=[r,v,*[min(a*z+b for a,b in lines) for z in range(3)],seg],threshold=[ts[j] for j in schedule]+[ts[-1]],prefixValues=[0]*32)
assert len(q.rows)==5238
# Run the same complete prefix and ledger propagation, with the new rows included.
body=(ROOT/'expanded_A_old_slice.py').read_text().split('def breakpoints')[1]
body='def breakpoints'+body
body=body.replace("q.ROOT/'expanded_A_old_slice.json'","q.ROOT/'expanded_A_all_contexts.json'")
body=body.replace("Only old4970 contexts tested; base/chain/B/TCap and auxiliary sources frozen. NOT a certificate;268 extra contexts excluded.","All5238 contexts;268new singleton/base contexts constructed and packed, old4970base/singletons/chain/B/TCap/auxiliary sources frozen. NOT a certificate.")
exec(body)
(ROOT/'expanded_A_context_construction.json').write_text(json.dumps(dict(new_contexts=len(newkeys),new_singleton_bounds=new_own_count,packing_pairs=packing_pairs,all_new_contexts_have_source_threshold_zero=True,scope='New contexts use target source potentials and exact packing extension; old singleton/base inputs remain frozen.'),indent=2)+'\n')
