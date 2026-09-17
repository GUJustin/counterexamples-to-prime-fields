"""Symbolic recurrence and residual checks, independent coefficient solving."""
from pathlib import Path
import json
import sympy as s
X,z,c=s.symbols('X z c')
rows=[]
for D in range(1,5):
 t=4*D+1;T=s.prod(X-i for i in range(t))
 F=z*X**(D+1);G=(1+z)*X**(t-2)+1+z*X
 R=s.expand(F+G);S=s.expand(F*G)
 aa=s.symbols('a1:'+str(D+1));P=c+sum(aa[j-1]*X**j for j in range(1,D+1))
 residual=s.Poly(s.expand(T*s.diff(P,X)-P*P+R*P-S),X)
 known={}
 for j in range(D,0,-1):
  eq=s.expand(residual.coeff_monomial(X**(t+j-1)).subs(known))
  assert s.diff(eq,aa[j-1])==j
  aj=s.expand(-eq.subs(aa[j-1],0)/j)
  assert not aj.has(c,*aa)
  assert s.Poly(aj,z).degree()<=D-j+2
  known[aa[j-1]]=aj
 P=s.expand(P.subs(known));E=s.Poly(s.expand(T*s.diff(P,X)-P*P+R*P-S),X)
 assert all(E.coeff_monomial(X**i)==0 for i in range(t,t+D))
 E0=E.coeff_monomial(1);assert s.Poly(E0,c).coeff_monomial(c*c)==-1
 assert s.Poly(E0,z).degree()<=D+1
 nonzero=[]
 for i in range(1,t):
  e=E.coeff_monomial(X**i)
  assert s.Poly(e,c).degree()<=1
  assert s.Poly(s.diff(e,c),z).degree()<=D+1
  assert s.Poly(e.subs(c,0),z).degree()<=2*D+2
  if e!=0:nonzero.append(e)
 assert E.as_expr().subs({z:0,c:0})==0
 # This fixture has at least the known actual solution; test its isolation.
 gb=s.groebner([E0]+nonzero,c,z)
 assert gb.is_zero_dimensional
 rows.append({'D':D,'t':t,'degrees':[int(s.Poly(known[a],z).degree()) for a in aa],'isolated_zero_fixture':True,'groebner_basis':[str(g) for g in gb.polys]})
# A persistent nonlinear component. It must not be mistaken for isolated points.
D=2;t=5;T=s.prod(X-i for i in range(t));Q=z*X**2;R=2*Q;S=T*s.diff(Q,X)+Q**2-z
assert s.expand(T*s.diff(c+Q,X)-(c+Q)**2+R*(c+Q)-S)==z-c*c
# At characteristic2,D2 the top coefficient equation loses its pivot.
a=s.symbols('a');E=s.Poly(s.expand(X**5*s.diff(a*X**2,X)-(a*X**2)**2),X)
assert int(E.coeff_monomial(X**6).coeff(a))%2==0
out={'fixtures':rows,'persistent_nonlinear_component':'c^2=z','bad_characteristic_pivot_failure':{'p':2,'D':2}}
Path(__file__).with_name('symbolic_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
