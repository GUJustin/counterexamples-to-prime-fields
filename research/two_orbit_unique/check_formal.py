"""Finite-characteristic audits of the formal-series and rotation arguments."""
from pathlib import Path
from itertools import product,combinations
from math import comb,prod
import json,time
BASE=Path(__file__).resolve().parent

def convolution(a,b,p,N):
 r=[0]*(N+1)
 for i,x in enumerate(a):
  for j,y in enumerate(b[:N+1-i]):r[i+j]=(r[i+j]+x*y)%p
 return r

def power(a,d,p,N):
 r=[1]+[0]*N
 for _ in range(d):r=convolution(r,a,p,N)
 return r

def branch(i,d,p,N):
 # Solve B_i^d=(1-x^(i+1))/(1-x^i) coefficient by coefficient.
 rhs=[0]*(N+1)
 for h in range(0,N+1,i):rhs[h]+=1
 for h in range(i+1,N+1,i):rhs[h]-=1
 rhs=[x%p for x in rhs];a=[1]+[0]*N
 for h in range(1,N+1):a[h]=(rhs[h]-power(a,d,p,N)[h])*pow(d,-1,p)%p
 assert power(a,d,p,N)==rhs
 assert a[1:i]==[0]*(i-1) and a[i]==pow(d,-1,p)
 return a

def audit(p,d,M):
 assert (p-1)%d==0 and p>d**(d-1)
 omega=next(pow(h,(p-1)//d,p) for h in range(2,p) if pow(h,(p-1)//d,p)!=1)
 mu=[pow(omega,j,p) for j in range(d)]
 masks=set(range(1,2**d-1));classes=[]
 while masks:
  mask=min(masks);orbit={sum(1<<((i+j)%d) for i in range(d) if mask>>i&1) for j in range(d)}
  assert len(orbit)==d and orbit<=masks;masks-=orbit;classes.append(orbit)
 assert len(classes)==(2**d-2)//d
 coeff=sorted({sum(mu[j] for j in range(d) if mask>>j&1)%p for mask in range(1,2**d-1)})
 assert 0 not in coeff
 branches=[branch(i,d,p,M+2) for i in range(1,M+1)]
 checked=0
 for C in product([0]+coeff,repeat=M):
  if not any(C):continue
  series=[sum(c*a[h] for c,a in zip(C,branches))%p for h in range(M+3)]
  if sum(C)%p:assert series[0]!=0
  else:
   first=next(i for i,c in enumerate(C,1) if c)
   assert series[:first]==[0]*first and series[first]==C[first-1]*pow(d,-1,p)%p
  assert any(series);checked+=1
 T=M*(M+1)//2
 degree_sum=sum(comb(M,u)*len(classes)**u*d**u*(T+1) for u in range(1,M+1))
 assert degree_sum==(T+1)*((2**d-1)**M-1)
 # Distinct support products are distinct even in small characteristic:
 # this check is independent of p and uses full coefficient vectors.
 polynomials=0
 for char in (2,3,5,7):
  m=12
  for D in range(1,7):
   seen=set()
   for I in combinations(range(1,m+1),D):
    a=[1]
    for i in I:
     new=[0]*(len(a)+i)
     for j,v in enumerate(a):new[j]=(new[j]-v)%char;new[j+i]=(new[j+i]+v)%char
     a=new
    assert tuple(a) not in seen;seen.add(tuple(a));polynomials+=1
 return dict(p=p,d=d,M=M,rotation_classes=len(classes),nonzero_series_checked=checked,
  exact_rotation_degree_sum=str(degree_sum),distinct_product_polynomials=polynomials)

if __name__=='__main__':
 start=time.monotonic();rows=[audit(1009,2,7),audit(1009,3,4),audit(65521,5,3)]
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,
  scope='Formal-series leading terms, subset rotation counts, and product polynomial injectivity. These are proof audits, not numerical violation examples.')
 (BASE/'formal_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
