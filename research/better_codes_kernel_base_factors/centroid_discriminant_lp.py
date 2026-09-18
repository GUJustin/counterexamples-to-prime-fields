from fractions import Fraction as Q
from scipy.optimize import linprog
from pathlib import Path
import json
n=262144;w=131071;A=181275;C=6802316684345;t=3261;r=12
B=lambda a,b,h:a*b*(t+1-h)-b*a*(a-1)//2-a*b*(b-1)//2
R=lambda a:sum(B(k+1,r+1,0)-B(max(0,2*k+1-a),max(0,r+1-a+k),a-k) for k in range(a))
need=C-1-12*R(67);out=[]
for d,e in [(3,13),(3,14),(2,13),(2,14),(2,15)]:
 threshold=44-e
 if d==3:
  levels=[(0,43-2*e),(1,55-2*e),(2,43-e),(3,55-e),(6,43)]
  cost=lambda a:next(c for c,cap in levels if a<=cap)
 else:cost=lambda a:int(a>=44-e)+int(a>=56-e)
 budget=d*(d-1)*w
 sol=linprog([int(a>=threshold) for a in range(44)],A_ub=[[-R(a)/1e6 for a in range(44)],[cost(a) for a in range(44)]],b_ub=[-need/1e6,budget],A_eq=[[1]*44],b_eq=[n],bounds=(0,None),method='highs')
 if not sol.success:out.append(dict(d=d,e=e,status='infeasible'));continue
 active=[a for a,x in enumerate(sol.x) if x>1e-7]
 assert len(active)==3
 def solve3(mat,rhs):
  M=[[Q(x) for x in row]+[Q(v)] for row,v in zip(mat,rhs)]
  for k in range(3):
   z=next(i for i in range(k,3) if M[i][k]);M[k],M[z]=M[z],M[k]
   q=M[k][k];M[k]=[v/q for v in M[k]]
   for i in range(3):
    if i!=k:
     q=M[i][k];M[i]=[v-q*u for v,u in zip(M[i],M[k])]
  return [row[-1] for row in M]
 alpha,beta,gamma=solve3([[R(a),-cost(a),1] for a in active],[int(a>=threshold) for a in active])
 assert all(int(a>=threshold)>=alpha*R(a)-beta*cost(a)+gamma for a in range(44))
 masses=solve3([[1]*3,[R(a) for a in active],[cost(a) for a in active]],[n,need,budget])
 assert all(z>=0 for z in masses)
 assert alpha>=0 and beta>=0
 lb=alpha*need-beta*budget+gamma*n
 integer=-(-lb.numerator//lb.denominator)
 rec=dict(d=d,e=e,h=43-d*e,threshold=threshold,costs=[cost(a) for a in range(44)],alpha=str(alpha),beta=str(beta),gamma=str(gamma),lower=str(lb),integer_clean_centroid_nodes=integer,required_to_force_graph=n-A+w+1,forces_pencil=integer>n-A+w,support=[dict(a=a,count=str(x),cost=cost(a)) for a,x in zip(active,masses)])
 out.append(rec);print({k:v for k,v in rec.items() if k!='costs'},flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
