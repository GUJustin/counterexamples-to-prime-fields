import sympy as s,json,itertools,time
from pathlib import Path
P=Path(__file__).parent;u,v,z,d,b,c=s.symbols('u v z d b c');env={str(x):x for x in [u,v,z,d]}
source=json.loads((P/'nonfano2_projective.json').read_text());rows=[[s.sympify(x,locals=env) for x in row['primitive_row']] for row in source['rows']]
eq=[s.expand(row[0]+b*row[1]+c*row[2]) for row in rows]
p=83;q=4;iv=lambda x:pow(int(x)%p,-1,p)
point={u:(-q*q+13*q+3)*iv(20)%p,v:(-4*q*q+27*q+7)*iv(25)%p,z:q,d:(-3*q*q+29*q+4)*iv(20)%p,b:(135854572*q*q-1353831356*q+428344204)*iv(221646235)%p,c:(-143947248*q*q+1457491984*q-627685616)*iv(221646235)%p}
assert all(int(f.subs(point))%p==0 for f in eq)
J=[[int(s.diff(f,x).subs(point))%p for x in [u,v,z,d,b,c]] for f in eq]
minor=None
for inds in itertools.combinations(range(7),6):
 det=int(s.det(s.Matrix([J[i] for i in inds])))%p
 if det:minor=dict(rows=inds,determinant_mod83=det);break
assert minor
B=json.loads((P/'nonfano2_branchII_reduce.json').read_text());lookup={tuple(x['rows']):s.sympify(x['remaining'],locals={str(a):a for a in [v,z]}) for x in B['equations']}
E=lookup[0,1];F=lookup[1,3];G=lookup[1,5]
resEF=s.factor(s.resultant(E,F,v));resEG=s.factor(s.resultant(E,G,v));resFG=s.factor(s.resultant(F,G,v));gcd=s.factor(s.gcd(resEF,resEG))
# Exact polynomial remainders also determine v on the cubic z locus.
f=z**3-10*z*z+3*z+1
knownv=(-4*z*z+27*z+7)/25
redE=s.Poly(E,v,z).as_expr();
# Groebner of only the three small necessary equations is cheap and independently selected.
gb=s.groebner([E,F,G],v,z,order='lex')
out=dict(point={str(k):x for k,x in point.items()},jacobian=J,rank=6,nonzero_minor=minor,small_equations=[str(x) for x in [E,F,G]],resultant_EF=str(resEF),resultant_EG=str(resEG),resultant_FG=str(resFG),gcd_first_two=str(gcd),small_groebner=[str(x.as_expr()) for x in gb.polys])
(P/'orbit2_rigidity_audit.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
# Direct elimination with the now-forced cubic, with no guard saturation.
gb2=s.groebner([E,F,f],v,z,order='lex')
assert gb2.reduce(25*v+4*z*z-27*z-7)[1]==0
U=(-z*z+13*z+3)/20;V=knownv;DD=(-3*z*z+29*z+4)/20
D=v*v*z-v*v-v*z**3+2*v*z*z-v*z+v-z*z
reduce=lambda x:s.rem(s.together(x).as_numer_denom()[0],f,z)
assert reduce((u*D-v*z*z*(v-z)).subs({u:U,v:V}))==0
assert reduce((d*v*(z-1)-(u*v*(z-1)+z*(u-v))).subs({u:U,v:V,d:DD}))==0
M=s.Matrix([[int(x.subs(point))%83 for x in row] for row in rows])
am=None
for rr in itertools.combinations(range(7),2):
 for cc in itertools.combinations(range(3),2):
  val=int(M.extract(rr,cc).det())%83
  if val:am=dict(rows=rr,columns=cc,determinant_mod83=val);break
 if am:break
assert am
out['cubic_elimination_basis']=[str(x.as_expr()) for x in gb2.polys]
out['amplitude_rank_at_least_two_minor']=am
out['node_formulas']={str(u):str(U),str(v):str(V),str(d):str(DD)}
(P/'orbit2_rigidity_audit.json').write_text(json.dumps(out,indent=2))
print('Unique v, node formulas, and amplitude rank verified:',am)
