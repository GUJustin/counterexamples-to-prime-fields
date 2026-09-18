"""Check every identity with independent sparse Fraction polynomial arithmetic."""
from fractions import Fraction as F
from pathlib import Path
import ast,gzip,json,time,hashlib
r=Path(__file__).parent;start=time.monotonic();zero=(0,0,0,0)
def clean(a):return {m:c for m,c in a.items() if c}
def add(a,b):
 c=a.copy()
 for m,v in b.items():c[m]=c.get(m,F(0))+v
 return clean(c)
def neg(a):return {m:-v for m,v in a.items()}
def mul(a,b):
 c={}
 for m,x in a.items():
  for n,y in b.items():
   q=tuple(i+j for i,j in zip(m,n));c[q]=c.get(q,F(0))+x*y
 return clean(c)
def parse(s):
 def go(t):
  if isinstance(t,ast.Constant):return clean({zero:F(t.value)})
  if isinstance(t,ast.Name):return {tuple(int(i=='tvwz'.index(t.id)) for i in range(4)):F(1)}
  if isinstance(t,ast.UnaryOp):return neg(go(t.operand)) if isinstance(t.op,ast.USub) else go(t.operand)
  a=go(t.left)
  if isinstance(t.op,ast.Pow):
   assert isinstance(t.right,ast.Constant) and t.right.value>=0
   out={zero:F(1)}
   for _ in range(t.right.value):out=mul(out,a)
   return out
  b=go(t.right)
  if isinstance(t.op,ast.Add):return add(a,b)
  if isinstance(t.op,ast.Sub):return add(a,neg(b))
  if isinstance(t.op,ast.Mult):return mul(a,b)
  assert isinstance(t.op,ast.Div) and set(b)=={zero}
  return {m:c/b[zero] for m,c in a.items()}
 return go(ast.parse(s,mode='eval').body)
def decode(a):
 out={}
 for m,n,d in a:
  m=tuple(m);assert len(m)==4 and all(isinstance(v,int) and v>=0 for v in m) and m not in out
  out[m]=F(int(n),int(d))
 return clean(out)
path=r/'orbit7_identity_certificate.json.gz'
with gzip.open(path,'rt') as f:d=json.load(f)
assert d['variables']==['t','v','w','z']
expected=set(row['core'] for row in json.loads((r/'orbit7_branches.json').read_text())[0]['rows']+json.loads((r/'orbit7_symmetry.json').read_text()) if row['core']!='0')
assert set(d['input_expressions'])==expected
polys=[];inputs=0;linear=0
for i,row in enumerate(d['nodes']):
 actual=decode(row['polynomial'])
 if row['kind']=='input':
  inputs+=1;label=row['label']
  expr='t*(v-z)*(w-1)-1' if label=='inverse_mandatory_guard' else d['input_expressions'][int(label.split('_')[1])]
  want=parse(expr)
 else:
  assert row['kind']=='linear';linear+=1;want={}
  for j,c in row['terms']:
   assert 0<=j<i;want=add(want,mul(decode(c),polys[j]))
 assert actual==want,('identity_failure',i)
 polys.append(actual)
assert len(d['outputs'])==len(d['output_expressions'])
for i,e in zip(d['outputs'],d['output_expressions']):assert polys[i]==parse(e)
targets=['(z-1)*(w*w+w-z)','(z-1)*(w*z-2*w+z-1)','(z-1)*(v-z+1)']
for e in targets:assert parse(e) in [polys[i] for i in d['outputs']]
out={'verdict':'PASS','arithmetic':'independent sparse dictionaries over fractions.Fraction; exact AST input parser; no SymPy','nodes':len(polys),'input_nodes':inputs,'linear_identity_nodes':linear,'verified_targets':targets,'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
(r/'orbit7_certificate_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
