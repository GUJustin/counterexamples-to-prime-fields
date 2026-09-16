"""Exact Gauss-duality and prefix checks, including a characteristic-three field."""
import itertools
import json
from pathlib import Path


def binary_field(m, modulus):
    n = 1 << m
    def mul(a, b):
        out = 0
        while b:
            if b & 1:
                out ^= a
            b >>= 1
            a <<= 1
            if a & n:
                a ^= modulus
        return out
    table = [[mul(a, b) for b in range(n)] for a in range(n)]
    for generator in range(2, n):
        values, x = [], 1
        while x not in values:
            values.append(x)
            x = table[x][generator]
        if len(values) == n-1 and x == 1:
            break
    else:
        raise AssertionError('no primitive element')
    logs = {x: i for i, x in enumerate(values)}
    trace = []
    for a in range(n):
        value, total = a, 0
        for _ in range(m):
            total ^= value
            value = table[value][value]
        assert total in (0, 1)
        trace.append(total)
    masks = [sum(1 << v for v in range(1, n) if not trace[table[a][v]])
             for a in range(n)]
    return n, table, trace, logs, masks


def subspaces(n, r):
    out = set()
    for basis in itertools.combinations(range(1, n), r):
        values = [0]
        for x in basis:
            if x in values:
                break
            values += [v ^ x for v in values]
        else:
            out.add(tuple(sorted(values[1:])))
    return sorted(out)


def annihilator(u, masks, n):
    mask = (1 << n)-2
    for a in u:
        mask &= masks[a]
    return [v for v in range(1, n) if mask >> v & 1]


def factors(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**0.5)+1))


def prefix(roots, length, p):
    coeff = [1]+[0]*length
    for count, x in enumerate(roots, 1):
        for j in range(min(count, length), 0, -1):
            coeff[j] = (coeff[j]-x*coeff[j-1]) % p
    return tuple(coeff[1:])


