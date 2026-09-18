#!/usr/bin/env python3
import sympy as s, pathlib,json,time
start=time.monotonic();base=pathlib.Path(__file__).resolve().parent
u,v,z,d=s.symbols('u v z d'); env={str(a):a for a in [u,v,z,d]}
data=json.loads((base/'nonfano2_minors.json').read_text())
rawguards=[u,v,z,d,u-1,v-1,z-1,d-1,u-v,u-z,u-d,v-z,v-d,z-d]
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
branches=[('I',u*v-u*z+z,s.Integer(1)),('II',u*v*(z-1)+z*(u-v),v*(z-1))]
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
(base/'nonfano2_branches.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
