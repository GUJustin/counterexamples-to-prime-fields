"""Exact rational certificate, independent of the p-adic reconstruction used to discover it."""
import json, math
from fractions import Fraction as F
from pathlib import Path
D=Path(__file__).parent
nodes=list(map(F,['11/9','11/5','77/65','1','66/65','22/25','6/5','55/52','11/10','77/95']))+[None]+list(map(F,['0','33/5','33/25','99/95','33/35']))
polys=[list(map(F,row.split())) for row in [
'693/25 -165/2 883/11 -6175/242',
'-99/14 90/7 -81/14 0',
'-198/25 69/5 -65/11 0',
'0 0 0 0','0 -1 1 0','0 -12/5 38/11 -130/121','0 6 -54/11 0','0 -6 116/11 -50/11']]
seed=json.loads((D/'local_search.json').read_text());supports=seed['selected_supports']
def ev(c,x):return c[3] if x is None else sum(a*x**j for j,a in enumerate(c))
word=[]
for j in range(16):
 values={ev(polys[i],nodes[j]) for i,S in enumerate(supports) if j in S}
 assert len(values)==1;word.append(values.pop())
assert [[j for j in range(16) if ev(c,nodes[j])==word[j]] for c in polys]==supports
fresh=[F(14,9)*a for a in polys[1]]
fresh_support=[j for j in range(16) if ev(fresh,nodes[j])==word[j]]
assert fresh_support==[0,1,3,8,10]
assert fresh not in polys
# Affine chart U=1/(X-3), with section transformed to U^3 P(3+1/U).
assert F(3) not in nodes
affine_nodes=[F(0) if x is None else 1/(x-3) for x in nodes]
def transform(c):
 out=[F(0)]*4
 for j,a in enumerate(c):
  for k in range(j+1):out[3-k]+=a*math.comb(j,k)*3**(j-k)
 return out
affine_polys=list(map(transform,polys));affine_fresh=transform(fresh)
affine_word=[word[j] if x is None else affine_nodes[j]**3*word[j] for j,x in enumerate(nodes)]
assert len(set(affine_nodes))==16
assert all(ev(affine_polys[i],affine_nodes[j])==affine_word[j] for i,S in enumerate(supports) for j in S)
assert [j for j,x in enumerate(affine_nodes) if ev(affine_fresh,x)==affine_word[j]]==fresh_support
encode=lambda xs:[None if x is None else str(x) for x in xs]
out=dict(projective_nodes=encode(nodes),projective_polynomials=[encode(c) for c in polys],projective_word=encode(word),affine_nodes=encode(affine_nodes),affine_polynomials=[encode(c) for c in affine_polys],affine_word=encode(affine_word),fresh_projective=encode(fresh),fresh_affine=encode(affine_fresh),fresh_support=fresh_support,selected_supports=supports,exact_56_incidences=True,exact_fifth_match=True)
(D/'rational_seed.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 56 rational incidences, exact fresh five-match cubic, and affine chart.')
