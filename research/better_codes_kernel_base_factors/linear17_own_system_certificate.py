"""Exact arithmetic for a graph-power helper excluding linear multiplicity >=17.

Binding shape only. No optimizer and no benchmark-score claim.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
n=262144;w=131071;C=6802316684345;t=3261;r=12
def box(a,b,h):return a*b*(t+1-h)-b*a*(a-1)//2-a*b*(b-1)//2
def rank(a):return sum(box(k+1,r+1,0)-box(max(0,2*k+1-a),max(0,r+1-a+k),a-k) for k in range(a))
need=C-1-12*rank(67)
bad_cost=12*43+2*12
centroid_lower=Q(need-n*rank(30),rank(43)-rank(30))
centroid_count=-(-centroid_lower.numerator//centroid_lower.denominator)
assert centroid_count>w+1
slope25=Q(25,rank(43)-rank(25))
for a in range(44):
 assert (a if a<=25 else 0)<=slope25*(rank(43)-rank(a))
bound25=slope25*(n*rank(43)-need)+bad_cost
floor25=bound25.numerator//bound25.denominator
assert floor25<=12*w
slope26=Q(26,rank(42)-rank(26))
last_increment=rank(43)-rank(42)
for a in range(44):
 assert (a if a<=26 else 0)<=slope26*(rank(42)-rank(a)+last_increment*int(a==43))
bound26=slope26*(n*rank(42)-need+(w+12)*last_increment)+bad_cost
floor26=bound26.numerator//bound26.denominator
assert floor26<=12*w
def nu(s):return max(0,(s+1)//2,s-12)
profiles=[]
for e in range(13,17):
 h=43-e
 counts={h:60000,42:71073,43:131071}
 profile_rank=sum(rank(a)*count for a,count in counts.items())
 assert profile_rank>=C-1
 slacks=[]
 for j in range(h):
  cost=71073*nu(h-1-j)+131071*nu(h-j)
  slack=(h-j)*w+12-cost
  assert slack>=0
  slacks.append(slack)
 # At the two centroid states, take the centered H coefficients to have
 # exactly these t-orders. Each monomial of A=Y^e H meets the contact box.
 for contact in [42,43]:
  local_terms=[(nu(contact-e-j),e+j) for j in range(h)]+[(0,43)]
  assert min(u+k+min(u,r) for u,k in local_terms)==contact
 weights={power:power*w+60000*h+71073*max(42-power,0)+131071*max(43-power,0) for power in range(56)}
 best=min(weights.values())
 assert best>55*w
 profiles.append(dict(e=e,h=h,noncentroid_count=60000,centroid_contact42_count=71073,centroid_contact43_count=131071,centroid_total=202144,rank=profile_rank,rank_surplus=profile_rank-(C-1),minimum_coefficient_budget_slack=min(slacks),best_graph_power_weight=best,minimizing_graph_powers=[power for power,weight in weights.items() if weight==best],excess_over_own_weight=best-55*w,scope='A necessary-resource profile with compatible local Newton orders; no global polynomial realization is asserted.'))
out=dict(status='PASS: linear multiplicities17 through43 excluded by own-system helper at exact binding shape',n=n,w=w,own_system_dimension=C,good_rank_required=need,bad_node_rank_allowance=12*rank(67),bad_locator_allowance=bad_cost,affine_descent_centroid_lower=str(centroid_lower),affine_descent_centroid_count=centroid_count,locator_budget=12*w,h25=dict(slope=str(slope25),locator_bound=str(bound25),locator_floor=floor25,slack=12*w-floor25),h26_nonzero_trace_coefficient=dict(slope=str(slope26),rank43_minus_rank42=last_increment,contact43_count_cap=w+12,locator_bound=str(bound26),locator_floor=floor26,slack=12*w-floor26),helper_caps=dict(R_degree=0,joint_YR_degree=43,joint_YRZ_degree=43,weight_upper_h25=43*w+floor25,weight_upper_h26=43*w+floor26,own_weight=55*w),remaining_profiles=profiles,scope='v=55w,y=55,r=12,t=3261 and q=43. Excludes a linear factor of leading R coefficient repeated at least17. Does not cover multiplicities13..16, other shapes, smaller-multiplicity/squarefree branches, or the complete benchmark ledger.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
