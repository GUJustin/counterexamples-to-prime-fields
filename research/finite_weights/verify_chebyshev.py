"""Verify finite certificates using exact arithmetic and independent identities."""
from pathlib import Path
from collections import defaultdict, Counter
from itertools import combinations
from math import comb
import json
import sys

ROOT = Path(__file__).parent
sys.path.insert(0,str(ROOT.parent.parent/'moment_certificates'))
from compute_moments import moments, centered

saved = json.loads((ROOT/'moments40.json').read_text())
assert (saved['n'],saved['t'],saved['q'],saved['center'],saved['degree']) == (64,34,1071,22138,40)
assert len(saved['raw_moments']) == len(saved['centered_moments']) == saved['degree']+1
old = json.loads((ROOT.parent.parent/'moment_certificates/exact_moments.json').read_text())
assert saved['raw_moments'][:21] == old['raw_moments']
assert saved['centered_moments'][:21] == old['centered_moments']
degree = saved['degree']
cases = subsets = classes = 0
for n in range(4,11):
    for t in range(2,n):
        direct = defaultdict(Counter)
        for A in combinations(range(n),t):
            direct[sum(A)][sum(comb(a,2) for a in A)] += 1
            subsets += 1
        calculated,_ = moments(n,t,t*(n-1),degree)
        assert set(calculated) == set(direct)
        for q,h in direct.items():
            exact = [sum(count*y**j for y,count in h.items()) for j in range(degree+1)]
            assert exact == calculated[q]
            classes += 1
        cases += 1
n,t,q,c = [saved[k] for k in ['n','t','q','center']]
complement,_ = moments(n,n-t,comb(n,2)-q,degree)
assert centered(complement[comb(n,2)-q],comb(n,3)-c) == [
    (-1)**j*m for j,m in enumerate(saved['centered_moments'])]

# Independently recover the exact support endpoints via an extrema DP.
extrema = [{} for _ in range(t+1)]
extrema[0][0] = (0,0)
for a in range(n):
    b = comb(a,2)
    for size in range(min(t,a+1),0,-1):
        for total,(low,high) in extrema[size-1].items():
            target = total+a
            if target > q:
                continue
            old_pair = extrema[size].get(target)
            new_pair = (low+b,high+b)
            if old_pair is not None:
                new_pair = (min(old_pair[0],new_pair[0]),max(old_pair[1],new_pair[1]))
            extrema[size][target] = new_pair
verified = []
for cert in json.loads((ROOT/'chebyshev_certificates.json').read_text()):
    assert (cert['low'],cert['high']) == extrema[t][q]
    coeff = cert['coefficients_ascending']
    assert cert['center'] == c
    assert isinstance(cert['degree'],int) and 0 <= cert['degree'] <= degree
    assert len(coeff) == cert['degree']+1
    assert all(isinstance(a,int) for a in coeff) and coeff[-1] != 0
    def evaluate(x):
        value = 0
        for a in reversed(coeff):
            value = value*x+a
        return value
    lo,hi = cert['low']-c,cert['high']-c
    for x in [lo,-1,0,1,hi]:
        assert evaluate(x) == sum(a*x**j for j,a in enumerate(coeff))
    numerator = sum(a*m for a,m in zip(coeff,saved['centered_moments']))
    denominator = sum(max(0,evaluate(x)) for x in range(lo,hi+1))
    assert numerator == cert['numerator'] > 0
    assert denominator == cert['denominator'] > 0
    bound = (numerator+denominator-1)//denominator
    assert bound == cert['list_lower_bound']
    verified.append(dict(degree=cert['degree'],list_lower_bound=bound))
result = dict(status='passed',moment_degree=degree,
    exhaustive_parameter_pairs=cases,exhaustive_subsets=subsets,
    exhaustive_conditional_classes=classes,independent_complement_identity=True,
    independent_support_extrema=True,previous_moments_match=True,
    certificates=verified,best_list_lower_bound=max(v['list_lower_bound'] for v in verified),
    scope='Pure integer subset counts; no claim about any fixed protocol or contest submission.')
(ROOT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
