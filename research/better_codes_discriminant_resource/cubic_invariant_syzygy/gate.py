import json
from pathlib import Path
P=Path(__file__).parent;D=json.loads((P.parent/'quartic_remainder_resource_lp.json').read_text());out=[];total=0
for r in D['profile']:
 h0,h1,h2=r['H_coefficient_orders'];a=min(h1,2*h2);b=min(h0,h1+h2,3*h2);g=int(r['costs'][1]);k=None
 if 3*a!=2*b:
  assert g==min(3*a,2*b);lower=a+b-1;kind='unbalanced_exact'
 else:
  assert a%2==0;b0=3*a
  if g==b0:lower=a+b;kind='balanced_minimal'
  else:
   assert g>b0;lower=a+g-b-1;kind='balanced_discriminant_excess_exact'
 assert lower>=0
 total+=r['count']*lower;out.append(dict(count=r['count'],contact=r['contact'],p_order=a,q_order=b,disc_order=g,W_order_lower=lower,case=kind))
w=131071;d=dict(rows=out,total_W_order_lower=total,degree_W_bound=5*w-2,slack=5*w-2-total,scope='archived locally generic resource profile; no global existence inference');(P/'gate.json').write_text(json.dumps(d,indent=2));print(d)

common=sum(r['count']*min(3*r['p_order'],2*r['q_order']) for r in out)
residual=[sum(r['count']*(val(r)-min(3*r['p_order'],2*r['q_order'])) for r in out) for val in [lambda r:3*r['p_order'],lambda r:2*r['q_order'],lambda r:r['disc_order']]]
radical=sum(r['count']*sum(z>0 for z in [3*r['p_order']-min(3*r['p_order'],2*r['q_order']),2*r['q_order']-min(3*r['p_order'],2*r['q_order']),r['disc_order']-min(3*r['p_order'],2*r['q_order'])]) for r in out)
d.update(common_gcd_degree_lower=common,residual_zero_degree_totals=residual,residual_polynomial_degree_upper=6*w-common,selected_radical_count=radical,coalescence_support=sum(r['count'] for r in out if r['p_order']>0 and r['q_order']>0));(P/'gate.json').write_text(json.dumps(d,indent=2));print('Mason data',common,residual,6*w-common,radical)
