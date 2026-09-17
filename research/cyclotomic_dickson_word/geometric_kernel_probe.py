"""Bounded split-prime exclusion test for constant-numerator deleted kernels."""
import itertools,json
from collections import Counter
from pathlib import Path
import sympy as sp

rows=[]
for r in [11,19,23,31]:
    p=4*r*((1000000+4*r-1)//(4*r))+1
    while not sp.isprime(p): p+=4*r
    z=pow(int(sp.primitive_root(p)),(p-1)//(4*r),p)
    roots=[pow(z,4*j,p) for j in range(r)]
    nodes=[pow(z,j,p) for j in range(4*r) if j%4]
    weights=[(pow(x,r,p)-1)*pow(2,-1,p)%p for x in nodes]
    differences=[[(x-a)%p for x in nodes] for a in roots]
    for t in range(1,6):
        best=0;witness=None;tested=0
        for tail in itertools.combinations(range(1,r),t-1):
            indices=(0,)+tail
            vals=weights.copy()
            for j in indices:
                vals=[a*b%p for a,b in zip(vals,differences[j])]
            c,extra=Counter(vals).most_common(1)[0]
            assert c
            tested+=1
            if extra>best: best=extra;witness=dict(indices=indices,c=c)
        rows.append(dict(r=r,t=t,p=p,root=z,anchored_supports=tested,
                         max_modular_agreement=r-t+best,witness=witness))
print(json.dumps(rows,indent=2))
Path(__file__).with_name('geometric_kernel_probe.json').write_text(json.dumps(rows,indent=2)+'\n')
