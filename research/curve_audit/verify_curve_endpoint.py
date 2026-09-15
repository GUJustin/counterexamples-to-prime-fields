#!/usr/bin/env python3
"""Exact endpoint sharpness checks; pure finite-field coding theory."""
import json
from itertools import combinations, product
from math import comb
from pathlib import Path


def evaluate(coefficients, x, p):
    value = 0
    for coefficient in reversed(coefficients):
        value = (value*x+coefficient) % p
    return value


def vanishing_values(subset, domain, p):
    result = []
    for x in domain:
        value = 1
        for a in subset:
            value = value*(x-a) % p
        result.append(value)
    return tuple(result)


def main():
    fixtures = [(4, 2, 2, 13, 10), (4, 2, 3, 31, 15),
                (4, 2, 4, 61, 59), (4, 2, 5, 151, 15),
                (5, 2, 2, 79, 3), (5, 3, 3, 31, 0)]
    results = []
    for n, k, e, p, shift in fixtures:
        assert all(p % d for d in range(2, int(p**0.5)+1))
        assert p % e == 1
        domain = [2**i for i in range(n)]
        subsets = list(combinations(range(n), k+1))
        labels = {sum(domain[i] for i in support) % p: support
                  for support in subsets}
        assert len(labels) == comb(n, k+1)
        assert shift not in labels
        fibers = {label: [z for z in range(p)
                          if (pow(z, e, p)+shift) % p == label]
                  for label in labels}
        assert all(len(fiber) == e for fiber in fibers.values())
        codewords = [tuple(evaluate(c, x, p) for x in domain)
                     for c in product(range(p), repeat=k)]
        anchor = domain[:k]
        anchor_sum = sum(anchor)
        anchor_vanishing = vanishing_values(anchor, domain, p)
        nearby = concurrency = distance_checks = 0
        for z in range(p):
            h = (pow(z, e, p)+shift) % p
            received = tuple((pow(x, k+1, p)-h*pow(x, k, p)) % p
                             for x in domain)
            attained_curve = tuple(
                (pow(x, k+1, p)-(x+anchor_sum)*v
                 +h*(v-pow(x, k, p))) % p
                for x, v in zip(domain, anchor_vanishing))
            witnesses = []
            for codeword in codewords:
                support = tuple(i for i in range(n)
                                if received[i] == codeword[i])
                distance_checks += 1
                if len(support) >= k+1:
                    witnesses.append((codeword, support))
            assert len(witnesses) == (1 if h in labels else 0)
            if witnesses:
                witness, support = witnesses[0]
                assert support == labels[h]
                assert len(support) == k+1
                nearby += 1
                concurrency += witness == attained_curve
        assert nearby == e*comb(n, k+1)
        assert concurrency == e*(n-k)
        results.append(dict(n=n, k=k, degree=e, field=p, shift=shift,
                            nearby_pairs=nearby,
                            attained_concurrency=concurrency,
                            codeword_distance_checks=distance_checks))
    result = dict(status='passed', fixtures=results,
                  total_distance_checks=sum(r['codeword_distance_checks']
                                            for r in results),
                  scope='All parameters and codewords of six endpoint curves.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
