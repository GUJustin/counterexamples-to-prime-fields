"""Independent exact replay of orbit parameters, roots, and unique witnesses."""
from pathlib import Path
from fractions import Fraction
from math import comb,isqrt,prod
import hashlib,json,random,time
BASE=Path(__file__).resolve().parent

def decode(t,m,D,d):
 if t<1:return None
 if t==1:s=0
 elif t.bit_length()%d:return None
 else:s=t.bit_length()//d
 if s>m*(m+1)//2:return None
 u=Fraction(t,1<<(d*s));I=[]
 for i in range(1,m+1):
  factor=Fraction((1<<(d*i))-1,1<<(d*i))
  if u<=factor:u/=factor;I.append(i)
 if u!=1 or len(I)!=D:return None
 if prod((1<<(d*i))-1 for i in I)!=t:return None
 return I

def polynomial(I,d,p):
 out=[1]
 for i in I:
  root=1<<(d*i);new=[0]*(len(out)+1)
  for j,a in enumerate(out):new[j]=(new[j]-root*a)%p;new[j+1]=(new[j+1]+a)%p
  out=new
 return out

def evaluate(c,y,p):
 v=0
 for a in reversed(c):v=(v*y+a)%p
 return v

if __name__=='__main__':
 start=time.monotonic();source=json.loads((BASE/'parameters.json').read_text())['rows'];roots=json.loads((BASE/'roots.json').read_text())['rows'];rng=random.Random(20260917);rows=[];instances=[]
 for row,root in zip(source,roots):
  b=row['b'];d=row['d'];p=(1<<b)-1;m=row['m'];D=row['D'];c=row['extra_coordinates'];n=row['n'];K=row['K']
  assert (root['b'],root['d'])==(b,d)
  assert all(b%j for j in range(2,isqrt(b)+1)) and all(d%j for j in range(2,isqrt(d)+1))
  # Independent placement of the subtraction in the Mersenne reduction.
  s=4
  for _ in range(b-2):
   square=s*s;s=(square&p)+(square>>b)-2
   if s<0:s+=p
   elif s>=p:s-=p
  assert s==0
  assert (p-1)%d==0 and 1<=D<m and 0<=c<d and n==d*(m+1)+c and K==d*D-1 and n==2*K
  A=(1<<(m+1))*(d+(1<<c));E=d*D*(2*m-D+1)//2
  assert p>A**(d-1) and p>1<<E
  J=comb(m,D);assert str(J)==row['nearby_count']
  w=row['ratio_greater_than_power_two'];assert J**(d+1)>n**(d+1)*(1<<(n+w*(d+1)))
  assert (d+1)*(b-1)>n
  omega=int(root['omega_hex'],16);assert 1<omega<p and pow(omega,d,p)==1
  assert hashlib.sha256(omega.to_bytes((b+7)//8,'big')).hexdigest()==root['sha256']
  op=[pow(omega,j,p) for j in range(d)]
  domain=[((1<<i)*v)%p for i in range(1,m+1) for v in op]+[1<<(m+t) for t in range(1,c+1)]+op
  assert len(domain)==len(set(domain))==n
  reference=list(range(1,D+1));F=polynomial(reference,d,p);assert len(F)==D+1 and F[-1]==1
  witnesses=[]
  for trial in range(16):
   I=sorted(rng.sample(range(1,m+1),D));T=prod((1<<(d*i))-1 for i in I)
   assert T<p and decode(T,m,D,d)==I
   z=(T if D%2 else -T)%p
   if trial<2:
    H=polynomial(I,d,p);Q=[(a-bb)%p for a,bb in zip(F,H)];assert Q[-1]==0 and d*(len(Q)-2)<K
    agreements=0
    for i in range(1,m+1):agreements+=d*(evaluate(F,1<<(d*i),p)==evaluate(Q,1<<(d*i),p))
    for t in range(1,c+1):agreements+=evaluate(F,1<<(d*(m+t)),p)==evaluate(Q,1<<(d*(m+t)),p)
    agreements+=d*((evaluate(F,1,p)+z)%p==evaluate(Q,1,p))
    assert agreements==K+d+1
    witnesses.append(dict(parameter_hex=hex(z),support=I,polynomial_in_X_to_d_coefficients_hex=[hex(v) for v in Q[:-1]]))
  for _ in range(16):
   T=rng.randrange(1,p);I=decode(T,m,D,d)
   if I is not None:assert prod((1<<(d*i))-1 for i in I)==T
  instances.append(dict(b=b,prime_form='2^b-1',d=d,omega_hex=root['omega_hex'],n=n,K=K,m=m,D=D,c=c,
   core_rule='2^i*omega^j for 1<=i<=m, 0<=j<d',extra_rule='2^(m+t) for 1<=t<=c',padding_rule='omega^j for 0<=j<d',
   reference_support=reference,direction='one on padding, zero elsewhere',exact_nearby_count=str(J),witnesses=witnesses))
  rows.append(dict(b=b,d=d,n=n,K=K,nearby_count=str(J),separation=f'{d}/{d+1}',ratio_greater_than_power_two=w,
   certified_root=True,distinct_domain_points=n,decoded_support_tests=16,explicit_witnesses_checked=2))
  print('PASS b='+str(b)+' d='+str(d),flush=True)
 (BASE/'instances.json').write_text(json.dumps(instances,indent=2)+'\n')
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,
  scope='Deterministic classification and decoding given the saved certified roots. Root search is zero-error; no coverage success event is assumed. No global list-size or prescribed-domain claim.')
 (BASE/'independent_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
