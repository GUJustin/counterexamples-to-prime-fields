#!/usr/bin/env python3
"""Bounded orbit classification and exhaustive 3^7-dimensional-space check."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import (
    fmpz_mod_poly_ctx, fq_default_ctx, fq_default_poly_ctx, nmod_mat,
)


def orbit_check(p, s):
    Q, n = p**s, p**(2*s)
    cap = (n+Q)//p
    unseen = set(range(1, n-1))
    allowed, rejected = [], []
    while unseen:
        first = min(unseen)
        orbit, exponent = [], first
        while exponent not in orbit:
            orbit.append(exponent)
            exponent = p*exponent % (n-1)
        assert exponent == first and set(orbit) <= unseen
        unseen.difference_update(orbit)
        (allowed if max(orbit) <= cap else rejected).append(sorted(orbit))
    expected = [
        sorted(p**i for i in range(2*s)),
        sorted((Q+1)*p**i for i in range(s)),
    ]
    assert sorted(allowed) == sorted(expected)
    dimension = 1+sum(len(orbit) for orbit in allowed)
    assert dimension == 3*s+1
    return dict(
        p=p, s=s, Q=Q, native_size=n, degree_cap=cap,
        modulus_for_nonzero_exponents=n-1,
        allowed_nonconstant_orbits=allowed,
        coefficient_frobenius_periods=sorted(len(orbit) for orbit in allowed),
        prime_field_coefficient_space_dimension=dimension,
        space_size=p**dimension,
        rejected_orbit_count=len(rejected),
        constant_coefficient_dimension=1,
        exponent_n_minus_one_excluded_by_degree=n-1 > cap,
    )


def main():
    started = time.monotonic()
    root = Path(__file__).resolve().parent
    parent = root.parent
    saved = json.loads((parent/"receipt.json").read_text())
    bank_bytes = (parent/"parameters_and_labels.json").read_bytes()
    bank_records = json.loads(bank_bytes)["records"]
    orbit_receipts = [orbit_check(p, s) for p, s in ((3, 2), (3, 3), (5, 2))]
    p, Q, n, cap, D, k, T = 3, 9, 81, 30, 54, 34, 51
    modulus = fmpz_mod_poly_ctx(p)(saved["modulus_coefficients_ascending"])
    assert modulus.is_irreducible()
    field = fq_default_ctx(modulus=modulus, var="z")
    polys = fq_default_poly_ctx(field)
    X, beta = polys.gen(), field.gen()
    Lambda = X**n-X

    def decode(value):
        return field([(value//p**j) % p for j in range(8)])

    def encode(value):
        return sum(int(coefficient)*p**j for j, coefficient in enumerate(value.to_list()))

    def signature(poly):
        return tuple(encode(coefficient) for coefficient in poly.coeffs())

    def trace_poly(poly, length):
        result = polys.zero()
        for i in range(length):
            result += poly**(p**i)
        return result

    native = [decode(value) for value in saved["native_elements_encoded"]]
    small = [field.zero()]+[decode(value) for value in saved["FQ_nonzero_elements_encoded"]]
    assert len(native) == n and len(small) == Q
    assert all(value**n == value for value in native)
    assert all(value**Q == value for value in small)

    # An explicit coefficient-space basis over F3, verified in the degree-8
    # ambient representation rather than inferred merely by parameter counting.
    native_generator = decode(saved["native_generator_encoded"])
    small_generator = decode(saved["FQ_generator_encoded"])
    basis = [polys.one()]
    basis += [trace_poly((native_generator**i)*X, 4) for i in range(4)]
    basis += [trace_poly((small_generator**i)*X**10, 2) for i in range(2)]
    basis_rows = []
    for polynomial in basis:
        row = []
        for j in range(cap+1):
            coefficient = encode(polynomial[j])
            row.extend((coefficient//p**i) % p for i in range(8))
        basis_rows.append(row)
    basis_rank = nmod_mat(basis_rows, p).rank()
    assert basis_rank == 7

    # Reconstruct the existing normalized bank independently of this census.
    bank_polynomials = {}
    bank_locators = {}
    for a_code, center_code, label_code in bank_records:
        a, center = decode(a_code), decode(center_code)
        G = trace_poly(a*(X+center)**10, 2)+1
        F = a**3*(X+center)**3
        quotient, remainder = divmod(Lambda, G)
        assert remainder.is_zero()
        P = F*quotient
        assert encode(P(beta)) == label_code
        key = signature(P)
        assert key not in bank_polynomials
        bank_polynomials[key] = (a_code, center_code, label_code)
        bank_locators[signature(G/G.leading_coefficient())] = key
    assert len(bank_polynomials) == len(bank_locators) == 648

    linear_parts = [(linear, trace_poly(linear*X, 4)) for linear in native]
    norm_parts = [(a, trace_poly(a*X**10, 2)) for a in small]
    root_histogram, degree_histogram = Counter(), Counter()
    complete_levels = Counter()
    monic_locator_multiplicities = Counter()
    residual_multiplicities = Counter()
    all_signatures = set()
    squarefree_full_degree = 0
    non_squarefree_full_degree = 0
    value_checks = 0
    basic_identity_checks = 0
    residual_identity_checks = 0
    for a, norm_part in norm_parts:
        for linear, linear_part in linear_parts:
            for constant in range(p):
                G = norm_part+linear_part+constant
                key = signature(G)
                assert key not in all_signatures
                all_signatures.add(key)
                degree_histogram[G.degree()] += 1
                derivative = G.derivative()
                assert G**p-G == Lambda*derivative
                basic_identity_checks += 1
                values = [G(x) for x in native]
                assert all(value**p == value for value in values)
                root_count = sum(value.is_zero() for value in values)
                root_histogram[root_count] += 1
                value_checks += n
                if G.degree() != cap:
                    assert a.is_zero()
                    continue
                assert not a.is_zero()
                center = (linear/a)**Q
                level = G(-center)
                assert level**p == level
                assert G == trace_poly(a*(X+center)**10, 2)+level
                complete_levels[encode(level)] += 1
                squarefree = G.gcd(derivative).degree() == 0
                if not squarefree:
                    non_squarefree_full_degree += 1
                    assert level.is_zero() and root_count == cap-Q
                    assert divmod(G, (X+center)**(Q+1))[1].is_zero()
                    continue
                squarefree_full_degree += 1
                assert not level.is_zero() and root_count == cap
                quotient, remainder = divmod(Lambda, G)
                assert remainder.is_zero()

                # Extract the unique polynomial cube root of G'.
                root_coefficients = [field.zero()]*(derivative.degree()//p+1)
                for exponent, coefficient in enumerate(derivative.coeffs()):
                    if exponent % p:
                        assert coefficient.is_zero()
                    else:
                        root_coefficients[exponent//p] = coefficient**(p**7)
                F = polys(root_coefficients)
                assert F**p == derivative
                P = F*quotient
                assert P.is_monic() and P.degree() == D
                assert (P-X**D).degree() == k
                assert P**p-Lambda**(p-1) == -(quotient**(p-1))
                assert sum(P(x).is_zero() for x in native) == T
                P_key = signature(P)
                assert P_key in bank_polynomials
                residual_multiplicities[P_key] += 1

                # Literal identities from the equality-case proof.
                L = G/G.leading_coefficient()
                V, remainder = divmod(Lambda, L)
                assert remainder.is_zero() and V.degree() == T
                H, remainder = divmod(P, V)
                assert remainder.is_zero() and H.degree() == 3
                bracket = H**p*V-L**(p-1)
                assert bracket.degree() == 0 and not bracket.is_zero()
                c = bracket[0]
                v = next(x for x, value in zip(native, values) if not value.is_zero())
                alpha = L(v)
                assert not alpha.is_zero() and c == -(alpha**(p-1))
                assert L**p+c*L == Lambda*(H**p)
                descended_G = L/alpha
                assert descended_G**p-descended_G == Lambda*(H/alpha)**p
                normalized_G = G/level
                normalized_F = F/level
                expected_a = a/level
                assert normalized_G == trace_poly(expected_a*(X+center)**10, 2)+1
                assert normalized_F == expected_a**3*(X+center)**3
                assert normalized_F*divmod(Lambda, normalized_G)[0] == P
                assert bank_polynomials[P_key][:2] == (encode(expected_a), encode(center))
                L_key = signature(L)
                assert bank_locators[L_key] == P_key
                monic_locator_multiplicities[L_key] += 1
                residual_identity_checks += 7

    assert len(all_signatures) == 3**7 == 2187
    assert dict(root_histogram) == {81: 1, 0: 2, 27: 240, 21: 648, 30: 1296}
    assert squarefree_full_degree == 1296 and non_squarefree_full_degree == 648
    assert dict(complete_levels) == {0: 648, 1: 648, 2: 648}
    assert len(monic_locator_multiplicities) == len(residual_multiplicities) == 648
    assert set(monic_locator_multiplicities.values()) == {2}
    assert set(residual_multiplicities.values()) == {2}

    output = dict(
        status="PASS",
        orbit_checks=orbit_receipts,
        coefficient_basis_rank_over_F3=basis_rank,
        coefficient_basis_count=len(basis),
        enumerated_parameter_space="a in F9, linear coefficient in F81, constant in F3",
        total_distinct_polynomials=len(all_signatures),
        native_value_checks=value_checks,
        degree_histogram=dict(sorted(degree_histogram.items())),
        native_root_count_histogram=dict(sorted(root_histogram.items())),
        full_degree_completed_level_histogram=dict(sorted(complete_levels.items())),
        full_degree_squarefree_polynomials=squarefree_full_degree,
        full_degree_repeated_root_polynomials=non_squarefree_full_degree,
        distinct_monic_split_locators=len(monic_locator_multiplicities),
        each_monic_locator_multiplicity=2,
        distinct_reconstructed_bank_polynomials=len(residual_multiplicities),
        each_reconstructed_polynomial_multiplicity=2,
        existing_bank_recovered_exactly=True,
        identities_G_p_minus_G_equals_Lambda_G_derivative=basic_identity_checks,
        literal_equality_case_identity_checks=residual_identity_checks,
        scope=(
            "exact exponent-orbit ledgers in three parameter cases and exhaustive "
            "enumeration of all 2187 elements of the dimension-seven space for p3s2; "
            "not an enumeration of all codewords, received residuals or challenge-field words; "
            "the general equality classification remains the algebraic theorem"
        ),
        source_bank_sha256=hashlib.sha256(bank_bytes).hexdigest(),
        source_verifier_sha256=saved["verifier_sha256"],
        verifier_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    )
    (root/"receipt.json").write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
