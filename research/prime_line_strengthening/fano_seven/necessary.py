import sympy as S,itertools,json,time
from pathlib import Path
start=time.time();u,v,w,z=S.symbols('u v w z');bs=[None,0,1,u,v,w,z]
lines=[{1,2,3},{1,4,5},{1,6,7},{2,4,6},{2,5,7},{3,4,7},{3,5,6}]
eq=[];pairs=[]
for line in lines:
 rows=[];pp=[]
 for i,j in itertools.combinations(sorted(line),2):
  inds=[l for l,L in enumerate(lines) if i not in L and j not in L];assert len(inds)==2
  a,b=[bs[l] for l in inds];pp.append(inds)
  rows.append([0,1,-(b if a is None else a)] if a is None or b is None else [1,-a-b,a*b])
 eq.append(S.factor(S.det(S.Matrix(rows))));pairs.append(pp)
print(eq,flush=True)
g=S.groebner(eq,u,v,w,z);print(g,flush=True)
out={'lines':[sorted(x) for x in lines],'pairs':pairs,'equations':list(map(str,eq)),'groebner':list(map(str,g.polys)),'seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
