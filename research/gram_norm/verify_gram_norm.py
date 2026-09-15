#!/usr/bin/env python3
"""Independent exact-rational checks of uniform-grid Gram norms."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, factorial, prod
import json
from pathlib import Path


def inner(a, b):
    return sum((x*y for x, y in zip(a,b)), Q(0)) / len(a)


def falling(x, j):
    return prod(x-i for i in range(j))


def rodrigues(n, j, x):
    return Q(sum((-1)**(j-h)*comb(j,h)*falling(x+h,j)*falling(x+h-n,j)
                 for h in range(j+1)), factorial(2*j))


def norm(n, j):
    return Q(prod(n*n-i*i for i in range(1,j+1)),
             (2*j+1)*comb(2*j,j)**2*factorial(j)**2)


counts = dict(grid_degree_cases=0, pairwise_inner_products=0,
              summation_by_parts_cases=0, subset_covariance_cases=0,
              subset_visits=0, aggregate_correction_identities=0)
for n in range(2, 25):
    basis = []
    norms = []
    for j in range(n):
        # Orthogonalize sampled binomial polynomials independently of Rodrigues.
        v = [Q(comb(x,j)) if x >= j else Q(0) for x in range(n)]
        for u, uu in zip(basis, norms):
            c = inner(v,u)/uu
            v = [x-c*y for x,y in zip(v,u)]
        assert v == [rodrigues(n,j,x) for x in range(n)]
        nv = inner(v,v)
        assert nv == norm(n,j)
        assert nv*n == Q(factorial(j)**2*comb(n+j,2*j+1),factorial(2*j))
        for i,u in enumerate(basis):
            assert inner(v,u) == 0
            counts['pairwise_inner_products'] += 1
        basis.append(v)
        norms.append(nv)
        counts['grid_degree_cases'] += 1
        # Test the boundary identity against larger-degree polynomials as well.
        for d in range(n+2):
            lhs = sum(Q(x**d)*rodrigues(n,j,x)*factorial(2*j) for x in range(n))
            rhs = (-1)**j*sum(falling(y,j)*falling(y-n,j)*
                sum((-1)**h*comb(j,h)*(y-h)**d for h in range(j+1))
                for y in range(j,n))
            assert lhs == rhs
            counts['summation_by_parts_cases'] += 1
    assert norms[-1] == Q(1,n*comb(2*n-2,n-1))
    if n <= 10:
        for t in range(1,n):
            sums = [[sum(basis[j][x] for x in A) for j in range(1,n)]
                    for A in combinations(range(n),t)]
            counts['subset_visits'] += len(sums)
            for i in range(1,n):
                assert sum(row[i-1] for row in sums) == 0
                for j in range(1,i+1):
                    empirical = sum(row[i-1]*row[j-1] for row in sums)/len(sums)
                    expected = Q(t*(n-t),n-1)*norms[i] if i==j else 0
                    assert empirical == expected
                    counts['subset_covariance_cases'] += 1

for m in range(1,1001):
    assert sum((m-i+1)*i*i for i in range(1,m+1)) == m*(m+1)**2*(m+2)//12
    counts['aggregate_correction_identities'] += 1

out = dict(status='all exact assertions passed', **counts)
Path(__file__).with_name('verified.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
