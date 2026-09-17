import json
import sympy as s
X,z,c,d,y,w=s.symbols('X z c d y w')
rows=[]
for D in range(1,4):
 for j in range(1,D+1):
  t=2*D+1; tau=z+1; delta=tau**D; K=D+1; M=2*K+1
  T=tau*X**t+X+z+2
  R=-j*tau*X**(t-1)+(z+2)*sum(X**i for i in range(t-1))
  S=sum((z+i+1)*X**(t+i-1) for i in range(1,D+1))+z
  P=c
  for i in range(D,0,-1):
   if i==j:P+=d*X**i;continue
   trial=P+y*X**i
   eq=s.Poly(s.expand(T*s.diff(trial,X)+R*trial-S),X).nth(t+i-1)
   value=s.cancel(-eq.subs(y,0)/((i-j)*tau))
   assert not value.has(c)
   P+=value*X**i
  V=s.cancel(s.diff(P,d)*delta)
  Q=s.cancel((P-c-d*s.diff(P,d))*delta)
  V=s.Poly(V,X).as_expr(); Q=s.Poly(Q,X).as_expr()
  assert s.Poly(V,X).LC()==s.expand(delta)
  assert max(s.degree(V,z),s.degree(Q,z))<=K
  Qt=s.expand(Q.subs(X,X+w)-Q.subs(X,w))
  Vt=s.expand(V.subs(X,X+w)-V.subs(X,w))
  # The constant residual divided by delta has leading -delta*c².
  v=s.expand(T.subs(X,w)*s.diff(V,X).subs(X,w))
  assert v!=0 and s.degree(v,z)<=M
  N=s.expand(delta*c*c-R.subs(X,w)*delta*c-T.subs(X,w)*s.diff(Q,X).subs(X,w)+S.subs(X,w)*delta)
  assert s.Poly(N,c).LC()==s.expand(delta)
  # The cleared X^(2j) residual has leading -delta²*d² and no cd.
  W=Qt+d*Vt
  E2=s.Poly(s.expand(T.subs(X,X+w)*s.diff(W,X)*delta-(delta*c+W)**2+R.subs(X,X+w)*(delta*c+W)*delta-S.subs(X,X+w)*delta**2),X).nth(2*j)
  assert s.expand(E2).coeff(d,2)==-s.expand(delta**2)
  assert s.expand(E2).coeff(c).coeff(d)==0
  assert s.degree(E2,c)<=1
  quartic=s.expand(s.expand(E2).coeff(d,2)*s.Poly(N,c).LC()**2)
  assert quartic==-s.expand(delta**4)
  rows.append(dict(D=D,j=j,delta_degree=D,shared_numerator_degree=int(max(s.degree(V,z),s.degree(Q,z))),quartic_lead=str(s.factor(quartic))))
print(json.dumps(dict(passed=True,fixtures=rows),indent=2))
