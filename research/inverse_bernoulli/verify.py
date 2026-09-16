"""Exact checks of the inverse-Bernoulli classification, with no CAS."""
import itertools
import json
from pathlib import Path


def trim(a):
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % p
    return trim(c)


def power(a, e, p):
    b = [1]
    for _ in range(e):
        b = mul(b, a, p)
    return b


def deriv(a, p):
    return trim([i*a[i] % p for i in range(1, len(a))] or [0])


def sub(a, b, p):
    return trim([((a[i] if i < len(a) else 0) -
                  (b[i] if i < len(b) else 0)) % p
                 for i in range(max(len(a), len(b)))])


def monic(a, p):
    c = pow(a[-1], -1, p)
    return [x*c % p for x in a]


def quotient(a, b, p):
    a = a[:]
    q = [0] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        j = len(a)-len(b)
        c = a[-1]*pow(b[-1], -1, p) % p
        q[j] = c
        for i, x in enumerate(b):
            a[i+j] = (a[i+j]-c*x) % p
        trim(a)
    return trim(q), a


def gcd(a, b, p):
    while b != [0]:
        a, b = b, quotient(a, b, p)[1]
    return monic(a, p)


def image(a, s, p):
    return tuple(mul(power(a, s-1, p), deriv(a, p), p))


def enumerate_monic(p, s, cap):
    assert p > s and cap < p
    max_group = 0
    collisions = 0
    examined = 0
    pair_checks = 0
    histogram = {}
    for d in range(1, cap+1):
        groups = {}
        for coefficients in itertools.product(range(p), repeat=d):
            a = list(coefficients) + [1]
            key = image(a, s, p)
            examined += 1
            if key not in groups:
                groups[key] = [1, a]
            else:
                entry = groups[key]
                entry[0] += 1
                collisions += 1
                b = entry[1]
                c = sub(power(a, s, p), power(b, s, p), p)
                assert all(not x or i % p == 0 for i, x in enumerate(c))
                if s >= 3:
                    assert p % s == 1
                    g = (p-1)//s
                    assert d == (s-1)*g+1
                    common = gcd(a, b, p)
                    u, ru = quotient(a, common, p)
                    v, rv = quotient(b, common, p)
                    assert ru == rv == [0] and len(u) == len(v) == 2
                    z = monic(sub(power(u, s, p), power(v, s, p), p), p)
                    assert common == power(z, g, p)
                pair_checks += 1
        counts = [v[0] for v in groups.values()]
        bound = 2 if p > s+1 else s+1
        assert max(counts) <= bound
        max_group = max(max_group, max(counts))
        for count in counts:
            histogram[count] = histogram.get(count, 0)+1
    return dict(p=p, s=s, degree_cap=cap, monic_polynomials=examined,
                distinct_images=sum(histogram.values()),
                maximum_monic_solutions=max_group, collisions=collisions,
                pair_classifications=pair_checks, group_histogram=histogram,
                main_characteristic_guard=p > s+1)


def sharp_pair(p, s):
    assert p % s == 1 and p > s+1
    g = (p-1)//s
    u, v = [0, 1], [-1 % p, 1]
    z = monic(sub(power(u, s, p), power(v, s, p), p), p)
    common = power(z, g, p)
    a, b = mul(common, u, p), mul(common, v, p)
    assert a != b and image(a, s, p) == image(b, s, p)
    roots = [x for x in range(1, p) if pow(x, s, p) == 1]
    polys = {tuple(x*c % p for x in q) for q in (a, b) for c in roots}
    assert len(polys) == 2*s
    assert all(image(list(q), s, p) == image(a, s, p) for q in polys)
    return dict(p=p, s=s, degree=len(a)-1, solutions_checked=len(polys))


def exceptional(p):
    s = p-1
    vanishing = [0, -1 % p] + [0]*(p-2) + [1]
    polys = set()
    images = set()
    for x in range(p):
        q, remainder = quotient(vanishing, [-x % p, 1], p)
        assert remainder == [0]
        for c in range(1, p):
            a = [y*c % p for y in q]
            polys.add(tuple(a))
            images.add(image(a, s, p))
    assert len(polys) == p*(p-1) and len(images) == 1
    return dict(p=p, s=s, degree=p-1, actual_solutions=len(polys),
                failed_without_strict_guard_bound=2*s)


def main():
    fixtures = [(3, 2, 2), (5, 2, 4), (5, 3, 4), (5, 4, 4)]
    fixtures += [(7, s, 5) for s in range(2, 7)]
    fixtures += [(11, s, 4) for s in (2, 3, 4, 5)]
    rows = []
    for args in fixtures:
        row = enumerate_monic(*args)
        print(json.dumps(row), flush=True)
        rows.append(row)
    sharp = [sharp_pair(p, s) for p, s in
             [(7, 3), (13, 3), (13, 4), (11, 5), (13, 6), (29, 7)]]
    controls = [exceptional(p) for p in (3, 5, 7, 11)]
    result = dict(status='PASS', exhaustive_fixtures=rows,
                  sharp_fixtures=sharp, exceptional_controls=controls,
                  scope='Finite monic classification and sharp examples. '
                        'The universal bound and full-MCA consequence require '
                        'the written proof; no quadratic MCA lower bound.')
    Path(__file__).with_name('inverse_bernoulli_verification.json').write_text(
        json.dumps(result, indent=2)+'\n')


if __name__ == '__main__':
    main()
