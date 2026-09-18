import sympy as S,json,time
from pathlib import Path
start=time.time();a,b,c,d=S.symbols('a b c d')
r=a*b;s=a*c
rows=[]
for u,v in ((b,c),(b,d),(c,d)):
 C=-(a*a-u*u)*(a*a-v*v)/(a*a)
 U=(u*u*v*v+r*s)/C
 rows.append([S.Integer(1),U,C])
# 3x3 determinant using only three differences avoids premature expansion.
f=S.factor(S.together((rows[1][1]-rows[0][1])*(rows[2][2]-rows[0][2])-(rows[2][1]-rows[0][1])*(rows[1][2]-rows[0][2])))
out={'necessary_difference_determinant':str(f),'elapsed_seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
cs=-a*a/b
Cs=[];Us=[];Vs=[]
for u,v in ((b,cs),(b,d),(cs,d)):
 C=S.factor(-(a*a-u*u)*(a*a-v*v)/(a*a))
 U=S.factor((u*u*v*v+a*b*a*cs)/C)
 V=S.factor(-(a*b+a*cs)*u*v/C)
 Cs.append(C);Us.append(U);Vs.append(V)
gamma=S.factor(-(Cs[1]-Cs[0])/(2*(a*b+a*cs)*(Us[1]-Us[0])))
beta=S.factor(-Cs[0]/(a*b+a*cs)-2*gamma*Us[0])
alphas=[S.factor(-beta*U-gamma*(U*U+V*V)) for U,V in zip(Us,Vs)]
out.update({'forced_c':'-a^2/b','beta':str(beta),'gamma':str(gamma),'alpha_values':list(map(str,alphas)),'alpha_difference_1':str(S.factor(alphas[1]-alphas[0])),'alpha_difference_2':str(S.factor(alphas[2]-alphas[0]))})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
