import sympy as s,json,pathlib,time
start=time.monotonic();p=pathlib.Path(__file__).resolve().parent
u,v,z,d=s.symbols('u v z d');env={str(x):x for x in [u,v,z,d]}
j=json.loads((p/'nonfano_involution_3.json').read_text());ds={tuple(r['rows']):s.sympify(r['determinant'],locals=env) for r in j['minors']}
F=(u*u*(v+2*z)+v*z*z)/(u*u+2*v*z+z*z)
G=z*(-u*u+3*u*v+u*z+v*z)/(u*u+u*v+3*u*z-v*z)
out=[]
for label,sub,inds in [('F',F,(0,2,3)),('F',F,(2,4,5)),('G',G,(0,3,4))]:
    expr=s.factor(s.cancel(ds[inds].subs(d,sub)))
    out.append({'branch':label,'rows':inds,'exact_determinant':str(expr)})
res={'identities':out,'seconds':time.monotonic()-start};(p/'nonfano3_exact_minors.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
