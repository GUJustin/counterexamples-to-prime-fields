"""Independent arithmetic replay and exhaustive direction-count audit.

No helper from the construction verifiers is imported. Uses a different
variance formula, integral square-root rounding, complement moment
ranges and a smooth collision bound rather than balanced occupancies.
"""
from fractions import Fraction as Q
from math import comb,factorial,isqrt,prod
from itertools import combinations,product
from pathlib import Path
import json,time


def ceilq(x):return -(-x.numerator//x.denominator)


def prime_mersenne(b):
 assert b>=3 and all(b%j for j in range(2,isqrt(b)+1))
 p=(1<<b)-1;state=4
 for _ in range(b-2):state=(state*state-2)%p
 assert state==0
 return p


def replay(b,n,K,A,m,s,expected,bits=None,use_box=False):
 p=prime_mersenne(b);missing=m-A;N=m-1;q=n-N;old=A-1;degree=K-1
 assert s==A-K-1 and 0<missing<m and q>0
 if not use_box:
  variances=[Q(A*(m-A),m-1)*Q(comb(m-1,j)*comb(m+j,j),(2*j+1)*comb(2*j,j)**2)
             for j in range(1,s+1)]
  volume=(Q(355,113)**(s//2)/factorial(s//2) if s%2==0 else
          Q(2**s*factorial((s-1)//2),factorial(s))*Q(355,113)**((s-1)//2))
  radicand=(s+2)**s*prod(v+Q(1,12) for v in variances)
  root=isqrt(radicand.numerator//radicand.denominator)
  if root*root<radicand:root+=1
  assert root*root>=radicand
  L0=ceilq(Q(comb(m,A))/(volume*root))
  L=ceilq(Q(A*L0,m));method='Independent binomial variance and integral sqrt upper bound'
 else:
  # Complement supports have the same moment ranges as full supports.
  ranges=[1+sum(comb(m-1-u,j)-comb(u,j) for u in range(missing)) for j in range(1,s+1)]
  L=ceilq(Q(comb(m-1,missing),prod(ranges)))
  method='Direct sums for complement moment ranges, no Gram bound'
 assert L>=2
 if b in (521,2203):assert L>p
 R=p-N
 # Cauchy over old support incidences, without integer occupancy rounding.
 residual=Q(degree)-Q(old*old,N)
 M=Q(L*R)/(R+L*residual+old-degree)
 assert 0<M<p
 U=p-1
 scale=1<<128;x=Q((M/U*scale).__floor__(),scale)
 polynomial=sum((Q(comb(q,j))*x**j for j in range(min(q,32)+1)),Q(0))
 density=Q(U,p)*(1-1/polynomial)
 if b==31:density=max(density,Q(ceilq(U*(1-(1-x)**q)),p))
 if bits is not None:assert n**(A-K)*2**(n+bits*(A-K))<p**(A-K)
 assert density>Q(expected)
 assert p>2*q and 2*comb(n,A)<p**(A-K)
 assert p**(A-K)*A**A*(n-A)**(n-A)>n**n
 if b==521:
  assert n**(A-K)*2**(n+255*(A-K)) < p**(A-K)
  # Full p-ary entropy inequality, independently of the sufficient guard.
  assert p**(n-K)*A**A*(n-A)**(n-A)>n**n*(p-1)**(n-A)
 return dict(b=b,n=n,K=K,A=A,verified_density_lower=expected,
             independent_count_method=method,full_entropy_checked=b==521)


def directions():
 p=17;old=range(1,7);new=(0,7,8,9);q=4;K=2;A=4
 bad=set()
 # Enumerate all forbidden direction vectors from the codewords, rather
 # than testing candidate directions as in verify_dense_padding.py.
 for intercept,slope in product(range(p),repeat=2):
  if intercept==slope==0:continue
  zeros=sum((intercept+slope*x)%p==0 for x in old)
  need=A-zeros
  if need>q:continue
  vals=[(intercept+slope*x)%p for x in new]
  for indices in combinations(range(q),need):
   if any(vals[j]==0 for j in indices):continue
   free=[j for j in range(q) if j not in indices]
   for fill in product(range(1,p),repeat=len(free)):
    g=vals[:]
    for j,v in zip(free,fill):g[j]=v
    bad.add(tuple(g))
 total=(p-1)**q
 union_bound=Q(comb(len(old)+q,A)*p**q,p**(A-K)*(p-1)**q)
 assert Q(len(bad),total)<=union_bound<1
 assert (1,1,1,2) not in bad and (1,1,1,1) in bad
 return dict(total_directions=total,bad_directions=len(bad),good_directions=total-len(bad),
             exact_bad_probability=str(Q(len(bad),total)),union_bound=str(union_bound))


def main():
 start=time.monotonic()
 out=dict(status='passed',direction_audit=directions(),
          independent_certificates=[replay(31,92,46,50,75,3,'0.74303810',1),
                                    replay(61,216,108,113,154,4,'0.91025173',10),
                                    replay(127,468,234,240,308,5,'0.96160200',40),
                                    replay(521,2800,1400,1411,1677,10,'0.99485642',255),
                                    replay(2203,21940,10970,10990,11895,19,'0.99999545',use_box=True),
                                    replay(2203,4128,2064,2066,2752,1,'0.93155073',126),
                                    replay(4423,26520,13260,13267,14144,6,'0.99999974',619),
                                    replay(9689,58110,29055,29062,30992,6,'0.99999970',1371)],
          scope='Far-point multiplicative p-1 label formula. Independent finite arithmetic and complete F17 direction counting. The all-prime asymptotic still rests on the written proof.')
 out['seconds']=time.monotonic()-start
 Path(__file__).with_name('density_independent_audit.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
