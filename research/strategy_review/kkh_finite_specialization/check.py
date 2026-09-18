import math,json
from pathlib import Path
n=262144;k=131072;A=139782
rows=[]
for b in range(19):
 s=2**b;m=n//s
 r=min(s,(k-1)//m+2)
 if r<2:continue
 rows.append(dict(s=s,m=m,r=r,degree_bound=(r-2)*m,agreement=r*m,bank_size=math.comb(s,r),reaches_target=r*m>=A))
accepted=[r for r in rows if r['reaches_target']]
assert max(r['bank_size'] for r in accepted)==11440
Path(__file__).with_suffix('.json').write_text(json.dumps({'n':n,'strict_dimension':k,'target_agreement':A,'rows':rows,'maximum_qualifying_bank':11440},indent=2)+'\n')
print(json.dumps({'maximum_qualifying_bank':11440,'qualifying_s':[r['s'] for r in accepted]}))
