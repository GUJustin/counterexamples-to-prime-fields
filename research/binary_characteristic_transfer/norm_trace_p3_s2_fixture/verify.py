#!/usr/bin/env python3
"""Exact p=3,s=2 norm-trace fixture, using FLINT finite-field arithmetic."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import fmpz_mod_poly_ctx, fq_default_ctx, fq_default_poly_ctx


def main():
    started = time.monotonic()
    p, s, Q = 3, 2, 9
    n, challenge_size = 81, 6561
    degree_G, degree_F, D, K, T = 30, 3, 54, 34, 51
    assert Q == p**s and n == Q*Q and challenge_size == n*n
    assert degree_G == (Q+1)*(Q//p)
    assert degree_F == Q//p and D == n-n//p
    assert T == n-degree_G and K == (p-1)*T//p

    modulus_coefficients = [2, 2, 2, 0, 1, 2, 0, 0, 1]
    modulus = fmpz_mod_poly_ctx(p)(modulus_coefficients)
    assert modulus.is_irreducible()
    field = fq_default_ctx(modulus=modulus, var="z")
    polynomials = fq_default_poly_ctx(field)
    X = polynomials.gen()
    beta = field.gen()
    assert beta**(challenge_size-1) == field.one()
    assert challenge_size-1 == 2**5*5*41
    assert all(beta**((challenge_size-1)//r) != field.one() for r in (2, 5, 41))

    def encode(value):
        return sum(int(coefficient)*p**j for j, coefficient in enumerate(value.to_list()))

    def polynomial_encoding(poly):
        return [encode(coefficient) for coefficient in poly.coeffs()]

    native_generator = beta**((challenge_size-1)//(n-1))
    small_generator = beta**((challenge_size-1)//(Q-1))
    native = sorted([field.zero()]+[native_generator**j for j in range(n-1)], key=encode)
    small_nonzero = sorted([small_generator**j for j in range(Q-1)], key=encode)
    assert len({encode(x) for x in native}) == n
    assert len({encode(a) for a in small_nonzero}) == Q-1
    assert all(x**n == x for x in native)
    assert all(a**Q == a and not a.is_zero() for a in small_nonzero)
    assert beta**n != beta

    Lambda, R = X**n-X, X**D
    lambda_beta = Lambda(beta)
    r_beta = beta**D
    cstar = (lambda_beta**(p-1))**(p**7)
    assert cstar**p == lambda_beta**(p-1)
    assert cstar == lambda_beta**D
    assert not cstar.is_zero()
    inverse_denominators = [(x-beta).inverse() for x in native]
    source_f = [(x**D-r_beta)*denominator
                for x, denominator in zip(native, inverse_denominators)]
    endpoint_r0 = [value+cstar*denominator
                   for value, denominator in zip(source_f, inverse_denominators)]
    endpoint_r1 = [cstar*denominator for denominator in inverse_denominators]
    bank = []
    affine_bank = []
    affine_parameters = set()
    labels, scaled_G_values, distinct_polynomials = set(), set(), set()
    witness_digest = hashlib.sha256()
    witness_degrees, G_root_counts, P_root_counts = Counter(), Counter(), Counter()
    algebra_identity_checks = 0
    residual_evaluation_checks = 0
    affine_residual_evaluation_checks = 0
    for a in small_nonzero:
        for b in native:
            Y = X+b
            norm_term = a*Y**(Q+1)
            G = norm_term+norm_term**p+1
            F = a**(Q//p)*Y**(Q//p)
            assert G.degree() == degree_G and F.degree() == degree_F
            assert G.leading_coefficient() == F.leading_coefficient() == a**(Q//p)
            assert G.derivative() == F**p
            assert G**p-G == Lambda*(F**p)
            J, remainder = divmod(Lambda, G)
            assert remainder.is_zero()
            P = F*J
            assert P.degree() == D and P.is_monic()
            assert P**p == Lambda**(p-1)-J**(p-1)
            C = P-R
            assert C.degree() == K
            assert C.leading_coefficient() == -(a.inverse()**2)
            assert G(-b) == field.one()
            assert divmod(P, Y**4)[1].is_zero()
            assert not divmod(P, Y**5)[1].is_zero()
            algebra_identity_checks += 8

            G_values = [G(x) for x in native]
            assert all(value**p == value for value in G_values)
            G_roots = {encode(x) for x, value in zip(native, G_values) if value.is_zero()}
            P_roots = {encode(x) for x in native if P(x).is_zero()}
            assert len(G_roots) == degree_G
            assert P_roots == {encode(x) for x in native}-G_roots
            assert len(P_roots) == T
            G_root_counts[len(G_roots)] += 1
            P_root_counts[len(P_roots)] += 1
            signature = tuple(polynomial_encoding(G))
            assert signature not in distinct_polynomials
            distinct_polynomials.add(signature)

            label, g_beta = P(beta), G(beta)
            encoded_label = encode(label)
            assert not label.is_zero() and not g_beta.is_zero()
            assert encoded_label not in labels
            labels.add(encoded_label)
            assert label**p == lambda_beta**(p-1)*(1-g_beta**(1-p))
            for scalar in range(1, p):
                scaled_value = encode(scalar*g_beta)
                assert scaled_value not in scaled_G_values
                scaled_G_values.add(scaled_value)

            H, remainder = divmod(R-P+label-r_beta, X-beta)
            assert remainder.is_zero() and H.degree() < K
            witness_degrees[H.degree()] += 1
            scale = cstar/label
            affine_parameter = 1-scale
            encoded_affine_parameter = encode(affine_parameter)
            assert encoded_affine_parameter not in (0, 1)
            assert encoded_affine_parameter not in affine_parameters
            affine_parameters.add(encoded_affine_parameter)
            scaled_H = scale*H
            assert scaled_H.degree() < K
            agreement = 0
            affine_agreement = 0
            for x, f_value, denominator, r0_value, r1_value in zip(
                native, source_f, inverse_denominators, endpoint_r0, endpoint_r1
            ):
                residual = f_value+label*denominator-H(x)
                assert residual == P(x)*denominator
                agreement += residual.is_zero()
                residual_evaluation_checks += 1
                affine_word = (1-affine_parameter)*r0_value+affine_parameter*r1_value
                affine_residual = affine_word-scaled_H(x)
                assert affine_residual == scale*residual
                affine_agreement += affine_residual.is_zero()
                affine_residual_evaluation_checks += 1
            assert agreement == T
            assert affine_agreement == T
            record = [encode(a), encode(b), encoded_label]
            bank.append(record)
            affine_bank.append([encoded_label, encoded_affine_parameter, encode(scale)])
            witness_digest.update(json.dumps(
                record+[polynomial_encoding(H)], separators=(",", ":")
            ).encode())

    population = n*(Q-1)
    assert len(bank) == len(labels) == len(distinct_polynomials) == population == 648
    assert len(scaled_G_values) == (p-1)*population
    assert len(affine_parameters) == population and encode(cstar) not in labels
    source_r0_upper = ((p+1)*K-1)//p
    assert source_r0_upper == 45 < T
    assert (p+1)*K-1 >= D+(p-2)*n

    # Exact finite placement at the strict dimension K.
    Johnson_slack = n*(K-1)-T*T
    first_order_sign_numerator = (
        (8*n-K)*T*T-6*K*T*n+K*(4*K-5*n)*n
    )
    assert 16*K > 3*n  # K/n > 3/16 > the branch switch 11-3sqrt(13).
    assert Johnson_slack == 72 and first_order_sign_numerator == 13464
    assert Johnson_slack > 0 and first_order_sign_numerator > 0

    root = Path(__file__).parent
    bank_path = root/"parameters_and_labels.json"
    bank_path.write_text(json.dumps(
        dict(encoding="base-3 polynomial coefficients in the displayed degree-8 modulus",
             columns=["a", "b", "P(beta)"], records=bank),
        indent=2,
    )+"\n")
    affine_bank_path = root/"affine_parameters.json"
    affine_bank_path.write_text(json.dumps(
        dict(encoding="base-3 polynomial coefficients in the displayed degree-8 modulus",
             columns=["P(beta)", "affine_parameter_1_minus_cstar_over_label", "witness_scale"],
             records=affine_bank),
        indent=2,
    )+"\n")
    receipt = dict(
        task="p3,s2 norm-trace exact finite bank",
        characteristic=p, s=s, Q=Q, n=n,
        challenge_size=challenge_size,
        modulus_coefficients_ascending=modulus_coefficients,
        modulus_irreducible=True,
        pole_encoded=encode(beta),
        native_generator_encoded=encode(native_generator),
        FQ_generator_encoded=encode(small_generator),
        native_elements_encoded=[encode(x) for x in native],
        FQ_nonzero_elements_encoded=[encode(a) for a in small_nonzero],
        G_degree=degree_G, F_degree=degree_F, P_degree=D,
        correction_degree=K, strict_code_dimension=K,
        exact_witness_agreement=T,
        distinct_G_polynomials=len(distinct_polynomials),
        distinct_nonzero_labels=len(labels),
        scaled_G_pole_values=len(scaled_G_values),
        G_root_count_distribution=dict(sorted(G_root_counts.items())),
        P_root_count_distribution=dict(sorted(P_root_counts.items())),
        witness_degree_distribution=dict(sorted(witness_degrees.items())),
        center_root_multiplicity_in_P=4,
        algebra_identity_check_groups=algebra_identity_checks,
        residual_evaluation_checks=residual_evaluation_checks,
        affine_residual_evaluation_checks=affine_residual_evaluation_checks,
        exact_Johnson_slack=Johnson_slack,
        first_order_sign_numerator_with_denominator_n_cubed=first_order_sign_numerator,
        above_full_first_order_and_below_exact_Johnson=True,
        code_rate=f"{K}/{n}",
        agreement_fraction=f"{T}/{n}",
        common_agreement_by_reciprocal_proof=K,
        native_field_endpoint_pair=dict(
            r0="f+cstar*g",
            r1="cstar*g",
            cstar_encoded=encode(cstar),
            cstar_pth_power_equals_Lambda_beta_to_p_minus_one=True,
            cstar_outside_canonical_bank=True,
            affine_parameters="1-cstar/P(beta)",
            distinct_affine_parameters=population,
            all_affine_parameters_avoid_zero_and_one=True,
            all_scaled_witness_degrees_less_than_K=True,
            exact_scaled_witness_agreement=T,
            source_r0_agreement_upper_by_multiplicity_proof=source_r0_upper,
            source_r1_and_common_agreement_by_reciprocal_proof=K,
            source_r0_exact_agreement_not_claimed=True,
            smaller_guaranteed_loss_fraction=f"{T-source_r0_upper}/{n}",
            smaller_loss_to_capacity_margin=f"{T-source_r0_upper}/{T-K}",
            source_bounds_verified_by_codeword_enumeration=False,
        ),
        projection_extension=dict(
            characteristic=p,
            degree=16,
            size=p**16,
            field_constructed_or_enumerated=False,
            both_endpoint_and_common_agreement_by_coefficient_projection=K,
            exhibited_affine_exceptional_parameters=population,
            threshold_loss_fraction=f"{T-K}/{n}",
        ),
        scope=(
            "648 exhibited labels and explicit witnesses; no codeword enumeration, "
            "no complete-label or singleton-list classification, "
            "native-field source bounds use the multiplicity/reciprocal proofs; "
            "optional degree-16 equalities use the coefficient-projection proof"
        ),
        bank_sha256=hashlib.sha256(bank_path.read_bytes()).hexdigest(),
        affine_bank_sha256=hashlib.sha256(affine_bank_path.read_bytes()).hexdigest(),
        witness_bank_sha256=witness_digest.hexdigest(),
        verifier_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        pass_all_checks=True,
    )
    (root/"receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n")
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
