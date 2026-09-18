import sympy as s,json,pathlib,time
start=time.monotonic();p=pathlib.Path(__file__).resolve().parent
u,v,z=s.symbols('u v z'); env={str(x):x for x in [u,v,z]}; data=json.loads((p/'nonfano2_branches.json').read_text())['branches'][0]
D=v+z*z-v*z;U=v*z/D
baseguards=[u,v,z,u-1,v-1,z-1,u-v,u-z,v-z,u*v-u*z+z,u*v-u*z+z-1,u*v-u*z-u+z,D]
def norm(f):return s.Poly(f,v,z,domain=s.QQ).monic().as_expr()
G=set()
for g in baseguards:
 num=s.cancel(g.subs(u,U)).as_numer_denom()[0]
 G.update(norm(q) for q,e in s.factor_list(num,v,z)[1])
out=[]
for row in data['equations']:
 f=s.sympify(row['remaining'],locals=env);num,den=s.cancel(f.subs(u,U)).as_numer_denom();fac=s.factor_list(num,v,z);rem=s.Integer(1)
 if num==0:rem=s.Integer(0)
 else:
  for q,e in fac[1]:
   if norm(q) not in G:rem*=q**e
 out.append({'rows':row['rows'],'exact_numerator':str(s.factor(num)),'denominator':str(s.factor(den)),'remaining':str(s.factor(rem))})
eq=[s.sympify(row['remaining'],locals=env) for row in out if row['remaining']!='0']
gb=s.groebner(eq,v,z,order='lex')
res={'u':str(U),'nonzero_guards':[str(q) for q in sorted(G,key=str)],'equations':out,'groebner_basis':[str(q) for q in gb.polys],'seconds':time.monotonic()-start};(p/'nonfano2_branchI_reduce.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
