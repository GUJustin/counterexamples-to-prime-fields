"""Independent primality, roots, exact comparisons, and Kummer witness replay."""
from pathlib import Path
from math import comb,isqrt,prod
from fractions import Fraction
import json,time,random,hashlib
BASE=Path(__file__).resolve().parent

def decode(t,m,D):
 if t<=1:return None
 s=t.bit_length()
 if s>(m+1)*(m+2)//2-1:return None
 u=Fraction(t,1<<s);I=[]
 for i in range(2,m+2):
  threshold=1-Fraction(1,1<<i)
  if u<=threshold:u/=threshold;I.append(i)
 if u!=1 or len(I)!=D:return None
 if prod((1<<i)-1 for i in I)!=t:return None
 return I

def poly(I,p):
 v=[1]
 for i in I:
  w=[0]*(len(v)+1)
  for j,a in enumerate(v):w[j]=(w[j]-(a<<i))%p;w[j+1]=(w[j+1]+a)%p
  v=w
 return v

def ev(P,y,p):
 v=0
 for a in reversed(P):v=(v*y+a)%p
 return v

if __name__=='__main__':
 start=time.monotonic();rows=[];instances=[];rng=random.Random(2026091719)
 source=json.loads((BASE/'kummer_certificates.json').read_text())['rows']
 assert [(r['b'],r['d']) for r in source]==[(521,2),(1279,3),(9689,5),(23209,13),(44497,19)]
 for row in source:
  t0=time.monotonic();b=row['b'];p=(1<<b)-1;d=row['d'];m=row['m'];D=row['D'];c=row['c'];n=row['n'];K=row['K']
  assert all(b%q for q in range(2,isqrt(b)+1)) and all(d%q for q in range(2,isqrt(d)+1))
  s=4
  for _ in range(b-2):
   square=s*s;s=(square&p)+(square>>b)-2
   if s<0:s+=p
   elif s>=p:s-=p
  assert s==0 and (p-1)%d==0
  omega=int(row['omega_hex'],16);v=row['alpha_power_two_exponent'];alpha=1<<v
  assert pow(alpha,d,p)==2 and omega!=1 and pow(omega,d,p)==1
  assert hashlib.sha256(omega.to_bytes((b+7)//8,'big')).hexdigest()==row['omega_sha256']
  assert n==d*(m+1)+c and K==d*D-1 and 0<=c<d and 1<=D<m
  A=n*2**((m+c+d)//d);E=sum(range(m-D+2,m+2));assert E==row['product_exponent']
  assert A**(d*(d-1))<p and (1<<E)<p
  J=comb(m,D);q=row['ratio_greater_than_power_two'];assert str(J)==row['nearby_count']
  assert J**(d+1)*K**K*(n-K)**(n-K)>n**(n+d+1)*(1<<(q*(d+1)))
  assert (d+1)*(b-1)>n
  mu=[pow(omega,j,p) for j in range(d)]
  domain=[(w<<((v*i)%b))%p for i in range(2,m+2) for w in mu]+[1<<((v*i)%b) for i in range(m+2,m+c+2)]+mu
  assert len(domain)==len(set(domain))==n
  digest=hashlib.sha256()
  for x in domain:digest.update(x.to_bytes((b+7)//8,'big'))
  # Direct field checks on full orbits supplement the algebraic root recipe.
  for i in [2,m+1]:
   for j in range(d):assert pow(domain[(i-2)*d+j],d,p)==1<<i
  ref=list(range(2,D+2));F=poly(ref,p);ys=[1<<i for i in range(2,m+2)]+[1<<i for i in range(m+2,m+c+2)]+[1];weights=[d]*m+[1]*c+[d]
  f=[ev(F,y,p) for y in ys];assert sum(w for w,x in zip(weights,f) if x==0)==K+1
  witnesses=[]
  for trial in range(16):
   I=sorted(rng.sample(range(2,m+2),D));T=prod((1<<i)-1 for i in I);assert T<p and decode(T,m,D)==I
   if trial<2:
    z=(T if D%2 else -T)%p;H=poly(I,p);Q=[(a-bb)%p for a,bb in zip(F,H)];assert Q[-1]==0 and d*(len(Q)-2)<K
    received=f[:-1]+[(f[-1]+z)%p]
    matches=sum(w for w,y,r in zip(weights,ys,received) if ev(Q,y,p)==r)
    assert matches==K+d+1
    witnesses.append(dict(support=I,parameter_hex=hex(z),polynomial_in_X_to_d_coefficients_hex=[hex(x) for x in Q[:-1]]))
  for _ in range(16):
   t=rng.randrange(1,p);I=decode(t,m,D)
   if I is not None:assert prod((1<<i)-1 for i in I)==t
  rows.append(dict(b=b,d=d,n=n,K=K,ratio_greater_than_power_two=q,separation=row['separation_fraction'],domain_sha256=digest.hexdigest(),distinct_domain_points=n,decoded_supports=16,fully_evaluated_witnesses=2,seconds=time.monotonic()-t0))
  instances.append(dict(b=b,d=d,n=n,K=K,m=m,D=D,c=c,alpha_power_two_exponent=v,omega_hex=row['omega_hex'],core_rule='alpha^i*omega^j for 2<=i<=m+1 and 0<=j<d',extra_rule='alpha^i for m+2<=i<=m+c+1',padding_rule='omega^j for 0<=j<d',direction='one on padding, zero elsewhere',reference_support=ref,nearby_count=str(J),witnesses=witnesses))
  print(f'REPLAY PASSED b={b} d={d} n={n}',flush=True)
 (BASE/'kummer_instances.json').write_text(json.dumps(instances,indent=2)+'\n')
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,scope='Deterministic specific-domain certificates with supplied certified roots. No random coverage event, global list upper bound, or prescribed FFT-domain assertion.')
 (BASE/'kummer_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
