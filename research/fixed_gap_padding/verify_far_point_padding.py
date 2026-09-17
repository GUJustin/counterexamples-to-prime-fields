"""Far-point padding: exact multiplicative averaging and prime-field certificates."""
from fractions import Fraction as F
from itertools import product
from math import comb,prod
from pathlib import Path
import json,time
from verify_average_padding import h,c
from verify_anchored_padding import locator,subtract,root_quotient,value


def fixture():
 p=17;m=7;N=6;K=2;A=4;q=4;n=N+q
 supports=[(0,1,2,6),(0,1,3,5),(0,2,3,4)]
 Fs=[locator(S,p) for S in supports]
 W=[0]*3+Fs[0][3:];w=root_quotient(W,0,p)
 Ps=[root_quotient(subtract(W,P,p),0,p) for P in Fs]
 old=list(range(1,m));L=len(Ps)
 assert all(sum(value(P,x,p)==value(w,x,p) for x in old)==A-1 for P in Ps)
 available=[x for x in range(p) if x not in old]
 images={x:{(value(P,x,p)-value(w,x,p))%p for P in Ps} for x in available}
 assert all(0 not in image for image in images.values())
 T=(K-1)*comb(L,2)-h.pairs(L*(A-1),N);R=p-N
 M=F(L*L*R,L*R+2*T)
 xs=sorted(available,key=lambda x:(-len(images[x]),x))[:q]
 expected=(p-1)*(1-prod(1-F(len(images[x]),p-1) for x in xs))
 guarantee=h.ceil((p-1)*(1-(1-M/(p-1))**q))
 total=maximum=0;chosen=None
 for gs in product(range(1,p),repeat=q):
  labels=set().union(*({v*pow(g,-1,p)%p for v in images[x]} for x,g in zip(xs,gs)))
  assert 0 not in labels
  total+=len(labels)
  if len(labels)>maximum:maximum=len(labels);chosen=(gs,labels)
 assert F(total,(p-1)**q)==expected and maximum>=guarantee
 gs,labels=chosen;domain=old+xs;f=[value(w,x,p) for x in domain];g=[0]*N+list(gs)
 codewords=list(product(range(p),repeat=K))
 profile=[max(sum(value(P,x,p)==(a+z*b)%p for x,a,b in zip(domain,f,g)) for P in codewords) for z in range(p)]
 assert profile[0]==A-1
 assert all(profile[z]>=A for z in labels)
 Fmasks=[sum((value(P,x,p)==v)<<j for j,(x,v) in enumerate(zip(domain,f))) for P in codewords]
 Gmasks=[sum((value(P,x,p)==v)<<j for j,(x,v) in enumerate(zip(domain,g))) for P in codewords]
 joint=max((a&b).bit_count() for a in Fmasks for b in Gmasks)
 assert joint<A
 return dict(p=p,n=n,K=K,A=A,directions_enumerated=(p-1)**q,exact_union_expectation=str(expected),
             guarantee=guarantee,largest_selected_union=maximum,full_agreement_profile=profile,
             all_nearby_labels=[z for z,a in enumerate(profile) if a>=A],far_point_agreement=profile[0],
             joint_agreement_max=joint,domain=domain,f=f,g=g,candidates=Ps)


def certificate(b,n,K,A,m,s,bits):
 p=h.lucas_lehmer(b);N=m-1;q=n-N;gap=A-K
 assert 2*K==n and s==gap-1 and K+1<A<m<n<p
 L0,_,_=h.gram_bound(m,A,s);L=h.ceil(F(A*L0,m))
 T=(K-1)*comb(L,2)-h.pairs(L*(A-1),N);assert T>=0
 R=p-N;M=F(L*L*R,L*R+2*T);U=p-1
 assert 0<M<=U
 assert p**gap*A**A*(n-A)**(n-A)>n**n
 scale=2**128;x=F((M/U*scale).__floor__(),scale)
 assert 0<x<=M/U
 partial=sum((F(comb(q,j))*x**j for j in range(min(q,64)+1)),F(0))
 density=F(U,p)*(1-1/partial)
 if b==31:density=max(density,F(h.ceil(U*(1-(1-M/U)**q)),p))
 J=h.ceil(p*density)
 assert 0<J<=p-1
 assert n**gap*2**(n+bits*gap)<p**gap
 assert density>F(1,2**bits)
 return dict(prime_exponent=b,n=n,K=K,A=A,seed_length=m,moments=s,q=q,
             anchored_list_lower=L,nearby_fraction_lower=c.decimal_lower(density,8),
             prescription_fraction_less_than_power_two=-bits,label_lower_bound=J,
             exact_far_agreement=A-1,strict_elias=True,
             scope='Far point z0, all guaranteed nearby parameters nonzero, no correlated agreement; no whole-line uniqueness.')


def main():
 start=time.monotonic()
 rows=[certificate(*r) for r in [(31,92,46,50,75,3,1),(61,216,108,113,154,4,10),
                                (127,468,234,240,308,5,40),(521,2800,1400,1411,1677,10,255)]]
 out=dict(status='passed',small_fixture=fixture(),finite_certificates=rows,seconds=time.monotonic()-start,
          scope='Far-point strengthening of dense padding. Uses p-1 multiplicative label universe; exact small-field exhaustion and exact finite density/Elias/prescription certificates. The small F17 fixture is a mechanism check, not an Elias claim.')
 Path(__file__).with_name('far_point_padding_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
