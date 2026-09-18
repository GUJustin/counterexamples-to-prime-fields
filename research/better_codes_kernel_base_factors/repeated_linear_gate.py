from fractions import Fraction as Q
from pathlib import Path
import json
n=262144;w=131071;agree=181275;C=6802316684345;r=12;t=3261
box=lambda a,b,h:a*b*(t+1-h)-b*a*(a-1)//2-a*b*(b-1)//2
R=lambda a:sum(box(k+1,r+1,0)-box(max(0,2*k+1-a),max(0,r+1-a+k),a-k) for k in range(a))
b=lambda a:max(0,(a-42)//2)
M=max(Q(R(a)-R(43),b(a)) for a in range(44,68))
rows=[]
for e in range(13,44):
 h=43-e
 assert all(R(a)<=R(h)+(R(43)-R(h))*(a>h)+M*b(a) for a in range(68))
 lb=Q(C-1-n*R(h)-12*M,R(43)-R(h));N=max(0,-(-lb.numerator//lb.denominator))
 # Exact feasible integer profile for these abstract inequalities.
 profile={h:n-N,43:N-1,67:1}
 assert sum(profile.values())==n and sum(cnt*b(a) for a,cnt in profile.items())==12
 assert sum(cnt*R(a) for a,cnt in profile.items())>=C-1
 assert n*R(h)+(N-1)*(R(43)-R(h))+12*M<C-1
 rows.append(dict(e=e,h=h,rank_high_node_lower=N,clean_agreement_lower=N-(n-agree)-12,graph_forced=N-(n-agree)-12>w,extremal_abstract_profile=profile))
# Concrete obstruction to quadratic helper conclusion, without spending B-order budget.
inside=[(33,1,0,87300),(43,1,10,13108),(43,2,0,80867)]
assert sum(z for a,u,v,z in inside)==agree
assert sum(u*z for a,u,v,z in inside)<=2*w
assert sum(v*z for a,u,v,z in inside)<=w+12
assert all(21*u+v>=max((a+1)//2,a-12) for a,u,v,z in inside)
rank=(n-agree)*R(43)+sum(z*R(a) for a,u,v,z in inside)
assert rank>=C-1
out=dict(rank_excess_slope=str(M),rank_excess_total=str(12*M),rows=rows,quadratic_counterprofile=dict(inside=inside,outside_contact=43,outside_count=n-agree,total_rank=rank,required=C-1))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)); print(json.dumps({'first_forcing_e':next(x['e'] for x in rows if x['graph_forced']),'e27':rows[14],'e43':rows[-1],'quadratic_profile_rank':rank},indent=2))
