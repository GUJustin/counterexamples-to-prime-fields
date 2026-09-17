"""Best actual weighted-degree class, not an assumed universal erosion."""
import json
from pathlib import Path
from wedge_probe import C,rank,A,N
from wedge_route_probe import band
m,L,S,H,k=1000,60000,310,1538,2;r,y,z=12,55,3206
gap=C(m*A,L,S,H,k)-N*rank(m,L,S,H,k)
rows=[]
for degree in [max(y,k*r),y+(k-1)*r]:
 b=band(m,L,S,H,k,r,y,y+z,actual_weighted_degree=degree)
 rows.append(dict(actual_weighted_degree=degree,gap=gap,slab=b,margin=gap-b))
out=dict(rows=rows,all_integer_degree_classes_fail=rows[-1]['margin']<=0,reason='Slab budget is nonincreasing in the actual weighted factor degree. Even the maximum permissible degree fails for this fixed wedge.',scope='Only this fixed source wedge and critical factor context, not an exclusion of other support geometries.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
