"""Critical-context routing using the proved exact weighted slab support bound.
Arithmetic only: the new recursive rank/budget lemma still needs a Lean port.
"""
import json,sys
from pathlib import Path
import exact_contact_thresholds as old
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'phase_source_feasibility'))
from exact_slab import thin

def passes(source,r,v,z,total=9678):
 D,L,Y,S,gap=source
 if z>total-r-v:return True
 if r+v+z>L or r+v>Y or r>S:return False
 return thin(D,L,Y,S,r,v,z,old.DELTA)<gap

def threshold(source,r,v,total=9678,upper=None):
 lo=0;hi=total+1-r-v if upper is None else upper
 assert passes(source,r,v,hi,total)
 while lo<hi:
  mid=(lo+hi)//2
  if passes(source,r,v,mid,total):hi=mid
  else:lo=mid+1
 assert passes(source,r,v,lo,total)
 if lo:assert not passes(source,r,v,lo-1,total)
 return lo

if __name__=='__main__':
 rows=[]
 prior=json.loads((old.ROOT/'exact_contact_critical.json').read_text())
 for j,source in enumerate(old.sources()):
  z=threshold(source,12,43,upper=prior[j]['exact_D_threshold'])
  rows.append(dict(source=j,old_threshold=prior[j]['old_threshold'],exact_D_threshold=prior[j]['exact_D_threshold'],exact_slab_threshold=z,strict_surplus_at_threshold=source[-1]-thin(*source[:4],12,43,z,old.DELTA)))
 out=dict(context=[12,43],rows=rows,scope='Exact slab arithmetic; requires new support-rank and recursive-budget Lean lemmas. No full-certificate or score claim.')
 (old.ROOT/'exact_slab_critical.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
