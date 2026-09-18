import sympy as S,json,itertools,time
from pathlib import Path
root=Path(__file__).parent;u,v,w,z=S.symbols('u v w z');vs=[u,v,w,z]
d=json.loads((root/'design_orbits.jsonl').read_text().splitlines()[7]);T={tuple(a) for a in d['T']};C=[tuple(a) for a in d['C']];Cs=set(C)
perms=[]
for p in itertools.permutations(range(1,8)):
 tr=lambda cl:tuple(sorted(p[a-1] for a in cl))
 if {tr(a) for a in T}==T and {tr(a) for a in C}==Cs:perms.append((p,[C.index(tr(a)) for a in C]))
print('automorphisms',len(perms),flush=True)
bs=[(S.Integer(1),S.Integer(0)),(0,1),(1,1),(u,1),(v,1),(w,1),(z,1)]
det=lambda a,b:a[0]*b[1]-a[1]*b[0]
F=(w-1)*(z-v)*u+v*w*(w-v);U=v*w*(v-w)/((w-1)*(z-v))
guards=vs+[a-1 for a in vs]+[a-b for a,b in itertools.combinations(vs,2)]
gf=set()
for g in guards:
 for f,e in S.factor_list(S.fraction(S.factor(g.subs(u,U)))[0])[1]:gf.add(f)
out=[]
for p,cp in perms:
 nb=[bs[cp.index(i)] for i in range(7)];a,b,c=nb[:3]
 ns=[S.cancel(S.sympify(det(x,b)*det(c,a))/(det(x,a)*det(c,b))) for x in nb[3:]]
 f=S.fraction(S.factor(F.subs(dict(zip(vs,ns)),simultaneous=True).subs(u,U)))[0]
 for g in gf:
  while f!=0:
   q,r=S.div(f,g,v,w,z)
   if r!=0:break
   f=S.factor(q)
 out.append({'permutation':p,'quad_permutation':cp,'core':str(f)})
 print(p,str(f),flush=True)
(root/'orbit7_symmetry.json').write_text(json.dumps(out,indent=2)+'\n')