def prime_fixture(m, modulus, r):
    n, table, trace, logs, masks = binary_field(m, modulus)
    p = next(k*(n-1)+1 for k in range(2, 1000, 2) if prime(k*(n-1)+1))
    zeta = next(pow(a, (p-1)//(n-1), p) for a in range(2, p)
                if all(pow(pow(a, (p-1)//(n-1), p), (n-1)//q, p) != 1
                       for q in factors(n-1)))
    chi = {v: pow(zeta, logs[v], p) for v in range(1, n)}
    assert len(set(chi.values())) == n-1
    t = (1 << r)-1
    gauss = {}
    for j in range(1, t+1):
        a = sum((-1)**trace[v]*pow(chi[v], j, p) for v in chi) % p
        b = sum((-1)**trace[v]*pow(chi[v], -j, p) for v in chi) % p
        assert a*b % p == n % p
        gauss[j] = a
    spaces = subspaces(n, r)
    seen, affine_seen = set(), set()
    one_moment, short_prefixes = {}, {}
    for u in spaces:
        support = annihilator(u, masks, n)
        assert len(support) == n//(1 << r)-1
        for j in range(1, t+1):
            actual = sum(pow(chi[v], j, p) for v in support) % p
            dual = sum(pow(chi[v], -j, p) for v in u) % p
            assert actual == gauss[j]*dual*pow(1 << r, -1, p) % p
        raw = prefix([chi[v] for v in support], t, p)
        affine = prefix([(7*chi[v]+11) % p for v in support], t, p)
        assert raw not in seen and affine not in affine_seen
        seen.add(raw)
        affine_seen.add(affine)
        one_moment[raw[0]] = one_moment.get(raw[0], 0)+1
        short_prefixes[raw[:-1]] = short_prefixes.get(raw[:-1], 0)+1
    if r == 2 and m % 2 == 0:
        assert short_prefixes[(0, 0)] == (n-1)//3
    return dict(N=n, p=p, binary_codimension=r, dual_size=t,
                subspaces=len(spaces), prefix_length=t,
                distinct_raw_prefixes=len(seen), distinct_affine_prefixes=len(affine_seen),
                gauss_product_checks=t, moment_duality_checks=t*len(spaces),
                largest_one_coefficient_class=max(one_moment.values()))


def subfield_sharpness():
    n, table, trace, logs, masks = binary_field(9, 0b1000010001)
    p = next(k*(n-1)+1 for k in range(2, 1000, 2) if prime(k*(n-1)+1))
    zeta = next(pow(a, (p-1)//(n-1), p) for a in range(2, p)
                if all(pow(pow(a, (p-1)//(n-1), p), (n-1)//q, p) != 1
                       for q in factors(n-1)))
    chi = {v: pow(zeta, logs[v], p) for v in range(1, n)}
    subfield = []
    for x in range(n):
        y = x
        for _ in range(3):
            y = table[y][y]
        if y == x:
            subfield.append(x)
    assert len(subfield) == 8
    orbit = {tuple(sorted(table[a][u] for u in subfield if u))
             for a in range(1, n)}
    assert len(orbit) == 73
    seen = set()
    for u in orbit:
        support = annihilator(u, masks, n)
        assert len(support) == 63
        coefficients = prefix([chi[v] for v in support], 7, p)
        assert coefficients[:6] == (0,)*6
        seen.add(coefficients)
    assert len(seen) == 73
    return dict(N=n, p=p, binary_codimension=3, subspaces=73,
                shared_zero_prefix_length=6, distinct_seven_coefficient_prefixes=73,
                agreement_support_size=63)


def characteristic_three():
    # ord_31(3)=30, so Phi_31 is irreducible over F3. This is the field
    # F_(3^30), represented by 31 cyclic coefficients modulo their common shift.
    assert next(i for i in range(1, 31) if pow(3, i, 31) == 1) == 30
    m, p = 31, 3
    def canonical(a):
        return tuple((x-a[-1]) % p for x in a)
    def scalar(c):
        return (c % p,)+(0,)*(m-1)
    def shift(a, e):
        e %= m
        return canonical(a[-e:]+a[:-e] if e else a)
    def add(a, b, sign=1):
        return canonical([(x+sign*y) % p for x, y in zip(a, b)])
    def mul(a, b):
        out = [0]*m
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[(i+j) % m] += x*y
        return canonical(out)
    def moment(values, j, logs):
        out = [0]*m
        for v in values:
            out[j*logs[v] % m] += 1
        return canonical(out)
    n, table, trace, logs, masks = binary_field(5, 0b100101)
    gauss = {}
    for j in range(1, 6):
        def g(e):
            out = [0]*m
            for v in range(1, n):
                out[e*logs[v] % m] += (-1)**trace[v]
            return canonical(out)
        gauss[j] = g(j)
        assert mul(g(j), g(-j)) == scalar(n)
    seen = set()
    spaces = subspaces(n, 2)
    for u in spaces:
        support = annihilator(u, masks, n)
        for j in range(1, 6):
            # 1/4=1 in F3.
            assert moment(support, j, logs) == mul(gauss[j], moment(u, -j, logs))
        coeff = [scalar(1)]+[scalar(0)]*5
        for count, v in enumerate(support, 1):
            for j in range(min(count, 5), 0, -1):
                coeff[j] = add(coeff[j], shift(coeff[j-1], logs[v]), -1)
        key = tuple(coeff[1:])
        assert key not in seen
        seen.add(key)
    return dict(N=32, characteristic=3, extension_degree=30,
                binary_codimension=2, subspaces=len(spaces), prefix_length=5,
                distinct_prefixes=len(seen), gauss_product_checks=5,
                moment_duality_checks=5*len(spaces))


def main():
    fixtures = [(4, 0b10011, 2), (5, 0b100101, 2),
                (6, 0b1000011, 2), (7, 0b10000011, 2),
                (8, 0x11B, 2), (7, 0b10000011, 3)]
    rows = []
    for args in fixtures:
        row = prime_fixture(*args)
        rows.append(row)
        print(json.dumps(row), flush=True)
    small_char = characteristic_three()
    result = dict(status='PASS', prime_field_fixtures=rows,
                  characteristic_three_fixture=small_char,
                  sharpness_fixture=subfield_sharpness(),
                  scope='Exact Gauss-product and primal-dual moment identities; '
                        'exhaustive subspace prefix uniqueness under multiplicative '
                        'and affine-multiplicative relabeling. Arbitrary relabeling '
                        'is outside this theorem.')
    Path(__file__).with_name('multiplicative_label_rigidity_verification.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(small_char), flush=True)


if __name__ == '__main__':
    main()
