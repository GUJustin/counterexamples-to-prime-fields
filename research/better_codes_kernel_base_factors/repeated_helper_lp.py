from scipy.optimize import linprog
from fractions import Fraction
import json
from pathlib import Path
n=262144;A=181275;w=131071;C=6802316684345;t=3261;r=12
B=lambda a,b,h:a*b*(t+1-h)-b*a*(a-1)//2-a*b*(b-1)//2
R=lambda a:sum(B(k+1,r+1,0)-B(max(0,2*k+1-a),max(0,r+1-a+k),a-k) for k in range(a))
nu=lambda a:max((a+1)//2,a-r)
results=[]
for e,g in [(21,2),(20,2),(14,3)]:
 h=43-e*g; states=[(a,u,max(0,nu(a)-e*u)) for a in range(44) for u in range((nu(a)+e-1)//e+1)]
 obj=[-R(a)/1e6 for a,u,v in states]
 res=linprog(obj,A_ub=[[u for a,u,v in states],[v for a,u,v in states]],b_ub=[g*w+12//e,h*w+12],A_eq=[[1]*len(states)],b_eq=[A],bounds=(0,None),method='highs')
 assert res.success
 dual=[Fraction(float(z*1e6)).limit_denominator(1000000) for z in [-res.eqlin.marginals[0],-res.ineqlin.marginals[0],-res.ineqlin.marginals[1]]]
 c,x,y=dual
 # Repair roundoff only upward on intercept, then exact pointwise certificate.
 c=max(Fraction(R(a))-x*u-y*v for a,u,v in states)
 assert x>=0 and y>=0
 inside=A*c+(g*w+12//e)*x+(h*w+12)*y
 total=inside+(n-A)*R(43)+49897120
 supp=[dict(a=states[i][0],u=states[i][1],v=states[i][2],count=float(z)) for i,z in enumerate(res.x) if z>1e-7]
 rec=dict(e=e,g=g,h=h,dual=[str(z) for z in [c,x,y]],rank_upper=str(total),required=C-1,excluded=total<C-1,margin=str(Fraction(C-1)-total),support=supp)
 results.append(rec);print(rec,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2))
