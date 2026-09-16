"""Exact Fourier checks for transfer within fixed binary multiplicative orbits."""
import itertools
import json
import random
from pathlib import Path

MULT4 = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]


def dot4(a, b, k):
    ans = 0
    for _ in range(k):
        ans ^= MULT4[a & 3][b & 3]
        a >>= 2
        b >>= 2
    return ans


def span(basis):
    values = [0]
    for b in basis:
        assert b not in values
        values += [x ^ b for x in values]
    return values


def walsh(values):
    values = values[:]
    width = 1
    while width < len(values):
        for start in range(0, len(values), 2*width):
            for j in range(width):
                a, b = values[start+j], values[start+j+width]
                values[start+j], values[start+j+width] = a+b, a-b
        width *= 2
    return values


def check_flat(k, basis, shift, rng):
    n = 4**k
    directions = span(basis)
    assert len(directions) == 32 and shift not in directions
    normals = [shift ^ x for x in directions]
    rows = [[int(dot4(a, v, k) == 0) for v in range(1, n)]
            for a in normals]
    assert all(sum(row) == n//4-1 for row in rows)
    coefficients = list(zip(*(walsh(list(col)) for col in zip(*rows))))
    nonzero = 0
    max_support = 0
    characteristic_three_nonzero = 0
    p = 257 if n == 64 else 769
    labels = rng.sample(range(p), n-1)
    moment_contradictions = 0
    for beta in range(1, 32):
        vector = coefficients[beta]
        active = [(v+1, c) for v, c in enumerate(vector) if c]
        assert len(active) <= 3*n//32
        max_support = max(max_support, len(active))
        # Compare integer Walsh sums with the character-fiber expansion.
        for v in range(1, n):
            total = 0
            for t in (1, 2, 3):
                mask = sum(((MULT4[t][dot4(w, v, k)] >> 1) << i)
                           for i, w in enumerate(basis))
                if mask == beta:
                    total += (-1)**(MULT4[t][dot4(shift, v, k)] >> 1)
            assert vector[v-1] == 8*total
        if active:
            nonzero += 1
            assert sum(c for _, c in active) == 0
            # Distinct labels force some moment below the support size nonzero.
            moments = [sum(c*pow(labels[v-1], j, p) for v, c in active) % p
                       for j in range(len(active))]
            assert any(moments) and not moments[0]
            moment_contradictions += 1
        if any(c % 3 for c in vector):
            characteristic_three_nonzero += 1
    assert nonzero and characteristic_three_nonzero
    return dict(nonzero_fourier_vectors=nonzero, max_support=max_support,
                characteristic_three_nonzero=characteristic_three_nonzero,
                checked_moment_contradictions=moment_contradictions)


def hyperplanes(k):
    n = 4**k
    return sorted({tuple(v for v in range(1, n) if dot4(a, v, k) == 0)
                   for a in range(1, n)})


def locator(roots, p):
    a = [1]
    for x in roots:
        b = [0]*(len(a)+1)
        for i, c in enumerate(a):
            b[i] = (b[i]-x*c) % p
            b[i+1] = (b[i+1]+c) % p
        a = b
    return a


def prefix_fixtures(k, count, rng):
    n = 4**k
    p = 257 if n == 64 else 769
    supports = hyperplanes(k)
    assert len(supports) == (n-1)//3
    maximum = 0
    for _ in range(count):
        labels = rng.sample(range(p), n-1)
        classes = {}
        for support in supports:
            loc = locator([labels[v-1] for v in support], p)
            prefix = tuple(loc[-2:-(n//8+1):-1])
            assert len(prefix) == n//8-1
            classes[prefix] = classes.get(prefix, 0)+1
        maximum = max(maximum, max(classes.values()))
    return dict(N=n, relabelings=count, supports_per_relabeling=len(supports),
                maximum_prefix_class=maximum)


def gf64_mul(a, b):
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        b >>= 1
        a <<= 1
        if a & 64:
            a ^= 0b1000011
    return ans


def binary_control():
    for a in range(1, 64):
        value = 1
        for _ in range(63):
            value = gf64_mul(value, a)
        assert value == 1
    prefixes = set()
    supports = hyperplanes(3)
    for support in supports:
        a = [1]
        for x in support:
            b = [0]*(len(a)+1)
            for i, c in enumerate(a):
                b[i] ^= gf64_mul(x, c)
                b[i+1] ^= c
            a = b
        prefixes.add(tuple(a[-2:-9:-1]))
    assert prefixes == {(0,)*7}
    # These 32 normals form a five-flat avoiding zero, all in the prefix class.
    normals = [32 ^ x for x in range(32)]
    assert all(tuple(v for v in range(1, 64) if dot4(a, v, 3) == 0)
               in supports for a in normals)
    return dict(N=64, common_prefix_length=7, hyperplanes=len(supports),
                affine_five_flat_normals=len(normals),
                scope='Violates the odd-characteristic flat exclusion, '
                      'not the numerically weak asymptotic count at N=64.')


def multiplicative_orbit(alpha):
    table = [[gf64_mul(a, b) for b in range(64)] for a in range(64)]
    trace = []
    for a in range(64):
        total, value = 0, a
        for _ in range(6):
            total ^= value
            value = table[value][value]
        assert total in (0, 1)
        trace.append(total)
    u_space = (0, 1, alpha, 1 ^ alpha)
    rows = {a: [int(all(trace[table[table[a][u]][v]] == 0
                       for u in u_space)) for v in range(1, 64)]
            for a in range(1, 64)}
    stabilizer = [c for c in range(1, 64)
                  if {table[c][u] for u in u_space} == set(u_space)]
    assert len(stabilizer) in (1, 3)
    assert len({tuple(row) for row in rows.values()}) == 63//len(stabilizer)
    vectors = 0
    largest = 0
    for functional in range(1, 64):
        pivot = (functional & -functional).bit_length()-1
        basis = [(1 << i) ^ (((functional >> i) & 1) << pivot)
                 for i in range(6) if i != pivot]
        for u in u_space[1:]:
            assert len(span([table[u][w] for w in basis])) == 32
        normals = [(1 << pivot) ^ x for x in span(basis)]
        coefficients = list(zip(*(walsh(list(col))
                                  for col in zip(*(rows[a] for a in normals)))))
        nonzero = 0
        for beta in range(1, 32):
            vector = coefficients[beta]
            support = sum(c != 0 for c in vector)
            assert support <= 6 and sum(vector) == 0
            largest = max(largest, support)
            nonzero += any(c % 3 for c in vector)
            vectors += 1
        assert nonzero
    return dict(N=64, alpha=alpha, stabilizer_size=len(stabilizer),
                orbit_hyperplanes=63//len(stabilizer), five_flats=63,
                fourier_vectors_checked=vectors, maximum_support=largest)


def small_odd_transfer():
    # N=16 has only four binary normal dimensions, hence no five-flat.
    p = 97
    unity = [x for x in range(1, p) if pow(x, 3, p) == 1]
    cosets = sorted({tuple(sorted(c*x % p for x in unity))
                     for c in range(1, p)})[:5]
    supports = hyperplanes(2)
    labels = {}
    for support, values in zip(supports, cosets):
        labels.update(zip(support, values))
    assert len(labels) == len(set(labels.values())) == 15
    assert {locator([labels[v] for v in h], p)[-2] for h in supports} == {0}
    return dict(N=16, p=p, hyperplanes=5, common_prefix_length=1)


def higher_codimension(rng):
    def mul256(a, b):
        ans = 0
        while b:
            if b & 1:
                ans ^= a
            b >>= 1
            a <<= 1
            if a & 256:
                a ^= 0x11B
        return ans
    table = [[mul256(a, b) for b in range(256)] for a in range(256)]
    for a in range(1, 256):
        value, base, exponent = 1, a, 255
        while exponent:
            if exponent & 1:
                value = table[value][base]
            base = table[base][base]
            exponent >>= 1
        assert value == 1
    trace = []
    for a in range(256):
        total, value = 0, a
        for _ in range(8):
            total ^= value
            value = table[value][value]
        assert total in (0, 1)
        trace.append(total)
    u_space = list(range(8))
    stabilizer = [c for c in range(1, 256)
                  if {table[c][u] for u in u_space} == set(u_space)]
    assert stabilizer == [1]
    rows = {a: [int(all(trace[table[table[a][u]][v]] == 0
                       for u in (1, 2, 4))) for v in range(1, 256)]
            for a in range(1, 256)}
    labels = rng.sample(range(769), 255)
    maximum = 0
    nonzero_vectors = 0
    for functional in rng.sample(range(1, 256), 8):
        pivot = (functional & -functional).bit_length()-1
        basis = [(1 << i) ^ (((functional >> i) & 1) << pivot)
                 for i in range(8) if i != pivot]
        for u in u_space[1:]:
            assert len(span([table[u][w] for w in basis])) == 128
        normals = [(1 << pivot) ^ x for x in span(basis)]
        assert all(sum(rows[a]) == 31 for a in normals)
        coefficients = list(zip(*(walsh(list(col))
                                  for col in zip(*(rows[a] for a in normals)))))
        for beta in range(1, 128):
            vector = coefficients[beta]
            active = [(i, c) for i, c in enumerate(vector) if c]
            assert len(active) <= 14 and sum(vector) == 0
            maximum = max(maximum, len(active))
            if active:
                nonzero_vectors += 1
                assert any(sum(c*pow(labels[i], j, 769) for i, c in active) % 769
                           for j in range(1, len(active)))
    assert nonzero_vectors
    return dict(N=256, binary_codimension=3, prefix_length=15,
                parameter_flat_dimension=7, flats_checked=8,
                fourier_vectors_checked=8*127, maximum_support=maximum,
                nonzero_vectors=nonzero_vectors, stabilizer_size=1)


def main():
    rng = random.Random(20260916)
    flats = []
    # All 63 affine binary five-flats in F2^6 avoiding zero.
    for functional in range(1, 64):
        pivot = (functional & -functional).bit_length()-1
        basis = [(1 << i) ^ (((functional >> i) & 1) << pivot)
                 for i in range(6) if i != pivot]
        flats.append(check_flat(3, basis, 1 << pivot, rng))
    larger = []
    for _ in range(20):
        basis = []
        while len(basis) < 5:
            candidate = rng.randrange(1, 256)
            if candidate not in span(basis):
                basis.append(candidate)
        subspace = span(basis)
        shift = next(x for x in range(1, 256) if x not in subspace)
        larger.append(check_flat(4, basis, shift, rng))
    result = dict(status='PASS', all_N64_five_flats=len(flats),
                  N256_five_flats=len(larger),
                  fourier_vectors_checked=31*(len(flats)+len(larger)),
                  nonzero_vectors=sum(x['nonzero_fourier_vectors'] for x in flats+larger),
                  max_support_N64=max(x['max_support'] for x in flats),
                  max_support_N256=max(x['max_support'] for x in larger),
                  odd_prefix_fixtures=[prefix_fixtures(3, 30, rng),
                                       prefix_fixtures(4, 10, rng)],
                  binary_control=binary_control(),
                  multiplicative_orbits=[multiplicative_orbit(2),
                                         multiplicative_orbit(next(a for a in range(2, 64)
                                             if gf64_mul(a, a) ^ a ^ 1 == 0))],
                  small_odd_transfer=small_odd_transfer(),
                  higher_codimension=higher_codimension(rng),
                  scope='Exact Fourier support formulas, Vandermonde moment '
                        'controls, and finite prefix classes. Universal bound '
                        'requires the written proof; general binary codimension-two '
                        'families are not covered.')
    Path(__file__).with_name('multiplicative_orbit_transfer_verification.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
