"""Exact symbolic verification of the theta=1 scalar native-label criterion."""
import sympy as s
from pathlib import Path
import json
z=s.symbols('z'); t=s.symbols('t0:5'); M=s.zeros(5)
for j in range(5):
 for a,b,c in [(j,(j+2)%5,1),(j,(j+1)%5,-1),((j+1)%5,(j+2)%5,-z)]:
  M[a,b]+=t[j]*c; M[b,a]-=t[j]*c
pf=[]
for k in range(5):
 a,b,c,d=[j for j in range(5) if j!=k]
 pf.append(s.expand(M[a,b]*M[c,d]-M[a,c]*M[b,d]+M[a,d]*M[b,c]))
e0={t[0]:1,**{t[i]:0 for i in range(1,5)}}
J=s.Matrix([[s.diff(f,x).subs(e0) for x in t[1:]] for f in pf])
minor=s.factor(J.extract([1,3,4],[0,2,3]).det());assert minor in ((z-1)**2,-(z-1)**2)
Q=z*z+z+1; H=z**3+2*z*z+3*z+1
v=s.Matrix([0,z+1,1,-z,Q]); assert (J*v[1:,0]).applyfunc(s.expand)==s.zeros(5,1)
res=[s.factor(f.subs(dict(zip(t,v)))) for f in pf]
assert all(s.expand(a-b)==0 for a,b in zip(res,[z*H,-H,H,-H,z*z*H]))
plane=[s.expand(f.subs({t[0]:0,t[1]:0})) for f in pf]
assert plane[0]==t[2]*t[4]
assert s.expand(plane[1]+plane[0])==s.expand((1-z)*t[2]*t[3])
assert s.expand(plane[2]-z*z*plane[0])==s.expand((z-1)*t[3]*t[4])
e=s.eye(5); shifted=s.Matrix([v[4],v[0],v[1],v[2],v[3]])
line_minor=s.factor(s.Matrix.hstack(e[:,0],v,e[:,1],shifted).extract([0,1,2,3],[0,1,2,3]).det())
assert line_minor in (Q,-Q)
assert s.rem(H,Q,z)==z
assert s.factor(z**5-3*z*z+z+1)==(z-1)**2*H
assert s.discriminant(H,z)==-23
result=dict(status='PASS',pfaffians=[str(f) for f in pf],jacobian=str(J),smooth_minor=str(minor),tangent_direction=[str(x) for x in v],tangent_residuals=[str(x) for x in res],plane_restrictions=[str(x) for x in plane],conjugate_line_minor=str(line_minor),cubic=str(H),cubic_discriminant=-23)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
