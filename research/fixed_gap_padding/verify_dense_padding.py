"""Exhaustive small-field check of the direction union bound and dense padding."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
from math import comb,prod
import json,time
from verify_anchored_padding import locator,subtract,root_quotient,value
from verify_average_padding import h


def main():
 start=time.monotonic();p=17;m=7;N=6;K=2;A=4;q=4;n=N+q
 assert comb(n,A)*p**q < p**(A-K)*(p-1)**q
 supports=[(0,1,2,6),(0,1,3,5),(0,2,3,4)]
 Fs=[locator(S,p) for S in supports]
 assert all(P[3:]==Fs[0][3:] for P in Fs)
 W=[0]*3+Fs[0][3:];w=root_quotient(W,0,p)
 Ps=[root_quotient(subtract(W,P,p),0,p) for P in Fs]
 old=list(range(1,m));L=len(Ps);d=K-1
 assert all(sum(value(P,x,p)==value(w,x,p) for x in old)==A-1 for P in Ps)
 R=p-N;T=d*comb(L,2)-h.pairs(L*(A-1),N);M=F(L*L*R,L*R+2*T)
 J=h.ceil(p*(1-(1-M/p)**q))
 available=[x for x in range(p) if x not in old]
 images={x:{value(P,x,p) for P in Ps} for x in available}
 xs=sorted(available,key=lambda x:(-len(images[x]),x))[:q]
 domain=old+xs;codewords=list(product(range(p),repeat=K))
 nonzero=[P for P in codewords if any(P)]
 oldzeros={P:sum(value(P,x,p)==0 for x in old) for P in nonzero}
 values={P:[value(P,x,p) for x in xs] for P in nonzero}
 directions_tested=0
 for gs in product(range(1,p),repeat=q):
  directions_tested+=1
  if all(oldzeros[P]+sum(a==b for a,b in zip(values[P],gs))<A for P in nonzero):break
 else:raise AssertionError('No good direction')
 g=[0]*N+list(gs)
 assert max(sum(value(P,x,p)==v for x,v in zip(domain,g)) for P in nonzero)<A
 maximum=total=0;chosen=None
 for bs in product(range(p),repeat=q):
  labels=set().union(*({(v-b)*pow(gj,-1,p)%p for v in images[x]} for x,b,gj in zip(xs,bs,gs)))
  total+=len(labels)
  if len(labels)>maximum:maximum=len(labels);chosen=(bs,labels)
 expected=p*(1-prod(1-F(len(images[x]),p) for x in xs))
 assert F(total,p**q)==expected and maximum>=J
 bs,labels=chosen;f=[value(w,x,p) for x in old]+list(bs)
 for z in labels:
  assert any(sum(value(P,x,p)==(a+z*b)%p for x,a,b in zip(domain,f,g))>=A for P in Ps)
 Fmasks=[sum((value(P,x,p)==v)<<j for j,(x,v) in enumerate(zip(domain,f))) for P in codewords]
 Gmasks=[sum((value(P,x,p)==v)<<j for j,(x,v) in enumerate(zip(domain,g))) for P in codewords]
 joint=max((a&b).bit_count() for a in Fmasks for b in Gmasks)
 assert joint<A
 out=dict(status='passed',p=p,n=n,K=K,A=A,q=q,old_padding_condition_fails=K-1+q>=A,
          union_bound=str(F(comb(n,A)*p**q,p**(A-K)*(p-1)**q)),
          direction_candidates_tested=directions_tested,direction_values=list(gs),
          offsets_tested=p**q,joint_pairs_tested=p**(2*K),guaranteed_labels=J,
          maximum_selected_label_union=maximum,joint_agreement_max=joint,
          domain=domain,f=f,g=g,candidates=Ps,labels=sorted(labels),seconds=time.monotonic()-start,
          scope='Exact small-field mechanism check. Asymptotic density uses the written proof, not this finite example.')
 Path(__file__).with_name('dense_padding_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
