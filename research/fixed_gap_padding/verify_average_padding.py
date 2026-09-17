"""Exact averaged-padding certificates and exhaustive small-field checks."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from collections import defaultdict
from math import comb,prod
import importlib.util,json,time
from verify_anchored_padding import locator,subtract,root_quotient,value,prime
BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('coeff',BASE.parent/'prime_exponent_coefficients/verify.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
h=c.h


def bound(p,N,K,A,q,L,D):
 assert 0<N<p and 1<=q<=p-N and K<A and K-1+q<A and A-1<=N
 T=D*comb(L,2)-h.pairs(L*(A-1),N)
 assert T>=0
 R=p-N;M=F(L*L*R,L*R+2*T)
 assert 0<M<=min(L,p)
 expected=p*(1-(1-M/p)**q)
 return h.ceil(expected),T,M,expected


def certificate(b,m,k,t):
 p=h.lucas_lehmer(b);s=t-k;N=m-1;K=k-1;A=t;q=s+1;n=N+q;D=k-2
 assert 1<=s and 2<=k<t<m<p
 L0,vs,den=h.gram_bound(m,t,s)
 L=h.ceil(F(t*L0,m))
 J,T,M,expected=bound(p,N,K,A,q,L,D)
 assert p**q*A**A*(n-A)**(n-A)>n**n
 ratio=F(J**q*K**K*(n-K)**(n-K),n**(n+q))
 lo,hi=c.narrow_log2(ratio);lo/=q;hi/=q
 assert (lo*10**5).__floor__()==(hi*10**5).__floor__()
 return dict(prime_exponent=b,p=p,seed_length=m,seed_dimension=k,seed_threshold=t,
             n=n,K=K,A=A,q=q,seed_list_lower=L0,anchored_list_lower=L,
             pair_collision_budget=T,average_image_lower=str(M),
             label_lower_bound=J,excess_bits_lower=c.decimal_lower(lo),
             exact_elias_sufficient_check=True,
             gram_denominator_numerator_sha256=c.digest_integer(den.numerator),
             gram_denominator_denominator_sha256=c.digest_integer(den.denominator))


def small_fixture(m,k,t,p):
 assert prime(p) and p>m
 s=t-k;q=s+1;N=m-1;K=k-1;A=t
 groups=defaultdict(list)
 for rest in combinations(range(1,m),t-1):
  S=(0,)+rest
  groups[tuple(sum(x**j for x in S) for j in range(1,s+1))].append(S)
 supports=max(groups.values(),key=len);L=len(supports)
 assert L>=2
 Fs=[locator(S,p) for S in supports]
 assert all(P[k:]==Fs[0][k:] for P in Fs)
 W=[0]*k+Fs[0][k:];Gs=[subtract(W,P,p) for P in Fs]
 w=root_quotient(W,0,p);Ps=[root_quotient(G,0,p) for G in Gs]
 old=list(range(1,m));D=k-2
 assert len(w)-1==A-1 and all(len(P)-1<K for P in Ps)
 assert all(sum(value(P,x,p)==value(w,x,p) for x in old)==A-1 for P in Ps)
 J,T,M,_=bound(p,N,K,A,q,L,D)
 available=[x for x in range(p) if x not in old]
 images={x:{value(P,x,p) for P in Ps} for x in available}
 collisions=sum(sum(a==b for a,b in combinations([value(P,x,p) for P in Ps],2)) for x in available)
 assert collisions<=T and F(sum(map(len,images.values())),len(available))>=M
 xs=sorted(available,key=lambda x:(-len(images[x]),x))[:q]
 exact_expectation=p*(1-prod(1-F(len(images[x]),p) for x in xs))
 assert exact_expectation>=p*(1-(1-M/p)**q)
 maximum=0;total=0;chosen=None
 for bs in product(range(p),repeat=q):
  labels=set().union(*({(v-b)%p for v in images[x]} for x,b in zip(xs,bs)))
  total+=len(labels)
  if len(labels)>maximum:maximum=len(labels);chosen=(bs,labels)
 assert F(total,p**q)==exact_expectation and maximum>=J
 bs,labels=chosen;domain=old+xs;f=[value(w,x,p) for x in old]+list(bs);g=[0]*N+[1]*q
 for z in labels:
  assert any(sum(value(P,x,p)==(y+z*d)%p for x,y,d in zip(domain,f,g))>=A for P in Ps)
 # Exhaust every codeword pair, including unselected candidates.
 assert K<=2
 codewords=[list(P) for P in product(range(p),repeat=K)]
 Fmasks=[sum((value(P,x,p)==y)<<j for j,(x,y) in enumerate(zip(domain,f))) for P in codewords]
 Gmasks=[sum((value(P,x,p)==y)<<j for j,(x,y) in enumerate(zip(domain,g))) for P in codewords]
 jointmax=max((u&v).bit_count() for u in Fmasks for v in Gmasks)
 assert jointmax<A and jointmax<=max(A-1,K-1+q)
 return dict(p=p,m=m,k=k,t=t,L=L,q=q,guarantee=J,maximum_union=maximum,
             offsets_tested=p**q,joint_pairs_tested=p**(2*K),joint_agreement_max=jointmax,
             padding_points=xs,offsets=list(bs),labels=sorted(labels))


def main():
 start=time.monotonic()
 small=[small_fixture(7,3,4,17),small_fixture(9,3,5,17)]
 discoveries=json.loads((BASE/'average_padding_search.json').read_text())['best']
 rows=[]
 for b in (31,61,127,521):
  # Replay a few close finalists to protect against approximate ranking.
  candidates=[certificate(b,r['m'],r['k'],r['t']) for r in discoveries[str(b)][:3]]
  rows.append(max(candidates,key=lambda r:F(r['excess_bits_lower'])))
 result=dict(status='passed',small_fixtures=small,finite_certificates=rows,seconds=time.monotonic()-start,
             scope='Exact existence certificates for arbitrary padded domains, with actual ordinary correlated-agreement failure. Count-ratio comparison assumes c1=c2=1; no protocol attack, prescribed subgroup, optimality or uniqueness claim.')
 (BASE/'average_padding_verification.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(dict(status='passed',small_fixtures=small,certificates=[{k:r[k] for k in ('prime_exponent','n','K','A','label_lower_bound','excess_bits_lower')} for r in rows],seconds=result['seconds']),indent=2))
if __name__=='__main__':main()
