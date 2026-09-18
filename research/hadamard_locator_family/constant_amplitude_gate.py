"""Exact symbolic H-complement reduction and one rational amplitude-curve point."""
import json
from pathlib import Path
import sympy as s
x,y,z,u,v,w=s.symbols('x y z u v w');a=s.symbols('a0:4')
E=[y*(z-u)*a[0]*a[2]+z*(v-y)*a[0]*a[3]+u*(y-v)*a[1]*a[2]+v*(u-z)*a[1]*a[3],
   x*(z-u)*a[0]*a[1]+z*(w-x)*a[0]*a[3]+u*(x-w)*a[1]*a[2]+w*(u-z)*a[2]*a[3],
   x*(y-v)*a[0]*a[1]+y*(w-x)*a[0]*a[2]+v*(x-w)*a[1]*a[3]+w*(v-y)*a[2]*a[3]]
assert s.expand((w-x)*E[0]+(y-v)*E[1]-(z-u)*E[2])==0
A,B=s.symbols('A B');curve=(72*A+12)*B**2+(-100*A**2+30)*B-5*A**2-9*A
disc=s.factor(s.discriminant(curve,B));assert s.gcd(s.Poly(disc,A),s.Poly(s.diff(disc,A),A)).degree()==0
p0=(s.Rational(3,10),s.Rational(1,8));sub={A:p0[0],B:p0[1]}
assert curve.subs(sub)==0
slope=-s.diff(curve,A).subs(sub)/s.diff(curve,B).subs(sub)
line=p0[1]+slope*(A-p0[0]);restriction=s.factor(curve.subs(B,line))
remaining=s.cancel(restriction/(A-p0[0])**2)
assert s.Poly(remaining,A).degree()==1
aa=s.solve(remaining,A)[0];bb=s.factor(line.subs(A,aa));cc=s.factor(aa*(20*bb+1)/(6*bb+15))
point=[s.Integer(1),aa,bb,cc]
fixture_sub=dict(zip((x,y,z,u,v,w),(1,2,3,4,5,6)))
fixture_sub.update(dict(zip(a,point)))
assert all(s.factor(e.subs(fixture_sub))==0 for e in E)
guarded=all(point[i]!=0 and point[i]!=point[j] and point[i]!=-point[j] for i in range(4) for j in range(i)) and point[0]!=0
H=s.factor((point[0]*2*3-point[1]*4*5)/(point[0]-point[1]))
out={'linear_dependence':'(w-x)E01|23+(y-v)E02|13-(z-u)E03|12=0',
     'quadrics':[str(e) for e in E],'fixture_edges':[1,2,3,4,5,6],
     'affine_curve':str(curve),'quartic_discriminant':str(disc),
     'quartic_squarefree':True,'normalization_genus':1,
     'starting_point':list(map(str,p0)),'tangent_slope':str(slope),
     'tangent_restriction':str(restriction),'rational_amplitudes':list(map(str,point)),
     'nonzero_distinct_signed_amplitude_guard':bool(guarded),'H01':str(H),
     'scope':'Constant complement equations only; not an incidence-bank realization.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
