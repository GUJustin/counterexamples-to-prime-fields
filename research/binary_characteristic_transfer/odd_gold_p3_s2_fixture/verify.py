#!/usr/bin/env python3
"""Bounded exact odd-Gold bank check; no scan of the challenge field."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import fmpz_mod_poly_ctx, fq_default_ctx, fq_default_poly_ctx


def main():
    started = time.monotonic()
    root = Path(__file__).resolve().parent
    p, s, n, q = 3, 2, 243, 3**15
    d, D, k, T, U, expected_bank = 90, 162, 102, 153, 135, 29403
    modulus_coefficients = [1, 1, 2, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1]
    modulus = fmpz_mod_poly_ctx(p)(modulus_coefficients)
    assert modulus.is_irreducible()
    field = fq_default_ctx(modulus=modulus, var="z", fq_type="FQ_NMOD")
    polynomial = fq_default_poly_ctx(field)
    X, beta = polynomial.gen(), field.gen()
    assert q-1 == 2*11**2*13*4561
    assert all(all(r % a for a in range(2, int(r**0.5)+1)) for r in (2, 11, 13, 4561))
    assert beta**(q-1) == 1
    assert all(beta**((q-1)//r) != 1 for r in (2, 11, 13, 4561))
    assert beta**n != beta and beta**(n**3) == beta
    native_generator = beta**((q-1)//(n-1))
    assert (q-1)//(n-1) == 59293
    assert native_generator**242 == 1
    assert native_generator**121 != 1 and native_generator**22 != 1

    def encode(value):
        return sum(int(coefficient)*p**i for i, coefficient in enumerate(value.to_list()))

    def polynomial_encoding(poly):
        return [encode(coefficient) for coefficient in poly.coeffs()]

    def check_resources():
        if time.monotonic()-started > 110:
            raise RuntimeError("Stopped at the bounded 110-second internal cap")
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 512*1024**2:
            raise RuntimeError("Stopped at the 512 MiB memory cap")

    native = sorted(
        [field.zero()]+[native_generator**i for i in range(n-1)], key=encode
    )
    assert len({encode(x) for x in native}) == n
    assert all(x**n == x for x in native)
    nonzero_native = [x for x in native if not x.is_zero()]
    exponents = [10, 30, 90, 28, 84]
    assert exponents == [(10*p**i) % (n-1) for i in range(5)]
    native_powers = [[x**exponent for exponent in exponents] for x in native]

    coefficient_rows, good_coefficients = [], []
    native_level_histogram = Counter()
    native_value_checks = 0
    for a in nonzero_native:
        coefficients = [a**(p**i) for i in range(5)]
        root_count = 0
        for powers in native_powers:
            value = field.one()
            for coefficient, power in zip(coefficients, powers):
                value += coefficient*power
            assert value**p == value
            root_count += value.is_zero()
            native_value_checks += 1
        assert root_count in (72, 90)
        assert (root_count == d) == (a**121 == -field.one())
        native_level_histogram[root_count] += 1
        coefficient_rows.append([encode(a), root_count])
        if root_count == d:
            good_coefficients.append((a, coefficients))
        check_resources()
    assert native_level_histogram == {72: 121, 90: 121}

    Lambda = X**n-X
    delta, beta_head = Lambda(beta), beta**D
    cstar = (delta**(p-1))**(p**14)
    assert cstar**p == delta**(p-1) and not cstar.is_zero()
    shifted_powers = []
    for b in native:
        z = beta+b
        shifted_powers.append((
            b, [z**exponent for exponent in exponents], z**3, z**9
        ))
    labels, affine_parameters, scaled_G_values = set(), set(), set()
    records = []
    lookup = {}
    for a, coefficients in good_coefficients:
        for b, powers, z3, z9 in shifted_powers:
            G_beta = field.one()
            for coefficient, power in zip(coefficients, powers):
                G_beta += coefficient*power
            F_beta = coefficients[4]*z3+coefficients[2]*z9
            assert not G_beta.is_zero() and not F_beta.is_zero()
            label = delta*F_beta/G_beta
            assert not label.is_zero()
            assert label**p == delta**(p-1)*(1-G_beta**(1-p))
            label_code = encode(label)
            assert label_code not in labels
            labels.add(label_code)
            for scalar in (1, 2):
                scaled = encode(scalar*G_beta)
                assert scaled not in scaled_G_values
                scaled_G_values.add(scaled)
            affine_parameter = 1-cstar/label
            parameter_code = encode(affine_parameter)
            assert parameter_code not in (0, 1)
            assert parameter_code not in affine_parameters
            affine_parameters.add(parameter_code)
            a_code, b_code = encode(a), encode(b)
            records.append([a_code, b_code, label_code, parameter_code])
            lookup[(a_code, b_code)] = (label, affine_parameter)
        check_resources()
    assert len(records) == len(labels) == len(affine_parameters) == expected_bank
    assert len(scaled_G_values) == 2*expected_bank
    assert encode(cstar) not in labels

    # Full polynomial and native-coordinate checks for 12 x 3 deterministic pairs.
    sample_a_indices = [(j*len(good_coefficients))//12 for j in range(12)]
    assert len(set(sample_a_indices)) == 12
    sample_centers = [field.zero(), field.one(), native_generator]
    assert len({encode(b) for b in sample_centers}) == 3
    source_g = [(x-beta).inverse() for x in native]
    source_f = [(x**D-beta_head)*g for x, g in zip(native, source_g)]
    r0 = [f+cstar*g for f, g in zip(source_f, source_g)]
    r1 = [cstar*g for g in source_g]
    sample_records = []
    witness_hash = hashlib.sha256()
    coordinate_checks = 0
    for index in sample_a_indices:
        a, coefficients = good_coefficients[index]
        for b in sample_centers:
            Z = X+b
            G = polynomial.one()
            for coefficient, exponent in zip(coefficients, exponents):
                G += coefficient*Z**exponent
            F = coefficients[4]*Z**3+coefficients[2]*Z**9
            assert G.degree() == d and F.degree() == 9
            assert G.leading_coefficient() == F.leading_coefficient() == a**9
            assert G.derivative() == F**p
            assert G**p-G == Lambda*(F**p)
            quotient, remainder = divmod(Lambda, G)
            assert remainder.is_zero()
            P = F*quotient
            assert P.is_monic() and P.degree() == D
            assert (P-X**D).degree() == k
            assert P**p == Lambda**(p-1)-quotient**(p-1)
            assert G(-b) == 1
            assert divmod(P, Z**4)[1].is_zero()
            assert not divmod(P, Z**5)[1].is_zero()
            label, parameter = lookup[(encode(a), encode(b))]
            assert P(beta) == label
            witness, remainder = divmod(X**D-P+label-beta_head, X-beta)
            assert remainder.is_zero() and witness.degree() == k-1
            scale = cstar/label
            scaled_witness = scale*witness
            G_roots = P_roots = matches = affine_matches = 0
            for x, f, g, w0, w1 in zip(native, source_f, source_g, r0, r1):
                G_roots += G(x).is_zero()
                P_roots += P(x).is_zero()
                residual = f+label*g-witness(x)
                assert residual == P(x)*g
                matches += residual.is_zero()
                affine_residual = (1-parameter)*w0+parameter*w1-scaled_witness(x)
                assert affine_residual == scale*residual
                affine_matches += affine_residual.is_zero()
                coordinate_checks += 1
            assert (G_roots, P_roots, matches, affine_matches) == (d, T, T, T)
            sample_records.append(dict(
                a=encode(a), center=encode(b), label=encode(label),
                affine_parameter=encode(parameter), witness_degree=witness.degree(),
                native_matches=matches, affine_native_matches=affine_matches,
            ))
            witness_hash.update(json.dumps(
                [encode(a), encode(b), polynomial_encoding(witness)],
                separators=(",", ":")
            ).encode())
        check_resources()
    assert len(sample_records) == 36 and coordinate_checks == 36*n

    johnson_slack = n*(k-1)-T*T
    first_order_numerator = (8*n-k)*T*T-6*k*T*n+k*(4*k-5*n)*n
    assert johnson_slack == 1134
    assert first_order_numerator*59049 == 1496*n**3
    assert ((p+1)*k-1)//p == U == 135 < T
    assert (p+1)*k-1 >= D+(p-2)*n

    bank_path = root/"parameters_and_labels.json"
    bank_path.write_text(json.dumps(dict(
        encoding="base-3 coefficients in the displayed degree-15 modulus",
        columns=["a", "center_b", "P(beta)", "affine_parameter_1_minus_cstar_over_label"],
        records=records,
    ), indent=2)+"\n")
    output = dict(
        status="PASS", p=p, s=s, native_size=n, challenge_size=q,
        native_extension_degree=5, challenge_extension_degree=15,
        challenge_degree_over_native=3,
        modulus_coefficients_ascending=modulus_coefficients,
        modulus_irreducible=True, field_implementation="FLINT FQ_NMOD",
        challenge_generator_primitive=True,
        challenge_multiplicative_order_factorization={"2":1,"11":2,"13":1,"4561":1},
        beta_encoded=encode(beta), beta_native=False,
        native_generator_power_of_beta=59293,
        native_generator_encoded=encode(native_generator),
        native_elements_encoded=[encode(x) for x in native],
        reduced_Gold_exponents_in_frobenius_coefficient_order=exponents,
        a_native_root_count_records=coefficient_rows,
        a_native_root_count_histogram=dict(sorted(native_level_histogram.items())),
        native_level_value_checks=native_value_checks,
        good_a_count=len(good_coefficients), good_a_are_exactly_native_nonsquares=True,
        degree_G=d, degree_P=D, code_dimension=k, threshold=T,
        population=expected_bank, all_labels_distinct_nonzero=True,
        scaled_G_beta_distinct_count=len(scaled_G_values),
        affine_parameters_distinct_and_interior=True,
        cstar_encoded=encode(cstar), cstar_cube_equals_delta_squared=True,
        cstar_outside_bank=True,
        endpoint_pair=["f+cstar*g","cstar*g"],
        source_r0_agreement_upper_by_proof=U,
        source_r1_and_common_agreement_by_proof=k,
        source_bounds_verified_by_codeword_enumeration=False,
        smaller_guaranteed_loss_fraction=f"{T-U}/{n}",
        smaller_loss_to_capacity_margin=f"{T-U}/{T-k}",
        johnson_squared_slack=johnson_slack,
        first_order_sign="1496/59049",
        full_polynomial_sample_count=len(sample_records),
        sample_coordinate_checks=coordinate_checks,
        samples=sample_records,
        sample_witness_bank_sha256=witness_hash.hexdigest(),
        bank_sha256=hashlib.sha256(bank_path.read_bytes()).hexdigest(),
        verifier_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        scope=(
            "all 242 native coefficient level counts, all 29403 exterior labels, "
            "and 36 full polynomial/native-coordinate witness checks; "
            "source bounds and complete singleton classification use the audited theorem; "
            "no scan of the challenge field or enumeration of all codewords"
        ),
    )
    (root/"receipt.json").write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({key:value for key,value in output.items()
                      if key not in ("native_elements_encoded","a_native_root_count_records","samples")},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
