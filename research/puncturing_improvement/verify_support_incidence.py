#!/usr/bin/env python3
"""Exact finite-field checks for the attributed support-incidence corollary.

No protocol code, floating-point tests, or optional dependencies are used.
"""
import json
import random
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path


def ev(coeffs, x, p):
    y = 0
    for c in reversed(coeffs):
        y = (y * x + c) % p
    return y


def code(n, k, p):
    return [tuple(ev(c, x, p) for x in range(n))
            for c in product(range(p), repeat=k)]


def restriction_sets(words, n, k):
    return {a: {tuple(w[i] for i in a) for w in words}
            for b in range(k + 1, n + 1)
            for a in combinations(range(n), b)}


def main():
    totals = dict(local_words=0, local_noncodewords=0, local_checks=0,
                  curves=0, parameters=0, distance_evaluations=0,
                  bad_pairs=0, bad_pairs_on_joint_curves=0,
                  weighted_checks=0, ownership_checks=0,
                  degree_at_least_field_size_curves=0,
                  optimization_checks=0, puncturing_identity_checks=0)
    # Exhaustive words, not just sampled words, for the local ingredient.
    for n, k, p in [(3, 1, 3), (4, 1, 5), (4, 2, 5), (5, 2, 5)]:
        words = code(n, k, p)
        cset = set(words)
        restrictions = restriction_sets(words, n, k)
        for w in product(range(p), repeat=n):
            totals['local_words'] += 1
            if w in cset:
                continue
            totals['local_noncodewords'] += 1
            for b in range(k + 1, n + 1):
                rejecting = sum(tuple(w[i] for i in a) not in restrictions[a]
                                for a in combinations(range(n), b))
                assert rejecting >= comb(n - 1, b - 1)
                totals['local_checks'] += 1
        for x in range(n):
            w = tuple(int(i == x) for i in range(n))
            for b in range(k + 1, n + 1):
                rejecting = sum(tuple(w[i] for i in a) not in restrictions[a]
                                for a in combinations(range(n), b))
                assert rejecting == comb(n - 1, b - 1)

    rng = random.Random(202609151943)
    for n, k, p in [(4, 2, 5), (5, 2, 7), (6, 2, 7), (5, 1, 7)]:
        words = code(n, k, p)
        restrictions = restriction_sets(words, n, k)
        for e in (0, 1, 2, 3, p, p + 1):
            for fixture in range(12):
                fs = [[rng.randrange(p) for _ in range(n)] for _ in range(e + 1)]
                # Mixed fixtures include joint supports and formal degrees >=q.
                t = k + 1 + fixture % (n - k)
                if fixture % 2 == 0:
                    for f in fs:
                        c = rng.choice(words)
                        f[:t] = c[:t]
                if e >= p and fixture == 1:
                    # z^p-z vanishes as a function, but is formally nonzero.
                    f = [rng.randrange(p) for _ in range(n)]
                    fs = [[0] * n for _ in range(e + 1)]
                    fs[p] = f[:]
                    fs[1] = [(-x) % p for x in f]
                unexplained = {
                    a: any(tuple(f[i] for i in a) not in vals for f in fs)
                    for a, vals in restrictions.items()}
                has_joint = any(not bad for a, bad in unexplained.items()
                                if len(a) == t)
                bad_supports = []
                owners = {a: [] for a, bad in unexplained.items() if bad}
                for z in range(p):
                    received = tuple(ev([f[i] for f in fs], z, p) for i in range(n))
                    for ci, c in enumerate(words):
                        support = tuple(i for i in range(n) if received[i] == c[i])
                        if len(support) < t:
                            continue
                        if unexplained[support]:
                            bad_supports.append(support)
                            for b in range(k + 1, t + 1):
                                for a in combinations(support, b):
                                    if unexplained[a]:
                                        owners[a].append((z, ci))
                for b in range(k + 1, t + 1):
                    weighted = sum(comb(len(s) - 1, b - 1) for s in bad_supports)
                    tb = sum(bad for a, bad in unexplained.items() if len(a) == b)
                    assert weighted <= min(e, p) * tb
                    assert len(bad_supports) * comb(t - 1, b - 1) <= min(e, p) * comb(n, b)
                    totals['weighted_checks'] += 1
                for a, owner_list in owners.items():
                    if len(a) <= t:
                        assert len(owner_list) == len(set(owner_list))
                        assert len(owner_list) <= min(e, p)
                        totals['ownership_checks'] += 1
                totals['curves'] += 1
                totals['parameters'] += p
                totals['distance_evaluations'] += p * len(words)
                totals['bad_pairs'] += len(bad_supports)
                totals['bad_pairs_on_joint_curves'] += len(bad_supports) * has_joint
                totals['degree_at_least_field_size_curves'] += e >= p
    assert totals['bad_pairs_on_joint_curves'] > 0

    for n in range(3, 61):
        for k in range(1, n):
            for t in range(k + 1, n + 1):
                bstar = min(t, max(k + 1, (t + n - t) // (n - t + 1)))
                optimum = Fraction(comb(n, bstar), comb(t - 1, bstar - 1))
                for b in range(k + 1, t + 1):
                    assert optimum <= Fraction(comb(n, b), comb(t - 1, b - 1))
                if 2 * (n - t) >= n - k:
                    assert bstar == k + 1
                totals['optimization_checks'] += 1
            a = n - k
            for r in range((a + 1) // 2, a):
                t = n - r
                base = Fraction(comb(n, k + 1), comb(t - 1, k))
                for u in range(r + 1):
                    punctured = (Fraction(comb(n, u), comb(r, u)) *
                                 Fraction(comb(n - u, k + 1), comb(t - 1, k)))
                    assert punctured == base * Fraction(comb(n - k - 1, u), comb(r, u))
                    assert punctured >= base
                    totals['puncturing_identity_checks'] += 1

    examples = []
    for n, k, r in [(10, 2, 6), (16, 4, 9), (32, 16, 14),
                    (64, 32, 30), (10, 2, 4), (10, 2, 7)]:
        a = n - k
        d = 2 * r - a
        pbound = Fraction((n - d) * comb(n, d), comb(r, d))
        cbound = Fraction(comb(n, k + 1), comb(n - r - 1, k))
        examples.append(dict(n=n, k=k, r=r, t=n-r,
                             puncturing_floor=pbound.numerator // pbound.denominator,
                             circuit_floor=cbound.numerator // cbound.denominator,
                             improvement_factor=str(pbound / cbound)))
    result = {'status': 'passed', 'coverage': totals, 'comparisons': examples,
              'scope': 'Local words exhaustive in four fixtures; all parameters and codewords for 288 deterministic curves. No protocol experiments.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
