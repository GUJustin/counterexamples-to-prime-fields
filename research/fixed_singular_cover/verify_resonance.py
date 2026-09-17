import json
import sympy as s
X,z,c,d,y,w=s.symbols('X z c d y w')
rows=[]
for D in range(1,4):
 for j in range(1,D+1):
  t=2*D+1; K=D+1; M=2*K+1
  T=X**t+X+1
  R=-j*X**(t-1)+(z+1)*sum(X**i for i in range(t-1))
  S=sum((z+i+1)*X**(t+i-1) for i in range(1,D+1))+z
  P=c
  for i in range(D,0,-1):
   if i==j:P+=d*X**i;continue
   trial=P+y*X**i
   eq=s.expand(T*s.diff(trial,X)+R*trial-S).coeff(X,t+i-1)
   value=s.solve(eq,y)[0]
   assert not value.has(c)
   P=s.expand(P+value*X**i)
  compat=s.expand(T*s.diff(P,X)+R*P-S).coeff(X,t+j-1)
  assert not compat.has(c,d)
  S=s.expand(S+compat*X**(t+j-1))
  for i in range(1,D+1):assert s.expand(T*s.diff(P,X)+R*P-S).coeff(X,t+i-1)==0
  V=s.expand(P).coeff(d); Q=s.expand(P-c-d*V)
  assert s.degree(V,X)==j and s.expand(V).coeff(X,j)==1
  assert max(s.degree(Q,z),s.degree(V,z))<=K
  Qt=s.expand(Q.subs(X,X+w)-Q.subs(X,w))
  Vt=s.expand(V.subs(X,X+w)-V.subs(X,w))
  Pt=c+Qt+d*Vt
  residual=s.Poly(s.expand(T.subs(X,X+w)*s.diff(Pt,X)-Pt**2+R.subs(X,X+w)*Pt-S.subs(X,X+w)),X)
  E0=residual.nth(0); E2=residual.nth(2*j)
  v=s.expand(E0).coeff(d)
  assert v!=0 and s.expand(v-T.subs(X,w)*s.diff(V,X).subs(X,w))==0
  assert s.expand(E0).coeff(c,2)==-1
  assert s.expand(E2).coeff(d,2)==-1
  assert s.expand(E2).coeff(c).coeff(d)==0
  N=-s.expand(E0-v*d) # c²-u*c-w0
  # Leading c^4 after multiplication by v² comes only from -N².
  assert s.Poly(N,c).degree()==2 and s.Poly(N,c).LC()==1
  assert s.degree(E2,c)<=1
  rows.append(dict(D=D,resonant_index=j,t=t,coefficient_zdegree=int(max(s.degree(Q,z),s.degree(V,z))),quartic_leading_coefficient=-1))
print(json.dumps(dict(fixtures=rows,passed=True),indent=2))
