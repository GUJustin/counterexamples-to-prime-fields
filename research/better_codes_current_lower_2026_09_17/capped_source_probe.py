"""One fixed Source00 shape with explicit YS-cap sensitivity; no grid."""
import json,sys
from pathlib import Path
from capped_source_count import count
from fast_firstjet_count import coefficient_count
from affine_local_source_gate import rank
import exact_contact_thresholds as q
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'phase_source_feasibility'))
from exact_slab import thin
checks=0
for w in [3,7]:
 for D in range(1,20):
  for L,Y,S in [(0,0,0),(4,2,3),(3,6,4),(6,6,6)]:
   brute=sum((L+1-i-j)*max(D-w*i-(w-1)*j,0) for j in range(min(S,Y,L)+1) for i in range(min(Y,L)-j+1))
   assert count(D,L,Y,S,w)==brute;checks+=1
m,L,S=64000,3840000,19840;D=m*q.A;Y0=(D+S-1)//q.W;R=rank(m,L,S);C0=count(D,L,Y0,S)
assert C0==coefficient_count(D,L,S)
rows=[]
for cut in [0,1,10,100,500,1000,5000,Y0-m+1]:
 Y=Y0-cut;C=count(D,L,Y,S);gap=C-262144*R
 bands={str(z):thin(D,L,Y,S,12,43,z,q.DELTA) for z in [2975,3206]}
 rows.append(dict(Y=Y,cut=cut,coefficient_loss=C0-C,gap=gap,bands=bands,margins={z:gap-band for z,band in bands.items()},local_characteristic_max=max(12*L+9678*S,55*L+9678*Y,55*S+12*Y)))
out=dict(shape=dict(m=m,L=L,S=S,D=D,automatic_Y=Y0),brute_checks=checks,rows=rows,scope='Explicit YS support with unchanged conservative local-rank upper bound; requires restricted-kernel/source adapter. One fixed shape, not optimized geometry or score certificate.')
(q.ROOT/'capped_source_probe.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
