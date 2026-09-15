"""Exact audits of the uniform triangular-moment concentration bound."""
from fractions import Fraction as F
from math import comb, isqrt, prod
from itertools import combinations
from collections import Counter
from pathlib import Path
import json


def ceil_sqrt(x):
    r=isqrt(x.numerator//x.denominator)
    return r if r*r==x else r+1


def parameters(n,t,m,decorrelate):
    values=[[F(comb(a,j)) for a in range(n)] for j in range(1,m+1)]
    if decorrelate:
        assert m==2
        values[1]=[F(comb(a,2))-F(n-2,2)*a for a in range(n)]
    means=[sum(row)/n for row in values]
    variances=[F(t*(n-t),n-1)*(sum(x*x for x in row)/n-mu*mu)
               for row,mu in zip(values,means)]
    widths=[ceil_sqrt((m+2)*v) for v in variances]
    den=(m+2)*prod(2*h+1 for h in widths)
    bound=(2*comb(n,t)+den-1)//den
    return values,means,variances,widths,bound


fixtures=subsets=0
for n in range(4,13):
    for t in range(2,n):
        for m in range(1,min(t,5)):
            for decorrelate in ([False,True] if m==2 else [False]):
                values,means,vs,hs,bound=parameters(n,t,m,decorrelate)
                histogram=Counter()
                retained=0
                for A in combinations(range(n),t):
                    signature=tuple(sum(row[a] for a in A) for row in values)
                    histogram[signature]+=1
                    retained+=all(abs(x-t*mu)<=h for x,mu,h in zip(signature,means,hs))
                    subsets+=1
                C=comb(n,t)
                for j in range(m):
                    mu=t*means[j]
                    assert sum(count*(sig[j]-mu)**2 for sig,count in histogram.items())/C==vs[j]
                assert retained*(m+2)>=2*C
                box=[sig for sig in histogram if all(abs(x-t*mu)<=h for x,mu,h in zip(sig,means,hs))]
                assert len(box)<=prod(2*h+1 for h in hs)
                assert bound<=max(histogram.values())
                # Triangular signatures identify exactly the original moment classes.
                raw=Counter(tuple(sum(comb(a,j) for a in A) for j in range(1,m+1)) for A in combinations(range(n),t))
                assert sorted(raw.values())==sorted(histogram.values())
                if decorrelate:
                    assert vs==[F(t*(n-t)*(n+1),12),F(t*(n-t)*(n+1)*(n*n-4),720)]
                    assert sum(count*(sig[0]-t*means[0])*(sig[1]-t*means[1]) for sig,count in histogram.items())==0
                fixtures+=1
_,_,vs,hs,bound=parameters(64,34,2,True)
assert vs==[5525,376805] and hs==[149,1228] and bound==1102772374154
result=dict(status='passed',exhaustive_fixtures=fixtures,subset_visits=subsets,
            n64_variances=[int(x) for x in vs],n64_radii=hs,n64_list_lower_bound=bound,
            scope='Uniform interval-code concentration bound; no fixed-domain contest claim.')
Path(__file__).with_name('concentration_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
