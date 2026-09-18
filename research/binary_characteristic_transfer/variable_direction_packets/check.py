"""Small exact direction-set gate; no enumeration of received words."""
import itertools,json
from pathlib import Path
out=[]
for p in (3,5):
 d=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
 def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
 def neg(x):return ((-x[0])%p,(-x[1])%p)
 def mul(x,y):return ((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
 def power(x,n):
  z=(1,0)
  while n:
   if n&1:z=mul(z,x)
   x=mul(x,x);n//=2
  return z
 E=list(itertools.product(range(p),repeat=2));zero=(0,0);one=(1,0)
 dirs=[a for a in E if power(a,p+1)==one]
 for r in range(2,p+2):
  hist={};zero_heads={k:0 for k in range(1,r)}
  for S in itertools.combinations(dirs,r):
   e=[one]+[zero]*r
   for a in S:
    for j in range(r,0,-1):e[j]=add(e[j],mul(a,e[j-1]))
   for j in range(r+1):assert e[r-j]==mul(e[r],power(e[j],p))
   first=next(j for j in range(1,r+1) if e[j]!=zero)
   hist[first]=hist.get(first,0)+1
   for k in zero_heads:zero_heads[k]+=all(v==zero for v in e[1:k+1])
   roots=[x for x in E if x==zero or power(x,p-1) in S]
   assert len(roots)==r*(p-1)+1
   for x in roots:
    val=zero
    for j in range(r+1):
     term=mul(e[j],power(x,(r-j)*(p-1)+1))
     val=add(val,neg(term) if j%2 else term)
    assert val==zero
  out.append(dict(p=p,nonsquare=d,r=r,sets=sum(hist.values()),first_nonzero_elementary_symmetric=hist,vanishing_prefix_counts=zero_heads))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
