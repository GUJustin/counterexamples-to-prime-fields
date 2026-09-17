from pathlib import Path
import json
rows=[]
for p in (17,41,97,257,65537):
 n=p-1;chi=[-1]*p;chi[0]=0
 for s in range(1,p):chi[s*s%p]=1
 for L in (1,2,4):
  if 2*L>=p:continue
  counts=[n//4]*L
  for s in range(1,(p+1)//2):
   pairs=[(chi[(a+s)%p],chi[(a-s)%p]) for a in range(1,L+1)]
   sigma=1 if sum(x+y for x,y in pairs)>=0 else -1
   for j,(x,y) in enumerate(pairs):
    a=j+1
    match=(chi[2*a%p]==sigma) if s==a or s==p-a else x==y==sigma
    counts[j]+=bool(match)
  certified=p>=4096*L**3*4**L
  met=all(16*c-6*n>=0 and (16*c-6*n)**2*L>=n*n for c in counts)
  if certified:assert met
  rows.append(dict(p=p,L=L,agreement_counts=counts,finite_prime_condition=certified,displayed_gain_met=met))
Path(__file__).with_name('dickson_majority_lower_checks.json').write_text(json.dumps(rows,indent=2)+'\n')
print('Passed',len(rows),'majority constructions;',sum(r['finite_prime_condition'] for r in rows),'meets sufficient prime bound.')
