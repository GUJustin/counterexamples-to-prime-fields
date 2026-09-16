"""Exact anchored product fibers, incidences, and strengthened circle banks."""
from math import comb
from pathlib import Path
import json
from check_circle_collisions import minimum_pairs,bank_from_pairs,certificate

ROOT=Path(__file__).resolve().parent

def product_classes(m,h):
    # Root 1 is fixed. Exponents 1,...,m-1 index the remaining roots.
    rows=[[0]*m for _ in range(h)]
    rows[0][0]=1
    for a in range(1,m):
        for k in range(min(a,h-1),0,-1):
            old=rows[k-1];new=rows[k]
            for c,value in enumerate(old):
                if value:new[(c+a)%m]+=value
    assert sum(rows[h-1])==comb(m-1,h-1)
    N=max(rows[h-1]);targets=[c for c,v in enumerate(rows[h-1]) if v==N]
    target=targets[0]
    incidences=[N]
    for a in range(1,m):
        # Divide the generating polynomial by (1+z*u^a).
        # Only the one coefficient needed at each stage is followed, giving
        # sum_{j=0}^{h-2} (-1)^j rows[h-2-j][target-(j+1)*a].
        value=sum((-1)**j*rows[h-2-j][(target-(j+1)*a)%m] for j in range(h-1))
        assert 0<=value<=N
        incidences.append(value)
    assert sum(incidences)==N*h
    return dict(M=m,h=h,N=N,product_exponent=target,
                maximizing_product_exponents=targets,
                all_class_counts=rows[h-1],incidences=incidences)

def strengthened(p,m,h,d,N,ext,incidences=None):
    if incidences is None:
        a,e=divmod(N*(h-1),m-1)
        bins=[N]+[a]*(m-1-e)+[a+1]*e
    else:
        bins=incidences
        assert len(bins)==m and bins[0]==N and sum(bins)==N*h
    on_G=sum(comb(s,2)+minimum_pairs(N-s,p-1) for s in bins)
    on_rest=(p+1-m)*minimum_pairs(N,p)
    budget=d*comb(N,2)-on_G-on_rest
    assert budget>=0
    poles=p*p-p-1 if ext==2 else p**4-p*p
    pairs=budget//poles
    J=bank_from_pairs(N,pairs)
    return dict(N=N,J=J,on_G_lower=on_G,on_unit_rest_lower=on_rest,
                off_circle_pair_budget=budget,poles=poles,some_pole_pairs=pairs,
                exact_incidences=incidences is not None)

def main():
    out=[];p=2**31-1
    for m,h in [(64,19),(64,35),(128,19),(512,11)]:
        exact=product_classes(m,h);N=exact['N'];d=h-2
        avg=(comb(m-1,h-1)+m-1)//m
        old=certificate(p,m,h,d,avg,2)
        joint_only=strengthened(p,m,h,d,avg,2)
        full=strengthened(p,m,h,d,N,2,exact['incidences'])
        out.append(dict(p=p,product_classes=exact,average_N=avg,
                        previous_bank=int(old['new_bank']),joint_only=joint_only,full=full))
    toy=product_classes(16,9)
    small=strengthened(31,16,9,7,toy['N'],2,toy['incidences'])
    result=dict(status='computed_pending_independent_check',large=out,toy=dict(classes=toy,certificate=small))
    (ROOT/'exact_circle_product_classes.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps([dict(M=r['product_classes']['M'],h=r['product_classes']['h'],
                          N=r['product_classes']['N'],previous_bank=r['previous_bank'],
                          joint_only=r['joint_only']['J'],full=r['full']['J']) for r in out],indent=2),flush=True)
    print('toy',small,flush=True)

if __name__=='__main__':main()
