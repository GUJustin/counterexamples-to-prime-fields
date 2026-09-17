"""Exhaustively check normalized Riccati collinearity for small domains.

Enumerates every nonzero degree<=D polynomial supported on the domain,
with multiplicities, and every affine line containing >=3 image points.
"""
import importlib.util
from itertools import combinations_with_replacement
from collections import Counter
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('riccati_helpers', BASE/'verify.py')
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def normalized(poly, p):
    index = next(i for i, value in enumerate(poly) if value)
    return tuple(value*pow(poly[index], -1, p) % p for value in poly)


def verify(p, n, D):
    require(n > 4*D and p > n, 'hypotheses')
    domain = list(range(n))
    T = h.h.locator(domain, p)
    quotients = {x: h.divide(T, [-x % p, 1], p)[0] for x in domain}
    points, polynomials, monics = [], [], []
    for degree in range(D+1):
        for roots in combinations_with_replacement(domain, degree):
            Q = h.h.locator(roots, p)
            logarithmic = [0]
            for x, multiplicity in Counter(roots).items():
                logarithmic = h.add(logarithmic, h.scale(quotients[x], multiplicity, p), p)
            for scalar in range(1, p):
                P = h.scale(Q, scalar, p)
                R = h.subtract(P, logarithmic, p)
                require(h.mul(T, h.derivative(P, p), p) ==
                        h.mul(P, h.subtract(P, R, p), p), 'Riccati identity')
                matches = sum(h.evaluate(P, x, p) == h.evaluate(R, x, p) for x in domain)
                require(matches == n-len(set(roots)), 'exact agreement set')
                points.append(tuple(R + [0]*(n-len(R))))
                polynomials.append(P)
                monics.append(tuple(Q))
    require(len(set(points)) == len(points), 'injective image map')
    triples, pairs = 0, 0
    for i, R in enumerate(points):
        directions = {}
        for j in range(i+1, len(points)):
            difference = [(b-a) % p for a,b in zip(R, points[j])]
            direction = normalized(difference, p)
            pairs += 1
            if direction in directions:
                previous = directions[direction]
                require(monics[i] == monics[j] == monics[previous], 'proportionality on rich line')
                common = sum(all(h.evaluate(polynomials[t], x, p) ==
                                 h.evaluate(list(points[t]), x, p)
                                 for t in (i, j, previous)) for x in domain)
                require(common >= n-D, 'common correlated set')
                triples += 1
            else:
                directions[direction] = j
    return dict(p=p, n=n, D=D, candidates=len(points), pairs=pairs,
                collinear_triple_checks=triples)


if __name__ == '__main__':
    result = dict(status='PASS', fixtures=[verify(7,5,1), verify(11,9,2)])
    (BASE/'zero_branch_verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
