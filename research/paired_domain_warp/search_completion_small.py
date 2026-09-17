"""Bounded exact sufficient-certificate search; absence is not nonexistence."""
from verify_completion import schedule
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();rows=[]
 for b in [31,61,89,107,127]:
  p=2**b-1;first=None;beating=None;trials=0
  for n in range(2*b,3*b,4):
   if n%4!=2:continue
   for t in range(1,16):
    try:row=schedule(b,1,n,t)
    except AssertionError:continue
    trials+=1
    if row:
     if first is None:first=row
     if n**3*2**n<p**3:
      beating=row;break
   if beating:break
  rows.append(dict(b=b,trials=trials,first_sufficient=first,first_beating_prescription=beating))
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,scope='Half-rate r1 dyadic sufficient certificates, 2b<=n<3b, t<=15. No negative existence conclusion.')
 (BASE/'small_completion_search.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
