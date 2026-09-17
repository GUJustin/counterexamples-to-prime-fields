"""Independent finite proof checks and rational witness recovery.

The product decoder uses exact fractions, independently of check.py's
integer comparisons. The construction itself is deterministic.
"""
from pathlib import Path
from fractions import Fraction
from math import comb,isqrt,prod
import json,random,time
BASE=Path(__file__).resolve().parent

def support_from_product(t,m,D):
 if t<1:return None
 if t==1:s=0
 else:s=(t.bit_length()+1)//2
 if s>m*(m+1)//2:return None
 u=Fraction(t,1<<(2*s))
 if not Fraction(2,3)<u<=1:return None
 out=[]
 for i in range(1,m+1):
  factor=Fraction((1<<(2*i))-1,1<<(2*i))
  if u<=factor:u/=factor;out.append(i)
 if u!=1 or len(out)!=D:return None
 if prod((1<<(2*i))-1 for i in out)!=t:return None
 return out

def locator(roots,p):
 c=[1]
 for a in roots:
  out=[0]*(len(c)+2)
  for i,v in enumerate(c):out[i]=(out[i]-a*a*v)%p;out[i+2]=(out[i+2]+v)%p
  c=out
 return c

def value(c,x,p):
 y=0
 for a in reversed(c):y=(y*x+a)%p
 return y

if __name__=='__main__':
 start=time.monotonic();rows=[];instances=[];rng=random.Random(20260917)
 for b,m,D,w in [(521,36,8,0),(1279,40,21,3),(2203,52,27,6),(9689,112,57,25)]:
  assert all(b%j for j in range(2,isqrt(b)+1));p=(1<<b)-1;ll=4
  for _ in range(b-2):ll=(ll*ll-2)%p
  assert ll==0
  n=2*m+2;K=2*D-1;J=comb(m,D);E=D*(2*m-D+1)
  assert p>1<<E and p>(1<<(m+1))-2
  assert J**3*K**K*(n-K)**(n-K)>(1<<(3*w))*n**(n+3)
  assert 3*(b-1)>n
  extra=m*(m+1)//2+2*m+2;two_level=p>1<<extra
  assert two_level==(b!=521)
  reps=[1<<i for i in range(1,m+1)];domain=[x for a in reps+[1] for x in (a,p-a)]
  ref=locator(reps[:D],p);f=[value(ref,x,p) for x in domain];g=[0]*(2*m)+[1,1]
  assert len(ref)==K+2 and ref[-1]==1 and ref[-2]==0 and sum(a==0 for a in f)==K+1
  witnesses=[]
  for trial in range(64):
   I=sorted(rng.sample(range(1,m+1),D));t=prod((1<<(2*i))-1 for i in I)
   assert t<p and support_from_product(t,m,D)==I
   z=(t if D%2 else -t)%p
   H=locator([1<<i for i in I],p);q=[(a-c)%p for a,c in zip(ref,H)]
   assert q[K:]==[0,0]
   if trial<3:
    assert sum((a+z*c)%p!=value(q,x,p) for a,c,x in zip(f,g,domain))==n-K-3
    witnesses.append(dict(parameter=str(z),support=I,polynomial_coefficients=[str(a) for a in q[:K]]))
  for _ in range(64):
   t=rng.randrange(1,p);I=support_from_product(t,m,D)
   if I is not None:assert prod((1<<(2*i))-1 for i in I)==t
  rows.append(dict(b=b,n=n,K=K,m=m,D=D,nearby_count=str(J),ratio_greater_than_power_two=w,
   no_wrap_exponent=E,two_level_exponent=extra,two_level=two_level,decoded_support_tests=64))
  if b==1279:
   instances.append(dict(p=str(p),n=n,K=K,domain=[str(x) for x in domain],f=[str(x) for x in f],g=g,
    exact_nearby_parameters=str(J),nearby_distance_numerator=n-K-3,other_distance_numerator=n-K-1,witnesses=witnesses))
 (BASE/'deterministic_instance.json').write_text(json.dumps(instances[0],indent=2)+'\n')
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,
  scope='Deterministic domains and complete mathematical classification of nearby parameters, not a sampling guarantee. Exact rational support recovery is independently replayed.')
 (BASE/'independent_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
