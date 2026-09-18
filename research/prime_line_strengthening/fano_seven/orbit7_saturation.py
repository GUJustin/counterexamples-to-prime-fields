import sympy as S,json,time
from pathlib import Path
root=Path(__file__).parent;t,v,w,z=S.symbols('t v w z');st=time.time()
d=json.loads((root/'orbit7_symmetry_basis.json').read_text())
p=[S.sympify(f) for f in d['basis']]
guard=(v-z)*(w-1)
g=S.groebner(p+[t*guard-1],t,v,w,z,order='grevlex')
out={'variables':['t','v','w','z'],'order':'grevlex','inverted_guard':str(guard),'basis':[str(S.factor(f.as_expr())) for f in g.polys],'seconds':time.time()-st}
print(json.dumps(out,indent=2),flush=True)
(root/'orbit7_saturation.json').write_text(json.dumps(out,indent=2)+'\n')
