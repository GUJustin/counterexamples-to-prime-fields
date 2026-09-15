#!/usr/bin/env python3
"""The formal-degree condition cannot be replaced by functional degree."""
import json
from itertools import combinations, product
from pathlib import Path


def main():
    fixtures = []
    for q in (5, 7, 11):
        n, k, r = 4, 2, 1
        domain = range(n)
        codewords = [tuple((c0+c1*x) % q for x in domain)
                     for c0, c1 in product(range(q), repeat=2)]
        bad_coefficient = tuple(x*x % q for x in domain)
        for support in combinations(domain, k+1):
            assert not any(all(c[x] == bad_coefficient[x] for x in support)
                           for c in codewords)
        nearby = 0
        for z in range(q):
            received = tuple((pow(z, q, q)-z)*x*x % q for x in domain)
            assert received == (0,)*n
            witnesses = [c for c in codewords
                         if sum(a != b for a, b in zip(c, received)) <= r]
            assert witnesses == [(0,)*n]
            nearby += len(witnesses)
        assert nearby == q
        fixtures.append(dict(field=q, formal_degree=q, functional_degree=0,
                             unexplained_pairs=nearby,
                             sharp_capped_bound=q,
                             distance_checks=q**3))
    result = dict(status='passed', fixtures=fixtures)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
