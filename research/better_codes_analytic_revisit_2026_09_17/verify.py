"""Independent direct-sum checks for both reported supports."""
from fractions import Fraction as F
from pathlib import Path
import json,math
from finite_scan import counts,direct,evaluate,n,D,p,budget
out=[]
for A,m,b,B in [(183210,26,7,36),(181284,152,47,210)]:
 rows=direct(m,b,A)[:B+1];assert rows==counts(m,b,A)[:B+1]
 r=evaluate(m,b,A,B);H=r['H'];ds=[N-n*R for N,R in rows]
 assert all(sum(max(0,h-t+1)*v for t,v in enumerate(ds))<=0 for h in range(H))
 assert sum(max(0,H-t+1)*v for t,v in enumerate(ds))>0
 tau=2*D-3;u=1+tau*(B-1);v=min(u,tau*(b-1)+D)
 ff=B*v+b*(u-v);j=H*(2*u*v-v*v)+2*(1+tau*H)*ff
 lam=F(n-D,A-D)
 def reg(L):return F(n-L+1,A-L+1)*lam*j+F((n-L)*(n-D),L-D)*ff
 allbest=min((reg(L),L) for L in range(D+1,A+1))
 assert allbest==(F(r['exact_regular']),r['optimal_L'])
 total=allbest[0]+F(r['ordinary'])+F(r['list'])
 if A==183210:assert total*2**128<=p**6
 else:assert allbest[0]>1100*budget
 out.append(dict(A=A,m=m,b=b,B=B,H=H,minimal_graded_height=True,thresholds_checked=A-D,regular_optimum_L=allbest[1],total_budget_ratio=float(total/budget),passes=total*2**128<=p**6))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
