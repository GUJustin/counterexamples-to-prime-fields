#!/usr/bin/env python3
from pathlib import Path
import json
checks=0
for n in range(3,501):
 for k in range(1,n-1):
  a=n-k;L=a-1
  assert (L+1)*(a-1)==L*a
  # Sufficient bound 2*L*k < 2^((7a-1)n), without huge powers.
  assert (2*L*k).bit_length() <= (7*a-1)*n
  # Distinct-subset-sum failure upper bound below 2^(-2an).
  assert 2*n-1-10*a*n < -2*a*n
  # p>k 2^(10an)>n^2, and log2(p)>n.
  assert (n*n).bit_length() <= 10*a*n
  checks+=1
p=101
fixtures=0;witnesses=0;coordinate_checks=0
def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
 return out
def vp(roots):
 f=[1]
 for z in roots:f=mul(f,[-z%p,1])
 return f
def ev(f,x):
 y=0
 for c in reversed(f):y=(y*x+c)%p
 return y
for n in range(4,31):
 for k in range(1,n-1):
  a=n-k;L=a-1;h=k-a+2
  if h<0:continue
  D=list(range(n)); A=D[:h]; al=D[h:h+L];be=D[h+L:]
  assert len(be)==L
  F=vp(A);polys=[]
  for i in range(L):
   vv=vp(al[:i]+al[i+1:]);rr=[(-c)%p for c in vv]
   rr[-1]=(rr[-1]+1)%p
   while len(rr)>1 and rr[-1]==0:rr.pop()
   q=mul(F,rr)
   while len(q)>1 and q[-1]==0:q.pop()
   assert len(q)<=k
   polys.append(q)
  w={x:0 for x in A}
  for x in al:w[x]=ev(F,x)*pow(x,L-1,p)%p
  for i,x in enumerate(be):w[x]=ev(polys[i],x)
  enc=[tuple(ev(q,x) for x in D) for q in polys]
  assert len(set(enc))==L
  for row in enc:
   assert sum(row[x]==w[x] for x in D)>=k+1
   coordinate_checks+=n
  witnesses+=L;fixtures+=1
out={'parameter_inequality_checks':checks,'sharpness_fixtures':fixtures,
     'distinct_lower_bound_witnesses':witnesses,'coordinate_checks':coordinate_checks,
     'status':'passed','scope':'Checks parameter arithmetic and explicit global-list lower-bound witnesses; generic-rank upper bound remains a cited theorem.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
