import sympy as S,json,itertools,time
from pathlib import Path
st=time.time();data=[json.loads(x) for x in Path(__file__).with_name('design_orbits.jsonl').read_text().splitlines()][5];T=data['T'];C=data['C'];w,z=S.symbols('w z');bs=[None,0,1,w/(w+z-1),z/(w+z-1),w,z];rows=[]
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
