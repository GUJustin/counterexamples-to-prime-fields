from math import comb
from collections import Counter
from pathlib import Path
import json,random
rng=random.Random(20260918)
rows=[]
for p in (17,41,73,97):
 n=p-1;k=n//4;e=2*k+1
 reps=[];seen=set()
 for a in range(1,p):
  if a*a%p not in seen:seen.add(a*a%p);reps.append(a)
 values=[[sum(comb(e,2*j+1)*pow(a,2*k-2*j,p)*pow(x,j,p) for j in range(k+1))%p for x in range(1,p)] for a in reps]
 chi=lambda x:0 if x%p==0 else (1 if pow(x%p,n//2,p)==1 else -1)
 subsets=[tuple(i for i in range(len(reps)) if mask>>i&1) for mask in range(1,1<<len(reps))] if p==17 else [tuple(sorted(rng.sample(range(len(reps)),L))) for L in range(1,len(reps)+1) for _ in range(3)]
 for ids in subsets:
  L=len(ids);T=0;zero=plus=minus=0
  for x in range(1,p):
   counts=Counter(values[i][x-1] for i in ids);T+=max(counts.values())
   if chi(x)==-1:zero+=counts[0]
   else:plus+=counts[1];minus+=counts[p-1]
  assert 4*zero==L*n and 8*plus==L*n and 8*minus==L*n
  excess=8*T-3*L*n-8*n-2*L
  assert excess<=0 or excess*excess<=n*(2*L*p-4*L*L)
  gap=8*T-3*L*n
  assert gap<=0 or gap*gap<64*L*n*n
 rows.append(dict(p=p,bank_size=len(reps),subsets_checked=len(subsets),status='passed'))
Path(__file__).with_name('dickson_sharp_threshold_checks.json').write_text(json.dumps(rows,indent=2)+'\n')
print('Passed',sum(r['subsets_checked'] for r in rows),'subset bucket audits:',rows)
