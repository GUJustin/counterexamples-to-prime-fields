#!/usr/bin/env python3
"""Exact p=5,7 regression for the Hermitian norm specialization.

No codeword enumeration is used or claimed for the analytic source bound.
All arithmetic in the fixtures is implemented here using quadratic towers.
Sympy is used only for the separate symbolic threshold identities.
The compact decoder is compared with the bank on every field label.
"""

from collections import Counter
import hashlib
import json
from pathlib import Path
import resource
import time


def fixture(p):
    assert p >= 5 and all(p % d for d in range(2, int(p**0.5) + 1))
    nonresidue = next(d for d in range(2, p) if pow(d, (p - 1) // 2, p) == p - 1)
    native_size = p * p

    # B=Fp[v]/(v^2-nonresidue), encoded a+b*p.
    def add0(a, b):
        return ((a % p + b % p) % p) + p * ((a // p + b // p) % p)

    def mul0(a, b):
        a0, a1 = a % p, a // p
        b0, b1 = b % p, b // p
        return (a0*b0 + nonresidue*a1*b1) % p + p*((a0*b1 + a1*b0) % p)

    add_table = [[add0(a, b) for b in range(native_size)] for a in range(native_size)]
    mul_table = [[mul0(a, b) for b in range(native_size)] for a in range(native_size)]
    neg_table = [((-a % p) % p) + p*((-(a // p)) % p) for a in range(native_size)]

    def add(a, b):
        return add_table[a][b]

    def neg(a):
        return neg_table[a]

    def sub(a, b):
        return add(a, neg(b))

    def mul(a, b):
        return mul_table[a][b]

    def power(a, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = mul(result, a)
            a = mul(a, a)
            exponent >>= 1
        return result

    assert all(power(a, native_size) == a for a in range(native_size))
    inverse = [0] + [power(a, native_size - 2) for a in range(1, native_size)]
    epsilon = next(a for a in range(1, native_size)
                   if power(a, (native_size - 1) // 2) == p - 1)

    # E=B[w]/(w^2-epsilon), encoded a+b*native_size.  beta=w.
    def eadd(a, b):
        return add(a % native_size, b % native_size) + native_size * add(
            a // native_size, b // native_size)

    def eneg(a):
        return neg(a % native_size) + native_size * neg(a // native_size)

    def esub(a, b):
        return eadd(a, eneg(b))

    def emul(a, b):
        a0, a1 = a % native_size, a // native_size
        b0, b1 = b % native_size, b // native_size
        return add(mul(a0, b0), mul(epsilon, mul(a1, b1))) + native_size * add(
            mul(a0, b1), mul(a1, b0))

    def epower(a, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = emul(result, a)
            a = emul(a, a)
            exponent >>= 1
        return result

    def einverse(a):
        assert a
        a0, a1 = a % native_size, a // native_size
        denominator = sub(mul(a0, a0), mul(epsilon, mul(a1, a1)))
        assert denominator
        out = mul(a0, inverse[denominator]) + native_size * mul(neg(a1), inverse[denominator])
        assert emul(a, out) == 1
        return out

    beta = native_size
    assert epower(beta, native_size) == eneg(beta)
    assert epower(beta, native_size * native_size) == beta

    def trim(poly):
        while len(poly) > 1 and not poly[-1]:
            poly.pop()
        return poly

    def padd(a, b):
        result = a[:] + [0] * max(0, len(b)-len(a))
        for i, value in enumerate(b):
            result[i] = add(result[i], value)
        return trim(result)

    def pscale(a, scalar):
        return trim([mul(x, scalar) for x in a])

    def psub(a, b):
        return padd(a, pscale(b, p-1))

    def pmul(a, b):
        result = [0] * (len(a) + len(b) - 1)
        for i, av in enumerate(a):
            if not av:
                continue
            for j, bv in enumerate(b):
                if bv:
                    result[i+j] = add(result[i+j], mul(av, bv))
        return trim(result)

    def ppower(a, exponent):
        result = [1]
        while exponent:
            if exponent & 1:
                result = pmul(result, a)
            a = pmul(a, a)
            exponent >>= 1
        return result

    def pdiv(a, b):
        remainder = trim(a[:])
        result = [0] * max(1, len(a)-len(b)+1)
        while remainder != [0] and len(remainder) >= len(b):
            offset = len(remainder)-len(b)
            coefficient = mul(remainder[-1], inverse[b[-1]])
            result[offset] = coefficient
            for j, value in enumerate(b):
                remainder[offset+j] = sub(remainder[offset+j], mul(coefficient, value))
            trim(remainder)
        return trim(result), remainder

    def pev(poly, x):
        value = 0
        for coefficient in reversed(poly):
            value = add(mul(value, x), coefficient)
        return value

    def epev(poly, x):
        value = 0
        for coefficient in reversed(poly):
            value = eadd(emul(value, x), coefficient)
        return value

    def pfrobenius(poly):
        result = [0] * ((len(poly)-1)*p+1)
        for j, coefficient in enumerate(poly):
            result[j*p] = power(coefficient, p)
        return trim(result)

    D = native_size-p
    K = native_size-2*p
    T0, T = D-1, D-2
    rp = next(e for e in range(2, p+1) if e*e-e+1 >= p)
    Lambda = [0]*(native_size+1)
    Lambda[1], Lambda[native_size] = p-1, 1
    head = [0]*D+[1]
    lambda_at_beta = esub(epower(beta, native_size), beta)
    r_at_beta = epower(beta, D)
    inverse_denominators = [einverse(esub(x, beta)) for x in range(native_size)]
    source_f = [emul(esub(power(x, D), r_at_beta), inverse_denominators[x])
                for x in range(native_size)]
    source_g = inverse_denominators

    # The fixed-A pair parametrization covers every circle p+1 times.
    A = 2
    other_A = (1-A) % p
    pair_coverage = Counter()
    for t in range(native_size):
        for u in range(native_size):
            if t == u:
                continue
            s = add(mul(A, t), mul(other_A, u))
            c = add(mul(A, power(t, p+1)), mul(other_A, power(u, p+1)))
            delta = sub(c, power(s, p+1))
            assert c < p and delta < p and delta
            assert delta == mul(mul(A, other_A), power(sub(t, u), p+1))
            pair_coverage[(s, c)] += 1

    assert len(pair_coverage) == native_size*(p-1)
    assert set(pair_coverage.values()) == {p+1}

    labels, scaled_g_values = set(), set()
    bank_parameters = {}
    agreements, strict_degrees = Counter(), Counter()
    h_digest = hashlib.sha256()
    polynomial_identity_count = 0
    for s, c in sorted(pair_coverage):
        G = [c, power(s, p)] + [0]*(p-2) + [s, 1]
        assert len(G)-1 == p+1
        circle_roots = [x for x in range(native_size) if pev(G, x) == 0]
        assert len(circle_roots) == p+1
        assert pev(G, neg(s)) != 0
        J, remainder = pdiv(Lambda, G)
        assert remainder == [0]
        P = pmul([s, 1], J)
        C = psub(P, head)
        assert len(P)-1 == D and P[-1] == 1
        assert len(C)-1 <= K
        assert (C[K] if len(C)>K else 0) == neg(power(s, p))
        roots = [x for x in range(native_size) if pev(P, x) == 0]
        assert len(roots) == T0
        assert set(roots) == set(range(native_size))-set(circle_roots)

        assert psub(pfrobenius(G), G) == pmul(Lambda, pfrobenius([s, 1]))
        assert pfrobenius(P) == psub(ppower(Lambda, p-1), ppower(J, p-1))
        polynomial_identity_count += 2

        g_value = epev(G, beta)
        label = epev(P, beta)
        assert g_value and label
        assert epower(label, p) == emul(
            epower(lambda_at_beta, p-1),
            esub(1, epower(einverse(g_value), p-1)),
        )
        assert label not in labels
        labels.add(label)
        bank_parameters[label] = (s, c)
        for scalar in range(1, p):
            scaled = emul(scalar, g_value)
            assert scaled not in scaled_g_values
            scaled_g_values.add(scaled)

        # H=(R-P+P(beta)-R(beta))/(X-beta), in ascending order.
        numerator = [eneg(v) for v in C]
        numerator[0] = eadd(numerator[0], esub(label, r_at_beta))
        assert epev(numerator, beta) == 0
        if len(numerator) == 1:
            assert numerator == [0]
            H = [0]
        else:
            H = [0]*(len(numerator)-1)
            H[-1] = numerator[-1]
            for i in range(len(H)-2, -1, -1):
                H[i] = eadd(numerator[i+1], emul(beta, H[i+1]))
            assert eadd(numerator[0], emul(beta, H[0])) == 0
            trim(H)
        assert len(H)-1 < K
        strict_degrees[len(H)-1] += 1
        agreement = 0
        for x in range(native_size):
            residual = esub(eadd(source_f[x], emul(label, source_g[x])), epev(H, x))
            assert residual == emul(pev(P, x), inverse_denominators[x])
            agreement += residual == 0
        agreements[agreement] += 1
        h_digest.update(json.dumps([s, c, label, H], separators=(",", ":")).encode())

    assert labels and len(labels) == native_size*(p-1)
    assert len(scaled_g_values) == native_size*(p-1)**2
    assert set(agreements) == {T0}
    assert D-rp < T
    assert T*T < native_size*(K-1) < T0*T0
    F_numerator = lambda agreement: (
        (8*native_size-K)*agreement*agreement
        - 6*K*agreement*native_size
        + K*(4*K-5*native_size)*native_size
    )
    assert F_numerator(T) < 0
    assert F_numerator(T0) < 0

    # Explicit far endpoint: cstar^p = Lambda(beta)^(p-1).
    decoder_started = time.monotonic()
    frobenius_scale = epower(lambda_at_beta, p-1)
    inverse_frobenius_scale = einverse(frobenius_scale)
    cstar = epower(frobenius_scale, p**3)
    assert cstar and epower(cstar, p) == frobenius_scale
    assert cstar not in labels
    inverse_cstar = einverse(cstar)
    affine_parameters = {emul(z, inverse_cstar) for z in labels}
    assert len(affine_parameters) == len(labels)
    assert not ({0, 1} & affine_parameters)

    # Matrices use the Fp basis (1,v,w,vw) of E, encoded by powers of p.
    def coordinates(value):
        return [(value // p**j) % p for j in range(4)]

    def encoded(vector):
        return sum((value % p)*p**j for j, value in enumerate(vector))

    def rref(matrix, width):
        rows = [[value % p for value in row] for row in matrix]
        pivots = []
        for column in range(width):
            pivot = next((j for j in range(len(pivots), len(rows))
                          if rows[j][column]), None)
            if pivot is None:
                continue
            row_index = len(pivots)
            rows[row_index], rows[pivot] = rows[pivot], rows[row_index]
            multiplier = pow(rows[row_index][column], p-2, p)
            rows[row_index] = [(value*multiplier) % p for value in rows[row_index]]
            for j in range(len(rows)):
                if j != row_index and rows[j][column]:
                    multiplier = rows[j][column]
                    rows[j] = [(value-multiplier*other) % p
                               for value, other in zip(rows[j], rows[row_index])]
            pivots.append(column)
        return rows, pivots

    # H=bX^(p+1)+(s0+s1*v)X^p+(s0+s1*v)^p X+d.
    evaluation_columns = [
        epower(beta, p+1),
        eadd(epower(beta, p), beta),
        eadd(emul(p, epower(beta, p)), emul(power(p, p), beta)),
        1,
    ]
    evaluation_matrix = [
        [coordinates(value)[j] for value in evaluation_columns]
        for j in range(4)
    ]
    augmented = [row + [int(i == j) for j in range(4)]
                 for i, row in enumerate(evaluation_matrix)]
    reduced, evaluation_pivots = rref(augmented, 4)
    assert evaluation_pivots == [0, 1, 2, 3]
    evaluation_inverse = [row[4:] for row in reduced]
    assert all(
        sum(evaluation_inverse[i][j]*evaluation_matrix[j][k] for j in range(4)) % p
        == int(i == k)
        for i in range(4) for k in range(4)
    )
    field_basis = [p**j for j in range(4)]
    frobenius_columns = [epower(value, p) for value in field_basis]
    decoder_categories, kernel_dimensions = Counter(), Counter()
    decoder_digest = hashlib.sha256()

    def compact_decode(z):
        u = esub(1, emul(epower(z, p), inverse_frobenius_scale))
        if not u:
            assert z == cstar
            return None, "u_zero"
        kernel_columns = [esub(value, emul(u, frobenius))
                          for value, frobenius in zip(field_basis, frobenius_columns)]
        matrix = [[coordinates(value)[i] for value in kernel_columns] for i in range(4)]
        reduced, pivots = rref(matrix, 4)
        dimension = 4-len(pivots)
        kernel_dimensions[dimension] += 1
        assert dimension in (0, 1)
        if not dimension:
            return None, "zero_kernel"
        free_column = next(j for j in range(4) if j not in pivots)
        vector = [0]*4
        vector[free_column] = 1
        for i, pivot in enumerate(pivots):
            vector[pivot] = -reduced[i][free_column] % p
        v = encoded(vector)
        assert v and esub(v, emul(u, epower(v, p))) == 0
        coefficients = [
            sum(row[j]*vector[j] for j in range(4)) % p
            for row in evaluation_inverse
        ]
        inverse_evaluation = 0
        for coefficient, value in zip(coefficients, evaluation_columns):
            inverse_evaluation = eadd(inverse_evaluation, emul(coefficient, value))
        assert inverse_evaluation == v
        b, s0, s1, d = coefficients
        if not b:
            return None, "zero_leading_coefficient"
        inverse_b = pow(b, p-2, p)
        s = mul(s0+p*s1, inverse_b)
        c = d*inverse_b % p
        if c == power(s, p+1):
            return None, "zero_radius"
        G = [c, power(s, p)] + [0]*(p-2) + [s, 1]
        assert epev(G, beta) == emul(v, inverse_b)
        return (s, c), "accepted"

    for z in range(native_size*native_size):
        decoded, category = compact_decode(z)
        assert decoded == bank_parameters.get(z)
        if z == 0:
            assert category == "zero_leading_coefficient"
        if z == cstar:
            assert category == "u_zero"
        decoder_categories[category] += 1
        decoder_digest.update(json.dumps([z, category, decoded], separators=(",", ":")).encode())
    assert decoder_categories == Counter(
        accepted=native_size*(p-1),
        zero_leading_coefficient=p*p+p+1,
        zero_radius=p*p,
        u_zero=1,
        zero_kernel=p**4-1-(p**3+p*p+p+1),
    )
    assert sum(decoder_categories.values()) == p**4

    return dict(
        characteristic=p,
        native_quadratic_modulus_v2_minus=nonresidue,
        extension_quadratic_modulus_w2_minus_encoded=epsilon,
        encoding="a+b*p for B; a+b*p^2 for E, with a,b in B in the latter",
        pole_encoded=beta,
        n=native_size,
        q=native_size*native_size,
        dimension=K,
        actual_witness_agreement=T0,
        tested_threshold=T,
        distinct_nonzero_labels=len(labels),
        scaled_Hermitian_pole_values=len(scaled_g_values),
        fixed_A=A,
        ordered_pair_count=native_size*(native_size-1),
        pair_multiplicity=p+1,
        polynomial_frobenius_identity_checks=polynomial_identity_count,
        evaluated_residual_checks=len(labels)*native_size,
        witness_agreement_distribution=dict(sorted(agreements.items())),
        witness_degree_distribution=dict(sorted(strict_degrees.items())),
        witness_bank_sha256=h_digest.hexdigest(),
        rp=rp,
        proven_source_f_agreement_upper=D-rp,
        proven_source_g_and_common_agreement=K,
        source_bound_method="all-witness rational-map proof; no codeword enumeration",
        exact_Johnson_slack=native_size*(K-1)-T*T,
        actual_witness_excess_above_exact_Johnson=T0*T0-native_size*(K-1),
        first_order_sign_numerator_at_tested_threshold=F_numerator(T),
        first_order_sign_numerator_at_actual_agreement=F_numerator(T0),
        explicit_endpoint=dict(
            cstar_encoded=cstar,
            frobenius_scale_encoded=frobenius_scale,
            cstar_pth_power_verified=True,
            outside_bank_verified=True,
            affine_exceptional_parameters=len(affine_parameters),
            affine_parameters_avoid_zero_and_one=True,
            both_endpoint_agreement_upper=D-rp,
            common_agreement=K,
        ),
        compact_decoder=dict(
            scope="all labels versus exact bank; no all-codeword enumeration",
            label_count=p**4,
            parameter_order=["b", "s0", "s1", "d"],
            evaluation_matrix=evaluation_matrix,
            evaluation_inverse=evaluation_inverse,
            categories=dict(sorted(decoder_categories.items())),
            kernel_dimensions=dict(sorted(kernel_dimensions.items())),
            all_membership_and_recovered_parameters_match_bank=True,
            membership_digest_sha256=decoder_digest.hexdigest(),
            elapsed_seconds=time.monotonic()-decoder_started,
        ),
        pass_all_checks=True,
    )


def symbolic_checks():
    import sympy as sp
    p = sp.symbols("p", positive=True)
    n, K, D = p*p, p*p-2*p, p*p-p
    rho = K/n
    F = lambda a: (8-rho)*a*a-6*rho*a+rho*(4*rho-5)
    values = {
        "tested_minus_Johnson_squared": sp.factor((D-2)**2-n*(K-1)),
        "actual_minus_Johnson_squared": sp.factor((D-1)**2-n*(K-1)),
        "first_order_at_tested": sp.factor(F((D-2)/n)),
        "first_order_at_actual": sp.factor(F((D-1)/n)),
    }
    assert sp.simplify(values["tested_minus_Johnson_squared"]-(-2*p*p+4*p+4)) == 0
    assert values["actual_minus_Johnson_squared"] == 2*p+1
    assert sp.simplify(values["first_order_at_tested"]+(p-2)*(p+2)*(9*p+2)/p**5) == 0
    assert sp.simplify(values["first_order_at_actual"]+(p**3-11*p-2)/p**5) == 0
    return {name: str(value) for name, value in values.items()}


if __name__ == "__main__":
    started = time.monotonic()
    result = {
        "task": "Hermitian norm injectivity and strict witness regression",
        "fixtures": [fixture(5), fixture(7)],
        "symbolic_identities": symbolic_checks(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.monotonic()-started,
        "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "pass": True,
    }
    destination = Path(__file__).with_suffix(".json")
    destination.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result, indent=2, sort_keys=True))
