import sympy as S,itertools,json,time
from pathlib import Path
import sys
start=time.time();u,v,w,z=S.symbols('u v w z');bs=[None,0,1,u,v,w,z]
orbit=int(sys.argv[1]); data=[json.loads(x) for x in Path(__file__).with_name('design_orbits.jsonl').read_text().splitlines()][orbit]
lines=list(map(set,data['T'])); clines=list(map(set,data['C']))
eq=[];pairs=[]
for line in lines:
 rows=[];pp=[]
 for i,j in itertools.combinations(sorted(line),2):
  inds=[l for l,L in enumerate(clines) if i not in L and j not in L];assert len(inds)==2
  a,b=[bs[l] for l in inds];pp.append(inds)
  rows.append([0,1,-(b if a is None else a)] if a is None or b is None else [1,-a-b,a*b])
 eq.append(S.factor(S.det(S.Matrix(rows))));pairs.append(pp)
print(eq,flush=True)
g=S.groebner(eq,u,v,w,z);print(g,flush=True)
out={'orbit':orbit,'T':data['T'],'C':data['C'],'pairs':pairs,'equations':list(map(str,eq)),'groebner':list(map(str,g.polys)),'seconds':time.time()-start}
Path(__file__).with_name('relative_fano_'+str(orbit)+'.json').write_text(json.dumps(out,indent=2))
