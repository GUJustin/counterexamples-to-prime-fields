"""Eliminate the final Walsh coordinate without discarding its zero chart."""
import json,itertools
from pathlib import Path
import sympy as s
base=Path(__file__).parent
data=json.loads((base/'independent_selector_gate.json').read_text())
t=s.symbols('t0:8'); loc={str(x):x for x in t}
f=[s.sympify(r['equation'],locals=loc) for r in data['conditions']]
a=[s.expand(v).coeff(t[7]) for v in f]; b=[v.subs(t[7],0) for v in f]
assert all(s.expand(v-ai*t[7]-bi)==0 for v,ai,bi in zip(f,a,b))
minors=[]
for i,j in itertools.combinations(range(6),2):
    g=s.expand(a[i]*b[j]-a[j]*b[i])
    minors.append({'rows':[i,j],'polynomial':str(g)})
result={'linear_coefficients':[str(s.factor(x)) for x in a], 'constant_coefficients':[str(s.factor(x)) for x in b], 'compatibility_minors':minors,'charts':'Where a_i is nonzero, t7=-b_i/a_i and all minors with row i must vanish. On the all-a-zero chart, every b_i must vanish; it is retained.'}
(base/'independent_selector_eliminate.json').write_text(json.dumps(result,indent=2))
print(json.dumps({'linear_coefficients':result['linear_coefficients'],'minor_term_counts':[len(s.Poly(s.sympify(v['polynomial'],locals=loc),*t).terms()) for v in minors]}))
