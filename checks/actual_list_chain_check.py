#!/usr/bin/env python3
"""Exact finite checks of an elementary RS list lower-bound construction.

No protocol implementation. The global upper bound and generic-domain existence
are theorem-level statements, not certified by these finite fixtures.
"""
from pathlib import Path
import json
import random


def multiply(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def evaluate(poly, x, p):
    value = 0
    for c in reversed(poly):
        value = (value*x+c) % p
    return value


def fixture(domain, k, p):
    n = len(domain)
    a = n-k
    assert k >= 2 and a >= 2 and len(set(domain)) == n
    common = domain[:k-2]
    x = domain[k-2:]
    A, B, z0, zero = x[:4]
    z = [z0] + x[4:]
    center = {A: 0, B: 0, zero: 0, z0: 1}
    # The zero polynomial plus a-2 nonzero affine polynomials.
    lines = [(0, 0)]
    slopes = []
    for j in range(1, a-1):
        anchor = A if j % 2 else B
        c = center[z[j-1]] * pow((z[j-1]-anchor) % p, -1, p) % p
        assert c != 0
        line = ((-c*anchor) % p, c)
        center[z[j]] = evaluate(line, z[j], p)
        assert all(evaluate(line, t, p) == center[t] for t in [anchor, z[j-1], z[j]])
        slopes.append(c)
        lines.append(line)
    # Verify every possible repeated-line condition against its cleared
    # denominator polynomial, including fixtures where repetition does occur.
    collision_checks = 0
    for i in range(1, a-1):
        for j in range(i+1, a-1):
            if (i-j) % 2:
                assert lines[i] != lines[j]
                continue
            first = second = 1
            for r in range(i, j):
                anchor = A if r % 2 else B
                other = B if r % 2 else A
                first = first*(z[r]-anchor) % p
                second = second*(z[r]-other) % p
            assert (first == second) == (lines[i] == lines[j])
            collision_checks += 1
    F = [1]
    for h in common:
        F = multiply(F, [-h % p, 1], p)
    lifted = [multiply(F, list(q), p) for q in lines]
    received = {h: 0 for h in common}
    received.update({t: evaluate(F, t, p)*center[t] % p for t in x})
    agreements = []
    for q in lifted:
        assert len(q) <= k
        agreements.append(sum(evaluate(q, t, p) == received[t] for t in domain))
    assert min(agreements) >= k+1
    distinct = len({tuple(q) for q in lifted})
    assert distinct == len(set(lines))
    return distinct == a-1, collision_checks, len(lifted), n*len(lifted)


def main():
    rng = random.Random(20260915)
    fixtures = successful = collisions = witnesses = coordinates = 0
    first_collision = None
    for p in [101, 65537, 2147483647]:
        for n in range(4, 41):
            for k in range(2, n-1):
                domain = rng.sample(range(p), n)
                good, checks, count, coords = fixture(domain, k, p)
                fixtures += 1
                successful += good
                collisions += checks
                witnesses += count
                coordinates += coords
                if not good and first_collision is None:
                    first_collision = {'p': p, 'n': n, 'k': k, 'domain': domain}
    assert first_collision is not None
    arithmetic = 0
    for n in range(4, 501):
        for k in range(2, n-1):
            a = n-k
            # a^3 / p < 2^(-2an), given p > k*2^(10an).
            assert (a**3).bit_length() <= 8*a*n
            assert 2*a*n >= 2  # equivalently, 3 < 2**(2*a*n)
            arithmetic += 1
    result = {
        'status': 'passed',
        'field_primes': [101, 65537, 2147483647],
        'fixtures': fixtures,
        'fixtures_with_all_n_minus_k_minus_1_distinct_witnesses': successful,
        'fixtures_with_repeated_chain_lines': fixtures-successful,
        'cleared_denominator_collision_checks': collisions,
        'polynomial_witnesses_checked_including_repetitions': witnesses,
        'coordinate_checks': coordinates,
        'simultaneous_domain_probability_inequalities': arithmetic,
        'example_showing_chain_distinctness_is_not_automatic': first_collision,
        'scope': 'Exact checks of degree, agreements, repetitions, and probability arithmetic. Generic nonvanishing and the global upper bound require the separate mathematical proofs.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
