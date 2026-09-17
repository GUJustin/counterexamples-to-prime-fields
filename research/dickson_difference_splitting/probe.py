"""Exact modular factorization probe; finite evidence, not a theorem."""
from math import comb
from itertools import combinations
from pathlib import Path
import json
import sympy as s
x=s.symbols('x')
rows=[]
for p in (17,41,73,89,97):
 k=(p-1)//4
 cs=[[comb(2*k+1,2*j+1)*pow(a,2*k-2*j,p)%p for j in range(k)] for a in range(1,(p+1)//2)]
 degrees={}; multiplicities={}; pairs=0; nonsplit=[]
 for ai,bi in combinations(range(len(cs)),2):
  a,b=cs[ai],cs[bi]
  f=s.Poly(sum(((v-u)%p)*x**j for j,(u,v) in enumerate(zip(a,b))),x,modulus=p)
  unit,factors=s.factor_list(f)
  rebuilt=s.Poly(unit,x,modulus=p)
  for fac,m in factors:
   rebuilt*=fac**m
   degrees[fac.degree()]=degrees.get(fac.degree(),0)+m
   multiplicities[m]=multiplicities.get(m,0)+1
  assert rebuilt==f and f.degree()==k-1
  if any(fac.degree()!=1 for fac,m in factors):nonsplit.append([ai+1,bi+1])
  pairs+=1
 row=dict(p=p,k=k,polynomials=len(cs),pairs=pairs,factor_degrees=degrees,multiplicities=multiplicities,nonsplit_pairs=nonsplit)
 rows.append(row);print(json.dumps(row),flush=True)
Path(__file__).with_name('probe.json').write_text(json.dumps(dict(scope='Exhaustive pairwise factorization at the listed five primes only; no general splitting theorem asserted.',rows=rows),indent=2)+'\n')
