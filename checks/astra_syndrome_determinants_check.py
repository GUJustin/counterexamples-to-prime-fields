#!/usr/bin/env python3
"""Exact finite-field determinant and puncturing counts; no protocol code."""
from collections import Counter
from itertools import combinations, product
from math import comb
from pathlib import Path
import json
import random


def poly_eval(v, x, p):
    out = 0
    for a in reversed(v):
        out = (out*x+a) % p
    return out


def determinant(rows, p):
    rows = [row[:] for row in rows]
    out = 1
    for j in range(len(rows)):
        pivot = next((i for i in range(j, len(rows)) if rows[i][j] % p), None)
        if pivot is None:
            return 0
        if pivot != j:
            rows[j], rows[pivot] = rows[pivot], rows[j]
            out = -out
        value = rows[j][j] % p
        out = out*value % p
        inv = pow(value, -1, p)
        for i in range(j+1, len(rows)):
            factor = rows[i][j]*inv % p
            for t in range(j+1, len(rows)):
                rows[i][t] = (rows[i][t]-factor*rows[j][t]) % p
    return out % p


def locator(indices, xs, p):
    out = [1]
    for i in sorted(indices):
        new = [0]*(len(out)+1)
        for j, c in enumerate(out):
            new[j] = (new[j]-xs[i]*c) % p
            new[j+1] = (new[j+1]+c) % p
        out = new
    return out


def mask(indices):
    return sum(1 << i for i in indices)


def interpolate_value(indices, values, x, xs, p):
    out = 0
    for i in indices:
        num = den = 1
        for j in indices:
            if i != j:
                num = num*(x-xs[j]) % p
                den = den*(xs[i]-xs[j]) % p
        out = (out+values[i]*num*pow(den, -1, p)) % p
    return out


