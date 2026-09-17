"""Check the sharp next-dimension cutoff in the integer construction."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json,time
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();rational=0
 for q in (8,16,32):
  for m in range(3,11):
   R=[Fraction(q**(i+1)-1,q**i-1) for i in range(1,m+1)]
   for D in range(2,m):
    values=[sum((R[i] for i in I),Fraction()) for I in combinations(range(m),D)]
    assert len(values)==len(set(values));rational+=len(values)
 rows=[]
 for row in json.loads((BASE/'integer_verification.json').read_text())['rows']:
  d,m,D,q=(row[k] for k in ('d','m','D','q'))
  if D<2:continue
  p=(1<<row['b'])-1;R=[pow(x,d,p) for x in row['line']['core_roots']]
  values={}
  for I in combinations(range(m),D):
   value=sum(R[i] for i in I)%p;assert value not in values;values[value]=I
  reference=sum(R[:D])%p;assert values[reference]==tuple(range(D))
  S=row['line']['selected_sum'];survivors=[I for v,I in values.items() if v==reference and sum(i+1 for i in I)==S]
  assert len(survivors)<=1
  rows.append(dict(b=row['b'],d=d,m=m,D=D,new_K=d*D-d,surviving_nearby_parameters=len(survivors)))
 out=dict(status='passed',rational_supports_checked=rational,finite_rows=rows,seconds=time.monotonic()-start)
 (BASE/'degree_cutoff_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
