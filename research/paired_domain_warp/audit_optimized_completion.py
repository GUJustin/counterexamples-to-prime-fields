"""Independent integer-inequality replay of every optimized completion row.

No search/rounding helper imports. The stored integers are upper bounds;
verifying their inequalities is sufficient even without trusting the search.
"""
from pathlib import Path
from math import comb,isqrt
import json,time
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();source=json.loads((BASE/'optimized_completion.json').read_text());rows=[];primes=set()
 for row in source['rows']:
  if row.get('found') is False:continue
  b=row['b'];p=(1<<b)-1;r=row['r'];n=row['n'];K=row['K'];t=row['t'];m=row['m0'];d=row['D0'];k=row['event_budget_bits']
  if b not in primes:
   assert all(b%i for i in range(2,isqrt(b)+1));s=4
   for _ in range(b-2):s=(s*s-2)%p
   assert s==0;primes.add(b)
  assert n==2*(m+2*t+r) and K==n//2 and K==2*(d+t)-1 and 0<d<m
  C=4*r+4;assert p>max((n+1)**2,C*C,2*m*m)
  scale=1<<row['precision'];u=list(map(int,row['scaled_missing']));assert len(u)==t+1
  assert all(0<x<scale for x in u)
  L=comb(m,d);den=L*(p-2*m*m);num=p**r*(p-2*m*m)+L*(C**(2*r+2)+2*m*m)
  assert num*scale*(1<<k)<=u[0]*den
  for before,after in zip(u,u[1:]):
   assert (p*before*before+C*C*before*scale)*(1<<k)<=after*(p-8)*scale
  assert (p-1)**r*u[-1]<scale
  target=row['failure_bits']
  if target is None:assert k==0
  else:assert (t+1)*(1<<target)<1<<k
  A=2*r+1;e=row['prescription_fraction_less_than_power_two'];left=n**A*(1<<n);right=p**A
  if e<0:left<<=-e*A
  else:right<<=e*A
  assert left<right
  assert row['strict_elias_sufficient']==(A*(b-1)>n)
  rows.append(dict(b=b,r=r,n=n,K=K,t=t,failure_bits=target,prescription_exponent=e,
   below_elias=A*(b-1)>n,eligible_for_main_table=e<0 and A*(b-1)>n))
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,
  scope='Independent exact schedule verification with weaker character and conditioning constants. Search optimality is not claimed. Only rows marked eligible contradict the prescription below Elias.')
 (BASE/'optimized_completion_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
