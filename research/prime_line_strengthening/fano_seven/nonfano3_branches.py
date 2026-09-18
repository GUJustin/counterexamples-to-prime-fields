#!/usr/bin/env python3
import sympy as s, pathlib,json,time
start=time.monotonic();base=pathlib.Path(__file__).resolve().parent
u,v,z,d=s.symbols('u v z d'); env={str(a):a for a in [u,v,z,d]}
data=json.loads((base/'nonfano_involution_3.json').read_text())
rawguards=[u,v,z,u-v,u+v,u-z,u+z,v-z,v+z,d-u,d+u,d-v,d+v,d-z,d+z]
def norm(f,vs):
    p=s.Poly(f,*vs,domain=s.QQ)
    return p.monic().as_expr() if not p.is_zero else s.Integer(0)
def strip(f, guards, vs):
    if f==0:return s.Integer(0)
    fac=s.factor_list(f,*vs)[1]; out=s.Integer(1)
    for q,e in fac:
        if norm(q,vs) not in guards:out*=q**e
    return s.factor(out)
rg={norm(g,(d,u,v,z)) for g in rawguards}
baseeq=[strip(s.sympify(row['determinant'],locals=env),rg,(d,u,v,z)) for row in data['minors']]
branches=[('F',u*u*(v+2*z)+v*z*z,u*u+2*v*z+z*z),('G',z*(-u*u+3*u*v+u*z+v*z),u*u+u*v+3*u*z-v*z)]
out=[]
for label,N,D in branches:
    guards=[]
    for g in rawguards+[D]:
        gg=s.cancel(g.subs(d,N/D)).as_numer_denom()[0]
        guards.extend(q for q,e in s.factor_list(gg,u,v,z)[1])
    gn={norm(g,(u,v,z)) for g in guards}
    eq=[]
    for row,f in zip(data['minors'],baseeq):
        num=s.cancel(f.subs(d,N/D)).as_numer_denom()[0]
        reduced=strip(num,gn,(u,v,z))
        eq.append({'rows':row['rows'],'remaining':str(reduced)})
        if reduced==1:break
    out.append({'branch':label,'d_numerator':str(N),'d_denominator':str(D),'nonzero_guard_factors':[str(g) for g in sorted(gn,key=str)],'equations':eq})
res={'branches':out,'seconds':time.monotonic()-start}
(base/'nonfano3_branches.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
