from pathlib import Path
import json,math
BASE=Path(__file__).resolve().parent
data=json.loads((BASE/'results.json').read_text());p=41;xs=data['nodes'];polys=data['polynomials']
def ev(c,x,m):return sum(a*pow(x,j,m) for j,a in enumerate(c))%m
assert data['complete'] and len(data['rows'])==24 and len(polys)==210
bank=set()
for j in range(4):bank.update(tuple(v) for v in json.loads((BASE.parent/'dickson_nearest_threshold'/f'bank_coset{j}.log').read_text().splitlines()[0])['values'])
assert {tuple(ev(c,x,p) for x in xs) for c in polys}==bank
word=[(pow(x,10,p)-1)**2*pow(2,-1,p)%p for x in xs]
supports=[{j for j,x in enumerate(xs) if ev(c,x,p)==word[j]} for c in polys]
assert all(len(s)==15 for s in supports)
reports=[]
for row in data['rows']:
 ids=row['ids'];assert len(set(ids))==16
 eq=[]
 for j in range(40):
  inc=[a for a,i in enumerate(ids) if j in supports[i]]
  if inc:eq.extend([j,a,inc[0]] for a in inc[1:])
 assert eq==row['equations'] and len(eq)==row['row_count']
 assert row['status']=='obstructed_mod_p_squared'
 z=row['left_kernel'];assert len(z)==len(eq)
 cols=[0]*200;dot=0
 for weight,(j,a,b) in zip(z,eq):
  ca,cb=polys[ids[a]],polys[ids[b]];x=xs[j]
  cols[j]+=weight*sum(t*(ca[t]-cb[t])*pow(x,t-1,p) for t in range(1,10))
  for t in range(10):
   cols[40+10*a+t]+=weight*pow(x,t,p);cols[40+10*b+t]-=weight*pow(x,t,p)
  residual=(ev(ca,x,p*p)-ev(cb,x,p*p))%(p*p);assert residual%p==0
  dot+=weight*(-residual//p)
 assert all(a%p==0 for a in cols)
 assert dot%p==row['obstruction'] and dot%p!=0
 reports.append(dict(mode=row['mode'],trial=row['trial'],left_kernel_verified=True,obstruction=dot%p))
(BASE/'verification.json').write_text(json.dumps(dict(passed=True,certificates=reports),indent=2)+'\n')
print('All24 first-order obstruction certificates independently verified; source bank and full incidence coverage verified.')