class Domain:
    def __init__(self, n, k, r, p, xs, counts):
        self.n, self.k, self.r, self.p = n, k, r, p
        self.xs, self.counts = xs, counts
        self.a, self.s, self.h = n-k, n-k-r, 2*r-(n-k)+1
        self.q = self.h-1
        assert self.a <= 2*r and r < self.a and p > self.s
        self.Ts = list(combinations(range(n), self.h))
        self.Qs = list(combinations(range(n), self.q))
        self.Q_masks = [mask(Q) for Q in self.Qs]
        self.T_index = {T: i for i, T in enumerate(self.Ts)}
        self.codewords = [[poly_eval(c, x, p) for x in xs]
                          for c in product(range(p), repeat=k)]
        self.dual = []
        for i, x in enumerate(xs):
            den = 1
            for j, y in enumerate(xs):
                if i != j:
                    den = den*(x-y) % p
            self.dual.append(pow(den, -1, p))
        self.vandermonde = [[pow(x, j, p) for j in range(r+1)] for x in xs]
        for degree in range(n-1):
            assert sum(w*pow(x, degree, p) for w, x in zip(self.dual, xs)) % p == 0
        assert sum(w*pow(x, n-1, p) for w, x in zip(self.dual, xs)) % p == 1
        self.ca_restrictions = []
        for I in combinations(range(n), n-r):
            self.ca_restrictions.append((I, {tuple(c[i] for i in I) for c in self.codewords}))
        assert self.s*comb(n, self.h)*comb(r, self.q) == (n-self.q)*comb(n, self.q)*comb(r, self.h)

    def syndrome(self, word):
        return [sum(w*y*pow(x, t, self.p) for w, y, x in zip(self.dual, word, self.xs)) % self.p
                for t in range(self.a)]

    def audit(self, f0, f1, label, forced_errors=None, force_admissible=False):
        n, k, r, p, s, h, q = self.n, self.k, self.r, self.p, self.s, self.h, self.q
        counts = self.counts
        S0, S1 = self.syndrome(f0), self.syndrome(f1)
        A = [[S0[l+j] for j in range(r+1)] for l in range(s)]
        B = [[S1[l+j] for j in range(r+1)] for l in range(s)]
        polynomials = []
        for T in self.Ts:
            coefficients = [0]*(s+1)
            bottom = [self.vandermonde[i] for i in T]
            # Multilinearity in the s affine rows gives exact coefficients.
            for choices in product((0, 1), repeat=s):
                top = [B[i] if choice else A[i] for i, choice in enumerate(choices)]
                d = sum(choices)
                coefficients[d] = (coefficients[d]+determinant(top+bottom, p)) % p
            polynomials.append(coefficients)
        zero_indices = [i for i, polynomial in enumerate(polynomials) if not any(polynomial)]
        admissible = not zero_indices
        if force_admissible:
            assert admissible and all(polynomial[s] for polynomial in polynomials)
        ca_sets = [I for I, code in self.ca_restrictions
                   if tuple(f0[i] for i in I) in code and tuple(f1[i] for i in I) in code]
        ca_masks = [mask(I) for I in ca_sets]
        ca = bool(ca_sets)
        if admissible:
            assert not ca
        support_core_cache = {}
        full_mask = (1 << n)-1

        def bad_core(support):
            if support not in support_core_cache:
                indices = [i for i in range(n) if support >> i & 1]
                assert len(indices) >= k
                anchors = indices[:k]
                failing = next((i for i in indices[k:]
                                if interpolate_value(anchors, f0, self.xs[i], self.xs, p) != f0[i]
                                or interpolate_value(anchors, f1, self.xs[i], self.xs, p) != f1[i]), None)
                support_core_cache[support] = None if failing is None else tuple(anchors+[failing])
            return support_core_cache[support]

        nearby, minimum_distances, near_by_Q = [], [], [[] for _ in self.Qs]
        bad_by_Q = [[] for _ in self.Qs]
        all_witnesses = bad_witnesses = 0
        incidence = 0
        min_multiplicity = None
        for z in range(p):
            word = [(a+z*b) % p for a, b in zip(f0, f1)]
            error_masks = [mask(i for i in range(n) if word[i] != c[i]) for c in self.codewords]
            distances = [E.bit_count() for E in error_masks]
            minimum_distances.append(min(distances))
            errors = [E for E, d in zip(error_masks, distances) if d <= r]
            zero_Ts = [i for i, polynomial in enumerate(polynomials) if poly_eval(polynomial, z, p) == 0]
            incidence += len(zero_Ts)
            # Check the coefficient calculation independently by scalar determinants.
            if z in (0, 1, p-1):
                rows = [[(a+z*b) % p for a, b in zip(ar, br)] for ar, br in zip(A, B)]
                for T, polynomial in zip(self.Ts, polynomials):
                    assert determinant(rows+[self.vandermonde[i] for i in T], p) == poly_eval(polynomial, z, p)
                    counts['independent_determinant_evaluations'] += 1
            q_hits = []
            bad_q_hits = Counter()
            for j, Q_mask in enumerate(self.Q_masks):
                survivors = [(ci, E) for ci, E in enumerate(error_masks) if (E & ~Q_mask).bit_count() <= s]
                assert len(survivors) <= 1
                if survivors:
                    near_by_Q[j].append(z)
                    q_hits.append(j)
                    ci, E = survivors[0]
                    assert E.bit_count() <= r
                    counts['unique_punctured_nearby_witness_checks'] += 1
                    if bad_core(full_mask & ~(E | Q_mask)) is not None:
                        bad_by_Q[j].append((z, ci))
                        bad_q_hits[E] += 1
                        counts['punctured_exact_support_bad_witness_pairs'] += 1
            if errors:
                nearby.append(z)
                assert len(zero_Ts) >= comb(r, h)
                assert len(q_hits) >= comb(r, q)
                min_multiplicity = len(zero_Ts) if min_multiplicity is None else min(min_multiplicity, len(zero_Ts))
                for E_mask in errors:
                    all_witnesses += 1
                    E = {i for i in range(n) if E_mask >> i & 1}
                    core = bad_core(full_mask & ~E_mask)
                    if core is not None:
                        bad_witnesses += 1
                        assert len(core) == k+1 and not (mask(core) & E_mask)
                        assert bad_core(mask(core)) is not None
                        assert bad_q_hits[E_mask] >= comb(r, q)
                        available = [i for i in range(n) if i not in E and i not in core]
                        protected_R = sorted(E | set(available[:r-len(E)]))
                        assert len(protected_R) == r and not (set(protected_R) & set(core))
                        for Q in combinations(protected_R, q):
                            assert (E_mask & ~mask(Q)).bit_count() <= s
                            assert not (set(Q) & set(core))
                            assert bad_core(full_mask & ~(E_mask | mask(Q))) is not None
                            counts['protected_core_puncturing_witnesses_checked'] += 1
                        counts['protected_bad_cores_checked'] += 1
                    else:
                        assert not bad_q_hits[E_mask]
                    R = sorted(E | set([i for i in range(n) if i not in E][:r-len(E)]))
                    assert len(R) == r
                    for T in combinations(R, h):
                        polynomial = locator(E | set(T), self.xs, p)
                        assert len(polynomial) <= r+1
                        padded = polynomial+[0]*(r+1-len(polynomial))
                        for ar, br in zip(A, B):
                            assert sum((a+z*b)*c for a, b, c in zip(ar, br, padded)) % p == 0
                        assert all(poly_eval(polynomial, self.xs[i], p) == 0 for i in T)
                        assert poly_eval(polynomials[self.T_index[T]], z, p) == 0
                        counts['extended_locator_witnesses_checked'] += 1
                    for Q in combinations(R, q):
                        assert (E_mask & ~mask(Q)).bit_count() <= s
                        counts['extended_puncturing_witnesses_checked'] += 1
            counts['parameters_exactly_decoded'] += 1
            counts['codeword_distances_checked'] += len(error_masks)
        if forced_errors is not None:
            assert minimum_distances[0] <= forced_errors
            counts[f'forced_error_{forced_errors}_fixtures'] += 1
        if ca:
            assert len(nearby) == p
            counts['ca_pencils_excluded_from_unconditional_bound'] += 1
        else:
            assert all(len(zs) <= n-q for zs in near_by_Q)
            assert len(nearby)*comb(r, q) <= sum(map(len, near_by_Q)) <= (n-q)*comb(n, q)
            assert len(nearby)*comb(r, h) <= s*comb(n, h)
            counts['non_ca_puncturing_bound_checks'] += 1
            assert all_witnesses == bad_witnesses
            assert all_witnesses*comb(r, q) <= (n-q)*comb(n, q)
            if not admissible:
                counts['non_ca_zero_determinant_pencils'] += 1
                counts['non_ca_zero_determinant_pencils_with_nearby_parameter'] += bool(nearby)
        for Q_mask, bad_pairs in zip(self.Q_masks, bad_by_Q):
            punctured_ca = any(not (I_mask & Q_mask) for I_mask in ca_masks)
            assert len(bad_pairs) <= (s if punctured_ca else n-q)
            counts['punctured_ca_exact_support_bound_checks' if punctured_ca
                   else 'punctured_non_ca_exact_support_bound_checks'] += 1
        assert bad_witnesses*comb(r, q) <= sum(map(len, bad_by_Q)) <= (n-q)*comb(n, q)
        assert bad_witnesses*comb(r, h) <= s*comb(n, h)
        counts['exact_support_mca_bound_checks_all_pencils'] += 1
        counts['all_nearby_witness_pairs'] += all_witnesses
        counts['exact_support_bad_witness_pairs'] += bad_witnesses
        counts['exact_support_bad_witness_pairs_on_ca_pencils'] += bad_witnesses if ca else 0
        if admissible:
            degree_sum = sum(max(i for i, c in enumerate(v) if c) for v in polynomials)
            assert len(nearby)*comb(r, h) <= incidence <= degree_sum <= s*len(self.Ts)
            counts['admissible_determinant_bound_checks'] += 1
        else:
            counts['identically_zero_determinant_pencils_excluded'] += 1
        counts['pencils_checked'] += 1
        counts['determinant_polynomials_checked'] += len(polynomials)
        counts['punctured_pencils_exactly_decoded'] += len(self.Qs)
        counts['nearby_parameters_checked'] += len(nearby)
        return dict(label=label, determinant_admissible=admissible, ca=ca,
                    identically_zero_determinants=len(zero_indices), nearby_parameters=nearby,
                    minimum_distances=minimum_distances, minimum_zero_determinant_multiplicity=min_multiplicity,
                    maximum_punctured_nearby_count=max(map(len, near_by_Q)),
                    puncturing_incidence=sum(map(len, near_by_Q)),
                    all_nearby_witness_pairs=all_witnesses,
                    exact_support_bad_witness_pairs=bad_witnesses,
                    maximum_punctured_exact_support_bad_count=max(map(len, bad_by_Q)),
                    exact_support_bad_puncturing_incidence=sum(map(len, bad_by_Q)))


