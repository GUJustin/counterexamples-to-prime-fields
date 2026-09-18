"""Exact identities for the sign-twist all-plus pencil; two algebraic controls."""
import sympy as s,json
from pathlib import Path
Y,T,tau=s.symbols('Y T tau');a,b,c,d,e,f=s.symbols('a b c d e f')
F=(e-a)*(d-b)*(f-c)-(d-a)*(f-b)*(e-c)
M=s.Matrix([[1,-a-f,a*f],[1,-b-e,b*e],[1,-c-d,c*d]])
assert s.expand(F-M.det())==0
edges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)];xs=dict(zip(edges,map(s.Integer,[1,2,3,4,5,6])));x=lambda i,j:xs[tuple(sorted((i,j)))];sigma=s.Integer(1);p=s.Integer(2)
C=[s.prod(Y-x(i,j)for j in range(4)if i!=j)for i in range(4)]
beta=[0,tau/(x(1,2)-x(0,1)),tau/(x(1,2)-x(0,2)),tau*(x(1,3)-x(0,1))/((x(1,2)-x(0,1))*(x(1,3)-x(0,3)))]
lead=[s.Integer(1)]+[s.factor((C[0].subs(Y,-p)+sigma*p*beta[i]*(-p-x(0,i)))/C[i].subs(Y,-p))for i in range(1,4)]
R=(Y+p)**2-sigma**2*Y;A=[s.expand(lead[i]*C[i])for i in range(4)];B=[s.Integer(0)]
for i in range(1,4):
 q,r=s.div(s.expand(sigma*C[0]-sigma*A[i]+R*beta[i]*(Y-x(0,i))),Y+p,Y);assert r==0;B.append(s.expand(q))
for i,j in edges:assert s.expand((B[i]-B[j]).subs(Y,x(i,j)))==0
L0=T*T-sigma*T+p
for i in range(1,4):assert s.rem(s.expand((A[i]-A[0]).subs(Y,T*T)+T*B[i].subs(Y,T*T)),L0,T)==0
out={'status':'PASS','Ceva_polynomial':str(s.expand(F)),'opposite_pair_determinant_identity':True,'fixture_edges':[1,2,3,4,5,6],'sigma':1,'p':2,'leading_pencil':list(map(str,lead)),'B_pencil':list(map(str,B)),'all_edge_equalities':True,'all_plus_divisibility':True,'scope':'Exact special-class identity, not a full eight-sextic realization.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
