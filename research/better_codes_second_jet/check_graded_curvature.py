"""Independent direct homogeneous matrix check of the proved upper profile."""
from pathlib import Path
import json
folder=Path(__file__).parent
scope={}
exec((folder/'restricted_curvature_rank.py').read_text().split('checks=0')[0],scope)
checks=0
for m in range(2,8):
 for s in range(1,m//2+1):
  base={}
  for ell in range(m+s+1):
   count=0
   for r in range(m):
    h=m-r
    count+=sum(i+j==ell for i in range(r+1) for j in range(s+1))
    if h<=min(r,s):
     count-=sum(i+j+h==ell for i in range(r-h+1) for j in range(s-h+1))
   base[ell]=count
  for ell in range(m+s+1):
   cols=[v for _,v in scope['columns'](m,s,1,m+s,ell)]
   actual=scope['rank'](cols)
   saved=sum(0<=ell-b<m+s-3*b for b in range(1,s+1))
   upper=base.get(ell,0)+base.get(ell-1,0)-saved
   assert actual<=upper,(m,s,ell,actual,upper)
   checks+=1
out={'independent_exact_homogeneous_matrix_checks':checks,'result':'PASS','range':'m2..7, all1<=S<=m/2, all nonzero jet degrees; pinned prime','scope':'Checks the per-degree rank upper profile, not a routing certificate.'}
(folder/'check_graded_curvature.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
