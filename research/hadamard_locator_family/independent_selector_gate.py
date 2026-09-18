"""Exact odd-quartic compatibility equations for independent selectors."""
import itertools,json
from pathlib import Path
import sympy as s
t=s.symbols('t0:8')
def chi(a,x): return (-1)**((a&x).bit_count())
r=[sum(chi(a,x)*t[a] for a in range(8)) for x in range(8)]
selectors=[0,1,2,4]
records=[]
for a,b in itertools.combinations(selectors,2):
    E=[chi(a,x)*r[x] for x in range(8) if chi(a,x)==chi(b,x)]
    D=[chi(a,x)*r[x] for x in range(8) if chi(a,x)!=chi(b,x)]
    def e3(v): return sum(s.prod(z) for z in itertools.combinations(v,3))
    E1=s.expand(sum(E));D1=s.expand(sum(D))
    E3=s.expand(e3(E));D3=s.expand(e3(D))
    f=s.Poly(s.expand(E1*D3-D1*E3),t)
    content,primitive=f.primitive()
    records.append({'selectors':[a,b],'E1':str(E1),'D1':str(D1),'E3':str(E3),'D3':str(D3),'removed_integer_content':int(content),'equation':str(s.factor(primitive.as_expr())),'terms':len(primitive.terms())})
out={'root_convention':'r_x = sum_a (-1)^popcount(a & x) t_a','selectors':selectors,'conditions':records,'scope':'Necessary odd/odd root-sharing conditions. Distinct nonzero root squares, distinct six edge squares, and full locator guards remain mandatory.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
