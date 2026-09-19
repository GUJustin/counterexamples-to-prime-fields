"""Exact arithmetic certificate for binding-shape quadratic13 pencil routing.

No optimizer, no claimed benchmark improvement. The geometric inputs are the
own-system rank inequality, quadratic discriminant bound, and centered H_j
Newton coefficient inequality stated in the accompanying task discussion.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
n=262144;w=131071;agreement=181275;C=6802316684345;t=3261;r=12
def box(a,b,h):return a*b*(t+1-h)-b*a*(a-1)//2-a*b*(b-1)//2
def rank(a):return sum(box(k+1,r+1,0)-box(max(0,2*k+1-a),max(0,r+1-a+k),a-k) for k in range(a))
def nu(s):return max(0,(s+1)//2,s-12)
def cost(j,a,d):return max(nu(a-j-26),nu(a-j)-13*d) if a>=31 else 0
need=C-1-12*rank(67)
rows=[]
for j in range(12):
 intercept=Q(rank(30))
 if j<=10:
  mu=Q(2*rank(42)-rank(43)-rank(30),2*cost(j,42,1)-cost(j,43,2))
  lam=rank(42)-intercept-mu*cost(j,42,1)
 else:
  lam=rank(36)-intercept
  mu=Q(rank(42)-rank(36),cost(j,42,1))
 assert lam>=0 and mu>=0
 checks=0
 for a in range(44):
  dmin=int(a>=31)+int(a>=43)
  for d in range(dmin,4):
   assert rank(a)<=intercept+lam*d+mu*cost(j,a,d),(j,a,d)
   checks+=1
  # For d>=3 the coefficient lower bound is constant. Nonnegative lam
  # therefore extends the finite check to every discriminant valuation.
  assert cost(j,a,3)==cost(j,a,4)
 budget=(17-j)*w+12
 upper=n*intercept+2*w*lam+budget*mu
 assert upper<need
 rows.append(dict(j=j,dual=[str(intercept),str(lam),str(mu)],rank_upper=str(upper),required=need,margin=str(need-upper),finite_checks=checks))
# H_0 through H_11 vanish, so H=Y^12 J and deg_Y J<=5. Any good
# noncentroid coordinate has received-root multiplicity at most13+5=18.
denom=2*rank(42)-rank(43)-rank(18)
alpha=Q(1,denom);beta=Q(rank(43)-rank(42),denom);gamma=-Q(rank(18),denom)
assert alpha>0 and beta>=0
for a in range(44):
 dmin=int(a>=19)+int(a>=43)
 assert int(a>=19)>=alpha*rank(a)-beta*dmin+gamma
lower=alpha*need-beta*(2*w)+gamma*n
count=-(-lower.numerator//lower.denominator)
assert count>n-agreement+w
out=dict(status='PASS: separable quadratic13 binding-shape branch routes to one affine codeword pencil',n=n,w=w,agreement=agreement,own_system_dimension=C,bad_node_rank_allowance=12*rank(67),good_rank_required=need,coefficient_certificates=rows,centroid_dual=[str(alpha),str(beta),str(gamma)],centroid_lower=str(lower),centroid_integer_lower=count,required_centroid_count=n-agreement+w+1,overlap_with_every_agreement_set=agreement+count-n,overlap_surplus=agreement+count-n-w,scope='Exact caps v=55w,y=55,r=12,t=3261; q=43; a quadratic factor of multiplicity13 with NONZERO discriminant. The zero-discriminant case is a linear factor of multiplicity26 and is not covered. Not an all-context ledger or benchmark certificate.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='coefficient_certificates'},indent=2))
