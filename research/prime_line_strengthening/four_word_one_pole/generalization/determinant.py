import itertools,json
from pathlib import Path
import sympy as s
xs=s.symbols('a b c d'); edges=list(itertools.combinations(range(4),2))
def entry(edge,sign,col):
 i,j=edge
 if col<4:
  e=[0]*4;e[i]=e[j]=col;return [(tuple(e),sign**col)]
 out=[]
 for k in edge:
  e=[0]*4;e[k]=2
  if col==4:e[i]+=1;e[j]+=1
  out.append((tuple(e),-sign if col==4 else -1))
 return out
def determinant(signs):
 out={}
 for perm in itertools.permutations(range(6)):
  parity=(-1)**sum(perm[i]>perm[j] for i in range(6) for j in range(i+1,6))
  terms={(0,0,0,0):parity}
  for row,col in enumerate(perm):
   nex={}
   for e,v in terms.items():
    for f,w in entry(edges[row],signs[row],col):
     g=tuple(a+b for a,b in zip(e,f));nex[g]=nex.get(g,0)+v*w
   terms=nex
  for e,v in terms.items():out[e]=out.get(e,0)+v
 return s.Poly.from_dict({e:v for e,v in out.items() if v},xs).as_expr()
records=[]
for rest in itertools.product((1,-1),repeat=3):
 signs=(1,1,1)+rest;expr=determinant(signs)
 vals={xs[i]:[1,2,5,13][i] for i in range(4)}
 rows=[]
 for (i,j),sig in zip(edges,signs):
  x=sig*vals[xs[i]]*vals[xs[j]];w=vals[xs[i]]**2+vals[xs[j]]**2
  rows.append([1,x,x*x,x**3,-w*x,-w])
 assert s.Matrix(rows).det()==expr.subs(vals)
 records.append({'signs':signs,'factor':str(s.factor(expr)),'zero':expr==0})
 print(records[-1],flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n')
