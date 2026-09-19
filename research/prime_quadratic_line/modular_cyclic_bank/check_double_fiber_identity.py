"""Independent exact finite-field replay of the h+2 double-fiber criterion."""
import json
from itertools import product
cases=[]
for p,n,h in [(17,16,2),(17,16,4),(17,16,8),(29,28,4),(29,28,7)]:
 r=n//h
 D=[x for x in range(1,p) if pow(x,n,p)==1]
 omegas=[x for x in range(1,p) if pow(x,h,p)==1 and x not in (1,p-1)]
 count=0
 for a,b,c in product(range(1,6),repeat=3):
  fibers={}
  for x in D:
   if pow(x,h+2,p)==(a*x*x+b*x+c)%p:
    z=pow(x,h,p); fibers[z]=fibers.get(z,0)+1
  direct=sum(v==2 for v in fibers.values())
  K=pow(-c*pow(b,-1,p)%p,h,p); B=b*b*pow(c,-1,p)%p
  valid=[]
  for w in omegas:
   v=(1+w)%p
   H1=(K*pow(v,h+2,p)-a*v*v+B*w)%p
   H2=(pow((a*v*v-B*w)%p,r,p)-pow(v,2*r,p))%p
   if H1==H2==0: valid.append(w)
  assert len(valid)==2*direct,(p,n,h,a,b,c,valid,fibers)
  assert all(pow(w,-1,p) in valid for w in valid)
  count+=1
 cases.append(dict(p=p,n=n,h=h,coefficients_checked=count))
print(json.dumps(dict(status='PASS',cases=cases,total=sum(c['coefficients_checked'] for c in cases)),indent=2))
