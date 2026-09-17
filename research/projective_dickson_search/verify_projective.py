"""Independent coefficient expansion and small exhaustive cross-check."""
from pathlib import Path
from math import comb
from fractions import Fraction as Q
from itertools import combinations
import json
from verify_samples import interpolate,evaluate


def multiply(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return c


def transform(seed,matrix,p):
    a,b,c,d=matrix;D=len(seed)-1
    left=[[1]];right=[[1]]
    for j in range(D):
        left.append(multiply(left[-1],[b,a],p))
        right.append(multiply(right[-1],[d,c],p))
    out=[0]*(D+1)
    for j,co in enumerate(seed):
        term=multiply(left[j],right[D-j],p)
        for t,v in enumerate(term):out[t]=(out[t]+co*v)%p
    return tuple(out)


def word(p):
    n=p-1;k=n//4
    return {x:((1+(1 if pow(x,n//2,p)==1 else -1))//2-pow(x,k,p))%p for x in range(1,p)}


def main():
    base=Path(__file__).resolve().parent
    checked=0;results=[]
    for name in ('search.json','affine_search.json'):
        data=json.loads((base/name).read_text())
        for row in data['fixtures']:
            p=row['p'];k=row['k'];w=word(p)
            seed=[comb(2*k+1,2*j+1)%p for j in range(k)]
            polynomials=set()
            for rec in row['candidates']:
                a,b,c,d=rec['matrix'];assert (a*d-b*c)%p
                v=[x*rec['scale']%p for x in transform(seed,rec['matrix'],p)]
                v[0]=(v[0]+rec.get('shift',0))%p
                assert sum(evaluate(v,x,p)==y for x,y in w.items())==rec['agreements']
                polynomials.add(tuple(v));checked+=1
            assert len(polynomials)==row['distinct_candidates_at_threshold']
            results.append(dict(file=name,p=p,distinct_verified=len(polynomials)))

    # Independently exhaust the complete F17 RS list by determining supports.
    p=17;k=4;w=word(p);nearest=set()
    for xs in combinations(range(1,p),k):
        c=interpolate(xs,[w[x] for x in xs],p)
        A=sum(evaluate(c,x,p)==y for x,y in w.items())
        assert A<=6
        if A==6:nearest.add(c)
    assert len(nearest)==22
    seed=[comb(9,2*j+1)%17 for j in range(4)]
    scalar_orbit=set();affine_orbit=set()
    matrices=[(a,b,0,1) for a in range(1,p) for b in range(p)]
    matrices += [(a,b,1,d) for d in range(p) for a in range(p) for b in range(p) if b!=a*d%p]
    assert len(matrices)==p*(p*p-1)
    # Check which complete-list candidates can be scalar/projective images,
    # allowing a constant output translation in the second comparison.
    for m in matrices:
        c=transform(seed,m,p)
        for t in range(1,p):
            scaled=tuple(t*v%p for v in c)
            if scaled in nearest:scalar_orbit.add(scaled)
            for target in nearest:
                if target[1:]==scaled[1:]:affine_orbit.add(target)
    assert len(scalar_orbit)==8 and len(affine_orbit)==14

    expectations=[]
    for p in (17,41,73,89,97,113,137,193,257):
        n=p-1;k=n//4;A=3*n//8
        expected=sum(Q(comb(n,j)*(p-1)**(n-j),p**(n-k)) for j in range(A,n+1))
        expectations.append(dict(p=p,n=n,k=k,A=A,mean_list_size_numerator=expected.numerator,
                                 mean_list_size_denominator=expected.denominator,
                                 mean_list_size_decimal=float(expected)))
    result=dict(status='passed',coefficient_replays=checked,fixtures=results,
                exhaustive_p17_list=22,independent_p17_scalar_orbit=8,
                independent_p17_affine_orbit=14,random_word_exact_expectations=expectations,
                scope='Saved candidate certificates and an independent exhaustive small orbit check. Random-word means are an exact baseline, not predictions for the specified structured word.')
    (base/'projective_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='random_word_exact_expectations'},indent=2))


if __name__=='__main__':main()
