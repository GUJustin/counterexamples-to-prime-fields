#!/usr/bin/env python3
"""Exact fixed-claim certificates. Standard library only; no protocol attack."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb, log2
from pathlib import Path
import json

P = 7


class F(tuple):
    """Fp[i,w], i^2=-1, w^2=2+i. This tower is a field for p=7."""
    def __new__(cls, value=0):
        if isinstance(value, (tuple, list)):
            return tuple.__new__(cls, (x % P for x in value))
        return tuple.__new__(cls, (value % P, 0, 0, 0))

    def __add__(a, b):
        return F(tuple(x + y for x, y in zip(a, F(b))))

    __radd__ = __add__

    def __neg__(a):
        return F(tuple(-x for x in a))

    def __sub__(a, b):
        return a + -F(b)

    def __rsub__(a, b):
        return F(b) + -a

    def __mul__(a, b):
        b = F(b)
        def cm(x, y):
            return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])
        ac, bd = cm(a[:2], b[:2]), cm(a[2:], b[2:])
        ad, bc = cm(a[:2], b[2:]), cm(a[2:], b[:2])
        kbd = cm((2, 1), bd)
        return F((ac[0]+kbd[0], ac[1]+kbd[1], ad[0]+bc[0], ad[1]+bc[1]))

    __rmul__ = __mul__

    def __pow__(a, exponent):
        if exponent < 0:
            return inverse(a) ** (-exponent)
        result = F(1)
        while exponent:
            if exponent & 1:
                result = result * a
            a = a * a
            exponent >>= 1
        return result

    def __truediv__(a, b):
        return a * inverse(F(b))


@lru_cache(None)
def inverse(a):
    assert a != F(0), "Zero denominator"
    return a ** (P**4 - 2)


def conjugate(a):
    return F((a[0], a[1], -a[2], -a[3]))


def parts(a):
    return F((a[0], a[1], 0, 0)), F((a[2], a[3], 0, 0))


def ceil_fraction(numerator, denominator):
    return (numerator + denominator - 1) // denominator


def large_certificate():
    p, K = 2**31-1, 128
    N = ceil_fraction(comb(255, 66), 256)
    S = (p*p-1)**2
    A = ceil_fraction(N*S*S, p*p*(S+K*(N-1)))
    old_D = ceil_fraction(N*S, S+2*K*(N-1))
    old_J = ceil_fraction(old_D, p*p)
    assert A == 766247768292072891947921916124690454684786490150411277
    assert old_J == 18014398492704768
    probability = Fraction(A, p**8)
    old_probability = Fraction(S*old_J, 2*p**8)
    assert probability > Fraction(1, 2**69)
    ratio = probability/old_probability
    assert Fraction(3999, 1000) < ratio < Fraction(4001, 1000)
    # Cross-multiplied checks of the exact ceiling and the rational bound.
    denominator = p*p*(S+K*(N-1))
    assert (A-1)*denominator < N*S*S <= A*denominator
    return dict(p=p, n=512, K=K, T=132, N=N, S=S, A=A,
                probability_numerator=probability.numerator,
                probability_denominator=probability.denominator,
                strict_lower_bound="2^-69", old_J=old_J,
                approximate_new_bits=-log2(probability),
                approximate_old_joint_bits=-log2(old_probability),
                approximate_improvement=float(ratio))


def exhaustive_toy():
    zero, one, i, w = F(0), F(1), F((0, 1, 0, 0)), F((0, 0, 1, 0))
    elements = [F(c) for c in product(range(P), repeat=4)]
    # Check the extension actually is a field; division never silently maps 0 to 0.
    assert all(a*inverse(a) == one for a in elements if a != zero)
    domain = [(F(x), F(y)) for x in range(P) for y in range(P)
              if (x*x+y*y) % P == 1]
    assert len(domain) == 8
    # F_0=0 and F_1=x lie in the outer band [-1,1]. They agree at two points.
    nonzero_positions = [j for j, (x, _) in enumerate(domain) if x != zero]
    f = [zero for _ in domain]
    for j in nonzero_positions[:3]:
        f[j] = domain[j][0]
    assert sum(v == zero for v in f) == 5
    assert sum(v == x for v, (x, _) in zip(f, domain)) == 5
    N, K, T = 2, 2, 5
    records, coset_totals = [], Counter()
    collisions, distinct_incidences = 0, 0
    collision_family_total, collision_family_distinct = 0, 0
    pair_roots = Counter()
    for a in elements:
        if a == zero or a[2:] == (0, 0):
            continue
        zx, zy = (a+inverse(a))/2, (a-inverse(a))/(2*i)
        if zy[2:] == (0, 0):
            continue
        assert a != conjugate(a)
        assert zx*zx+zy*zy == one
        vals = {zero, zx}
        collisions += int(zx == zero)
        distinct_incidences += len(vals)
        for b in vals:
            coset_totals[b[2:]] += 1
        records.append((a, zx, zy, vals))
    # Choose a nonzero real outer-band polynomial vanishing at a generic sample.
    # Its five coefficients satisfy four base-field linear equations.
    _, sx, sy, _ = records[0]
    basis = [one, sx, sy, sx*sx, sx*sy]
    matrix = [[b[row] for b in basis] for row in range(4)]
    pivots = []
    for col in range(5):
        row = len(pivots)
        pivot = next((r for r in range(row, 4) if matrix[r][col]), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        scale = pow(matrix[row][col], -1, P)
        matrix[row] = [v*scale % P for v in matrix[row]]
        for r in range(4):
            if r != row:
                scale = matrix[r][col]
                matrix[r] = [(v-scale*b) % P for v, b in zip(matrix[r], matrix[row])]
        pivots.append(col)
    free = next(c for c in range(5) if c not in pivots)
    coefficients = [0]*5
    coefficients[free] = 1
    for row, col in enumerate(pivots):
        coefficients[col] = -matrix[row][free] % P
    for _, zx, zy, _ in records:
        g = sum((c*b for c, b in zip(coefficients, [one, zx, zy, zx*zx, zx*zy])), zero)
        fs = [zero, g, g+one]
        multiplicities = Counter(fs)
        collision_family_distinct += len(multiplicities)
        collision_family_total += sum(c*(c-1)//2 for c in multiplicities.values())
        for j in range(3):
            for k in range(j):
                pair_roots[k, j] += int(fs[k] == fs[j])
    S = (P*P-1)**2
    assert len(records) == S == 2304
    assert distinct_incidences*(N*S+2*collisions) >= (N*S)**2
    assert collisions <= comb(N, 2)*K
    assert 0 < collision_family_total <= comb(3, 2)*4
    assert all(c <= 4 for c in pair_roots.values())
    assert collision_family_distinct*(3*S+2*collision_family_total) >= (3*S)**2

    # Exhaust the actual rational sampler, including the two singular draws.
    sampler_counts = Counter()
    singular = 0
    admissible_as = {a for a, _, _, _ in records}
    for t in elements:
        denominator = one+t*t
        if denominator == zero:
            singular += 1
            continue
        zx, zy = (one-t*t)/denominator, (2*t)/denominator
        a = zx+i*zy
        if a in admissible_as:
            sampler_counts[a] += 1
    assert singular == 2
    assert set(sampler_counts) == admissible_as
    assert all(count == 1 for count in sampler_counts.values())

    # Select the coset ONCE, outside the sample loop.
    coset = max(coset_totals, key=lambda c: (coset_totals[c], c))
    fixed_claim = F((0, 0, *coset))
    certificate = ceil_fraction(N*S*S, P*P*(S+K*(N-1)))
    assert coset_totals[coset] >= certificate
    checked_pairs, coordinate_identities = 0, 0
    sample_label_counts = Counter()
    for a, zx, zy, vals in records:
        X0, X1 = parts(zx)
        Y0, Y1 = parts(zy)
        slope = X1/Y1
        # u U_z is quadratic with two distinct nonzero roots.
        uc = [(one-i*slope)/4, (-X0+slope*Y0)/2, (one+i*slope)/4]
        assert uc[0] != zero and uc[2] != zero
        for root in (a, conjugate(a)):
            assert uc[0]+uc[1]*root+uc[2]*root*root == zero
        labels = {b-fixed_claim for b in vals if b[2:] == coset}
        assert all(alpha[2:] == (0, 0) for alpha in labels)
        sample_label_counts[len(labels)] += 1
        for alpha in labels:
            b = fixed_claim+alpha
            # For F=0 the witness is 0; for F=x, (x-ell_zx)/U_z=2.
            witness = zero if b == zero else F(2)
            agreement = 0
            for j, (x, y) in enumerate(domain):
                U = (x-X0-slope*(y-Y0))/2
                assert U != zero
                def ell(value):
                    B0, B1 = parts(value)
                    return B0+(B1/Y1)*(y-Y0)
                def raw(table_value, claim):
                    la = conjugate(claim)-claim
                    lc = conjugate(zy)-zy
                    lb = claim*lc-la*zy
                    den = (X0-x)*Y1-(Y0-y)*X1
                    return (lc*table_value-la*y-lb)/den/w
                r0, r1 = raw(f[j], fixed_claim), raw(zero, one)
                assert r0 == (f[j]-ell(fixed_claim))/U
                assert r1 == -one/U
                F_value = zero if b == zero else x
                assert r0+alpha*r1-witness == (f[j]-F_value)/U
                assert r0+alpha*r1 == (f[j]-ell(b))/U
                agreement += int(r0+alpha*r1 == witness)
                coordinate_identities += 4
            assert agreement == T
            checked_pairs += 1
    assert checked_pairs == coset_totals[coset]
    return dict(p=P, n=8, K=K, T=T, N=N, admissible_samples=S,
                sampler_singular_draws=singular, fixed_claim=list(fixed_claim),
                certified_pairs=certificate, observed_pairs=checked_pairs,
                sample_label_histogram=dict(sample_label_counts),
                coordinate_identities=coordinate_identities,
                evaluation_incidences=distinct_incidences,
                collision_family=dict(K=4, N=3, collisions=collision_family_total,
                    coefficients_in_basis_1_x_y_x2_xy=coefficients,
                    distinct_incidences=collision_family_distinct,
                    maximum_pair_roots=max(pair_roots.values())),
                observed_probability=str(Fraction(checked_pairs, P**8)))


if __name__ == "__main__":
    output = dict(status="passed", large_instance=large_certificate(),
                  exhaustive_toy=exhaustive_toy(),
                  scope="Exact finite checks of a raw quotient theorem; no full-proof test.")
    destination = Path(__file__).with_name("fixed_claim_results.json")
    destination.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, indent=2))
