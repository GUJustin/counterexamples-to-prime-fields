"""Bounded local-polynomial valuation states; LP discovery, exact integer verification."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json,math,time
import numpy as np
from scipy.optimize import linprog
start=time.monotonic();n=262144;w=131071;C=6802316684345
rr={r['a']:r['rank'] for r in json.loads(Path('research/better_codes_kernel_base_factors/newton_discriminant_gate.json').read_text())['rows']}
def poly(beta):
 pts=list(enumerate(beta+(0,)));h=[]
 for p in pts:
  while len(h)>=2 and (h[-1][0]-h[-2][0])*(p[1]-h[-1][1])<=(h[-1][1]-h[-2][1])*(p[0]-h[-1][0]):h.pop()
  h.append(p)
 roots=[]
 for (x,y),(xx,yy) in zip(h,h[1:]):roots += [Q(y-yy,xx-x)]*(xx-x)
 roots.sort();d=len(beta);disc=2*sum((d-i-1)*v for i,v in enumerate(roots))
 if d==4:
  e,dd,c,b=beta;iv=(min(c,2*b),min(dd,b+c,3*b),min(e,b+dd,2*b+c,4*b))
 else:
  dd,c,b=beta;iv=(min(c,2*b),min(dd,b+c,3*b))
 return roots,disc,iv
GG=[(b,poly(b)) for b in product(range(4),repeat=4)];HH=[(b,poly(b)) for b in product(range(4),repeat=3)]
states={}
for bg,(vg,dg,ig) in GG:
 for bh,(vh,dh,ih) in HH:
  vs=sorted(vg*10+vh);s=Q(0);a=43
  for k in range(44):
   j=43-k;a=min(a,math.floor(2*s+j),math.floor(s+12+j))
   if k<43:s+=vs[k]
  res=sum(min(x,y) for x in vg for y in vh)
  cost=(dg,dh,res,*ig,*ih,Q(min(bg[3],bh[2])),Q(bg[3]>0),Q(bh[2]>0))
  sig=(a,cost)
  if sig not in states:states[sig]={'a':a,'bg':bg,'bh':bh,'cost':cost}
states=list(states.values());names=['discG','discH','resultantGH','centerG2','centerG3','centerG4','centerH2','centerH3','centroid_difference','centroidG_support','centroidH_support']
budgets=[12*w,6*w,12*w,2*w,3*w,4*w,2*w,3*w,w,211940,211940]
M=np.array([[float(s['cost'][j]) for s in states] for j in range(len(names))]);ranks=np.array([rr[s['a']]/1000000 for s in states]);b=np.array(budgets)/n
sol=linprog(-ranks,A_ub=M,b_ub=b,A_eq=np.ones((1,len(states))),b_eq=[1],bounds=(0,None),method='highs')
out={'states':len(states),'raw_pairs':len(GG)*len(HH),'success':bool(sol.success),'message':sol.message,'seconds':time.monotonic()-start,'scope':'monic generic local polynomials with coefficient valuations0..3; distinct centroid branch; feasibility profile, not global source'}
if sol.success:
 counts=[max(0,math.floor(n*x-1e-7)) for x in sol.x];left=n-sum(counts);zero=next(i for i,s in enumerate(states) if s['a']==0 and not any(s['cost']));counts[zero]+=left
 rank=sum(k*rr[s['a']] for k,s in zip(counts,states));totals=[sum(k*s['cost'][j] for k,s in zip(counts,states)) for j in range(len(names))]
 assert sum(counts)==n and all(x<=y for x,y in zip(totals,budgets))
 out.update(maximum_relaxed_rank=float(-sol.fun*n*1000000),integer_rank=rank,required=C-1,rank_slack=rank-(C-1),resource_totals={nm:{'used':str(v),'budget':bud,'slack':str(bud-v)} for nm,v,bud in zip(names,totals,budgets)},profile=[{'count':k,'contact':s['a'],'G_coefficient_orders':s['bg'],'H_coefficient_orders':s['bh'],'costs':[str(x) for x in s['cost']]} for k,s in zip(counts,states) if k])
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
