"""Exact certificates for triangular-lattice quadratic concentration.

Standard library only. No floating-point arithmetic enters a certificate.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, isqrt
from pathlib import Path
import json


def ceilq(x):
    return -((-x.numerator) // x.denominator)


def centered_spectrum(v1, v2, upper=5):
    """Return all values v2*x*x+v1*y*y < upper*v1*v2, with multiplicity."""
    d = v1*v2
    spectrum = Counter()
    for x in range(isqrt(upper*v1)+1):
        left = upper*d-v2*x*x
        if left <= 0:
            continue
        for y in range(isqrt((left-1)//v1)+1):
            spectrum[v2*x*x+v1*y*y] += (1 if x == 0 else 2)*(1 if y == 0 else 2)
    return sorted(spectrum.items())


def optimal_certificate(n=64, t=34):
    v1 = F(t*(n-t)*(n+1), 12)
    v2 = F(t*(n-t)*(n+1)*(n*n-4), 720)
    assert v1.denominator == v2.denominator == 1
    # The shear and both centers are integral, so the centered lattice is Z^2.
    assert (n-2) % 2 == 0 and t*(n-1) % 2 == 0
    assert t*(n-1)*(n-2) % 12 == 0
    v1, v2 = int(v1), int(v2)
    d, population = v1*v2, comb(n,t)
    count = total = 0
    baseline_denominator = sum4count = 0
    result = None
    for e, multiplicity in centered_spectrum(v1,v2):
        if e < 4*d:
            baseline_denominator += multiplicity*(4*d-e)
            sum4count += multiplicity
        before = 2*d*count-total
        after = before + multiplicity*(2*d-e)
        if e > 2*d and before >= 0 and after <= 0 and result is None:
            numerator = population*(e-2*d)
            denominator = count*e-total
            result = dict(radius_squared=[e,d], positive_lattice_sites=count,
                          boundary_lattice_sites=multiplicity,
                          scaled_weight_sum=denominator,
                          scaled_numerator=numerator,
                          derivative_sign_before=before,
                          derivative_sign_after=after,
                          list_lower_bound=ceilq(F(numerator,denominator)))
        count += multiplicity
        total += multiplicity*e
    assert result is not None
    # Independent row summation for the radius-squared 4 denominator.
    independent = 0
    for x in range(-isqrt(4*v1),isqrt(4*v1)+1):
        a = 4*d-v2*x*x
        if a <= 0:
            continue
        h = isqrt((a-1)//v1)
        independent += (2*h+1)*a-v1*h*(h+1)*(2*h+1)//3
    assert independent == baseline_denominator
    baseline = F(2*d*population, baseline_denominator)
    assert F(result['scaled_numerator'],result['scaled_weight_sum']) >= baseline
    # pi < 355/113 gives a rigorous rational upper bound on the smoothed
    # denominator. Squaring permits an exact integer square-root certificate.
    # W1*W2 = (12*v1+1)*(12*v2+1)/144.
    # N/(4*pi*sqrt(W1*W2)) > 339*N/(355*sqrt(A)).
    a = (12*v1+1)*(12*v2+1)
    squared = F((339*population)**2,355**2*a)
    strict_integer_bound = isqrt(squared.numerator//squared.denominator)+1
    assert (strict_integer_bound-1)**2 <= squared < strict_integer_bound**2
    return dict(n=n,t=t,variances=[v1,v2], population=population,
                radius4=dict(positive_lattice_sites=sum4count,
                             scaled_weight_sum=baseline_denominator,
                             list_lower_bound=ceilq(baseline)),
                optimized=result,
                smoothed_pi_upper='355/113',
                smoothed_list_lower_bound=strict_integer_bound)


def check_tiling():
    fixtures = 0
    # Rational, nonintegral, large, and negative shears; boundary points included.
    for a,b,c in product([F(-7,3),F(0),F(1,2),F(8,3)], repeat=3):
        offset = [F(2,7),F(-3,5),F(1,11)]
        matrix = [[F(1),F(0),F(0)],[a,F(1),F(0)],[b,c,F(1)]]
        for x in product([F(-3,2),F(0),F(1,2),F(5,3)], repeat=3):
            z, center = [], []
            for j in range(3):
                preceding = offset[j]+sum(matrix[j][i]*z[i] for i in range(j))
                z.append((x[j]-preceding+F(1,2)).__floor__())
                center.append(preceding+z[j])
                assert F(-1,2) <= x[j]-center[j] < F(1,2)
            # Every alternative integer center in this neighborhood differs
            # first in a coordinate whose unit intervals are disjoint.
            for dz in product([-1,0,1], repeat=3):
                if not any(dz):
                    continue
                other = [offset[j]+sum(matrix[j][i]*(z[i]+dz[i])
                                      for i in range(j+1)) for j in range(3)]
                assert not all(F(-1,2) <= x[j]-other[j] < F(1,2) for j in range(3))
            fixtures += 1
    return fixtures


def exhaustive_small():
    fixtures = visits = 0
    for n in range(3,11):
        for t in range(1,n):
            counts = Counter((sum(a),sum(comb(x,2) for x in a))
                             for a in combinations(range(n),t))
            mu1,mu2 = F(t*(n-1),2),-F(t*(n-1)*(n-2),12)
            v1,v2 = F(t*(n-t)*(n+1),12), F(t*(n-t)*(n+1)*(n*n-4),720)
            shear = F(n-2,2)
            expected_weight = sum(count*(4-(u-mu1)**2/v1-(v-shear*u-mu2)**2/v2)
                                  for (u,v),count in counts.items())
            assert expected_weight == 2*comb(n,t)
            denominator = F(0)
            h1,h2 = isqrt(ceilq(4*v1))+2,isqrt(ceilq(4*v2))+2
            for u in range(mu1.__floor__()-h1,ceilq(mu1)+h1+1):
                center = shear*u+mu2
                for v in range(center.__floor__()-h2,ceilq(center)+h2+1):
                    denominator += max(F(0),4-(u-mu1)**2/v1-(v-center)**2/v2)
            assert ceilq(expected_weight/denominator) <= max(counts.values())
            fixtures += 1
            visits += comb(n,t)
    return dict(fixtures=fixtures,subset_visits=visits)


if __name__ == '__main__':
    result = dict(tiling_fixtures=check_tiling(), exhaustive=exhaustive_small(),
                  length64=optimal_certificate(),all_passed=True)
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
