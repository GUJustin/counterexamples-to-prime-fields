from fractions import Fraction as F
from math import prod,comb,factorial,isqrt,exp
import json,pathlib,time
start=time.monotonic()
def prime(n):return n>1 and all(n%i for i in range(2,isqrt(n)+1))
def nxt(n):
 while not prime(n):n+=1
 return n
def fall(n,k):return prod(range(n-k+1,n+1))
def rat(x):return [str(x.numerator),str(x.denominator)]
rows=[]
for L in [1500,1800,2000]:
 q=nxt(L);bb=[2*q*i+i*i%q for i in range(L)];p=nxt(4*max(bb)+3);T=2*L+1;A=T-3;n=(T*T+2)//2;t=n-L*(L-1)
 assert prime(p) and p-1>4*max(bb) and n+26*L+1<p and L+13<=A
 assert T*T<2*n
 base=[F(0)]*14
 for r in range(3,14):base[r]=F(comb(r-1,2),factorial(r))
 coef=[F(1)]+[F(0)]*13;mom=[]
 for k in range(1,5):
  coef=[sum(coef[j]*base[r-j] for j in range(r+1)) for r in range(14)]
  cut=13 if k==1 else 12
  mom.append(fall(L,k)*sum((-1)**(r-3*k)*coef[r]*F(fall(t,r),p**r) for r in range(3*k,cut+1)))
 lower=mom[0]-mom[1]+mom[2]/2-mom[3]/6
 badnodes=F(2*L*t,p);loss=2*L*badnodes;net=p*lower-loss
 guaranteed=net.numerator//net.denominator
 rows.append(dict(L=L,q=q,p=p,n=n,t=t,A=A,T=T,mu=t/p,exact_expected_qualifying_incumbents=rat(mom[0]),exact_expected_qualifying_incumbents_decimal=float(mom[0]),poisson_singleton_density_heuristic=float(mom[0])*exp(-float(mom[0])),factorial_moment_bounds=list(map(rat,mom)),rigorous_singleton_density_lower=rat(lower),rigorous_singleton_density_decimal=float(lower),expected_blacklisted_nodes_upper=rat(badnodes),expected_repair_loss_upper=rat(loss),repaired_singleton_expectation_lower=rat(net),guaranteed_canonical_singleton_labels=guaranteed,guaranteed_final_singleton_labels=guaranteed+1,exceeds_n=guaranteed+1>n))
assert rows[-1]['exceeds_n']
out=dict(rows=rows,seconds=time.monotonic()-start,scope='Exact finite expectation over random monic degree13; received polynomial not yet instantiated')
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
for r in rows:print({k:r[k] for k in ['L','p','n','mu','exact_expected_qualifying_incumbents_decimal','rigorous_singleton_density_decimal','guaranteed_final_singleton_labels','exceeds_n']})
