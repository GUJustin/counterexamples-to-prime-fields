import itertools,json
from pathlib import Path
rows=[]
for p in (3,5):
 d=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
 def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
 def mul(x,y):return ((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
 def pw(x,n):
  z=(1,0)
  while n:
   if n&1:z=mul(z,x)
   x=mul(x,x);n//=2
  return z
 B=list(itertools.product(range(p),repeat=2));z=(0,0);one=(1,0)
 nz=[x for x in B if x!=z];hist={};max_non_even=0;bank=0;zero_bank=0
 # Exact two-component counts for every B-coefficient quadratic.
 # On vB, odd coefficient c*v is outside B when c!=0, hence no nonzero matches.
 # Even polynomials count through y=x², two roots per nonzero y in B.
 for a,c,b in itertools.product(B,repeat=3):
  if c==z:
   count=2*sum(pw(y,p)==add(mul(a,y),b) for y in nz)
   canonical=pw(a,p+1)==one and add(pw(b,p),mul(pw(a,p),b))==z
   if canonical:
    assert count==(2*p if b!=z else 2*p-2)
    bank+=b!=z;zero_bank+=b==z
   else:assert count<=2
  else:
   count=sum(pw(x,2*p)==add(add(mul(a,pw(x,2)),mul(c,x)),b) for x in nz)
   assert count<=max(p,4)
   max_non_even=max(max_non_even,count)
  hist[count]=hist.get(count,0)+1
 assert bank==p*p-1 and zero_bank==p+1
 rows.append(dict(p=p,quadratics=p**6,histogram=hist,bank=bank,zero_bank=zero_bank,max_non_even_B_coefficients=max_non_even))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows))
