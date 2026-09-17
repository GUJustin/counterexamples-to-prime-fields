"""Independent complete interpolation check of a below-Elias exception."""
from pathlib import Path
from itertools import combinations
import json
from verify_unique_padding import interpolate
from verify_anchored_padding import value


def main():
    p,n,K,A=97,32,4,8
    nodes=[pow(19,i,p) for i in range(n)]
    assert len(set(nodes))==n and all(pow(x,n,p)==1 for x in nodes)
    W=[0]*9;W[4]=23;W[8]=1
    ys=[value(W,x,p) for x in nodes]
    pool=set()
    for indices in combinations(range(n),K):
        pool.add(interpolate([nodes[i] for i in indices],[ys[i] for i in indices],p))
    nearby=[]
    for P in sorted(pool):
        support=[i for i,x in enumerate(nodes) if value(P,x,p)==ys[i]]
        if len(support)>=A:
            nearby.append(dict(coefficients=list(P),support_indices=support))
    assert [row['coefficients'] for row in nearby]==[[8,0,16,0],[8,0,81,0],[75,0,0,0]]
    assert all(len(row['support_indices'])==A for row in nearby)
    assert n**n*(p-1)**(n-A)<(n-A)**(n-A)*A**A*p**(n-K)
    delta=[int(i in nearby[0]['support_indices'])-int(i in nearby[2]['support_indices']) for i in range(n)]
    # The characteristic-zero theorem requires q=4 periodic differences.
    assert any(delta[i]!=delta[(i+4)%n] for i in range(n))
    supports={tuple(row['support_indices']) for row in nearby[:2]}
    assert {tuple(sorted((i+8)%n for i in row['support_indices'])) for row in nearby[:2]}==supports
    assert all(tuple(sorted((i+16)%n for i in row['support_indices']))==tuple(row['support_indices']) for row in nearby[:2])
    result=dict(status='PASS',p=p,n=n,K=K,A=A,domain=nodes,
                received_coefficients=W,entire_list=nearby,
                determining_subsets=35960,distinct_interpolants=len(pool),
                strict_Elias=True,nonconstant_rotation_orbit_size=2,
                scope='Exact entire list and a finite-characteristic failure of the characteristic-zero support classification; not a violation of its uniform central-binomial bound, not a growing-length family.')
    Path(__file__).with_name('subgroup_exception_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
