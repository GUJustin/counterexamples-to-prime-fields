import sympy as S,json,time
from pathlib import Path
start=time.monotonic();x,w,z,K=S.symbols('x w z K');s=w+z-1;u=w/s;v=z/s
Q={2:(x-w)*(x-z),3:(x-u)*(x-v),4:(x-v)*(x-z),5:(x-u)*(x-w),6:(x-v)*(x-w),7:(x-u)*(x-z)}
L=K/((1-v)*(1-z))-1/(u*z)
P={1:S.Integer(0)}
for i in (2,3):P[i]=Q[i]*((K/Q[i].subs(x,1)-1/Q[i].subs(x,0))*x+1/Q[i].subs(x,0))
for i in (4,5):P[i]=Q[i]*(L*(x-1)+K/Q[i].subs(x,1))
for i in (6,7):P[i]=Q[i]*(L*x+1/Q[i].subs(x,0))
def quo(i,j,roots):
 f=S.cancel((P[i]-P[j])/S.prod(x-r for r in roots)); pol=S.Poly(f,x);assert pol.degree()<=1
 return [pol.coeff_monomial(x),pol.coeff_monomial(1)]
def determinant(a,b):return a[0]*b[1]-a[1]*b[0]
actual=[determinant(quo(2,4,[1,z]),quo(2,5,[1,w])),determinant(quo(2,6,[0,w]),quo(2,7,[0,z])),determinant(quo(3,4,[1,v]),quo(3,6,[0,v])),determinant(quo(3,5,[1,u]),quo(3,7,[0,u]))]
A=K*w*z*(w+z);H=(w-1)*(z-1)*(s-1);F3=-K*w*w*z+(w-1)*(z-1)**2;F4=K*w*z*z-(w-1)**2*(z-1);Delta=w*w*z*z*(w-1)**2*(z-1)**2
expected=[2*(z-w)*(A+H)/(w*w*z*z*(w-1)*(z-1)),2*K*(z-w)*(A+H)/(w*z*(w-1)**2*(z-1)**2),2*s*s*F3*(A-H)/Delta,-2*s*s*F4*(A-H)/Delta]
res=[str(S.cancel(a-b)) for a,b in zip(actual,expected)];assert res==['0']*4
out={'method':'Independent direct polynomial division and determinant expansion','determinant_identity_residuals':res,'seconds':time.monotonic()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