def main():
    rng = random.Random(2026091507)
    counts = Counter()
    configurations = []
    for n, k, r in [(6, 2, 2), (7, 1, 3), (6, 1, 3), (7, 2, 3), (6, 2, 3), (7, 1, 4)]:
        primes = [11, 17] + ([19] if (n, k, r) == (7, 1, 4) else [])
        for p in primes:
            for domain_type in ('consecutive', 'sampled'):
                xs = list(range(n)) if domain_type == 'consecutive' else rng.sample(range(p), n)
                domain = Domain(n, k, r, p, xs, counts)
                records = []
                for trial in range(6):
                    records.append(domain.audit([rng.randrange(p) for _ in range(n)],
                                                [rng.randrange(p) for _ in range(n)], f'random_{trial}'))
                for e in sorted({0, 1, r-1}):
                    for trial in range(2):
                        f0 = rng.choice(domain.codewords)[:]
                        for i in rng.sample(range(n), e):
                            f0[i] = (f0[i]+rng.randrange(1, p)) % p
                        # Degree n-r-1 gives all D_T nonzero leading coefficient.
                        direction = [rng.randrange(p) for _ in range(n-r-1)]+[rng.randrange(1, p)]
                        f1 = [poly_eval(direction, x, p) for x in xs]
                        records.append(domain.audit(f0, f1, f'forced_{e}_{trial}', e, True))
                records.append(domain.audit(rng.choice(domain.codewords), rng.choice(domain.codewords), 'codeword_line'))
                f0, f1 = rng.choice(domain.codewords)[:], rng.choice(domain.codewords)[:]
                for i in rng.sample(range(n), r):
                    f0[i] = (f0[i]+rng.randrange(1, p)) % p
                    f1[i] = (f1[i]+rng.randrange(1, p)) % p
                records.append(domain.audit(f0, f1, 'fixed_error_support_line'))
                if domain.s >= 2:
                    beta = next(x for x in range(p) if x not in xs)
                    f0 = [pow((x-beta) % p, -1, p) for x in xs]
                    f1 = [0]*n
                    if domain.h >= domain.s:
                        A = list(range(k))
                        J = list(range(k, k+domain.s))
                        c = [interpolate_value(A, f0, x, xs, p) for x in xs]
                        for j in J:
                            f1[j] = (c[j]-f0[j]) % p
                        label = 'non_ca_zero_determinant_near_at_1'
                    else:
                        f1[0] = 1
                        label = 'non_ca_zero_determinant_single_point_direction'
                    result = domain.audit(f0, f1, label)
                    assert not result['ca'] and not result['determinant_admissible']
                    if domain.h >= domain.s:
                        assert 1 in result['nearby_parameters']
                    records.append(result)
                configurations.append(dict(n=n, k=k, r=r, p=p, a=domain.a, s=domain.s,
                    h=domain.h, q=domain.q, domain_type=domain_type, domain=xs,
                    bound_numerator=domain.s*comb(n, domain.h), bound_denominator=comb(r, domain.h),
                    integer_parameter_bound=domain.s*comb(n, domain.h)//comb(r, domain.h), records=records))
    result = dict(status='all exact assertions passed', seed=2026091507,
                  counts=dict(counts), configurations=configurations,
                  scope='Small ordinary Reed-Solomon codes; complete parameter and codeword enumeration for each tested pencil.')
    target = Path(__file__).with_name('astra_syndrome_determinants_verified.json')
    target.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps(dict(status=result['status'], counts=dict(counts), configurations=len(configurations)), indent=2))


if __name__ == '__main__':
    main()
