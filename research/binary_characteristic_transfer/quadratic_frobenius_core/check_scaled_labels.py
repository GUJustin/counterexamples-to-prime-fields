"""Independent exact bank-label census; does not enumerate all E quadratics."""
import itertools,json
from pathlib import Path
rows=[]
for p in [3,5,7]:
 d=next(j for j in range(2,p) if pow(j,(p-1)//2,p)==p-1)
 zero=(0,0);one=(1,0)
 def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
 def neg(x):return ((-x[0])%p,(-x[1])%p)
 def mul(x,y):return ((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
 def power(x,n):
  r=one
  while n:
   if n&1:r=mul(r,x)
   x=mul(x,x);n//=2
  return r
 B=list(itertools.product(range(p),repeat=2));nonzero=[x for x in B if x!=zero]
 norms=[a for a in B if power(a,p+1)==one]
 seen={};target=0
 for a in norms:
  I={add(power(t,p),neg(mul(a,t))) for t in B}
  assert len(I)==p
  for b,v in itertools.product(I,repeat=2):
   # Label z=b-eta*v in direct B-basis (1,eta).
   z=(b,neg(v))
   core=2*sum(add(power(t,p),neg(mul(a,t)))==b for t in nonzero)
   fresh=2*sum(add(power(t,p),neg(mul(a,t)))==v for t in nonzero)
   assert core+fresh==4*p-2*(b==zero)-2*(v==zero)
   if z!=(zero,zero):assert z not in seen
   seen.setdefault(z,[]).append((a,core+fresh))
   if b!=zero and v!=zero:target+=1
 assert target==(p+1)*(p-1)**2
 assert len(seen)==1+(p+1)*(p*p-1)
 assert len(seen[(zero,zero)])==p+1
 rows.append({'p':p,'target_distinct_labels':target,'union_planes':len(seen),'target_agreement':4*p,'zero_label_witnesses':p+1,'passed':True})
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows))
