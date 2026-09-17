from pathlib import Path
import json
import sympy as S
z,v=S.symbols('z v')
fixtures=[z*((z-1)*v-(z+1))**2*(v-z*z),(z-1)*((z+1)*v-z)**3,((z-1)*v-z)**2,(z-2)*(v+z),v**3+z*v+z-1,z*z-1]
rows=[]
for p in (7,11,13):
 for idx,F0 in enumerate(fixtures):
  F=S.Poly(F0,v,z, modulus=p).as_expr()
  co=[S.Poly(S.expand(F).coeff(v,j),z,modulus=p) for j in range(4)]
  m=max(j for j,c in enumerate(co) if not c.is_zero)
  d,c,b,a=[x.as_expr() for x in co]
  num=den=None
  if m==3:
   disc=S.Poly(b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d,z,modulus=p)
   U=S.Poly(b*b-3*a*c,z,modulus=p)
   if not disc.is_zero:E=disc.as_expr()
   elif not U.is_zero:E=a*U.as_expr();num=9*a*d-b*c;den=2*U.as_expr()
   else:E=a;num=-b;den=3*a
  elif m==2:
   disc=S.Poly(c*c-4*b*d,z,modulus=p)
   if not disc.is_zero:E=disc.as_expr()
   else:E=b;num=-c;den=2*b
  elif m==1:E=c
  else:E=d
  count=0
  for zz in range(p):
   for vv in range(p):
    if int(F.subs({z:zz,v:vv}))%p==0 and int(S.diff(F,v).subs({z:zz,v:vv}))%p==0:
     count+=1
     if int(S.sympify(E).subs(z,zz))%p:assert num is not None and int((num-vv*den).subs(z,zz))%p==0
  rows.append(dict(p=p,fixture=idx,generic_degree=m,singular_pairs=count,status='passed'))
Path(__file__).with_name('cubic_jet_checks.json').write_text(json.dumps(rows,indent=2)+'\n')
print('Passed',len(rows),'fixtures; singular pairs:',sum(x['singular_pairs'] for x in rows))
