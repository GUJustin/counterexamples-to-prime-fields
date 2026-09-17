from finite_scan import evaluate,counts,D
from pathlib import Path
import json
records=[];attempted=0
for A,ms in [(183210,range(16,41)),(181284,range(80,321,8))]:
 best=None;feasible=0
 for m in ms:
  for b in sorted({m*j//100 for j in range(25,38)}):
   top=(m*A+b-1)//D
   for B in sorted({top-j for j in (0,1,2,4,8,16,32,64) if top-j>=b}):
    attempted+=1;r=evaluate(m,b,A,B)
    if r:
     feasible+=1
     if best is None or r['exact_regular_ratio']<best['exact_regular_ratio']:best=r
 records.append(dict(A=A,feasible=feasible,best=best))
out=dict(attempted=attempted,records=records)
print(json.dumps(out,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
