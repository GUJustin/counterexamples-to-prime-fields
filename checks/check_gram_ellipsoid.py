"""Exact arithmetic checks for Gram norms and quadratic moment weights."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial, isqrt, prod
from collections import Counter
from pathlib import Path
import json


def falling(x, j):
    return prod(x - i for i in range(j))


def gram(n, j, x):
    return F(sum((-1)**(j-i) * comb(j, i) * falling(x+i, j)
                 * falling(x+i-n, j) for i in range(j+1)), factorial(2*j))


def ceilq(x):
    return -((-x.numerator)//x.denominator)


def sqrt_upper(x, scale=10**12):
    z = x*scale**2
    r = isqrt(z.numerator//z.denominator)
    if r*r*z.denominator < z.numerator:
        r += 1
    upper = F(r,scale)
    assert upper**2 >= x
    return upper


def dither_lower(n, t, v1, v2):
    # Classical strict upper bound pi < 355/113; all other arithmetic exact.
    denominator = 4*F(355,113)*sqrt_upper((v1+F(1,12))*(v2+F(1,12)))
    return ceilq(F(comb(n,t),1)/denominator)


def main():
    norms = orthogonality = fixtures = subsets = 0
    for n in range(2, 33):
        for j in range(1, min(n, 10)):
            b = [gram(n, j, x) for x in range(n)]
            assert sum(b) == 0
            expected = F(prod(n*n-i*i for i in range(1,j+1)),
                         (2*j+1)*comb(2*j,j)**2*factorial(j)**2)
            assert sum(v*v for v in b)/n == expected
            for i in range(j):
                assert sum(b[x]*comb(x,i) for x in range(n)) == 0
                orthogonality += 1
            norms += 1

    for n in range(3, 13):
        for t in range(1, n):
            v1 = F(t*(n-t)*(n+1), 12)
            v2 = F(t*(n-t)*(n+1)*(n*n-4), 720)
            mu1 = F(t*(n-1), 2)
            mu2 = -F(t*(n-1)*(n-2), 12)
            shear = F(n-2, 2)
            counts = Counter((sum(a),sum(comb(x,2) for x in a))
                             for a in combinations(range(n),t))
            weighted = F(0)
            for (u,v), count in counts.items():
                q = (u-mu1)**2/v1 + (v-shear*u-mu2)**2/v2
                weighted += count*(4-q)
            assert weighted == 2*comb(n,t)
            # Full triangular lattice, including unattainable signatures.
            radius1 = isqrt(ceilq(4*v1))+1
            radius2 = isqrt(ceilq(4*v2))+1
            denominator = F(0)
            for u in range(mu1.numerator//mu1.denominator-radius1-1,
                           ceilq(mu1)+radius1+2):
                center2 = shear*u+mu2
                for v in range(center2.numerator//center2.denominator-radius2-1,
                               ceilq(center2)+radius2+2):
                    weight = 4-(u-mu1)**2/v1-(v-center2)**2/v2
                    denominator += max(F(0),weight)
            bound = ceilq(weighted/denominator)
            assert bound <= max(counts.values())
            assert dither_lower(n,t,v1,v2) <= max(counts.values())
            fixtures += 1
            subsets += comb(n,t)

    n,t = 64,34
    v1 = F(t*(n-t)*(n+1),12)
    v2 = F(t*(n-t)*(n+1)*(n*n-4),720)
    assert v1.denominator == v2.denominator == 1
    v1,v2 = int(v1),int(v2)
    assert F(t*(n-1),2).denominator == 1
    assert F(t*(n-1)*(n-2),12).denominator == 1
    assert (n-2)%2 == 0
    d = v1*v2
    denominator = positive_sites = 0
    for x in range(-isqrt(4*v1),isqrt(4*v1)+1):
        a = 4*d-v2*x*x
        if a <= 0:
            continue
        h = isqrt((a-1)//v1)
        denominator += (2*h+1)*a-v1*h*(h+1)*(2*h+1)//3
        positive_sites += 2*h+1
    bound = ceilq(F(2*d*comb(n,t),denominator))
    result = dict(gram_norms=norms,orthogonality_identities=orthogonality,
                  exhaustive_fixtures=fixtures,subset_visits=subsets,
                  length64=dict(n=n,t=t,variances=[v1,v2],radius_squared=4,
                                positive_lattice_sites=positive_sites,
                                scaled_denominator=denominator,
                                numerator=2*d*comb(n,t),list_lower_bound=bound,
                                dither_certified_lower_bound=dither_lower(n,t,F(v1),F(v2))),
                  all_passed=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
