#!/usr/bin/env python3
"""Small exact checks of covariance and the sampling-uniform CLT bound.

This checks finite algebra only; it cannot certify a CLT convergence rate.
Standard library only. No protocol or verifier code is exercised.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, factorial, prod
import json


def falling(x, j):
    return prod(x - r for r in range(j))


def gram(n, j, x):
    return Q(sum((-1) ** (j-r) * comb(j, r)
                 * falling(x+r, j) * falling(x+r-n, j)
                 for r in range(j+1)), factorial(2*j))


counts = dict(parameter_cases=0, enumerated_subsets=0,
              projection_inequalities=0, covariance_entries=0)
for n in range(3, 10):
    for m in range(1, min(3, n-1)+1):
        b = [[gram(n, j, x) for x in range(n)] for j in range(1, m+1)]
        sigma = [Q(prod(n*n-i*i for i in range(1, j+1)),
                   (2*j+1)*comb(2*j, j)**2*factorial(j)**2)
                 for j in range(1, m+1)]
        h = max(sum(b[j][x]**2/sigma[j] for j in range(m)) for x in range(n))
        for coefficients in ([Q(1)]*m, [Q((-1)**j, j+1) for j in range(m)],
                             [Q(j+1) for j in range(m)]):
            a = [sum(coefficients[j]*b[j][x] for j in range(m)) for x in range(n)]
            v = sum(x*x for x in a)/(n-1)
            assert max(x*x for x in a)/v <= Q(n-1, n)*h
            counts['projection_inequalities'] += 1
        for t in range(1, n):
            ys = [tuple(sum(b[j][x] for x in subset) for j in range(m))
                  for subset in combinations(range(n), t)]
            assert len(ys) == comb(n, t)
            for j in range(m):
                assert sum(y[j] for y in ys) == 0
                for i in range(m):
                    covariance = sum(y[i]*y[j] for y in ys)/len(ys)
                    target = Q(t*(n-t), n-1)*sigma[j] if i == j else 0
                    assert covariance == target
                    counts['covariance_entries'] += 1
            counts['parameter_cases'] += 1
            counts['enumerated_subsets'] += len(ys)

print(json.dumps({'status': 'all_exact_assertions_passed', **counts}, indent=2))
