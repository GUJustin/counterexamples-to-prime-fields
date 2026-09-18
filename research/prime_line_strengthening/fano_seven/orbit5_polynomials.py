import sympy as S,json,itertools,time
from pathlib import Path
st=time.time();data=[json.loads(x) for x in Path(__file__).with_name('design_orbits.jsonl').read_text().splitlines()][5];T=data['T'];C=data['C'];bs=[None,0,1,S.Rational(1,2),S.Rational(3,4),2,3];rows=[]
for L,b in zip(C,bs):
 I=[i for i in range(1,8) if i not in L]
 for j in I[1:]:
  row=[0]*24
  for i,sg in ((I[0],1),(j,-1)):
   if i!=1:
    for k in range(4):row[(i-2)*4+k]+=sg*((int(k==3)) if b is None else b**k)
  rows.append(row)
ns=S.Matrix(rows).nullspace();print('nullity',len(ns),flush=True)
h=S.symbols('h0:'+str(len(ns)));X=S.symbols('X');coef=sum((v*a for v,a in zip(ns,h)),S.zeros(24,1));Ps=[S.Integer(0)]+[sum(coef[(i-2)*4+k]*X**k for k in range(4)) for i in range(2,8)]
print('P',list(map(S.factor,Ps)),flush=True);rr=[]
for L in T:
 i,j,k=L;f=Ps[i-1]-Ps[j-1];g=Ps[i-1]-Ps[k-1]
 common=[b for CL,b in zip(C,bs) if not(set(CL)&set(L))]
 for b in common:
  if b is not None:f=S.cancel(f/(X-b));g=S.cancel(g/(X-b))
 r=S.factor(S.resultant(f,g,X));rr.append(r);print(L,'knowncommon',common,'resultant',r,flush=True)
out={'orbit':5,'b':list(map(str,bs)),'nullity':len(ns),'polynomials':list(map(str,map(S.factor,Ps))),'triple_resultants':list(map(str,rr)),'seconds':time.time()-st}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
fac=[]
for f in rr:
 if f:
  for ff,mul in S.factor_list(f)[1]:
   if ff not in fac:fac.append(ff)
pts=set()
for f,g in itertools.combinations(fac,2):
 fv=S.Matrix([f.coeff(t) for t in h]);gv=S.Matrix([g.coeff(t) for t in h]);v=fv.cross(gv)
 if v==S.zeros(3,1):continue
 first=next(t for t in v if t);v=tuple(S.cancel(t/first) for t in v)
 if all(S.expand(r).subs(dict(zip(h,v)))==0 for r in rr):pts.add(v)
checks=[]
for v in sorted(pts):
 pol=[S.factor(p.subs(dict(zip(h,v)))) for p in Ps];distinct=len(set(pol))==7
 roots=[];valid=distinct
 for L in T:
  i,j,k=L;gg=S.gcd(pol[i-1]-pol[j-1],pol[i-1]-pol[k-1]);rrr=S.solve(gg,X) if gg!=0 else []
  good=[r for r in rrr if r not in bs];roots.append(list(map(str,good)))
  if not good:valid=False
 if valid and all(len(x)==1 for x in roots):valid=len(set(x[0] for x in roots))==7
 checks.append({'h':list(map(str,v)),'distinct_polynomials':distinct,'admissible_triple_roots':roots,'possible':valid})
out['projective_solutions']=checks
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print('solutions',checks,flush=True)
