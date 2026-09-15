#!/usr/bin/env python3
"""Exact research checks plus a model of the pinned quotient schedule.

The Python schedule is checked against the recorded Rust source, not a native
execution of Stwo. No complete-proof acceptance is tested.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, gcd, log2
from pathlib import Path
import hashlib
import json
import verify_fixed_claim as ff

F = ff.F


def bound(N, S, p, K, T, n0, G):
    q, r = divmod(N*T, n0)
    overlap = (n0-r)*comb(q, 2)+r*comb(q+1, 2)
    collisions = K*comb(N, 2)-overlap
    assert collisions >= 0
    numerator = G*N*N*S*S
    denominator = p**4*(N*S+2*collisions)
    A = ff.ceil_fraction(numerator, denominator)
    assert (A-1)*denominator < numerator <= A*denominator
    return A, overlap, collisions


def certificates():
    p = 2**31-1
    N = ff.ceil_fraction(comb(255, 66), 256)
    S = (p*p-1)**2
    linear, R, C = bound(N, S, p, 128, 132, 510, p*p)
    cubic, _, _ = bound(N, S, p, 128, 132, 510, 2*p*p-1)
    trimmed, _, _ = bound(N, S-(p*p-1), p, 128, 132, 510, 2*p*p-1)
    assert linear == 1045232662865816582797566371469227027334159065108360767
    assert (2**68)*trimmed > p**8
    assert trimmed <= cubic
    assert p**96 * 95**95 * 33**33 < (p-1)**95 * 128**128
    power_rows = []
    for d, exponent in [(1, 69), (2, 68), (5, 67), (10, 66)]:
        assert (p*p+1) % d == 0
        good = 1+(p*p-1)*gcd(d, p*p+1)
        pairs, _, _ = bound(N, S, p, 128, 132, 510, good)
        assert (2**exponent)*pairs > p**8
        power_rows.append(dict(power_gap=d, columns=d+1, qualifying_challenges=good,
                               pairs=pairs, approximate_bits=-log2(Fraction(pairs, p**8)),
                               strict_probability_lower=f'2^-{exponent}'))
    return dict(N=N, admissible_samples=S, selected_coordinate_pool=510,
        forced_pair_roots_lower=R, admissible_pair_collisions_upper=C,
        linear_pairs=linear, cubic_pairs=cubic, source_cubic_pairs=trimmed,
        source_admissible_samples_lower=S-(p*p-1),
        linear_bound_bits=-log2(Fraction(linear, p**8)),
        cubic_bound_bits=-log2(Fraction(cubic, p**8)),
        source_cubic_bound_bits=-log2(Fraction(trimmed, p**8)),
        source_cubic_strict_probability_lower_bound="2^-68",
        power_gap_rows=power_rows,
        radius_audit=dict(rate="1/4", gap="1/128", radius="95/128",
                          exact_above_Elias_inequality=True))


def balanced_overlap_check():
    checked = 0
    for n in range(2, 7):
        for t in range(1, n+1):
            supports = list(map(set, combinations(range(n), t)))
            minimum = None
            for chosen in product(supports, repeat=3):
                degrees = [sum(x in a for a in chosen) for x in range(n)]
                root_count = sum(len(a & b) for a, b in combinations(chosen, 2))
                assert root_count == sum(comb(d, 2) for d in degrees)
                q, r = divmod(3*t, n)
                bound_value = (n-r)*comb(q, 2)+r*comb(q+1, 2)
                assert root_count >= bound_value
                minimum = root_count if minimum is None else min(minimum, root_count)
                checked += 1
            # These small set systems also attain the integer balancing bound.
            assert minimum == bound_value
    return checked


def circle(a):
    i = F((0, 1, 0, 0))
    return (a+a**-1)/2, (a-a**-1)/(2*i)


def admissible(a):
    return a != F(0) and a[2:] != (0, 0) and circle(a)[1][2:] != (0, 0)


def raw(table, claim, point, domain_point):
    zx, zy = point
    x, y = domain_point
    X0, X1 = ff.parts(zx)
    Y0, Y1 = ff.parts(zy)
    la, lc = ff.conjugate(claim)-claim, ff.conjugate(zy)-zy
    assert lc != F(0)
    lb = claim*lc-la*zy
    denominator = (X0-x)*Y1-(Y0-y)*X1
    return (lc*table-la*y-lb)/denominator/F((0, 0, 1, 0))


def power_schedule(columns, offsets=0):
    """Pinned branch: prepend duplicate current point for two maximal-size samples."""
    scheduled = []
    exponent = offsets
    for column, samples in enumerate(columns):
        expanded = ([samples[1]] if len(samples) == 2 else [])+samples
        for point, claim in expanded:
            scheduled.append((column, point, claim, exponent))
            exponent += 1
    return scheduled


def schedule_and_field_checks():
    p = ff.P
    assert p == 7
    zero, one, i = F(0), F(1), F((0, 1, 0, 0))
    elements = [F(c) for c in product(range(p), repeat=4)]
    powers = {}
    for d in [1, 2, 3, 5, 10]:
        observed = sum((a**d)[2:] == (0, 0) for a in elements)
        expected = 1+(p*p-1)*gcd(d, p*p+1)
        assert observed == expected
        powers[str(d)] = observed
    cubic_good = [a for a in elements if (a+a**3)[2:] == (0, 0)]
    assert len(cubic_good) == 2*p*p-1 == 97
    samples = [a for a in elements if admissible(a)]
    domain = [(F(x), F(y)) for x in range(p) for y in range(p)
              if (x*x+y*y) % p == 1]
    nonzero_positions = [j for j, (x, _) in enumerate(domain) if x != zero]
    table = [zero]*len(domain)
    for j in nonzero_positions[:3]:
        table[j] = domain[j][0]
    # Rotate the previous point by i. Both denominators are checked.
    h = i
    safe_samples = [a for a in samples if admissible(h*a)]
    assert len(samples)-len(safe_samples) == p*p-1
    # All incidences and all qualifying challenges are counted, including repeats
    # of a+a^3. Each fixed claim gets one count per distinct (sample, challenge).
    phi_counts = Counter(a+a**3 for a in cubic_good)
    claim_counts = Counter()
    incidence_count = 0
    for a in safe_samples:
        zx, _ = circle(a)
        values = {zero, zx}
        incidence_count += len(values)
        for b in values:
            for coefficient, multiplicity in phi_counts.items():
                claim_counts[b-coefficient] += multiplicity
    assert sum(claim_counts.values()) == incidence_count*len(cubic_good)
    fixed_claim = max(claim_counts, key=lambda c: (claim_counts[c], c))
    assert claim_counts[fixed_claim] >= ff.ceil_fraction(incidence_count*len(cubic_good), p**4)
    # Check an explicit fixed claim throughout 12 sample fixtures and EVERY
    # challenge in the extension field against the generated weighted schedule.
    fixtures = safe_samples[::max(1, len(safe_samples)//12)][:12]
    direct_checks, nonlinear_counterexamples, selected_checks = 0, 0, 0
    for a in fixtures:
        z, zprev = circle(a), circle(h*a)
        columns = [[(z, fixed_claim)], [(zprev, zero), (z, one)]]
        scheduled = power_schedule(columns)
        assert [entry[3] for entry in scheduled] == [0, 1, 2, 3]
        assert scheduled[1][1] == scheduled[3][1] == z
        for point_index in [0, 3, 7]:
            pt = domain[point_index]
            q0 = raw(table[point_index], fixed_claim, z, pt)
            q1 = raw(zero, one, z, pt)
            terms = [(raw(table[point_index] if col == 0 else zero, claim, zp, pt), exponent)
                     for col, zp, claim, exponent in scheduled]
            assert terms[2][0] == zero
            for challenge in elements:
                direct = sum((challenge**e * value for value, e in terms), zero)
                assert direct == q0+(challenge+challenge**3)*q1
                nonlinear_counterexamples += int(direct != q0+challenge*q1)
                direct_checks += 1
        # Verify every retained cubic label against its constant quotient witness
        # at all coordinates; claim is fixed across all samples and challenges.
        zx, _ = z
        for challenge in cubic_good:
            b = fixed_claim+challenge+challenge**3
            if b not in {zero, zx}:
                continue
            witness = zero if b == zero else F(2)
            agreements = 0
            for j, pt in enumerate(domain):
                result = raw(table[j], fixed_claim, z, pt)+(challenge+challenge**3)*raw(zero, one, z, pt)
                agreements += int(result == witness)
            assert agreements == 5
            selected_checks += 1
    assert nonlinear_counterexamples > 0
    padded_checks = 0
    # Exhaustive original challenges, for four gaps and three coordinates.
    a = fixtures[0]
    z = circle(a)
    for d in [1, 2, 5, 10]:
        columns = [[(z, fixed_claim)]]+([[(z, zero)]]*(d-1))+[[(z, one)]]
        scheduled = power_schedule(columns)
        assert len(scheduled) == d+1
        for j in [0, 3, 7]:
            terms = [(raw(table[j] if col == 0 else zero, claim, zp, domain[j]), e)
                     for col, zp, claim, e in scheduled]
            assert all(value == zero for value, _ in terms[1:-1])
            for challenge in elements:
                direct = sum((challenge**e*value for value, e in terms), zero)
                assert direct == terms[0][0]+challenge**d*terms[-1][0]
                padded_checks += 1
    return dict(field=p, power_preimage_counts=powers,
        cubic_preimage_count=len(cubic_good), admissible_samples=len(samples),
        safe_previous_rotation_samples=len(safe_samples),
        cubic_fixed_claim=list(fixed_claim), cubic_observed_pairs=claim_counts[fixed_claim],
        source_model_sample_fixtures=len(fixtures),
        source_model_identity_checks=direct_checks,
        non_linear_schedule_counterexamples=nonlinear_counterexamples,
        selected_cubic_witness_checks=selected_checks,
        padded_power_schedule_identity_checks=padded_checks,
        caveat="Python model of pinned source; no native Rust execution or full-proof verification.")


def source_provenance():
    root = Path('/Users/jthaler/Documents/stwo_audit_2026-09-15/repositories/proving_zk')
    paths = ['crates/stwo/src/core/pcs/quotients.rs', 'crates/stwo/src/core/constraints.rs',
             'crates/stwo/src/core/circle.rs', 'crates/stwo/src/core/pcs/verifier.rs']
    return dict(commit='cd7bc5f4697fb188a27e09f9242f1dd76df8afdc',
                files={p: hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths})


if __name__ == '__main__':
    result = dict(status='passed', large_instance=certificates(),
        balanced_support_systems=balanced_overlap_check(),
        field_and_schedule=schedule_and_field_checks(), source=source_provenance())
    Path(__file__).with_name('scheduled_transfer_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
