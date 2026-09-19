import json,math
from pathlib import Path
base=Path('research/prime_quadratic_line/modular_cyclic_bank')
rows=[json.loads(x) for x in (base/'normalized_gate.jsonl').read_text().splitlines()]
checks=[]; escaped=[]
for z in rows:
 n,m=z['n'],z['m']; h=m-1
 if h>=2 and n%h==0 and n//h>=2:
  r=n//h; bound=min(h+1,r+math.gcd(2,r)); A=z['full_coefficients']['A']
  assert A<=bound,(z,bound)
  checks.append(dict(p=z['p'],n=n,h=h,r=r,A=A,bound=bound))
 if m>=3 and n%m==0 and n//m>=2:
  A=z['full_coefficients']['A']
  if A*A>n: escaped.append(dict(p=z['p'],n=n,h=m,r=n//m,A=A,L=z['full_coefficients']['L']))
print(json.dumps(dict(check_count=len(checks),checks=checks,escaped=escaped),indent=2))
