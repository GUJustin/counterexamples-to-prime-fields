"""Exhaustive small subset-sum checks of the variance concentration lemma."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from math import comb,isqrt
import json,time
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();rows=[];count=0
 for m in range(2,21):
  for D in range(1,m):
   hist=Counter(map(sum,combinations(range(1,m+1),D)));A=comb(m,D);V=D*(m-D)*(m+1)
   assert sum(hist.values())==A
   assert 3*sum(n*(2*s-D*(m+1))**2 for s,n in hist.items())==A*V
   j=isqrt((A*A-1)//(V+1))+1;actual=max(hist.values())
   assert actual>=j and actual**2*(V+1)>=A*A
   if D in (1,m-1):assert j==actual==1
   rows.append(dict(m=m,D=D,lower=j,actual=actual));count+=A
 out=dict(status='passed',fixtures=len(rows),supports_enumerated=count,seconds=time.monotonic()-start,rows=rows)
 (BASE/'concentration_verification.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='rows'})
