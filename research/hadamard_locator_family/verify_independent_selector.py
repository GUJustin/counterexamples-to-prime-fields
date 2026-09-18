"""Independent integer coefficient replay; Python standard library only."""
import ast,itertools,json
from pathlib import Path
P=Path(__file__).parent
zero=(0,)*8

def add(a,b):
 d=dict(a)
 for k,v in b.items():
  d[k]=d.get(k,0)+v
  if not d[k]: del d[k]
 return d

def scale(a,c): return {k:v*c for k,v in a.items() if v*c}
def mul(a,b):
 d={}
 for k,v in a.items():
  for l,w in b.items():
   e=tuple(x+y for x,y in zip(k,l)); d[e]=d.get(e,0)+v*w
 return {k:v for k,v in d.items() if v}
def power(a,n):
 d={zero:1}
 for _ in range(n): d=mul(d,a)
 return d
variables={f't{i}':{tuple(int(j==i) for j in range(8)):1} for i in range(8)}
def parse(n):
 if isinstance(n,ast.Constant): return {zero:n.value} if n.value else {}
 if isinstance(n,ast.Name): return variables[n.id]
 if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub): return scale(parse(n.operand),-1)
 if isinstance(n,ast.BinOp):
  a=parse(n.left)
  if isinstance(n.op,ast.Pow): return power(a,n.right.value)
  b=parse(n.right)
  if isinstance(n.op,ast.Add): return add(a,b)
  if isinstance(n.op,ast.Sub): return add(a,scale(b,-1))
  if isinstance(n.op,ast.Mult): return mul(a,b)
 raise ValueError(ast.dump(n))
def expr(s): return parse(ast.parse(s,mode='eval').body)
def summand(v):
 d={}
 for a in v:d=add(d,a)
 return d
def chi(a,x):return 1 if (a&x).bit_count()%2==0 else -1
roots=[summand(scale(variables[f't{a}'],chi(a,x)) for a in range(8)) for x in range(8)]
def elementary3(v):return summand(mul(mul(a,b),c) for a,b,c in itertools.combinations(v,3))
data=json.loads((P/'independent_selector_gate.json').read_text())
for row in data['conditions']:
 a,b=row['selectors']
 E=[scale(roots[x],chi(a,x)) for x in range(8) if chi(a,x)==chi(b,x)]
 D=[scale(roots[x],chi(a,x)) for x in range(8) if chi(a,x)!=chi(b,x)]
 actual=add(mul(summand(E),elementary3(D)),scale(mul(elementary3(E),summand(D)),-1))
 assert actual==scale(expr(row['equation']),64)
 assert all(k[7]<=1 for k in actual)
elim=json.loads((P/'independent_selector_eliminate.json').read_text())
a=[expr(v) for v in elim['linear_coefficients']];b=[expr(v) for v in elim['constant_coefficients']]
for i,row in enumerate(data['conditions']):assert expr(row['equation'])==add(mul(a[i],variables['t7']),b[i])
for row in elim['compatibility_minors']:
 i,j=row['rows'];assert expr(row['polynomial'])==add(mul(a[i],b[j]),scale(mul(a[j],b[i]),-1))
out={'status':'PASS','exact_integer_quartic_identities':6,'linear_decompositions':6,'compatibility_minor_identities':15,'method':'Independent sparse integer polynomial arithmetic; no symbolic algebra library','existence_claim':False}
(P/'independent_selector.verified.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
