#!/usr/bin/env python3
"""Exhaustive global list profiles for small dimension-two RS codes.

Subtracting the unique affine polynomial interpolating a center's first two
coordinates normalizes those values to zero without changing any list size.
Thus p^(n-2) representatives cover every received word modulo the code.
"""
from itertools import product
from pathlib import Path
import json


def profile(p, domain):
    n = len(domain)
    a = n-2
    code = [tuple((b+c*x) % p for x in domain) for b in range(p) for c in range(p)]
    maximum = [0]*(a+1)
    attaining = [None]*(a+1)
    centers = 0
    for tail in product(range(p), repeat=n-2):
        center = (0, 0)+tail
        counts = [0]*(n+1)
        for word in code:
            distance = sum(x != y for x, y in zip(word, center))
            counts[distance] += 1
        cumulative = 0
        for radius in range(a+1):
            cumulative += counts[radius]
            if cumulative > maximum[radius]:
                maximum[radius] = cumulative
                attaining[radius] = center
        centers += 1
    expected = [1] + [(a-1)//(a-r) for r in range(1, a)]
    assert maximum[0] == 1
    assert all(maximum[r] >= expected[r] for r in range(a))
    return {'p':p,'domain':domain,'dimension':2,
            'normalized_centers_exhausted':centers,'codewords':len(code),
            'actual_global_maxima_by_radius_0_through_a':maximum,
            'generic_target_by_radius_0_through_a_minus_1':expected,
            'matches_generic_target':maximum[:a] == expected,
            'attaining_centers':attaining}


if __name__ == '__main__':
    fixtures = [profile(p, list(range(n))) for p,n in [(7,5),(7,6),(11,6),(13,6)]]
    result={'status':'passed','fixtures':fixtures,
            'scope':'True exhaustive global maxima on these small codes, not only a selected center. Small structured domains need not be generic.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
