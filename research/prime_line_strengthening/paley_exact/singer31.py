"""Exact q31 Singer alpha gcd over its degree-six Gaussian-period field.
No floating-point embeddings; the field and every support polynomial are
constructed directly inside Q[Z]/Phi_31. Low-level exact dense polynomial API.
"""
import argparse,json,time
import sympy as s
from sympy.polys.densearith import dup_rem,dup_sub,dup_mul_ground,dup_mul
from sympy.polys.euclidtools import dup_gcd
q=31;r=15;dim=30

def mul(a,b):
 out=[0]*q
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:out[(i+j)%q]+=x*y
 return tuple(out[i]-out[-1] for i in range(dim))
one=(1,)+(0,)*(dim-1)
def rootpoly(S):
 coeff=[one]
 for j in S:
  out=[[0]*dim for _ in range(len(coeff)+1)]
  for k,v in enumerate(coeff):
   shifted=[0]*q
   for i,a in enumerate(v):shifted[(i+j)%q]+=a
   for i in range(dim):
    out[k][i]-=shifted[i]-shifted[-1];out[k+1][i]+=v[i]
  coeff=list(map(tuple,out))
 return coeff

def construct(source="Singer",mixed=False):
 unseen=set(range(1,q));orbits=[]
 while unseen:
  j=min(unseen);O=sorted({j*pow(2,t,q)%q for t in range(5)})
  assert len(O)==5;orbits.append(O);unseen-=set(O)
 orbits.sort(key=lambda O:30 in O)
 def compress(v):
  out=[v[0]]
  for O in orbits[:-1]:
   assert len({v[j] for j in O})==1
   out.append(v[O[0]])
  assert all(v[j]==0 for j in orbits[-1] if j<30)
  return s.Matrix(out)
 eta=tuple(int(i in orbits[0]) for i in range(dim))
 powers=[one]
 for _ in range(6):powers.append(mul(powers[-1],eta))
 M=s.Matrix.hstack(*(compress(v) for v in powers[:6]));assert M.det()!=0
 inv=M.inv();rel=inv*compress(powers[6]);Z=s.Symbol('eta')
 f=s.Poly(Z**6-sum(rel[i]*Z**i for i in range(6)),Z,domain=s.QQ)
 assert f.is_irreducible
 K=s.QQ.algebraic_field((f,Z))
 def convert(v):
  c=inv*compress(v)
  return K([K.dom.convert(a) for a in reversed(c)])
 # Verify the field embedding on a spanning set of period vectors.
 basis=[one]+[tuple(int(i in O) for i in range(dim)) for O in orbits[:-1]]
 for a in basis:
  for b in basis:assert convert(mul(a,b))==convert(a)*convert(b)
 # trace support using primitive F32 basis X^5+X^2+1
 def fmul(a,b):
  out=0
  while b:
   if b&1:out^=a
   b>>=1;a<<=1
   if a&32:a^=0b100101
  return out
 def trace(a):
  out=0
  for _ in range(5):out^=a;a=fmul(a,a)
  assert out in [0,1]
  return out
 a=1;D=[];seen=[]
 for i in range(q):
  seen.append(a)
  if trace(a)==0:D.append(i)
  a=fmul(a,2)
 assert len(set(seen))==q and a==1 and len(D)==15
 S=sorted(set(range(q))-{(-i)%q for i in D})
 assert len(S)==16
 assert all(sum((a-b)%q==t for a in D for b in D)==7 for t in range(1,q))
 B=list(reversed([convert(v) for v in rootpoly(S)]))
 targets=[]
 for O in orbits:
  T=sorted(O[0]*j%q for j in D)
  targets.append((O[0],T,list(reversed([convert(v) for v in rootpoly(T)]))))
 assert len({tuple(a) for _,_,a in targets})==6
 negD=sorted((-j)%q for j in D)
 Aneg=next(a for _,t,a in targets if t==negD)
 assert dup_mul(B,Aneg,K)==[K.one]+[K.zero]*30+[-K.one]
 if mixed:
  QR=sorted({i*i%q for i in range(1,q)})
  NQR=sorted(set(range(1,q))-set(QR))
  for name,T in [('QR',QR),('NQR',NQR)]:
   targets.append((name,T,list(reversed([convert(v) for v in rootpoly(T)]))))
  if source=='Paley':
   S=[0]+QR
   B=list(reversed([convert(v) for v in rootpoly(S)]))
 return K,B,targets,{'source_family':source,'period_orbits':orbits,'field_minpoly':str(f.as_expr()),'D':D,'S':S,'source_coefficients':[[str(c) for c in a.to_list()] for a in B]}

def coeff(a,j,K):return a[-j-1] if j<len(a) else K.zero

def run(hs,output,source="Singer",mixed=False):
 start=time.time();K,B,targets,meta=construct(source,mixed);meta['setup_seconds']=time.time()-start
 rows=[]
 for h in hs:
  P=dup_rem([K.one]+[K.zero]*h,B,K)
  for multiplier,T,A in targets:
   t0=time.time();powers=[[K.one]]
   for j in range(1,max(h,r)+1):powers.append(dup_rem(powers[-1]+[K.zero],A,K))
   v=[coeff(powers[h],i,K) for i in range(r)]
   pivot=next(i for i,x in enumerate(v) if x)
   R=[[coeff(P,j,K)*coeff(powers[j],i,K) for j in range(r,-1,-1)] for i in range(r)]
   # strip initial zeros for low-level dense API
   def strip(a):
    while a and not a[0]:a=a[1:]
    return a
   R=list(map(strip,R));G=[];used=[]
   for i in range(r):
    if i==pivot:continue
    F=dup_sub(dup_mul_ground(R[i],v[pivot],K),dup_mul_ground(R[pivot],v[i],K),K)
    G=dup_gcd(G,F,K);used.append(i)
    if len(G)==1:break
   forbidden=[K.one]+[K.zero]*30+[-K.one,K.zero] # alpha^32-alpha
   valid=G
   while len(valid)>1:
    d=dup_gcd(valid,forbidden,K)
    if len(d)<=1:break
    from sympy.polys.densearith import dup_exquo
    valid=dup_exquo(valid,d,K)
   row={'h':h,'target_multiplier':multiplier,'target':T,'equations_used':used,'raw_degree':len(G)-1,'raw_coefficients':[[str(c) for c in a.to_list()] for a in G],'valid_degree':len(valid)-1,'valid_coefficients':[[str(c) for c in a.to_list()] for a in valid],'seconds':time.time()-t0}
   rows.append(row);print(json.dumps({k:row[k] for k in ['h','target_multiplier','raw_degree','valid_degree','seconds']}),flush=True)
   with open(output,'w') as fp:json.dump({**meta,'rows':rows,'elapsed':time.time()-start,'complete':False},fp,indent=2)
 with open(output,'w') as fp:json.dump({**meta,'rows':rows,'elapsed':time.time()-start,'complete':True},fp,indent=2)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--h',default='23');ap.add_argument('--output',required=True);ap.add_argument('--mixed',action='store_true');ap.add_argument('--source',default='Singer');a=ap.parse_args()
 run([int(x) for x in a.h.split(',')],a.output,a.source,a.mixed)
