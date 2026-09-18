import json,math
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).parent;s=json.loads((P/'local_search.json').read_text());cert=json.loads((P/'nine_exchange.verified.json').read_text());jc=json.loads((P/'ninth_quartic_jacobian.json').read_text());p=17;rows=cert['minor_rows'];cols=cert['minor_columns'];assert cols==list(range(62))
eq=[(i,k) for i,S in enumerate(s['selected_supports']) for k in S]+[(8,k) for k in [0,1,4,5,6,7,8,11]]
v=sum((c[:] for c in s['polynomials']),[])+s['nodes']+s['word']+[0]+[2,15,8,5,13]
def ev(c,x):
 a=0
 for t in c[::-1]:a=a*x+t
 return a
def res(v,i,k):
 x=v[32+k];w=v[48+k]
 return ev(v[4*i:4*i+4],x)-w if i<8 else ev(v[65:70],x)-(x-v[64])*w
J=[[jc['jacobian'][i][j] for j in cols] for i in rows];a=[r+[int(i==j) for j in range(62)] for i,r in enumerate(J)]
for c in range(62):
 z=next(i for i in range(c,62) if a[i][c]);a[z],a[c]=a[c],a[z];iv=pow(a[c][c],-1,p);a[c]=[x*iv%p for x in a[c]]
 for i in range(62):
  if i!=c:
   t=a[i][c];a[i]=[(u-t*w)%p for u,w in zip(a[i],a[c])]
inv=[r[62:] for r in a];M=17;checks=[]
for e in range(2,33):
 rhs=[-res(v,*eq[i])//M%17 for i in rows];dv=[sum(x*y for x,y in zip(r,rhs))%17 for r in inv]
 for j,d in zip(cols,dv):v[j]+=M*d
 M*=17;assert all(res(v,*eq[i])%M==0 for i in rows);checks.append(e)
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%M
 return c
def power(a,n):
 b=[1]
 for _ in range(n):b=mul(b,a)
 return b
a,b,c=v[42],v[43],v[35];lam=(c-a)*pow(c-b,-1,M)%M;num=[-lam*b%M,a];den=[-lam%M,1]
def transform(co,d):
 out=[0]*(d+1)
 for j,t in enumerate(co):
  term=mul(power(num,j),power(den,d-j))
  for k,z in enumerate(term):out[k]=(out[k]+t*z)%M
 return out
polys=[transform([(v[4*i+j]-v[12+j])%M for j in range(4)],3) for i in range(8)];scale=pow(polys[4][2],-1,M);polys=[[scale*z%M for z in co] for co in polys];assert polys[4]==[0,M-1,1,0]
xs=[None if k==10 else lam*(v[32+k]-b)*pow(v[32+k]-a,-1,M)%M for k in range(16)]
ws=[]
for k,x in enumerate(xs):
 val=(v[48+k]-ev(v[12:16],v[32+k]))%M
 ws.append(scale*val%M if x is None else scale*pow(x-lam,3,M)*val%M)
oldpole=v[64];pole=lam*(b-oldpole)*pow(a-oldpole,-1,M)%M
f=v[65:70][:];prod=mul([-oldpole%M,1],v[12:16]);f=[(x-y)%M for x,y in zip(f,prod)];nn=[scale*pow(a-oldpole,-1,M)*z%M for z in transform(f,4)]
for ri in rows:
 ci,k=eq[ri];x=xs[k]
 if ci<8:
  assert ((polys[ci][3] if x is None else ev(polys[ci],x))-ws[k])%M==0
 else:
  assert ((nn[4]-ws[k]) if x is None else ev(nn,x)-(x-pole)*ws[k])%M==0
def reconstruct(x):
 if x is None:return None
 B=math.isqrt(M//2);r0,r1=M,x;t0,t1=0,1
 while abs(r1)>B:
  q,r=divmod(r0,r1);r0,r1=r1,r;t0,t1=t1,t0-q*t1
 if not t1 or abs(t1)>B or math.gcd(r1,t1)!=1:return 'FAIL'
 y=F(r1,t1)
 if (y.numerator-x*y.denominator)%M:return 'FAIL'
 return str(y)
rec={'nodes':list(map(reconstruct,xs)),'word':list(map(reconstruct,ws)),'polynomials':[list(map(reconstruct,t)) for t in polys],'pole':reconstruct(pole),'numerator':list(map(reconstruct,nn))}
flat=[x for a in rec['polynomials'] for x in a]+rec['nodes']+rec['word']+[rec['pole']]+rec['numerator'];ok='FAIL' not in flat
if ok:
 xx=[None if x is None else F(x) for x in rec['nodes']];ww=list(map(F,rec['word']));pp=[list(map(F,c)) for c in rec['polynomials']];nb=list(map(F,rec['numerator']));beta=F(rec['pole'])
 for i in rows:
  ci,k=eq[i];x=xx[k]
  lhs=(pp[ci][3] if x is None else ev(pp[ci],x))-ww[k] if ci<8 else ((nb[4]-ww[k]) if x is None else ev(nb,x)-(x-beta)*ww[k])
  if lhs:ok=False;break
out={'modulus':M,'precision_exponent':32,'fixed_columns':list(range(62,70)),'coordinates':v,'verified_lift_stages':checks,'normalized_modular_incidences_verified':True,'normalized_coordinates':{'nodes':xs,'word':ws,'polynomials':polys,'pole':pole,'numerator':nn},'normalized_reconstruction':rec,'exact_62_incidences':ok};(P/'nine_exchange_rationalize.json').write_text(json.dumps(out,indent=2)+'\n');print('exact',ok,'failedcoords',flat.count('FAIL'));print(json.dumps(rec,indent=2))
