"""Independent replay of newly covered section indices and exact Elias filter."""
from pathlib import Path
import json
from verify_binomial_sections import fixture

BASE=Path(__file__).resolve().parent
rows=json.loads((BASE/'all_sections_scan.json').read_text())
assert len({(r['r'],r['k'],r['section']) for r in rows})==len(rows)
def prime(p):return p>=2 and all(p%d for d in range(2,__import__('math').isqrt(p)+1))
expected={(r,k) for r in range(2,49) for k in [16,32,64,128] if prime(2*r*k+1)}
assert {(x['r'],x['k']) for x in rows}==expected
for r,k in {(x['r'],x['k']) for x in rows}:
 assert {x['section'] for x in rows if x['r']==r and x['k']==k}==set(range(r))
checks=[]
for r,j,k,c in [(38,29,16,16),(44,4,16,16),(33,0,32,32),(2,1,64,4)]:
 checks.append(fixture(next(x for x in rows if (x['r'],x['section'],x['k'])==(r,j,k)),c))
summary={}
for c in [4,8,16,32]:
 hits=[]
 for row in rows:
  if len(row['cosets'])<c:continue
  k,p=row['k'],row['p'];n=c*k;A=sum(x[1] for x in row['cosets'][:c])
  if A<=k:continue
  if n**n*(p-1)**(n-A)<(n-A)**(n-A)*A**A*p**(n-k):
   hits.append(dict(r=row['r'],section=row['section'],k=k,p=p,n=n,A=A))
 summary[str(c)]=dict(below_elias_cases=len(hits),largest_k=max((x['k'] for x in hits),default=0),hits=hits)
assert all(x['r']==2 and x['section']==1 for x in summary['4']['hits'])
out=dict(status='passed',cases=len(rows),fixtures=checks,by_coset_count=summary,
         scope='All section indices covered for r2..48,k16,32,64,128 at prime2rk+1; independent orbit replay of four fixtures and exact Elias filtering. Finite search only.')
(BASE/'all_sections_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status='passed',cases=len(rows),summary={c:{k:v for k,v in x.items() if k!='hits'} for c,x in summary.items()}),indent=2))
