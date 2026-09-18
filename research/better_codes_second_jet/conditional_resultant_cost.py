"""Conditional exact helper costs; no source rank-two/avoidance claim."""
import json
from pathlib import Path
n,w,A,p=262144,131071,181275,2130706433
m,S,J,L=128,40,177,5515
right=(2*J-1,2*S,2*L-1)
rows=[]
for z in (2950,3193,3206):
 left=(55,12,55+z)
 y,r,t=left;Y,R,T=right
 mix=(r*T+t*R,y*T+t*Y,y*R+r*Y)
 ca=(1+2*w*y,w*(2*r-1),1+2*w*t)
 cb=(1+2*w*Y,w*(2*R-1),1+2*w*T)
 dot=lambda a,b:sum(x*y for x,y in zip(a,b))
 extra=(n-A+1)*(A-w)*mix[2]
 asym=((n-w)*dot(ca,mix)+extra)//(A-w)
 sym=((n-w)*dot(tuple(map(max,ca,cb)),mix)+extra)//(A-w)
 rows.append(dict(z=z,left=left,right=right,mixed=mix,char_ok=max(mix+left)<p,left_regular_count=asym,symmetric_regular_count=sym))
out=dict(scope='Conditional coprime known-identity helper costs only; no source rank-two or factor-avoidance proof.',m=m,S=S,J=J,L=L,resultant_contact=2*m-1,resultant_weight_cap_inclusive=2*m*A-w,resultant_firstjet_contact_budget=(2*m-1)*A,root_budget_excess=A-w,rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
# All cached factor contexts: helper cost and gates are monotone in total degree.
state=Path(__file__).resolve().parents[2]/'tmp/current-lower-primary-cache/regenerated_target_state.json'
contexts=json.loads(state.read_text())['rows']
def helper(left):
 y,r,t=left;Y,R,T=right
 mix=(r*T+t*R,y*T+t*Y,y*R+r*Y)
 vec=(1+2*w*y,w*(2*r-1),1+2*w*t)
 numerator=(n-w)*sum(a*b for a,b in zip(vec,mix))+(n-A+1)*(A-w)*mix[2]
 return numerator//(A-w),mix
maxrow=None
for r,v,_ in contexts:
 y=r+v
 for total in (y,9678):
  cost,mix=helper((y,r,total))
  assert max(mix+(y,r,total))<p
  record=dict(r=r,v=v,total=total,cost=cost,mixed=mix)
  if maxrow is None or cost>maxrow['cost']:maxrow=record
aggregate,mixed=helper((163,36,9678))
audit=dict(scope='Conditional coprime helper costs over cached factor degree contexts, not full receipt propagation.',contexts=len(contexts),endpoint_checks=2*len(contexts),all_char_gates_pass=True,max_context=maxrow,aggregate_regular_factor_cap=aggregate,aggregate_left_caps=[163,36,9678],aggregate_mixed=mixed)
Path(__file__).with_name('conditional_resultant_contexts.json').write_text(json.dumps(audit,indent=2)+'\n')
print(json.dumps(audit,indent=2))
