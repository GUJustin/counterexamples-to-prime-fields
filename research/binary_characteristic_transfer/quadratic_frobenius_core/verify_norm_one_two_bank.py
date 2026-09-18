"""Targeted exact verification; reuses only archived histogram data, not census code."""
from itertools import product
from pathlib import Path
import json
base=Path(__file__).parent
old={r['p']:r for r in json.loads((base/'check_norm_one_lists.json').read_text())}
rows=[]
for p in (5,7):
 poly=old[p]['cubic'];bb,aa=poly[0],poly[1]
 els=list(product(range(p),repeat=3));zero=(0,0,0);one=(1,0,0);negone=(p-1,0,0)
 assert all((x*x*x+aa*x+bb)%p for x in range(p))
 def add(x,y):return tuple((a+b)%p for a,b in zip(x,y))
 def neg(x):return tuple(-a%p for a in x)
 def mul(x,y):
  h=[0]*5
  for i,a in enumerate(x):
   for j,b in enumerate(y):h[i+j]+=a*b
  for i in (4,3):h[i-3]-=bb*h[i];h[i-2]-=aa*h[i]
  return tuple(a%p for a in h[:3])
 def power(x,n):
  y=one
  while n:
   if n&1:y=mul(y,x)
   x=mul(x,x);n//=2
  return y
 L=p*p+p+1
 norms={x:power(x,L) for x in els}
 domain=[x for x in els if norms[x] in (one,negone)]
 word={x:power(x,2*p+2) for x in domain}
 coeffs=set();support_checks=0
 for u in els:
  if norms[u] not in (one,negone):continue
  v=neg(power(u,p*p+1))
  a=mul(u,u);b=add(mul(u,v),mul(u,v));c=mul(v,v)
  assert b!=zero
  coeff=(a,b,c);assert coeff not in coeffs;coeffs.add(coeff)
  roots=[];matches=[]
  for x in domain:
   hx=add(mul(u,x),v)
   if power(x,p+1)==hx:roots.append(x)
   if word[x]==mul(hx,hx):matches.append(x)
  assert roots==matches and len(matches)==p+1
  assert all(norms[x]==neg(norms[u]) for x in matches)
  support_checks+=len(domain)
 assert len(domain)==2*L and len(coeffs)==2*L
 hist=old[p]['agreement_histogram']
 assert hist[str(p+1)]==2*L and hist[str(2*p+2)]==L
 assert all(int(k)<=4 or int(k) in (p+1,2*p+2) for k in hist)
 rows.append(dict(p=p,domain_size=len(domain),new_bank_size=len(coeffs),matches_each=p+1,coordinate_checks=support_checks,archived_complete_counts_match=True,passed=True))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
