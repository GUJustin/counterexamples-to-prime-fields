"""Exact independent replay of every finite cancellation case used in scope proof."""
import json
from pathlib import Path
out=[]
for k in (1,3):
 for pole in ('off_S','double_S','simple_S'):
  rows=[]
  for v1 in range(2*k+1):
   for v2 in range(k+1):
    if pole=='double_S' and v1:continue
    if pole=='simple_S' and v2:continue
    m1=2*k-v1+(pole=='double_S');m2=k-v2+(pole=='simple_S')
    genus=6*k-2*(v1+v2)
    cusp=m1//2
    intersection=min(m1,2*m2)
    budget=genus-cusp-intersection
    assert budget<=3*k
    rows.append(dict(v1=v1,v2=v2,m1=m1,m2=m2,arithmetic_genus_bound=genus,cusp_lower=cusp,intersection_lower=intersection,finite_budget=budget))
  out.append(dict(k=k,pole=pole,maximum=max(r['finite_budget'] for r in rows),cases=rows))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(pass_all=True,groups=out),indent=2))
print([(r['k'],r['pole'],len(r['cases']),r['maximum']) for r in out])
