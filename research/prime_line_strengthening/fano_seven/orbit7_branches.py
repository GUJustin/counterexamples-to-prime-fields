import sympy as S,json,time,itertools
from pathlib import Path
root=Path(__file__).parent;u,v,w,z=S.symbols('u v w z');vs=[u,v,w,z]
d=json.loads((root/'orbit7_minors.json').read_text()); polys=[S.sympify(a['core']) for a in d['minors']]
us=[v*w*(v-w)/((w-1)*(z-v)),w*z*(v-1)/(v*(w+z-1)-w*z)]
out=[]
for bi,U in enumerate(us):
 guards=[S.fraction(S.factor(g.subs(u,U)))[0] for g in vs+[x-1 for x in vs]+[a-b for a,b in itertools.combinations(vs,2)]]
 guards += [S.denom(U)]
 gf=set()
 for g in guards:
  for f,e in S.factor_list(g)[1]:gf.add(f)
 rows=[]
 for item,p in zip(d['minors'],polys):
  f=S.fraction(S.factor(p.subs(u,U)))[0]
  for g in gf:
   while f!=0:
    q,r=S.div(f,g,v,w,z)
    if r!=0:break
    f=S.factor(q)
  rows.append({'rows':item['rows'],'core':str(f)})
  print(bi,item['rows'],str(f),flush=True)
 out.append({'u':str(U),'nonzero_guards':[str(g) for g in gf],'rows':rows})
(root/'orbit7_branches.json').write_text(json.dumps(out,indent=2)+'\n')
