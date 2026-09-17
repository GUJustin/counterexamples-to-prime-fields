"""Exact small-field checks for the rational-envelope incidence proof."""
from itertools import combinations
from pathlib import Path
import json
P=101

def trim(a):
 a=list(a)
 while len(a)>1 and a[-1]%P==0:a.pop()
 return tuple(x%P for x in a)
def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def scale(a,c):return trim([c*x for x in a])
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def ev(a,x):
 y=0
 for v in reversed(a):y=(y*x+v)%P
 return y
def locator(xs):
 a=(1,)
 for x in xs:a=mul(a,(-x,1))
 return a
def interpolate(xs,ys):
 out=(0,)
 for i,x in enumerate(xs):
  basis=locator([y for j,y in enumerate(xs) if j!=i]);den=ev(basis,x)
  out=add(out,scale(basis,ys[i]*pow(den,-1,P)))
 return out

rootset=tuple(range(1,5));R=locator(rootset);domain=tuple(range(20));D=4
bank=[]
for B in combinations(rootset,2):
 for c in (1,2):
  den=locator(B);num=(c,1);poly=mul(locator([x for x in rootset if x not in B]),num)
  bank.append((poly,num,den))
triples=0;noncollinear=0
for ids in combinations(range(len(bank)),3):
 z0,z1,z2=ids;coeff=(z1-z2,z2-z0,z0-z1)
 polydet=(0,);numerator=(0,)
 for j,k in enumerate(ids):
  polydet=add(polydet,scale(bank[k][0],coeff[j]))
  term=bank[k][1]
  for l,k2 in enumerate(ids):
   if l!=j:term=mul(term,bank[k2][2])
  numerator=add(numerator,scale(term,coeff[j]))
 assert (polydet==(0,))==(numerator==(0,))
 assert len(numerator)-1<=6
 if numerator!=(0,):
  zeros=[x for x in range(P) if ev(R,x)!=0 and ev(polydet,x)==0]
  assert len(zeros)<=6;noncollinear+=1
 triples+=1
# A full pencil realizes a linear number of genuinely bad labels.
A=8;persistent=set(range(A-1));outside=set(domain)-persistent
f={x:0 if x in persistent else -x%P for x in domain}
g={x:(ev(R,x)+(x not in persistent))%P for x in domain}
bad=[]
for z in range(P):
 q=scale(R,z);support=[x for x in domain if ev(q,x)==(f[x]+z*g[x])%P]
 if len(support)<A:continue
 G=interpolate(support[:D+1],[g[x] for x in support[:D+1]])
 assert any(ev(G,x)!=g[x] for x in support)
 bad.append(z)
assert set(bad)==outside and len(bad)==len(domain)-A+1
# All selected bad points are collinear, and each is charged to one coordinate.
assert len(bad)<=len(domain)
for z in bad:
 accidents=[x for x in domain if ev(scale(R,z),x)==(f[x]+z*g[x])%P and (f[x]!=0 or g[x]!=ev(R,x))]
 assert accidents==[z]
# Integer incidence inequalities, including small-count boundary cases.
for b in range(100):assert b*(b-1)*(b-2)>=max(b-2,0)**3
result=dict(status='passed',prime=P,rational_triples=triples,noncollinear_triples=noncollinear,
 pencil=dict(n=len(domain),D=D,A=A,bad_labels=bad,expected=len(domain)-A+1),
 scope='Exact rational determinant degree/zero checks, all field labels and full supports for a linear bad-pencil family, and integer triple-incidence inequalities. Supplements the proof; not a proof of the universal theorem.')
Path(__file__).with_name('rational_envelope_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
