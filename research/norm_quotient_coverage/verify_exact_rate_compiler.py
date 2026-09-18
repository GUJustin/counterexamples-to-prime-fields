#!/usr/bin/env python3
"""Full-domain degree-five compiler fixtures; no large-p coverage inference."""
from itertools import combinations, product
from pathlib import Path
import json
import resource
import time

started = time.monotonic()
P, D = 5, 5
Q = P ** D
M = (Q - 1) // (P - 1)
ZERO = (0,) * D
ONE = (1,) + (0,) * (D - 1)
BETA = (0, 1, 0, 0, 0)


def base(a):
    return (a % P,) + (0,) * (D - 1)


def add(a, b):
    return tuple((x + y) % P for x, y in zip(a, b))


def neg(a):
    return tuple(-x % P for x in a)


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    out = [0] * (2 * D - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    # beta^5=beta+1; X^5-X-1 is Artin--Schreier irreducible over F_5.
    for j in range(2 * D - 2, D - 1, -1):
        out[j - D] += out[j]
        out[j - D + 1] += out[j]
    return tuple(x % P for x in out[:D])


def power(a, n):
    value = ONE
    while n:
        if n & 1:
            value = mul(value, a)
        a = mul(a, a)
        n //= 2
    return value


def inverse(a):
    assert a != ZERO
    out = power(a, Q - 2)
    assert mul(out, a) == ONE
    return out


def evaluate(coefficients, x):
    out = ZERO
    for c in reversed(coefficients):
        out = add(mul(out, x), c)
    return out


def polynomial_roots(roots):
    out = [ONE]
    for a in roots:
        new = [ZERO] * (len(out) + 1)
        for i, c in enumerate(out):
            new[i] = sub(new[i], mul(c, a))
            new[i + 1] = add(new[i + 1], c)
        out = new
    return out


def interpolate(tags, values):
    out = [ZERO] * len(tags)
    for i, a in enumerate(tags):
        other = [base(c) for j, c in enumerate(tags) if j != i]
        numerator = polynomial_roots(other)
        denominator = evaluate(numerator, base(a))
        scale = mul(values[a], inverse(denominator))
        for j, c in enumerate(numerator):
            out[j] = add(out[j], mul(c, scale))
    return out


assert power(BETA, P) == add(BETA, ONE)
assert power(BETA, P) != BETA
assert power(BETA, Q) == BETA
nodes = list(product(range(P), repeat=D))
norms = [power(x, M) for x in nodes]
assert all(y[1:] == (0,) * (D - 1) for y in norms)
assert norms.count(ZERO) == 1
assert all(norms.count(base(a)) == M for a in range(1, P))
norm_tags = [y[0] for y in norms]
fiber = [x for x, a in zip(nodes, norm_tags) if a == 1]
allowed = list(range(2, P))
denominators = [inverse(sub(base(a), BETA)) for a in range(P)]
g_values = [neg(a) for a in denominators]
records = []
for r in [2, 3]:
    f_values = [mul(sub(power(base(a), r), power(BETA, r)), denominators[a])
                for a in range(P)]
    source_tags = allowed[:r - 1]
    f_interp = interpolate(source_tags, f_values)
    g_interp = interpolate(source_tags, g_values)
    for w in [0, 1, 7]:
        core = fiber[:w]
        locator = polynomial_roots(core)
        multipliers = [evaluate(locator, x) for x in nodes]
        strict_degree = (r - 2) * M + w + 1
        source_agreement = (r - 1) * M + w
        near_agreement = r * M + w
        f = [mul(z, f_values[a]) for z, a in zip(multipliers, norm_tags)]
        g = [mul(z, g_values[a]) for z, a in zip(multipliers, norm_tags)]
        hf = [mul(z, evaluate(f_interp, base(a)))
              for z, a in zip(multipliers, norm_tags)]
        hg = [mul(z, evaluate(g_interp, base(a)))
              for z, a in zip(multipliers, norm_tags)]
        f_matches = [x == h for x, h in zip(f, hf)]
        g_matches = [x == h for x, h in zip(g, hg)]
        assert sum(f_matches) == sum(g_matches) == source_agreement
        assert sum(a and b for a, b in zip(f_matches, g_matches)) == source_agreement
        tested_labels = set()
        for tags in combinations(allowed, r):
            v = polynomial_roots(map(base, tags))
            ps = [neg(c) for c in v[:-1]]
            lam = neg(evaluate(v, BETA))
            assert lam != ZERO
            numerator = ps[:]
            numerator[0] = sub(numerator[0], evaluate(ps, BETA))
            quotient = [ZERO] * (r - 1)
            for j in range(r - 1, 0, -1):
                quotient[j - 1] = numerator[j]
                numerator[j - 1] = add(numerator[j - 1], mul(BETA, numerator[j]))
                numerator[j] = ZERO
            assert numerator[0] == ZERO
            assert (len(quotient) - 1) * M + w == strict_degree - 1
            matches = 0
            for x, a, z, fx, gx in zip(nodes, norm_tags, multipliers, f, g):
                h = mul(z, evaluate(quotient, base(a)))
                residual = sub(add(fx, mul(lam, gx)), h)
                expected = mul(mul(z, evaluate(v, base(a))), denominators[a])
                assert residual == expected
                assert (residual == ZERO) == (x in core or a in tags)
                if x == ZERO:
                    assert residual != ZERO
                matches += residual == ZERO
            assert matches == near_agreement
            tested_labels.add(lam)
        records.append(dict(r=r, padding=w, strict_degree=strict_degree,
                            source_and_common_agreement=source_agreement,
                            canonical_agreement=near_agreement,
                            distinct_labels_tested=len(tested_labels)))

out = dict(status="PASS", prime=P, extension_degree=D, field_size=Q,
           modulus="X^5-X-1", norm_packet_size=M, fixtures=records,
           elapsed_seconds=round(time.monotonic() - started, 3),
           peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
           scope="Exact degree-five full-domain padded compiler and simultaneous source attainment; no subset-product-surjectivity claim at p=5.")
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
