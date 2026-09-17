"""Small-field controls with extras and genuinely excluded parameters."""
from pathlib import Path
from math import isqrt
from array import array
import json,time
from check_exhaustive import audit
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();rows=[]
 for p,d,m,D,c in [(101,2,4,2,0),(103,2,4,2,0),(1009,3,3,1,1),(1009,3,3,2,1),(1009,2,5,2,1)]:
  assert all(p%q for q in range(2,isqrt(p)+1));inv=array('I',[0])*p;inv[1]=1
  for i in range(2,p):inv[i]=p-(p//i)*inv[p%i]%p
  row=audit(p,d,m,D,c,inv,False);rows.append(row);print(json.dumps(row),flush=True)
 assert any(r['bad_root_parameters'] for r in rows)
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,
  scope='Small fields test exclusions and extra coordinates. Positive finite existence bound not required, no numerical violation claimed.')
 (BASE/'negative_verification.json').write_text(json.dumps(out,indent=2)+'\n')
