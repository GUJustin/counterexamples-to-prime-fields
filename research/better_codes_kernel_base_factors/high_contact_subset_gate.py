import json
from pathlib import Path
n=262144;w=131071;t=3261;r=12;C=6802316684345
def box(a,b,h):return a*b*(t+1-h)-b*a*(a-1)//2-a*b*(b-1)//2
def R(m):return sum(box(k+1,r+1,0)-box(max(k+1-(m-k),0),max(r+1-(m-k),0),m-k) for k in range(m))
# For e=sum ord_x B<=12, certify the largest excess rank from exceptional nodes
# by exact finite integer partition DP, allowing any nonnegative distribution.
dp=[0]*13
for e in range(1,13):dp[e]=max(dp[e-v]+R(43+2*v)-R(43) for v in range(1,e+1))
excess=dp[12]
needed=C-1-n*R(39)-excess
count=max(0,(needed+R(43)-R(39)-1)//(R(43)-R(39)))
out={'maximum_rank_excess_over_contact43_for_total_B_order12':excess,'one_node_attains_dp':excess==R(67)-R(43),'forced_nodes_contact_at_least40':count,'candidate_complement_size':n-181275,'contact40_rank_sum':n*R(40),'own_rigidity_required_rank_sum':C-1,'contact40_factor_charge':15*w,'three_such_charges':45*w,'primary_charge_budget_strict':118*(181275-w),'linear_graph_nodes_required':n-181275+w+12+1}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
