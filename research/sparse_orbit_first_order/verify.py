from pathlib import Path
from itertools import combinations,product
from collections import Counter
from math import gcd
import json
folder=Path(__file__).resolve().parent
reports=[]
for p in (17,41,73):
 row=json.loads((folder/f'p{p}.log').read_text().splitlines()[0]);k=(p-1)//4;n=p-1;g=row['primitive_root']
 xs=[pow(g,j,p) for j in range(n)];assert len(set(xs))==n
 expected=Counter()
 for size in (1,2,3):
  for ex in combinations(range(1,k),size):
   h=k
   for e in ex:h=gcd(h,e)
   expected[k//h]+=(p-1)**(size-1)
 assert sum(expected.values())==row['polynomials']
 for a in row['rows']:
  assert a['cases']==expected[a['orbit']]
  ex=a['exponents'];cs=a['coefficients']
  def evaluate(x):return sum(c*pow(x,e,p) for e,c in zip(ex,cs))%p
  values=list(map(evaluate,xs));modes=[];freq=[]
  for j in range(4):
   h=Counter(values[j::4]);f=max(h.values());mode=min(v for v in h if h[v]==f)
   modes.append(mode);freq.append(f)
  assert modes==a['coset_modes'] and freq==a['coset_frequencies'] and sum(freq)==a['maximum_agreement']
  word=[modes[j%4] for j in range(n)]
  bank={tuple(evaluate(xs[(j+4*t)%n]) for j in range(n)) for t in range(k)}
  assert len(bank)==a['orbit']
  assert all(sum(u==v for u,v in zip(poly,word))==sum(freq) for poly in bank)
  above=31*sum(freq)**2-6*sum(freq)*n-4*n*n>0
  assert above==a['above_quarter_rate_first_order_curve']
 reports.append(dict(p=p,polynomials=row['polynomials'],orbit_rows=len(row['rows']),above_curve_orbits=[a['orbit'] for a in row['rows'] if a['above_quarter_rate_first_order_curve']]))
# Fully independent exhaustion for p17; all degree<4 polynomials modulo
# output translation/scaling, not only a small witness replay.
p=17;k=4;g=3;xs=[pow(g,j,p) for j in range(16)];maxima=Counter();counts=Counter()
for deg in range(1,4):
 for lower in product(range(p),repeat=deg-1):
  cs=[0]+list(lower)+[1];h=k
  for e,c in enumerate(cs):
   if c:h=gcd(h,e)
  orbit=k//h;values=[sum(c*pow(x,e,p) for e,c in enumerate(cs))%p for x in xs]
  M=sum(max(Counter(values[j::4]).values()) for j in range(4))
  maxima[orbit]=max(maxima[orbit],M);counts[orbit]+=1
assert maxima=={2:8,4:7} and sum(counts.values())==307
out=dict(status='passed',reports=reports,independent_p17_maxima=dict(maxima),independent_p17_count=sum(counts.values()),scope='All reported witness orbits and mode profiles replayed, normalized search counts checked independently, complete p17 enumeration independently repeated. Larger-field maximum claims rely on the C++ exhaustive sparse scan. No growing-family impossibility theorem.')
(folder/'verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
