"""Bounded symbolic shared-denominator and Newton-degree checks."""
from pathlib import Path
import json
import sympy as s
X,z,c=s.symbols('X z c');rows=[];small_characteristic_checks=0
for ell,ds in [(2,range(1,5)),(3,range(1,4)),(4,range(1,3))]:
 for D in ds:
  t=ell*D+1;a=1;T=(z+1)*X**t+z*X**(t-1)+1
  A1=z*X**(t-1)+z*X;A0=-z*X**(t+D-1)+z;Ae=z+2
  tp=s.Poly(T,X);rp=s.Poly(A1,X);sp=s.Poly(-A0,X)
  piv={j:s.expand(j*tp.coeff_monomial(X**t)+rp.coeff_monomial(X**(t-1))) for j in range(1,D+1)}
  den={j:s.prod(piv[h] for h in range(j,D+1)) for j in range(1,D+1)}
  nn={}
  for j in range(D,0,-1):
   nxt=den[j+1] if j<D else s.Integer(1)
   value=sp.coeff_monomial(X**(t+j-1))*nxt
   for i in range(j+1,D+1):
    kij=i*tp.coeff_monomial(X**(t+j-i))+rp.coeff_monomial(X**(t+j-1-i))
    quotient=s.prod(piv[h] for h in range(j+1,i))
    value-=kij*nn[i]*quotient
   nn[j]=s.expand(value)
   assert s.Poly(nn[j],z).degree()<=a*(D-j+1)
  Delta=s.expand(den[1]);W=s.expand(sum(nn[j]*s.prod(piv[h] for h in range(1,j))*X**j for j in range(1,D+1)))
  assert s.Poly(Delta,z).degree()<=a*D
  assert s.Poly(W,z).degree()<=a*D
  E=s.Poly(s.expand(Delta**(ell-1)*T*s.diff(W,X)+A1*(c*Delta+W)*Delta**(ell-1)+A0*Delta**ell+Ae*(c*Delta+W)**ell),X)
  assert all(E.coeff_monomial(X**i)==0 for i in range(t,t+D))
  M=a*(ell*D+1)
  assert s.Poly(E.as_expr(),z).degree()<=M
  assert s.Poly(E.as_expr(),c).degree()<=ell
  e0=E.coeff_monomial(1)
  assert s.expand(s.Poly(e0,c).coeff_monomial(c**ell)-Ae*Delta**ell)==0
  for prime in (2,3,5):
   assert all(not s.Poly(v,z,modulus=prime).is_zero for v in piv.values())
   assert not s.Poly(Delta,z,modulus=prime).is_zero
   for exponent in range(t,t+D):assert s.Poly(E.coeff_monomial(X**exponent),z,c,modulus=prime).is_zero
   small_characteristic_checks+=1
  rows.append({'ell':ell,'D':D,'t':t,'Delta_degree':int(s.Poly(Delta,z).degree()),'W_degree':int(s.Poly(W,z).degree()),'residual_z_degree':int(s.Poly(E.as_expr(),z).degree()),'cap_M':M,'leading_c_coefficient_checked':True})
# Exactly one identically resonant pivot is possible and must remain free.
tau=z+1;D=5;j0=3;r=-j0*tau
assert [j for j in range(1,D+1) if s.expand(j*tau+r)==0]==[j0]
out={'fixtures':rows,'nonresonant_small_characteristic_checks':small_characteristic_checks,'resonant_boundary':{'D':D,'zero_pivot':j0,'handled_by_theorem':False}}
Path(__file__).with_name('general_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
