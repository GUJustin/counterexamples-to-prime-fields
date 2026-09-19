"""Exact small-field verification of the three-point plane bound, not a proof of its general case."""
from itertools import combinations,product
from pathlib import Path
import json

def check(p,c):
 size=p**3;digits=[(x%p,(x//p)%p,x//(p*p)) for x in range(size)]
 enc=lambda a:sum((v%p)*p**i for i,v in enumerate(a))
 add=[[enc([digits[x][i]+digits[y][i] for i in range(3)]) for y in range(size)] for x in range(size)]
 neg=[enc([-z for z in a]) for a in digits]
 mul=[]
 assert all((x**3+c[1]*x+c[0])%p for x in range(p))
 for aa in digits:
  row=[]
  for bb in digits:
   z=[0]*5
   for i in range(3):
    for j in range(3):z[i+j]+=aa[i]*bb[j]
   for i in (4,3):
    z[i-3]-=z[i]*c[0];z[i-2]-=z[i]*c[1]
   row.append(enc(z[:3]))
  mul.append(row)
 def power(a,k):
  z=1
  while k:
   if k&1:z=mul[z][a]
   a=mul[a][a];k//=2
  return z
 assert all(power(a,size-1)==1 for a in range(1,size))
 bank=[(a,neg[power(a,p*p+1)]) for a in range(1,size) if power(a,p*p+p+1)==p-1]
 assert len(bank)==p*p+p+1
 B=set(bank);maxima={1:0,2:0};counts={1:0,2:0}
 for z,x,y in combinations(bank,3):
  dx=(add[x[0]][neg[z[0]]],add[x[1]][neg[z[1]]]);dy=(add[y[0]][neg[z[0]]],add[y[1]][neg[z[1]]])
  span={(add[z[0]][add[mul[u][dx[0]]][mul[v][dy[0]]]],add[z[1]][add[mul[u][dx[1]]][mul[v][dy[1]]]]) for u,v in product(range(p),repeat=2)}
  dim=1 if len(span)==p else 2
  assert len(span) in (p,p*p)
  hit=len(span&B);maxima[dim]=max(maxima[dim],hit);counts[dim]+=1
 assert maxima[2]<=3 and maxima[1]<=3
 return {'prime_base':p,'ambient_size':size,'modulus_ascending':[c[0],c[1],0,1],'bank_size':len(bank),'triple_spans_checked':counts,'maximum_bank_intersection':maxima,'scope':'All affine base-field planes containing three noncollinear bank points are covered; planes with fewer than three need no check.'}
out={'passed':True,'fixtures':[check(3,[1,2]),check(5,[1,1]),check(7,[2,0])]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
