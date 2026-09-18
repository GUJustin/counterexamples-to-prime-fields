from fractions import Fraction
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
rows=[]
for H in (2,3,4,6,8):
 bank=[(a,b) for a in range(1,H+1) for b in range(1,H+1)]
 roots=set()
 for (a,b),(c,d) in combinations(bank,2):
  if a!=c: roots.add(Fraction(d-b,a-c))
  roots.add(Fraction(-b-d,a+c))
 total=0
 for x in roots:
  u,v=x.numerator,x.denominator; height=max(abs(u),v)
  assert height<=2*H
  bucket=max(Counter((a*u+b*v)**2 for a,b in bank).values())
  assert bucket<=2*(1+(H-1)//height)
  total+=bucket
 assert total<=32*H*H
 rows.append({'H':H,'bank_size':H*H,'collision_coordinates':len(roots),'sum_max_buckets':total,'proved_bound':32*H*H})
L=10; bank=[(3**i,3**(2*i)) for i in range(1,L+1)]; roots=[]
for (a,b),(c,d) in combinations(bank,2):
 roots.extend((Fraction(d-b,a-c),Fraction(-b-d,a+c)))
assert len(set(roots))==L*(L-1)
for x in roots:
 u,v=x.numerator,x.denominator
 assert max(Counter((a*u+b*v)**2 for a,b in bank).values())==2
out={'status':'PASS_EXACT_RATIONAL_REPLAY','grid_cases':rows,'sparse_bank_size':L,'sparse_distinct_pair_roots':len(set(roots)),'scope':'small exact checks support, not replace, the symbolic proof'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
