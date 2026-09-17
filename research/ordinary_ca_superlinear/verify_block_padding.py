"""Complete support censuses over independently implemented F_(7^4), F_(7^6)."""
from itertools import combinations
from math import comb
from pathlib import Path
import json
import sympy as sp

class Field:
 def __init__(self,p,degree):
  self.p=p;self.d=degree;self.order=p**degree
  X=sp.symbols('X')
  for a in range(p):
   for b in range(1,p):
    f=sp.Poly(X**degree+a*X+b,X,modulus=p)
    if f.is_irreducible:
     self.mod=[int(f.nth(j))%p for j in range(degree)];break
   else:continue
   break
  else:raise AssertionError('no sparse irreducible found')
  self.zero=(0,)*degree;self.one=(1,)+(0,)*(degree-1)
  self.T=(0,1)+(0,)*(degree-2)
 def scalar(self,a):return (a%self.p,)+(0,)*(self.d-1)
 def add(self,a,b):return tuple((x+y)%self.p for x,y in zip(a,b))
 def sub(self,a,b):return tuple((x-y)%self.p for x,y in zip(a,b))
 def mul(self,a,b):
  p=self.p;d=self.d;c=[0]*(2*d-1)
  for i,x in enumerate(a):
   for j,y in enumerate(b):c[i+j]+=x*y
  for j in range(2*d-2,d-1,-1):
   z=c[j]%p
   if z:
    for h,m in enumerate(self.mod):c[j-d+h]-=z*m
  return tuple(x%p for x in c[:d])
 def power(self,a,e):
  z=self.one
  while e:
   if e&1:z=self.mul(z,a)
   a=self.mul(a,a);e//=2
  return z
 def inv(self,a):
  assert a!=self.zero
  z=self.power(a,self.order-2);assert self.mul(a,z)==self.one
  return z

def census(F,xs,ys,K):
 n=len(xs);inverses={(i,j):F.inv(F.sub(xs[i],xs[j])) for i in range(n) for j in range(n) if i!=j}
 maximum=0;hits=0;bank=set();count=0
 for support in combinations(range(n),K):
  c=[ys[j] for j in support]
  for h in range(1,K):
   for i in range(K-1,h-1,-1):c[i]=F.mul(F.sub(c[i],c[i-1]),inverses[support[i],support[i-h]])
  values=[]
  for x in xs:
   v=c[-1]
   for h in range(K-2,-1,-1):v=F.add(F.mul(v,F.sub(x,xs[support[h]])),c[h])
   values.append(v)
  agreements=sum(a==b for a,b in zip(values,ys));count+=1
  if agreements>maximum:maximum=agreements;hits=0;bank=set()
  if agreements==maximum:hits+=1;bank.add(tuple(values))
 assert count==comb(n,K) and hits==len(bank)*comb(maximum,K)
 return dict(length=n,dimension=K,determining_subsets=count,maximum=maximum,nearest_list=len(bank))

F=Field(7,4)
D=[F.scalar(x) for x in range(1,5)];w=[F.scalar(pow(x,-1,7)) for x in range(1,5)]
source=census(F,D,w,2);assert source['maximum']==2
newcoords=[F.scalar(x) for x in (0,5,6)]
newvalues=[F.power(F.T,j) for j in (1,2,3)]
noise=census(F,D+newcoords,w+newvalues,2);assert noise['maximum']==2
noise_row=dict(prime=7,degree=4,modulus_coefficients_low_to_high=F.mod+[1],source=source,result=noise,new_values=newvalues)

F=Field(7,6)
D=[F.scalar(x) for x in range(1,7)];s=2;a=F.power(F.T,s)
assert a!=F.scalar(a[0])
zeros=[]
for variant,newcoords in [('roots_of_unity',[F.T,F.sub(F.zero,F.T)]),('translates',[F.T,F.add(F.T,F.one)])]:
 assert len(set(D+newcoords))==8
 def locator(x):
  z=F.one
  for a0 in newcoords:z=F.mul(z,F.sub(x,a0))
  return z
 for ones in (3,2):
  w=[F.zero]*(6-ones)+[F.one]*ones
  source=census(F,D,w,2);M=source['maximum']
  assert s<=M-2+1
  transformed=[F.mul(locator(x),y) for x,y in zip(D,w)]+[F.zero]*s
  out=census(F,D+newcoords,transformed,2+s)
  assert out['maximum']==M+s
  for value in (F.zero,F.one):
   if sum(y==value for y in w)==M:
    lifted=[F.mul(locator(x),value) for x in D+newcoords]
    assert sum(x==y for x,y in zip(lifted,transformed))==M+s
  zeros.append(dict(variant=variant,source=source,result=out))
zero_row=dict(prime=7,degree=6,modulus_coefficients_low_to_high=F.mod+[1],block_size=s,minimal_degree_required=2+2*s,fixtures=zeros)

cases=0
for r in range(40,2501):
 for m in sorted({(3*r+1)//2,7*r//4,2*r}):
  Delta=m-r+1;u=13*Delta-3*r;s=2*Delta-r-1;n=16*Delta
  assert 1<=s<=Delta and r+2+s==2*Delta+1 and m+2+s==3*Delta
  D=r+2+2*s
  degree_bound=8*(u+1)*D
  assert degree_bound<=8*(10*r+14)*(3*r+4)<4*(8*r+16)**2<=4*n*n
  assert (4*r+1)**4>=2*(15*Delta+1)*r
  cases+=1
result=dict(status='passed',noise_block=noise_row,common_zero_block=zero_row,field_degree_parameter_cases=cases,scope='Complete determining-support censuses, not random search. Field irreducibility checked by SymPy; all node-difference inverses checked using independent tuple arithmetic. Asymptotic conclusions use the separately written algebraic proof.')
Path(__file__).with_name('block_padding_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
