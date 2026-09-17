"""Independent exact enlarged-code witness checks; lower bounds are algebraic."""
from itertools import combinations,product
from math import prod
from pathlib import Path
import json
rows=[]
for p,r,D in [(17,1,3),(19,1,4),(37,2,8)]:
    pad=list(range(1,r+1)); core=list(range(r+1,(p+1)//2))
    domain=[x for a in core+pad for x in (a,p-a)]
    H=lambda A,x:prod((x*x-a*a)%p for a in A)%p
    images={tuple(H(A,x) for x in pad):A for A in combinations(core,D)}
    assert len(images)==(p-1)**r
    ref=core[:D]; w=[H(ref,x) for x in domain]; n=len(domain);k=2*D
    assert sum(a==0 for a in w)==k
    count=0
    for zs in product(range(p),repeat=r):
        A=images[tuple((-z)%p if z else 1 for z in zs)]
        P=[(v-H(A,x))%p for v,x in zip(w,domain)]
        received=w[:]
        for j,z in enumerate(zs):
            for i in (2*len(core)+2*j,2*len(core)+2*j+1):received[i]=(received[i]+z)%p
        assert sum(u!=v for u,v in zip(received,P))==n-k-2*sum(z!=0 for z in zs)
        count+=1
    rows.append(dict(p=p,n=n,k=k,r=r,parameters_checked=count,far_distance=n-k,status='passed'))
out={'scope':'Upper bounds via exact witnesses; lower bounds via degree-k root counting, not exhaustive enlarged-code enumeration. No below-Elias assertion.','rows':rows}
Path(__file__).with_name('geometry_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
