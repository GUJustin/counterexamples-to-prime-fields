"""Independent Fraction field arithmetic and exact AST polynomial parser."""
import ast,json
from pathlib import Path
r=Path(__file__).parent
src=(r/'orbit7_independent_field_audit.py').read_text().split('w=K(')[0]
src=src.replace('c[j-1]-=2*c[j];c[j-2]+=c[j];c[j-3]+=c[j]','c[j-1]+=10*c[j];c[j-2]-=3*c[j];c[j-3]-=c[j]')
exec(src)
q=K([0,1,0]);assert q**3-10*q**2+3*q+1==0
# Neither +/-1 is a root, so the cubic is irreducible.
def add(a,b):return [(a[i] if i<len(a) else K(0))+(b[i] if i<len(b) else K(0)) for i in range(max(len(a),len(b)))]
def mul(a,b):
 c=[K(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=c[i+j]+x*y
 return c
def parse(s):
 def go(t):
  if isinstance(t,ast.Constant):return [K(t.value)]
  if isinstance(t,ast.Name):return [q] if t.id=='q' else [K(0),K(1)]
  if isinstance(t,ast.UnaryOp):return [-a for a in go(t.operand)]
  a=go(t.left)
  if isinstance(t.op,ast.Pow):
   n=t.right.value;c=[K(1)]
   for _ in range(n):c=mul(c,a)
   return c
  b=go(t.right)
  if isinstance(t.op,ast.Add):return add(a,b)
  if isinstance(t.op,ast.Sub):return add(a,[-x for x in b])
  if isinstance(t.op,ast.Mult):return mul(a,b)
  assert isinstance(t.op,ast.Div) and len(b)==1
  return [x/b[0] for x in a]
 return go(ast.parse(s,mode='eval').body)
d=json.loads((r/'orbit2_number_field.json').read_text());P=[parse(s) for s in d['polynomials']];P=[a+[K(0)]*(4-len(a)) for a in P]
# Remove common polynomial and rational denominators to simplify exact work.
P=[[221646235*(a-b) for a,b in zip(poly,P[0])] for poly in P]
nodes=[None if s is None else parse(s)[0] for s in d['quad_nodes']+d['triple_nodes']]
masks=d['quad_matches']+d['triple_matches']
def ev(a,x):
 if x is None:return a[3]
 y=K(0)
 for c in reversed(a):y=y*x+c
 return y
for i in range(14):
 for j in range(i):assert nodes[i] is None or nodes[j] is None or nodes[i]!=nodes[j]
for x,S in zip(nodes,masks):
 v=ev(P[S[0]-1],x);assert [i+1 for i,a in enumerate(P) if ev(a,x)==v]==S
assert all(sum(i in S for S in masks)==7 for i in range(1,8))
a=K(2);assert all(x is None or x!=a for x in nodes)
Q=[[c[3],c[2]+3*a*c[3],c[1]+2*a*c[2]+3*a*a*c[3],ev(c,a)] for c in P]
tnodes=[K(0) if x is None else 1/(x-a) for x in nodes];word=[]
for x,S in zip(tnodes,masks):
 v=ev(Q[S[0]-1],x);word.append(v);assert [i+1 for i,c in enumerate(Q) if ev(c,x)==v]==S
# Interpolate first four triple targets and test all seven.
R=[K(0)]*4
for i in range(7,11):
 term=[K(1)];den=K(1)
 for j in range(7,11):
  if j!=i:term=mul(term,[-tnodes[j],K(1)]);den=den*(tnodes[i]-tnodes[j])
 R=add(R,[a*word[i]/den for a in term])
errors=[ev(R,tnodes[i])-word[i] for i in range(7,14)]
out={'pass':True,'field_polynomial':'q^3-10q^2+3q+1','affine_nodes':[x.out() for x in tnodes],'affine_polynomials':[[x.out() for x in c] for c in Q],'affine_word':[x.out() for x in word],'agreement_masks':masks,'eighth_cubic_exists':not any(errors),'eighth_errors':[x.out() for x in errors]}
(r/'orbit2_independent_field_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'independent_incidence':'PASS','eighth_cubic_exists':out['eighth_cubic_exists'],'first_failure':next((x.out() for x in errors if x),None)}))
