"""Exact fixed-rate/gap examples for rational-path rigidity."""
from pathlib import Path
import json
p=1009

def ev(a,x):
 y=0
 for v in reversed(a):y=(y*x+v)%p
 return y
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return c
def locator(xs):
 q=[1]
 for x in xs:q=mul(q,[-x%p,1])
 return q
def newton(xs,ys):
 co=list(ys)
 for j in range(1,len(xs)):
  for i in range(len(xs)-1,j-1,-1):co[i]=(co[i]-co[i-1])*pow((xs[i]-xs[i-j])%p,-1,p)%p
 def value(x):
  out=co[-1]
  for i in range(len(co)-2,-1,-1):out=(out*(x-xs[i])+co[i])%p
  return out
 return value

rows=[]
for n in (160,320,640):
 K=n//4;D=K-1;A=3*n//8;t=A-D;J=10
 roots=list(range(1,K+1));domain=list(range(1,n+1));R=locator(roots)
 bank={0:[0]}
 for a in roots:bank[pow(a,-1,p)]=locator([b for b in roots if b!=a])
 f={x:0 for x in roots};g={x:0 for x in roots};assigned={}
 pos=K+1
 for a in range(1,J+1,2):
  b=a+1;za=pow(a,-1,p);zb=pow(b,-1,p);assigned[a]=[];assigned[b]=[]
  for _ in range(t):
   x=pos;pos+=1;va=ev(bank[za],x);vb=ev(bank[zb],x)
   g[x]=(va-vb)*pow((za-zb)%p,-1,p)%p;f[x]=(va-za*g[x])%p
   assigned[a].append(x);assigned[b].append(x)
 for x in range(pos,n+1):
  forbidden={ev(P,x) for P in bank.values()};v=next(v for v in range(p) if v not in forbidden)
  f[x]=v;g[x]=0
 assert len(f)==n and t>=2 and (A-K)*8==n
 near=[];counts={}
 for z,P in bank.items():
  support=[x for x in domain if ev(P,x)==(f[x]+z*g[x])%p]
  counts[z]=len(support)
  if len(support)>=A:
   assert len(support)==A
   G=newton(support[:K],[g[x] for x in support[:K]])
   assert any(G(x)!=g[x] for x in support)
   near.append(z)
 assert set(near)=={pow(a,-1,p) for a in range(1,J+1)}
 assert counts[0]==K and all(counts[pow(a,-1,p)]==D for a in roots[J:])
 # Persistent-coordinate ledger for T=R Z/(XZ-1).
 persistent=[];nonpersistent_incidences=0
 for x in domain:
  coeff=[f[x],(ev(R,x)-x*f[x]+g[x])%p,(-x*g[x])%p]
  if all(c%p==0 for c in coeff):
   persistent.append(x)
   assert sum(ev(bank[z],x)!=(f[x]+z*g[x])%p for z in near)<=1
  else:
   incidences=sum(ev(bank[z],x)==(f[x]+z*g[x])%p for z in near)
   assert incidences<=2;nonpersistent_incidences+=incidences
 assert persistent==roots and nonpersistent_incidences==J*t
 rows.append(dict(n=n,K=K,D=D,A=A,rate='1/4',capacity_gap='1/8',path_polynomial_members=len(bank),
  nearby_labels=len(near),all_nearby_path_labels_full_support_bad=True,persistent_coordinates=len(persistent),
  nonpersistent_incidences=nonpersistent_incidences,unused_padding=n-K-J*t//2))
result=dict(status='passed',prime=p,fixtures=rows,
 scope='Complete polynomial-member bank and all agreement supports for the specified rational path; exact full-support badness by independent interpolation. Does not enumerate all codewords of the ambient RS code.')
Path(__file__).with_name('rational_path_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
