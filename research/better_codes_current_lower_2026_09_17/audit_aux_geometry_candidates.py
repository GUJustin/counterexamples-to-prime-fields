"""Independent target identity and characteristic checks for local finalists."""
import json,math
from pathlib import Path
import sympy as sp
import repaired_auxiliary_roots as R
ROOT=Path(__file__).resolve().parent
a,b,c=sp.symbols('a b c');r=a+3;v=b+2;z=c+3
first=(131070*z,131070*v-131071,131070*(r-2));normal=(131074*z,131074*v-131072,131074*(r-1));raw=(131073*z,131073*v,131073*r-1)
identity=(655365+262146*a,1310730+524292*a,2097170+524292*a+524292*b+262146*c)
results=[]
for idx in (5,21,22):
 data=json.loads((ROOT/f'aux_geometry_opt_g11_s{idx}.json').read_text());p=data['best'][0]['parameters'];affected=[]
 for group,ids in enumerate(R.GROUPS):
  if idx not in ids:continue
  params=[p if j==idx else R.SOURCES[j] for j in ids];scale=math.lcm(*(q[5]+1 for q in params));mins=[]
  for h in range(3):
   f=tuple(int(h==j) for j in range(3));graph=scale*R.mixed(f,first,normal)
   for j,q in enumerate(params):graph+=(R.W*normal[j]+65539*raw[j])*(scale//(q[5]+1))*R.mixed(f,R.DIRECTIONS[j],R.flag(q))
   coefficients=sp.Poly(R.GAP*graph-scale*131073*80870*identity[h],a,b,c).coeffs();mins.append(int(min(coefficients)));assert min(coefficients)>=0
  affected.append(dict(group=group,identity_minima=mins))
 m,B,s,U,L,k,n0=p;assert 2*s<=B<=m and m+s<=U<=L and m+B+s<=L and k<=s<m and k+1<=n0 and 2*(n0-k-1)<=B
 rr,yy,tt=36,163,9678;cr,cy,ct=B+s*(rr-1),U+s*(yy-1),L+s*(tt-1);mixed=[rr*ct+tt*cr,yy*ct+tt*cy,yy*cr+rr*cy];assert max(mixed)<2130706433
 results.append(dict(source=idx,parameters=p,affected_groups=affected,characteristic_margin=2130706433-max(mixed)))
(ROOT/'aux_geometry_candidates_audit.json').write_text(json.dumps(dict(passed=True,results=results,scope='All affected group identity polynomials and source shape/characteristic gates. Positive exact kernel counts recorded by optimizer. No global envelope or Lean claim.'),indent=2)+'\n');print(json.dumps(results,indent=2))
