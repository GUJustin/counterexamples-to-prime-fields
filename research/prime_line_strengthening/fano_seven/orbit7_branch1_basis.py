import sympy as S,json,time
from pathlib import Path
root=Path(__file__).parent;v,w,z=S.symbols('v w z');st=time.time()
d=json.loads((root/'orbit7_branches.json').read_text())[0]
p=[S.sympify(r['core']) for r in d['rows'] if r['core']!='0']
g=S.groebner(p,v,w,z,order='grevlex')
out={'order':'grevlex','variables':['v','w','z'],'basis':[str(S.factor(f)) for f in g.polys],'seconds':time.time()-st}
print(out,flush=True)
(root/'orbit7_branch1_basis.json').write_text(json.dumps(out,indent=2)+'\n')
