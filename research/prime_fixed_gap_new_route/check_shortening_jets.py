"""Exact modular check of the two jet identities used in common-factor gate."""
import json
from math import comb, prod
from pathlib import Path
checks=0
primes=(13,17,29,41,73,97)
for p in primes:
 k=(p-1)//4;e=2*k+1
 ts=sorted({a*a%p for a in range(1,p)})
 ps={t:[comb(e,2*j+1)*pow(t,k-j,p)%p for j in range(k+1)] for t in ts}
 def ev(c,x,q):
  return sum(c[j]*(prod(range(j-q+1,j+1)) if q else 1)*pow(x,j-q,p) for j in range(q,len(c)))%p
 for x in range(1,p):
  sq=pow(x,(p-1)//2,p)==1
  for t,c in ps.items():
   g=ev(c,x,0)
   if not sq and g==0:
    assert ev(c,x,1)**2%p==t*pow(16*x*x*(t-x),-1,p)%p
    checks+=1
   if sq and g in (1,p-1) and t!=x:
    assert ev(c,x,2)==(3*g*pow(8*x*x,-1,p)+g*pow(16*x*(t-x),-1,p))%p
    checks+=1
result={'status':'PASS','exact_jet_checks':checks,'primes':primes}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
