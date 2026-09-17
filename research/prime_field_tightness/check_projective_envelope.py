"""Independent exact checks of projective-pencil and cross-ratio lemmas."""
from itertools import product
from pathlib import Path
from random import Random
import json
p=101

def trim(a):
 a=[x%p for x in a]
 while len(a)>1 and not a[-1]:a.pop()
 return tuple(a or [0])
def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def sc(a,c):return trim([c*x for x in a])
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def div(a,b):
 assert b!=(0,)
 a=list(trim(a));q=[0]*max(1,len(a)-len(b)+1)
 while tuple(a)!=(0,) and len(a)>=len(b):
  k=len(a)-len(b);v=a[-1]*pow(b[-1],-1,p)%p;q[k]=v
  for i,x in enumerate(b):a[i+k]=(a[i+k]-v*x)%p
  a=list(trim(a))
 return trim(q),trim(a)
def gcd(a,b):
 while b!=(0,):a,b=b,div(a,b)[1]
 return sc(a,pow(a[-1],-1,p))
def ev(a,x):
 y=0
 for v in reversed(a):y=(y*x+v)%p
 return y
def loc(xs):
 a=(1,)
 for x in xs:a=mul(a,(-x,1))
 return a

def members(a,b,c,d,D):
 out=[]
 for z in list(range(p))+[None]:
  num=a if z is None else add(sc(a,z),b)
  den=c if z is None else add(sc(c,z),d)
  if den==(0,):continue
  q,r=div(num,den)
  if r==(0,) and len(q)-1<=D:out.append((z,q))
 return out

rng=Random(20260917);fixtures=0;finite_cases=0;affine_cases=0
for prime in (7,11,101):
 p=prime
 for D in range(1,6):
  for _ in range(100):
   ps=[trim([rng.randrange(p) for i in range(D+1)]) for j in range(3)]
   if len(set(ps))<3:continue
   P0,P1,Pi=ps;A=add(P1,sc(Pi,-1));B=add(P1,sc(P0,-1));g=gcd(A,B)
   Ap=div(A,g)[0];Bp=div(B,g)[0]
   a=sc(mul(Pi,Bp),-1);b=mul(P0,Ap);c=sc(Bp,-1);d=Ap
   vals=members(a,b,c,d,D)
   assert len(vals)>=3 and len({q for z,q in vals})==len(vals)
   if len(Ap)==len(Bp)==1:affine_cases+=1
   else:
    finite_cases+=1;assert len(vals)<=D+2,(p,D,ps,vals)
   fixtures+=1
p=101
sharp=[]
for D in range(0,13):
 R=loc(range(1,D+2));vals=members(R,(0,),(0,1),(-1,),D)
 assert len(vals)==D+2
 sharp.append(dict(D=D,members=len(vals)))
# Exhaust all projective quadruples, including infinity and repeated values.
quadruples=0
for prime in (5,7):
 p=prime;pts=[(x,1) for x in range(p)]+[(1,0)];zs=(0,1,2,3)
 def wedge(a,b):return (a[0]*b[1]-a[1]*b[0])%p
 def coherent(w):
  return (wedge(w[0],w[2])*wedge(w[1],w[3])*(zs[0]-zs[3])*(zs[1]-zs[2])-wedge(w[0],w[3])*wedge(w[1],w[2])*(zs[0]-zs[2])*(zs[1]-zs[3]))%p==0
 for triple in product(pts,repeat=3):
  allowed=[v for v in pts if coherent(triple+(v,))]
  s=set(triple)
  if len(s)==3:assert len(allowed)==1
  elif len(s)==2:assert allowed==[next(x for x in s if triple.count(x)==2)]
  else:assert allowed==pts
  quadruples+=len(pts)
# Check the fourth-incidence lower inequality at the integer boundary.
for b in range(100):assert b*(b-1)*(b-2)*(b-3)>=max(b-3,0)**4
result=dict(status='passed',projective_pencil_fixtures=fixtures,finite_member_cases=finite_cases,
 affine_reparameterization_cases=affine_cases,sharp_polynomial_member_examples=sharp,
 projective_quadruples=quadruples,
 scope='Polynomial division over three prime fields; sharp D+2 examples; exhaustive cross-ratio degeneracies including infinity; integer fourth-incidence inequality. These checks supplement the universal written argument.')
Path(__file__).with_name('projective_envelope_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
