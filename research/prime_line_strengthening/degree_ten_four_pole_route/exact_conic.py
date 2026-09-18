"""Exact old-graph restriction and its canonical tangent conic over Q(eta)."""
import json
from fractions import Fraction as Q
from pathlib import Path
from verify_exact_kernel import add,mul,scale,powers,zero,one,mod29
P=Path(__file__).parent
K=json.loads((P/'exact_kernel.json').read_text())
def inv(x):
 a,b=x;den=a*a-a*b+2*b*b;assert den
 return ((a-b)/den,-b/den)
def div(x,y):return mul(x,inv(y))
def pmul(a,b):
 c=[zero]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=add(c[i+j],mul(x,y))
 return c
poly=[(Q(-1),Q(-1)),one,one,(Q(0),Q(1))]
pp=[ [one] ]
for _ in range(10):pp.append(pmul(pp[-1],poly))
restr=[]
for form in K['components']:
 out=[zero]*35
 for i,j,cc in form['terms']:
  cc=tuple(map(Q,cc))
  for d,z in enumerate(pp[j]):out[i+d]=add(out[i+d],mul(cc,z))
 restr.append(out)
pos=next(i for i,z in enumerate(restr[0]) if z!=zero)
lambdas=[v[pos] for v in restr];assert all(z!=zero for z in lambdas)
for a,lam in zip(restr,lambdas):assert all(mul(x,lambdas[0])==mul(y,lam) for x,y in zip(a,restr[0]))
kappa=div(mul(lambdas[1],lambdas[1]),scale(mul(lambdas[0],lambdas[2]),4))
assert mod29(kappa)==5
out={'status':'PASS','P0_coefficients':[list(map(str,x)) for x in poly],
 'restriction_pivot_X_degree':pos,'lambda':[list(map(str,x)) for x in lambdas],
 'kappa':list(map(str,kappa)),'kappa_mod29':mod29(kappa),
 'conic':'a*c=kappa*b^2','parameterization':'[kappa*u^2:u:1]',
 'restriction_proportionality_checked':True,
 'conic_family_parameter_discriminant':'F1^2-4*kappa*F0*F2',
 'structural_factor':'product_(j=0)^6(Y-P_j(X)) divides F1^2-4*kappa*F0*F2'}
(P/'exact_conic.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
