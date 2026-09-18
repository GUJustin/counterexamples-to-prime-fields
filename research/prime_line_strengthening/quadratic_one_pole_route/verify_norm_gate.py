import json,itertools,math
from pathlib import Path
P=Path(__file__).parent;p=29;z=16
assert pow(z,7,p)==1 and z!=1
eta=sum(pow(z,i,p) for i in [1,2,4])%p;alpha=(eta-1)*15%p;cw=3*(eta+3)*pow(4,-1,p)%p
xs=[pow(z,i,p) for i in range(7)]+[alpha*pow(z,i,p)%p for i in range(7)]
ys=[pow(z,5*i,p) for i in range(7)]+[cw*pow(z,5*i,p)%p for i in range(7)]
masks=[{i for i in range(7) if (j-i)%7 in ({0,1,2,4} if orbit==0 else {1,2,4})} for orbit in range(2) for j in range(7)]
assert len(set(xs))==14
expected=set()
for f in range(4):
 for F in itertools.combinations(range(14),f):
  for E in itertools.combinations(set(range(14))-set(F),f):
   if all(sum(i in masks[j] for j in F)<=sum(i in masks[j] for j in E) for i in range(7)):expected.add((F,tuple(sorted(E))))
rows=json.loads((P/'all_fiber_norm_gate.json').read_text());actual={(tuple(x['full']),tuple(x['empty'])) for x in rows};assert actual==expected and len(rows)==len(actual)==302

def product_poly(roots):
 c=[1]
 for root in roots:
  d=[0]*(len(c)+1)
  for j,v in enumerate(c):d[j]-=root*v;d[j+1]+=v
  c=[v%p for v in d]
 return c

def ev(c,x):return sum(v*pow(x,j,p) for j,v in enumerate(c))%p

def determinant(M):
 M=[r[:] for r in M];old=1;sign=1;n=len(M)
 for k in range(n-1):
  if M[k][k]==0:
   z=next(i for i in range(k+1,n) if M[i][k]);M[k],M[z]=M[z],M[k];sign=-sign
  pv=M[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    a=M[i][j]*pv-M[i][k]*M[k][j];assert a%old==0;M[i][j]=a//old
   M[i][k]=0
  old=pv
 return sign*M[-1][-1]
cert=[]
for rec in rows:
 F=rec['full'];E=rec['empty'];f=len(F);Q=product_poly([xs[j] for j in F]);R=[0]*max(1,f)
 for j in F:
  L=product_poly([xs[k] for k in F if k!=j]); scale=ys[j]*pow(ev(L,xs[j]),-1,p)%p
  for k,v in enumerate(L):R[k]=(R[k]+scale*v)%p
 singles=[j for j in range(14) if j not in F and j not in E]
 vv=[(ys[j]-ev(R,xs[j]))*pow(ev(Q,xs[j]),-1,p)%p for j in singles]
 M=[[v*v%p,x*v*v%p]+[v*pow(x,k,p)%p for k in range(5-f)]+[pow(x,k,p) for k in range(8-2*f)] for j,v in zip(singles,vv) for x in [xs[j]]]
 assert M==rec['matrix']
 sub=[[M[i][j] for j in rec['independent_columns']] for i in rec['independent_rows']]
 dd=determinant(sub)%p;assert dd
 if f:assert len(sub)==15-3*f
 else:
  assert len(sub)==14 and len(rec['kernel'])==1
  v=rec['kernel'][0];assert v[:2]==[0,0] and all(sum(a*b for a,b in zip(row,v))%p==0 for row in M)
 cert.append(dict(full=F,empty=E,minor_size=len(sub),minor_mod29=dd))
(P/'norm_gate_independent_verification.json').write_text(json.dumps(dict(status='PASS',patterns=len(cert),certificates=cert),indent=2));print('PASS: independent incidence set, rebuilt matrices,302 exact integer Bareiss minors, unique linear f0 kernel')
