"""Exact cyclotomic determinants excluding three collinear quotient points."""
from itertools import combinations
from pathlib import Path
import json
import sympy as s

x=s.Symbol('x')
modulus=s.Poly(x**4+1,x)
def reduce(f):
    return s.rem(s.Poly(f,x),modulus).as_expr()
points=[]
for j in range(8):
    node=reduce(x**j)
    twice_word=reduce(1+node**4-2*node**2)
    points.append((node,twice_word))
records=[]
exceptions=set()
for support in combinations(range(8),3):
    a,b,c=(points[j] for j in support)
    determinant=reduce((b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1]))
    norm=int(s.resultant(modulus.as_expr(),determinant,x))
    if not norm:
        raise AssertionError(('zero determinant',support))
    factors=s.factorint(abs(norm))
    exceptions.update(map(int,factors))
    records.append(dict(support=support,determinant=str(determinant),norm=norm,
                        prime_factors=list(map(int,factors))))
result=dict(status='PASS',triples=len(records),possible_exceptional_primes=sorted(exceptions),records=records)
Path(__file__).with_name('two_orbit_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
