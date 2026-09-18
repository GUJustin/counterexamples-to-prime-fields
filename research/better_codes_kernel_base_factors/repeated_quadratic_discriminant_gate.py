from fractions import Fraction as Q
from pathlib import Path
import json
n=262144;w=131071;C=6802316684345;t=3261;r=12
B=lambda a,b,h:a*b*(t+1-h)-b*a*(a-1)//2-a*b*(b-1)//2
R=lambda a:sum(B(k+1,r+1,0)-B(max(0,2*k+1-a),max(0,r+1-a+k),a-k) for k in range(a))
rows=[]
for e in range(13,22):
 low=43-e;mid=min(43,55-e)
 cost=lambda a:int(a>=44-e)+int(a>=56-e)
 slope=max(Q(R(mid)-R(low)),Q(R(43)-R(low),2))
 assert all(R(a)<=R(low)+slope*cost(a) for a in range(44))
 bound=n*R(low)+2*w*slope+12*R(67)
 rows.append(dict(e=e,h=43-2*e,first_threshold=44-e,second_threshold=56-e,rank_intercept=R(low),rank_slope=str(slope),rank_upper=str(bound),required=C-1,excluded=bound<C-1,margin=str(C-1-bound)))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2));print(json.dumps(rows,indent=2))
