"""Independent finite checks for the orbit count and incidence implementation."""
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path
import json
from certify_circle_product_dyadic import product_orbits,incidence_histogram,valuation


def main():
    cases=incidence_cases=0
    for m in (2,4,8,16):
        for k in range(m):
            counts=Counter();incidences={c:[0]*m for c in range(m)}
            for support in combinations(range(1,m),k):
                c=sum(support)%m;counts[c]+=1;incidences[c][0]+=1
                for a in support:incidences[c][a]+=1
            exact=product_orbits(m,k)
            assert [counts[c] for c in range(m)]==[exact[valuation(c,m)] for c in range(m)]
            for c in range(m):
                v=valuation(c,m)
                assert Counter(incidences[c])==dict(incidence_histogram(m,k+1,v))
                incidence_cases+=1
            cases+=1
    saved=json.loads(Path('exact_circle_product_classes.json').read_text())
    for row in saved['large']+[saved['toy']]:
        data=row.get('product_classes',row.get('classes'))
        m,h,c=(data[k] for k in ('M','h','product_exponent'))
        exact=product_orbits(m,h-1)
        assert data['all_class_counts']==[exact[valuation(j,m)] for j in range(m)]
        assert dict(incidence_histogram(m,h,valuation(c,m)))==Counter(data['incidences'])
    bound_checks=0
    for lm in range(1,11):
        m=1<<lm
        for k in range(1,m-1):
            K=comb(m//2-1,k//2)
            assert (m-1)*K<=comb(m-1,k)
            for ld in range(1,lm+1):
                L=1<<ld
                assert comb(m//L-1,k//L)<=K
            assert m*max(product_orbits(m,k))<=2*comb(m-1,k)
            bound_checks+=1
    result=dict(status='passed',exhaustive_parameter_cases=cases,
                exhaustive_incidence_histograms=incidence_cases,
                earlier_dynamic_program_certificates=len(saved['large'])+1,
                exact_two_average_bound_checks=bound_checks,
                note='Supports are exhaustively enumerated only for M<=16; saved larger cases came from a separate take-or-omit dynamic program.')
    Path('circle_product_orbits_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
