import sympy as s
T,Y,h=s.symbols('T Y h');p=-s.Rational(7,2);a=[s.Integer(1),-s.Rational(13,22),-s.Rational(19,44),s.Rational(4,11)];bt=[0,2,3,4];tau=s.Rational(15,88)/h;xs={(0,1):1,(0,2):2,(0,3):3,(1,2):4,(1,3):5,(2,3):6};x=lambda i,j:xs[tuple(sorted((i,j)))];C=[s.prod(Y-x(i,j)for j in range(4)if j!=i)for i in range(4)];A=[a[i]*C[i]for i in range(4)];R=(Y+p)**2-h*h*Y;B=[0]
for i in range(1,4):
 q,r=s.div(s.expand(h*C[0]-h*A[i]+R*tau*bt[i]*(Y-x(0,i))),Y+p,Y);assert r==0;B.append(q)
F=[s.expand(A[i].subs(Y,T*T)+T*s.sympify(B[i]).subs(Y,T*T))for i in range(4)];L0=T*T-h*T+p
gg=s.Poly(0,h)
for i in range(1,4):
 j,k=[j for j in range(1,4)if j!=i];q,r=s.div(F[0]-F[i],(T*T-x(0,i))*L0,T);assert r==0;L=s.cancel(q/(a[0]-a[i]));q2,r=s.div(F[j]-F[k],(T*T-x(j,k))*L0,T);assert r==0;assert s.cancel(L-q2.subs(T,-T)/(a[j]-a[k]))==0
 cross=s.expand(A[0].subs(Y,T*T)+A[j].subs(Y,T*T)-T*B[j].subs(Y,T*T));rem=s.rem(cross,L,T);print(i,'L',s.factor(L),'CROSS',s.factor(rem)); num=s.fraction(s.cancel(rem))[0]
 for cc in s.Poly(num,T).all_coeffs():gg=s.gcd(gg,s.Poly(cc,h))
print('GCD',gg)
import json
from pathlib import Path
out={'status':'EXCLUDED_FIXED_EDGE_CLASS','edges':[1,2,3,4,5,6],
 'leading_coefficients':[str(v)for v in a],'p':str(p),'sigma_tau':'15/88',
 'remaining_variable':'h=sigma nonzero','cross_coefficient_gcd':str(gg.as_expr()),
 'scope':'All sigma for this one edge fixture after the specified nondegenerate H/slope solution; not the variable Ceva class.'}
assert gg.degree()==0
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
