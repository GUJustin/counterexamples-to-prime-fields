"""Exact saturated-L feasibility for a source covering only the missing interval."""
import json
from pathlib import Path
from affine_local_source_gate import solve
ROOT=Path(__file__).parent
results=[]
for m in range(20000,160001,5000):
 for sig in [3040000,3043000,3045000,3046214,3048000,3050000,3053000]:
  s=(sig*m+5000000)//10000000
  results.append(solve(m,s,12,55,3030,gate_t=3261,exact_degree=True))
feasible=[x for x in results if x['feasible']]
ranked=sorted([x for x in results if 'value_at_upper' in x],key=lambda x:x['value_at_upper']/(131071*x['m']**4),reverse=True)
out=dict(tested=len(results),feasible=feasible,best_infeasible=ranked[:10],scope='Exact affine-L saturated regime;local gate validonlythrough total3261;desiredroute total3030. Finite m/s grid only, notglobalexclusion.')
(ROOT/'interval_local_source_grid.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
