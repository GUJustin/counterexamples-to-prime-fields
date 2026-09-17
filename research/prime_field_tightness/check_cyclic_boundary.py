"""Exact general-order cyclic moment classes and split-prime transfer checks."""
from itertools import combinations
from math import gcd,isqrt,lcm
from fractions import Fraction
from pathlib import Path
import json

def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def exact_div(a,b):
 a=list(a);q=[0]*(len(a)-len(b)+1)
 for i in range(len(q)-1,-1,-1):
  v=a[i+len(b)-1];q[i]=v
  for j,x in enumerate(b):a[i+j]-=v*x
 assert not any(a)
 return q
def divisors(n):return [d for d in range(1,n+1) if n%d==0]
def phi(n):return sum(gcd(i,n)==1 for i in range(1,n+1))
phis={}
def cyclotomic(n):
 if n not in phis:
  a=[-1]+[0]*(n-1)+[1]
  for d in divisors(n)[:-1]:a=exact_div(a,cyclotomic(d))
  phis[n]=a
 return phis[n]
def powers_mod(poly,n):
 degree=len(poly)-1;v=[1]+[0]*(degree-1);out=[]
 for _ in range(n):
  out.append(v[:]);v=[0]+v;top=v.pop()
  v=[a-top*b for a,b in zip(v,poly[:-1])]
 return out
def prime(n):
 if n<2:return False
 if n%2==0:return n==2
 return all(n%d for d in range(3,isqrt(n)+1,2))
def prime_above(n,orders):
 lower=2
 for N,R in orders:
  # Exact integer ceiling threshold by monotone doubling and bisection.
  target=n**phi(N);lo=1;hi=2
  while hi**R<=target:hi*=2
  while hi-lo>1:
   mid=(hi+lo)//2
   if mid**R>target:hi=mid
   else:lo=mid
  lower=max(lower,hi)
 p=((lower-1+n-1)//n)*n+1
 while not prime(p):p+=n
 assert all(p**R>n**phi(N) for N,R in orders)
 return p
def primitive_root_order(n,p):
 primes=[q for q in divisors(n)[1:] if prime(q)]
 for a in range(2,p):
  w=pow(a,(p-1)//n,p)
  if pow(w,n,p)==1 and all(pow(w,n//q,p)!=1 for q in primes):return w
 raise AssertionError('no root')

rows=[]
for n,A,s in ((6,3,1),(10,5,2),(12,6,3),(15,7,3),(18,9,4),(20,10,4)):
 allowed=[q for q in divisors(n) if q*s<n];M=sum(phi(q) for q in allowed);Q=lcm(*allowed)
 G=[-1,1]
 for q in divisors(n):
  if q*s>=n:G=mul(G,cyclotomic(q))
 assert len(G)-1==n-M+1
 vecs=powers_mod(G,n);C=max(abs(x) for v in vecs for x in v);base=2*n*C+1
 encoded=[sum(x*base**j for j,x in enumerate(v)) for v in vecs]
 classes={};subsets=0
 for support in combinations(range(n),A):
  key=sum(encoded[i] for i in support);mask=sum(1<<i for i in support)
  if key not in classes:classes[key]=[1,mask]
  else:
   classes[key][0]+=1;old=classes[key][1]
   delta=[((mask>>i)&1)-((old>>i)&1) for i in range(n)]
   assert all(delta[i]==delta[(i+Q)%n] for i in range(n))
  subsets+=1
 maximum=max(v[0] for v in classes.values());assert maximum<=2**(M-1)
 orders=[]
 for d in divisors(n):
  if d<=s:
   N=n//d;R=sum(gcd(u,N)==1 for u in range(1,s//d+1));orders.append((N,R))
 E=max(Fraction(phi(N),R) for N,R in orders)
 assert E<=125*Fraction(n,s)**3
 p=prime_above(n,orders);w=primitive_root_order(n,p)
 moment_vectors=[tuple(pow(w,i*j,p) for j in range(1,s+1)) for i in range(n)]
 finite={}
 for support in combinations(range(n),A):
  key=tuple(sum(moment_vectors[i][j] for i in support)%p for j in range(s))
  exact=sum(encoded[i] for i in support)
  if key in finite:
   assert finite[key][1]==exact;finite[key][0]+=1
  else:finite[key]=[1,exact]
 assert len(finite)==len(classes) and max(v[0] for v in finite.values())==maximum
 rows.append(dict(n=n,A=A,s=s,subsets=subsets,allowed_character_orders=allowed,dimension=M-1,
  period_bound=Q,list_upper=2**(M-1),actual_maximum_list=maximum,prime=p,root=w,
  exact_transfer_exponent=str(E),finite_classes=len(finite)))
 print(json.dumps(rows[-1]),flush=True)
# Exact small-N check of the uniform fixed-gap exponent estimate.
count=0
for N in range(2,301):
 ph=phi(N);R=0
 for m in range(1,N):
  R+=gcd(m,N)==1
  assert Fraction(ph,R)<=125*Fraction(N,m)**3
  count+=1
result=dict(status='passed',fixtures=rows,uniform_exponent_checks=count,
 scope='Complete subset classes on six composite/prime-power orders, exact cyclotomic linear dimension, periodic differences, and independent finite-field moment classes above the norm threshold. The proof, not these tests, establishes the universal theorem.')
Path(__file__).with_name('cyclic_boundary_verification.json').write_text(json.dumps(result,indent=2)+'\n')
