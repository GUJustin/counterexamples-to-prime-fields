#!/usr/bin/env python3
"""Exhaustive parameter/codeword checks for deterministic small curves."""
import json
import random
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path


def evaluate(coefficients, x, p):
    result = 0
    for c in reversed(coefficients):
        result = (result * x + c) % p
    return result


def main():
    rng = random.Random(2026091518)
    totals = dict(curves=0, parameters=0, codeword_distances=0,
                  nearby_pairs=0, unexplained_pairs=0,
                  unexplained_pairs_on_joint_agreement_curves=0,
                  degree_at_least_field_size_curves=0)
    for n, k, r, p in [(4, 2, 1, 11), (6, 2, 2, 17),
                       (6, 2, 3, 11), (5, 1, 2, 13), (4, 1, 2, 5)]:
        a = n - k
        d = 2*r - a
        bound = Fraction((n-d)*comb(n, d), comb(r, d))
        codewords = [tuple(evaluate(c, x, p) for x in range(n))
                     for c in product(range(p), repeat=k)]
        restrictions = {}
        for size in range(n-r, n+1):
            for support in combinations(range(n), size):
                restrictions[support] = {
                    tuple(c[i] for i in support) for c in codewords}
        for e in [0, 1, 2, 3, p]:
            for fixture in range(12):
                words = [[rng.randrange(p) for _ in range(n)]
                         for _ in range(e+1)]
                # Half the fixtures have a prescribed jointly explained set.
                if fixture % 2 == 0:
                    for word in words:
                        c = rng.choice(codewords)
                        word[:n-r] = c[:n-r]
                explained = {
                    support: all(tuple(w[i] for i in support) in values
                                 for w in words)
                    for support, values in restrictions.items()}
                has_joint = any(value for support, value in explained.items()
                                if len(support) == n-r)
                nearby = bad = 0
                for z in range(p):
                    received = tuple(evaluate([w[i] for w in words], z, p)
                                     for i in range(n))
                    for c in codewords:
                        support = tuple(i for i in range(n) if c[i] == received[i])
                        if len(support) >= n-r:
                            nearby += 1
                            bad += not explained[support]
                assert bad <= e*bound, (n, k, r, p, e, fixture, bad)
                if not has_joint:
                    assert nearby == bad
                    assert nearby <= e*bound
                if e == 0:
                    assert bad == 0
                totals['curves'] += 1
                totals['parameters'] += p
                totals['codeword_distances'] += p*len(codewords)
                totals['nearby_pairs'] += nearby
                totals['unexplained_pairs'] += bad
                if has_joint:
                    totals['unexplained_pairs_on_joint_agreement_curves'] += bad
                totals['degree_at_least_field_size_curves'] += e >= p
    assert totals['unexplained_pairs_on_joint_agreement_curves'] > 0
    result = {'status': 'passed', 'coverage': totals,
              'scope': 'All parameters and codewords for 300 deterministic curves; not all curves.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
