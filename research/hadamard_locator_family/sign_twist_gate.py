"""Exact C2 sign-twist reduction. One rational fixture, not a parameter scan."""
import sympy as s,json
from pathlib import Path
Y,T=s.symbols('Y T');edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
x=dict(zip(edges,map(s.Integer,range(1,7))));get=lambda i,j:x[tuple(sorted((i,j)))]
a=s.symbols('a0:4');u=s.symbols('u12 u13 u23');uv=dict(zip([(1,2),(1,3),(2,3)],u));amp=list(a)+list(u)
A=[a[i]*s.prod(Y-get(i,j)for j in range(4)if i!=j)for i in range(4)]
B=[s.Integer(0)]
for i in range(1,4):
 js=[j for j in range(1,4)if i!=j];q=0
 for j in js:
  k=next(k for k in js if k!=j)
  q+=uv[tuple(sorted((i,j))) ]*(Y-get(0,i))*(Y-get(i,k))/((get(i,j)-get(0,i))*(get(i,j)-get(i,k)))
 B.append(s.expand(q))
for i,j in edges:assert s.expand((B[i]-B[j]).subs(Y,get(i,j)))==0
L0=T*T-T+2
rows=[]
for i in range(1,4):
 f=s.expand((A[i]-A[0]).subs(Y,T*T)+T*B[i].subs(Y,T*T));r=s.Poly(s.rem(f,L0,T),T)
 rows.extend([[r.nth(k).coeff(v)for v in amp]for k in range(2)])
M=s.Matrix(rows);ker=M.nullspace();assert M.rank()==5 and len(ker)==2
z=s.symbols("z"); v=ker[0]+z*ker[1];sub=dict(zip(amp,v));AA=[s.expand(q.subs(sub))for q in A];BB=[s.expand(q.subs(sub))for q in B]
assert len(set([q for z in v[:4]for q in(z,-z)]))==8
F=[s.expand(AA[i].subs(Y,T*T)+T*BB[i].subs(Y,T*T))for i in range(4)]
checks=[]
for i in range(1,4):
 k,l=[j for j in range(1,4)if j!=i]
 q,r=s.div(F[0]-F[i],(T*T-get(0,i))*L0,T);assert r==0
 q=s.cancel(q/s.Poly(q,T).LC())
 q2,r=s.div(F[k]-F[l],(T*T-get(k,l))*L0,T);assert r==0
 q2=s.cancel(q2/s.Poly(q2,T).LC())
 delta=s.cancel(q-q2.subs(T,-T)); delta=s.fraction(delta)[0]
 checks.append({'partition':[0,i,k,l],'Q0i':str(q),'Qkl':str(q2),'necessary_reversal_difference':str(delta)})
out={'scope':'single rational fixture; no existence/exclusion theorem for variable shapes','edge_nodes':{str(e):str(v)for e,v in x.items()},'L0':str(L0),'all_plus_matrix_rank':5,'amplitude_pencil':[str(z)for z in v],'eight_leading_coefficients_distinct':True,'partition_checks':checks}
g=s.Poly(0,z)
for row in checks:
 for cc in s.Poly(s.sympify(row['necessary_reversal_difference']),T).all_coeffs():g=s.gcd(g,s.Poly(cc,z))
out['reversal_gcd']=str(g.as_expr())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
