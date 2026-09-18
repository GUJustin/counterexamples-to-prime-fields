from fractions import Fraction as F
import ast,itertools,json,pathlib,time
start=time.monotonic();base=pathlib.Path(__file__).resolve().parent;src=base.parent/'fano_seven'
class K:
 mod=(2,-1,-1)
 def __init__(self,x=0):self.a=x.a if isinstance(x,K) else tuple(map(F,x if isinstance(x,(list,tuple)) else (x,0,0)))
 def __add__(self,o):o=K(o);return K([a+b for a,b in zip(self.a,o.a)])
 __radd__=__add__
 def __neg__(self):return K([-a for a in self.a])
 def __sub__(self,o):return self+-K(o)
 def __rsub__(self,o):return K(o)+-self
 def __mul__(self,o):
  o=K(o);c=[F(0)]*5
  for i,a in enumerate(self.a):
   for j,b in enumerate(o.a):c[i+j]+=a*b
  for j in [4,3]:
   for h,m in enumerate(self.mod,1):c[j-h]-=m*c[j]
  return K(c[:3])
 __rmul__=__mul__
 def __pow__(self,n):
  if isinstance(n,K):assert n.a[1:]==(0,0);n=int(n.a[0])
  if n<0:return self.inv()**(-n)
  r=K(1)
  for _ in range(n):r=r*self
  return r
 def __eq__(self,o):return self.a==K(o).a
 def __bool__(self):return any(self.a)
 def inv(self):
  assert self
  cols=[(self*K([int(i==j) for i in range(3)])).a for j in range(3)]
  m=[[cols[j][i] for j in range(3)]+[F(i==0)] for i in range(3)]
  for j in range(3):
   q=next(i for i in range(j,3) if m[i][j]);m[j],m[q]=m[q],m[j];v=m[j][j];m[j]=[a/v for a in m[j]]
   for i in range(3):
    if i!=j:
     v=m[i][j];m[i]=[a-v*b for a,b in zip(m[i],m[j])]
  return K([m[i][3] for i in range(3)])
 def __truediv__(self,o):return self*K(o).inv()
 def __rtruediv__(self,o):return K(o)*self.inv()
 def out(self):return [str(a) for a in self.a]
def parse(text):
 def go(n):
  if isinstance(n,ast.Constant):return K(n.value)
  if isinstance(n,ast.Name):assert n.id in ['q','w'];return K([0,1,0])
  if isinstance(n,ast.UnaryOp):return -go(n.operand) if isinstance(n.op,ast.USub) else go(n.operand)
  a,b=go(n.left),go(n.right)
  if isinstance(n.op,ast.Add):return a+b
  if isinstance(n.op,ast.Sub):return a-b
  if isinstance(n.op,ast.Mult):return a*b
  if isinstance(n.op,ast.Div):return a/b
  if isinstance(n.op,ast.Pow):return a**b
  raise ValueError(n)
 return go(ast.parse(text,mode='eval').body)
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def order(p):
 r=list(range(1,8));n=0
 while True:
  r=[p[i-1] for i in r];n+=1
  if r==list(range(1,8)):return n
out=[]
for orbit,mod in [(7,(2,-1,-1)),(2,(-10,3,1))]:
 K.mod=mod
 data=json.loads((src/f'orbit{orbit}_number_field.json').read_text());design=json.loads((src/'design_orbits.jsonl').read_text().splitlines()[orbit]);T=list(map(tuple,design['T']));C=list(map(tuple,design['C']));Ts=set(T);Cs=set(C)
 raw=data['quad_nodes']+data['triple_nodes'];nodes=[(K(1),K(0)) if x is None else (parse(x),K(1)) for x in raw]
 records=[]
 for p in itertools.permutations(range(1,8)):
  tr=lambda cl:tuple(sorted(p[i-1] for i in cl))
  if set(map(tr,T))!=Ts or set(map(tr,C))!=Cs:continue
  cp=[C.index(tr(cl)) for cl in C];tp=[T.index(tr(cl)) for cl in T];np=cp+[7+i for i in tp]
  a,b,c=[nodes[np[h]] for h in [0,1,2]];lam=det(c,b);mu=det(a,c)
  M=[lam*a[0],mu*b[0],lam*a[1],mu*b[1]]
  assert M[0]*M[3]-M[1]*M[2]
  failures=[]
  for i,(x,y) in enumerate(nodes):
   tx,ty=nodes[np[i]]
   if (M[0]*x+M[1]*y)*ty-(M[2]*x+M[3]*y)*tx:failures.append(i)
  rr={'candidate_permutation':p,'order':order(p),'quad_permutation':cp,'triple_permutation':tp,'failed_nodes':failures}
  if not failures:
   lead=next(x for x in M if x);rr['mobius_matrix']=[(x/lead).out() for x in M]
   rr['trace_squared_over_determinant']=(((M[0]+M[3])**2)/(M[0]*M[3]-M[1]*M[2])).out()
  records.append(rr)
 out.append({'orbit':orbit,'automorphism_count':len(records),'geometric_count':sum(not r['failed_nodes'] for r in records),'geometric_orders':[r['order'] for r in records if not r['failed_nodes']],'records':records})
res={'banks':out,'seconds':time.monotonic()-start};(base/'actual_symmetry.json').write_text(json.dumps(res,indent=2));print(json.dumps({'summary':[{k:v for k,v in r.items() if k!='records'} for r in out],'seconds':res['seconds']},indent=2))
