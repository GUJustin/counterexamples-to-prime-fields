import sympy as S,json,itertools,time
from pathlib import Path
st=time.time();root=Path(__file__).parent;u,v,w,z=S.symbols('u v w z');vs=[u,v,w,z];d=json.loads((root/'orbit7_generic.json').read_text());M=S.Matrix([[S.sympify(x,locals=dict(zip(d['variables'],vs))) for x in r] for r in d['rows']]);guards=vs+[x-1 for x in vs]+[a-b for a,b in itertools.combinations(vs,2)]
rows=[];core=[]
for inds in itertools.combinations(range(7),3):
 det=S.factor(M[list(inds),:].det());f=det
 removed=[]
 for g in guards:
  while f!=0:
   q,r=S.div(f,g,*vs)
   if r!=0:break
   f=S.factor(q);removed.append(str(g))
 rows.append({'rows':inds,'core':str(f),'removed':removed})
 if f!=0:core.append(f)
 print(inds,str(f),flush=True)
(root/'orbit7_minors.json').write_text(json.dumps({'minors':rows,'seconds':time.time()-st},indent=2)+'\n')
