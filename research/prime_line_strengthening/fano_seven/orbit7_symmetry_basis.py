import sympy as S,json,time
from pathlib import Path
root=Path(__file__).parent;v,w,z=S.symbols('v w z');st=time.time()
d=json.loads((root/'orbit7_branches.json').read_text())[0]
rows=d['rows']+json.loads((root/'orbit7_symmetry.json').read_text())
p=list(set(S.sympify(r['core']) for r in rows if r['core']!='0'))
g=S.groebner(p,v,w,z,order='grevlex')
out={'order':'grevlex','variables':['v','w','z'],'basis':[str(S.factor(f.as_expr())) for f in g.polys],'seconds':time.time()-st}
print(json.dumps(out,indent=2),flush=True)
(root/'orbit7_symmetry_basis.json').write_text(json.dumps(out,indent=2)+'\n')
