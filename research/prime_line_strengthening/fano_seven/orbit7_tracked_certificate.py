"""Record a rational polynomial-identity DAG, not a trusted GB verdict."""
import sympy as S,json,inspect,gzip,time
from pathlib import Path
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from sympy.polys.groebnertools import _buchberger
root=Path(__file__).parent;st=time.time()
R,t,v,w,z=ring('t,v,w,z',QQ,order='grevlex')
nodes=[];ids={}
def add(p,kind,terms=None,label=None):
 if p in ids:return ids[p]
 i=len(nodes);ids[p]=i;nodes.append((p,kind,terms,label));return i
def inp(p,label):return add(p,'input',label=label)
def lin(p,terms):
 if p not in ids:add(p,'linear',[(ids[a],c) for a,c in terms if c])
 return p
def rem(p,ds):
 qs,r=p.div(ds)
 return lin(r,[(p,R.one)]+[(a,-q) for a,q in zip(ds,qs)])
def monic(p):return lin(p.monic(),[(p,R.ground_new(1/p.LC))])
def spoly(a,b,rr):
 lm=rr.monomial_lcm(a.LM,b.LM)
 ca=rr.from_dict({rr.monomial_div(lm,a.LM):QQ.one});cb=rr.from_dict({rr.monomial_div(lm,b.LM):QQ.one})
 return lin(ca*a-cb*b,[(a,ca),(b,-cb)])
source=inspect.getsource(_buchberger).replace('def _buchberger(', 'def tracked(')
source=source.replace('g.rem([ f[j] for j in J ])','rem(g, [f[j] for j in J])')
source=source.replace('h = h.monic()','h = monic(h)')
source=source.replace('p.rem(f[:i])','rem(p, f[:i])')
source=source.replace('f1.append(r.monic())','f1.append(monic(r))')
assert '.rem(' not in source and '.monic(' not in source
exec(source,globals())
d=json.loads((root/'orbit7_branches.json').read_text())[0]
rows=d['rows']+json.loads((root/'orbit7_symmetry.json').read_text())
exprs=sorted(set(row['core'] for row in rows if row['core']!='0'))
ps=[]
for i,e in enumerate(exprs):
 p=R.from_expr(S.sympify(e));inp(p,f'necessary_{i}');ps.append(p)
print('stage1',len(ps),flush=True)
g=tracked(ps,R)
print('stage1done',len(g),len(nodes),time.time()-st,flush=True)
guard=t*(v-z)*(w-1)-1;inp(guard,'inverse_mandatory_guard')
out=tracked(g+[guard],R)
print('stage2done',len(out),len(nodes),time.time()-st,flush=True)
outputs=[ids[p] for p in out]
needed=set(outputs);todo=outputs[:]
while todo:
 i=todo.pop();p,kind,terms,label=nodes[i]
 for j,c in terms or []:
  if j not in needed:needed.add(j);todo.append(j)
indices=sorted(needed);newid={old:new for new,old in enumerate(indices)}
def encode(p):return [[list(m),str(c.numerator),str(c.denominator)] for m,c in sorted(p.items())]
cert=[]
for i in indices:
 p,kind,terms,label=nodes[i]
 rec={'polynomial':encode(p),'kind':kind}
 if kind=='input':rec['label']=label
 else:rec['terms']=[[newid[j],encode(c)] for j,c in terms]
 cert.append(rec)
data={'variables':['t','v','w','z'],'input_expressions':exprs,'nodes':cert,'outputs':[newid[i] for i in outputs],'output_expressions':[str(p.as_expr()) for p in out],'seconds':time.time()-st}
with gzip.open(root/'orbit7_identity_certificate.json.gz','wt') as f:json.dump(data,f,separators=(',',':'))
(root/'orbit7_identity_certificate_summary.json').write_text(json.dumps({k:v for k,v in data.items() if k not in['nodes','input_expressions']},indent=2)+'\n')
print('saved',len(cert),'nodes',flush=True)
