"""Bounded high-L/m source06 branch, plus narrow source00 branch."""
import ast,json,math
from pathlib import Path
import fast_firstjet_count as fast
import trace_singleton_contacts as contact
ROOT=Path(__file__).parent
for filename,names in [('replay_phase_kernels.py',{'rank'}),('search_new_phase.py',{'channel','threshold'}),('search_early_phase.py',{'potential','evaluate'})]:
 tree=ast.parse((ROOT/filename).read_text().replace('9275','9678').replace('9276','9679'));exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names],type_ignores=[]),filename,'exec'))
A=181275;n=262144;w=131071;delta=A-w+1;p=2130706433
r,v=12,43;y=r+v;finish=9679-y;segments=contact.segments;oldpoints=contact.points
oldcache={z:min(a*z+b for lo,hi,a,b in segments if lo<=z<=hi) for z in oldpoints}
results=[];tested=0
for m in [4000,8000,14000,20000,24000]:
 for sr in [300000,302000,304000,304500,304786,305000,306000,308000,310000]:
  for lr in [120,160,200,260,320,400,520]:
   tested+=1;got=evaluate(m,m*lr,m*sr//1000000)
   if got:got['branch']='high_lambda';results.append(got)
for m in [64000,80000,84000,86000]:
 for sr in [309500,309700,309778,309850,310000,310140]:
  for lr in [66300,69000,70000,70443,71000,72000]:
   tested+=1;got=evaluate(m,(m*lr+999)//1000,m*sr//1000000)
   if got:got['branch']='narrow_low_lambda';results.append(got)
results.sort(key=lambda x:x['singleton_bound'])
out=dict(tested=tested,earlier_valid_sources=len(results),best=results[:40],scope='Exact singleton envelope filter on distinct highlambda and narrowstationary branches; no fullpropagation.')
(ROOT/'alternate_phase_grid.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'best':results[:5]},indent=2))
