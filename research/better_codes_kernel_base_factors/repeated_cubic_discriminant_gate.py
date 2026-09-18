from fractions import Fraction as Q
from pathlib import Path
import json
n=262144;w=131071;C=6802316684345;tcap=3261;r=12;agree=181275
box=lambda a,b,h:a*b*(tcap+1-h)-b*a*(a-1)//2-a*b*(b-1)//2
R=lambda a:sum(box(k+1,r+1,0)-box(max(0,2*k+1-a),max(0,r+1-a+k),a-k) for k in range(a))
def mul(P,Q):
 O={}
 for (u,k),v in P.items():
  for (s,j),z in Q.items():O[u+s,k+j]=O.get((u+s,k+j),0)+v*z
 return {i:v for i,v in O.items() if v}
def power(P,e):
 O={(0,0):1}
 for _ in range(e):O=mul(O,P)
 return O
out=[]
for e in [13,14]:
 h=43-3*e
 levels=[(0,43-2*e),(1,55-2*e),(2,43-e),(3,55-e),(6,43)]
 cost=lambda a:next(c for c,cap in levels if a<=cap)
 states=[(cost(a),R(a),a) for a in range(44)]
 budget=6*w
 candidates=[]
 for c1,v1,a1 in states:
  if n*c1<=budget:candidates.append((Q(n*v1),[(a1,n)]))
  for c2,v2,a2 in states:
   if c1<c2 and n*c1<=budget<=n*c2:
    z=Q(budget-n*c1,c2-c1)
    candidates.append(((n-z)*v1+z*v2,[(a1,str(n-z)),(a2,str(z))]))
 best,support=max(candidates,key=lambda x:x[0])
 # Exact local leading-polynomial compatibility witness.
 P=mul(power({(0,2):1,(1,0):-1},e),power({(0,1):1,(1,0):-1},14 if e==14 else 15))
 P=mul(P,power({(0,1):1,(0,0):-1},1 if e==14 else 2))
 contact=min(u+k+min(u,12) for u,k in P)
 assert contact==40
 rank=(n-2)*R(40)
 assert rank>=C-1 and 3*(n-2)==6*w
 assert 2*agree<=3*w and (0 if e==14 else 2)*agree<=h*w+12
 out.append(dict(e=e,h=h,cost_levels=levels,good_node_LP_max=str(best),LP_support=support,local_monomials=len(P),local_contact=contact,feasible_profile=dict(contact40_nodes=n-2,contact0_nodes=2,discriminant_total=3*(n-2),discriminant_budget=6*w,rank_total=rank,rank_required=C-1,rank_margin=rank-(C-1),candidate_G_order_total=2*agree,candidate_H_order_total=(0 if e==14 else 2)*agree)))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
