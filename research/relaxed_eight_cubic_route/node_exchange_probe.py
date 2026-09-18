"""Complete fresh-six census and one-node exchange test for the fixed ten/eleven seeds."""
import json,runpy,itertools
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq_poly as _poly, fmpq
def fmpq_poly(c):return _poly([fmpq(str(x)) for x in c])
D=Path(__file__).parent;v=runpy.run_path(str(D/'verify_eleven_cubic.py'));seen=v['seen'];X=v['X'];W=v['W'];ev=v['ev'];cs=v['cs']
# Ten-source: >=6 forces >=4 rational old matches, so all candidates are rational.
g10=fmpq_poly([F(-25),F(125),F(358)]);q0=fmpq_poly(cs[0]);ten=[];teninc=[]
for c,old in seen.items():
 pp=fmpq_poly(c);new=2 if (pp-q0)%g10==0 else 0
 total=len(old)+new
 if total==6:ten.append((c,old,new))
 if total>=7:teninc.append((c,old,new))
# Exact Q(sqrt39) arithmetic for all potential nonrational six-match cubics.
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return (a[0]*b[0]+39*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def inv(a):
 norm=a[0]*a[0]-39*a[1]*a[1];assert norm
 return (a[0]/norm,-a[1]/norm)
def evk(c,x):
 a=(F(0),F(0))
 for b in reversed(c):a=add(mul(a,x),b)
 return a
zero=(F(0),F(0));one=(F(1),F(0))
r,s=v['r'],v['s'];theta=(F(-4175,7652),F(55,7652))
xx=[(x,F(0)) for x in X]+[(r,F(0)),(s,F(0)),theta]
ww=[(w,F(0)) for w in W]+[(ev(cs[0],r),F(0)),(ev(cs[0],s),F(0)),evk([(a,F(0)) for a in cs[2]],theta)]
nonrat=[];old_counts=[]
for j in range(16):
 inds=[16,17,18,j];xs=[xx[i] for i in inds];dd=[ww[i] for i in inds]
 for k in range(1,4):
  for i in range(3,k-1,-1):dd[i]=mul(sub(dd[i],dd[i-1]),inv(sub(xs[i],xs[i-k])))
 c=[dd[3]]
 for k in range(2,-1,-1):
  z=[zero]*(len(c)+1)
  for i,a in enumerate(c):z[i]=sub(z[i],mul(xs[k],a));z[i+1]=add(z[i+1],a)
  z[0]=add(z[0],dd[k]);c=z
 hit=[i for i in range(19) if evk(c,xx[i])==ww[i]]
 old_counts.append(len(set(hit)&set(range(16))))
 if len(hit)>=6 and any(a[1] for a in c):nonrat.append((c,hit))
# Rational eleven census was exhaustive via old four-subsets; no six matches.
assert v['hist'].get(6,0)==0
# For ten, test every removal not matching the fresh six candidate, since a lost
# match would leave at most six after one insertion. All incumbents have seven.
locator=fmpq_poly([1])
for x in X:locator*=fmpq_poly([-x,1])
locator*=g10
exchanges=[]
for c,old,new in ten:
 fresh=fmpq_poly(c)
 for removed in range(18):
  if removed in old or (removed>=16 and new):continue
  deficient=[cc for cc,ss,nn in teninc if removed in ss or (removed>=16 and nn)]
  assert deficient
  base=fmpq_poly(deficient[0]);h=fresh-base
  for cc in deficient[1:]:h=h.gcd(fmpq_poly(cc)-base)
  if not h:raise AssertionError('Fresh candidate is incumbent')
  # Repeated factors at old coordinates do not represent fresh roots.
  while h.degree()>0:
   common=h.gcd(locator)
   if common.degree()==0:break
   h=h//common
  if h.degree()>0:exchanges.append(dict(candidate=list(map(str,c)),removed=removed,new_root_polynomial=list(map(str,h))))
out=dict(ten_fresh_six_count=len(ten),ten_fresh_six=[dict(coefficients=list(map(str,c)),old_support=ss,new_matches=nn) for c,ss,nn in ten],ten_exchange_leads=exchanges,eleven_rational_six_count=0,eleven_nonrational_test_count=16,eleven_nonrational_old_match_counts=old_counts,eleven_nonrational_six_count=len(nonrat),eleven_nonrational_six=[dict(coefficients=[[str(a),str(b)] for a,b in c],support=h) for c,h in nonrat])
(D/'node_exchange_probe.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
