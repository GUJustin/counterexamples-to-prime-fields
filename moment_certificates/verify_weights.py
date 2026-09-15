"""Verify polynomial-weight list certificates using only exact arithmetic."""
from collections import defaultdict, Counter
from itertools import combinations
from math import comb, prod
from pathlib import Path
import json
from compute_moments import moments, centered


def conditional_extrema(n, t, qmax):
    """Recompute second-moment support without using saved moment metadata."""
    rows = [{} for _ in range(t + 1)]
    rows[0][0] = (0, 0)
    for a in range(n):
        shift = comb(a, 2)
        for size in range(min(t, a + 1), 0, -1):
            for q, (low, high) in rows[size - 1].items():
                target = q + a
                if target > qmax:
                    continue
                candidate = (low + shift, high + shift)
                previous = rows[size].get(target)
                rows[size][target] = candidate if previous is None else (
                    min(previous[0], candidate[0]),
                    max(previous[1], candidate[1]))
    return rows[t]


root=Path(__file__).parent
saved=json.loads((root/'exact_moments.json').read_text())
degree=saved['degree']
assert len(saved['raw_moments']) == len(saved['centered_moments']) == degree + 1
cases=subsets=classes=0
for n in range(4,14):
    for t in range(3,n):
        hist=defaultdict(Counter)
        for A in combinations(range(n),t):
            hist[sum(A)][sum(comb(a,2) for a in A)]+=1
            subsets+=1
        actual,_=moments(n,t,t*(n-1),degree)
        extrema=conditional_extrema(n,t,t*(n-1))
        assert set(actual)==set(hist)
        assert set(extrema)==set(hist)
        for q,h in hist.items():
            assert extrema[q] == (min(h), max(h))
            direct=[sum(count*y**j for y,count in h.items()) for j in range(degree+1)]
            assert actual[q]==direct
            # Exercise signed weights with positive and negative regions.
            for zeros in [[0,3],[1,4,7,9],[0,2,4,6,8,10]]:
                lo,hi=min(h),max(h)
                den=sum(max(0,-prod(y-z for z in zeros)) for y in range(lo,hi+1))
                num=sum(count*(-prod(y-z for z in zeros)) for y,count in h.items())
                if den:
                    assert num<=max(h.values())*den
            classes+=1
        cases+=1

rows,updates=moments(saved['n'],saved['t'],saved['q'],degree)
assert rows[saved['q']]==saved['raw_moments']
assert centered(rows[saved['q']],saved['center'])==saved['centered_moments']
old=json.loads((root.parent/'checks/conditional_moment_results.json').read_text())
assert (old['certificate']['n'], old['certificate']['t']) == (saved['n'], saved['t'])
oldrow=next(r for r in old['certificate']['first_moment_classes'] if r['first_moment']==saved['q'])
assert saved['raw_moments'][:3]==[oldrow['count'],oldrow['sum_second_moments'],oldrow['sum_squared_second_moments']]
support_low,support_high=conditional_extrema(saved['n'],saved['t'],saved['q'])[saved['q']]
assert (oldrow['second_min'],oldrow['second_max']) == (support_low,support_high)

# Independent complementary-subset identity checks every high moment:
# sum binom(a,2) over all n elements is binom(n,3).
n,t,q=saved['n'],saved['t'],saved['q']
complement,_=moments(n,n-t,comb(n,2)-q,degree)
complement_center=comb(n,3)-saved['center']
cm=centered(complement[comb(n,2)-q],complement_center)
assert cm==[(-1)**j*v for j,v in enumerate(saved['centered_moments'])]

verified=[]
for item in json.loads((root/'weight_certificates.json').read_text()):
    assert item['center'] == saved['center']
    assert (item['low'],item['high']) == (support_low,support_high)
    assert 0 <= item['degree'] <= degree
    for label,cert in [('expanded',item),('factored',item.get('factored'))]:
        if cert is None:
            continue
        coeff=cert['coefficients_ascending']
        assert len(coeff) == item['degree'] + 1 and coeff[-1] != 0
        def evaluate(z):
            val=0
            for c in reversed(coeff):
                val=val*z+c
            return val
        support=range(item['low']-item['center'],item['high']-item['center']+1)
        if label=='factored':
            assert len(cert['roots']) == item['degree']
            expanded=[cert['leading_coefficient']]
            for zero in cert['roots']:
                product_coefficients=[0]*(len(expanded)+1)
                for j,value in enumerate(expanded):
                    product_coefficients[j] -= zero*value
                    product_coefficients[j+1] += value
                expanded=product_coefficients
            assert expanded == coeff
            assert all(evaluate(z)==cert['leading_coefficient']*prod(z-r for r in cert['roots']) for z in support)
        numerator=sum(a*m for a,m in zip(coeff,saved['centered_moments']))
        denominator=sum(max(0,evaluate(z)) for z in support)
        bound=(numerator+denominator-1)//denominator
        assert numerator==cert['numerator'] and denominator==cert['denominator']
        assert bound==cert['list_lower_bound'] and denominator>0
        verified.append(dict(degree=item['degree'],form=label,list_lower_bound=bound))
result=dict(status='passed',exhaustive_parameter_pairs=cases,exhaustive_subsets=subsets,
    exhaustive_conditional_classes=classes,moment_degree=degree,
    independent_complement_identity=True,exact_certificates=verified,
    best_list_lower_bound=max(r['list_lower_bound'] for r in verified),
    scope='Integer-moment list lower bounds; no claim about a fixed Koala NTT code or a contest score.')
(root/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
