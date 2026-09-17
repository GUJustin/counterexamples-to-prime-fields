"""Sharp integer agreement onset of positive untrimmed affine-L slope."""
from fractions import Fraction as F
from pathlib import Path
import json
from benchmark_source_gate import gate,N,W
threshold=183960;A=threshold-1;rows=[]
for S in range(4):
 worst=None
 for m in range(1,65):
  Y=(m*A+S-1)//W;g=gate(m,S,Y,A)
  assert g['slope']<=0
  if worst is None or g['slope']>worst['slope']:worst=g
 c=F(W-1,W)
 a=F(A*A,W)-N;b=A*(1-c*S)-N*(1-S)
 cc=W*(-c*S/2+c*c*S*(2*S+1)/6+F(1,4))-F(N*S*(2*S+1),3)
 assert a<0 and 2*a*64+b<0 and a*64**2+b*64+cc<0
 rows.append(dict(S=S,finite_max_slope=worst,tail_upper_at64=str(a*64**2+b*64+cc),tail_derivative_at64=str(2*a*64+b)))
witness=gate(19,3,(19*threshold+2)//W,threshold)
assert witness['slope']>0
out=dict(threshold=threshold,rows=rows,witness=witness,scope='Sharp for positive affine-L slope of automatic untrimmed source across ALL integer multiplicities and S0..3. Not a universal lower bound on arbitrary supports or finite-L positive intercepts.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
