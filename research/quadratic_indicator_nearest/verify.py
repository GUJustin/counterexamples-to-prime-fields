from pathlib import Path
from math import comb
import json
folder=Path(__file__).resolve().parent
rows=[]
for p in (5,13,17,29,37,41,73,97,113,193,257):
 k=(p-1)//4;zero=(0,)*(k+1);one=(1,)+(0,)*k
 bank={zero,one}
 for u in range(p):
  if u*u%p!=p-1:continue
  for v in (1,p-1):
   c=pow(v-u,-1,p);coeff=[0]*(k+1);coeff[0]=-u*c%p;coeff[k]=c;bank.add(tuple(coeff))
 assert len(bank)==6
 for coeff in bank:
  agreement=sum(sum(c*pow(x,j,p) for j,c in enumerate(coeff))%p==(1+pow(x,2*k,p))*pow(2,-1,p)%p for x in range(1,p))
  assert agreement==2*k
  if coeff[-1]:
   c=coeff[-1];t=coeff[0];assert (pow(c,4,p)*4+1)%p==0 and (t+c*c-pow(2,-1,p))%p==0
 if p in (17,41):
  scan=json.loads((folder/f'p{p}.log').read_text().splitlines()[0]);assert scan['complete']
  assert {tuple(c) for c in scan['coefficients']}==bank
  assert scan['root_subsets']==comb(2*k,k)
 rows.append(dict(p=p,length=p-1,dimension=k+1,maximum_agreement=2*k,nearest_list_size=6))
out=dict(status='passed',rows=rows,scope='Exact replay of exhaustive p17 and p41 lists and closed-form witnesses at eleven primes. The separate divisibility proof establishes completeness for all odd prime powers q=1 mod4 and extension coefficients.')
(folder/'verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
