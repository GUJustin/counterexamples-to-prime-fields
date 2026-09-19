#!/usr/bin/env python3
"""Bounded restriction ledger for the saved 648-word bank on F9."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import time

from flint import fmpz_mod_poly_ctx, fq_default_ctx, fq_default_poly_ctx


def main():
    started = time.monotonic()
    root = Path(__file__).parent
    parent = root.parent
    saved = json.loads((parent/"receipt.json").read_text())
    saved_bank = json.loads((parent/"parameters_and_labels.json").read_text())["records"]
    modulus = fmpz_mod_poly_ctx(3)(saved["modulus_coefficients_ascending"])
    field = fq_default_ctx(modulus=modulus, var="z")
    polynomial = fq_default_poly_ctx(field)
    X, beta = polynomial.gen(), field.gen()
    one, zero = field.one(), field.zero()

    def decode(value):
        return field([(value//3**j) % 3 for j in range(8)])

    def encode(value):
        return sum(int(coefficient)*3**j for j, coefficient in enumerate(value.to_list()))

    def coefficients(poly):
        values = poly.coeffs()
        return values+[zero]*(9-len(values))

    def rank(rows):
        basis = {}
        for source_row in rows:
            row = list(source_row)
            for pivot in sorted(basis):
                if not row[pivot].is_zero():
                    factor = row[pivot]
                    row = [value-factor*other for value, other in zip(row, basis[pivot])]
            pivot = next((j for j, value in enumerate(row) if not value.is_zero()), None)
            if pivot is not None:
                inverse = row[pivot].inverse()
                basis[pivot] = [value*inverse for value in row]
        return len(basis)

    small = sorted([zero]+[decode(a) for a in saved["FQ_nonzero_elements_encoded"]], key=encode)
    assert len(small) == 9 and all(x**9 == x for x in small)
    small_modulus = X**9-X
    Lambda, R = X**81-X, X**54
    cstar = decode(saved["native_field_endpoint_pair"]["cstar_encoded"])
    assert cstar**3 == Lambda(beta)**2
    g_reduced = (X-beta).inverse_mod(small_modulus)
    f_reduced = ((R-beta**54)*g_reduced) % small_modulus
    r0_reduced = (f_reduced+cstar*g_reduced) % small_modulus
    r1_reduced = (cstar*g_reduced) % small_modulus
    low_head, remainder = divmod(X**6-beta**6, X-beta)
    assert remainder.is_zero() and low_head.degree() == 5
    label_shift = beta**6-beta**54
    assert f_reduced == (low_head+label_shift*g_reduced) % small_modulus
    assert not (label_shift+cstar).is_zero()
    unique_codeword_label = -label_shift
    unique_codeword_affine_parameter = 1-cstar/unique_codeword_label

    records = []
    retained = Counter()
    degree_histogram, scaled_degree_histogram = Counter(), Counter()
    for a_code, b_code, label_code in saved_bank:
        a, b, label = decode(a_code), decode(b_code), decode(label_code)
        Y = X+b
        norm_term = a*Y**10
        G = norm_term+norm_term**3+1
        F = a**3*Y**3
        J, remainder = divmod(Lambda, G)
        assert remainder.is_zero()
        P = F*J
        assert P(beta) == label
        H, remainder = divmod(R-P+label-beta**54, X-beta)
        assert remainder.is_zero()
        reduced_H = H % small_modulus
        scale = cstar/label
        affine_parameter = 1-scale
        reduced_scaled_H = scale*reduced_H
        original_agreement = sum(
            (f_reduced(x)+label*g_reduced(x)-reduced_H(x)).is_zero() for x in small
        )
        affine_agreement = sum(
            ((1-affine_parameter)*r0_reduced(x)+affine_parameter*r1_reduced(x)
             -reduced_scaled_H(x)).is_zero()
            for x in small
        )
        assert original_agreement == affine_agreement
        assert original_agreement == sum(not G(x).is_zero() for x in small)
        retained[original_agreement] += 1
        degree_histogram[reduced_H.degree()] += 1
        scaled_degree_histogram[reduced_scaled_H.degree()] += 1
        records.append(dict(
            a=a_code, b=b_code, label=label, affine_parameter=affine_parameter,
            raw=coefficients(reduced_H), scaled=coefficients(reduced_scaled_H),
            raw_degree=reduced_H.degree(), scaled_degree=reduced_scaled_H.degree(),
            agreement=original_agreement,
        ))

    def span_summary(group):
        raw = [item["raw"] for item in group]
        scaled = [item["scaled"] for item in group]
        return dict(
            count=len(group),
            raw_linear_span_rank=rank(raw),
            raw_difference_span_rank=rank([
                [x-y for x, y in zip(row, raw[0])] for row in raw[1:]
            ]),
            scaled_linear_span_rank=rank(scaled),
            scaled_difference_span_rank=rank([
                [x-y for x, y in zip(row, scaled[0])] for row in scaled[1:]
            ]),
            retained_agreement_histogram=dict(sorted(Counter(
                item["agreement"] for item in group
            ).items())),
        )

    global_affine_high_ranks = {}
    threshold_groups = {}
    for minimum_agreement in (4, 5, 6, 7, 8):
        group = [item for item in records if item["agreement"] >= minimum_agreement]
        assert len(group) >= 2
        high_ranks = {}
        for k in range(1, 9):
            raw_rank = rank([
                [one, item["label"]]+item["raw"][k:] for item in group
            ])-2
            scaled_rank = rank([
                [one, item["affine_parameter"]]+item["scaled"][k:] for item in group
            ])-2
            assert raw_rank == scaled_rank
            high_ranks[k] = raw_rank
        threshold_groups[minimum_agreement] = dict(
            **span_summary(group),
            high_coefficient_rank_mod_affine_functions_of_label=high_ranks,
            exhibited_labels_with_unmodified_scaled_witness_degree_lt_k={
                k: sum(item["scaled_degree"] < k for item in group) for k in range(1, 9)
            },
        )
        if minimum_agreement == 4:
            global_affine_high_ranks = high_ranks

    fixed_a = {
        a: span_summary([item for item in records if item["a"] == a])
        for a in saved["FQ_nonzero_elements_encoded"]
    }
    output = dict(
        task="restriction of the saved norm-trace bank to F9",
        n_short=9, coefficient_field_size=6561,
        source_verifier_sha256=saved["verifier_sha256"],
        source_bank_sha256=saved["bank_sha256"],
        domain_encoded=[encode(x) for x in small],
        canonical_label_count=len(records),
        raw_reduced_degree_histogram=dict(sorted(degree_histogram.items())),
        scaled_reduced_degree_histogram=dict(sorted(scaled_degree_histogram.items())),
        retained_agreement_histogram=dict(sorted(retained.items())),
        global_span=span_summary(records),
        global_high_coefficient_rank_mod_affine_functions_of_label=global_affine_high_ranks,
        threshold_groups=threshold_groups,
        fixed_a_groups=fixed_a,
        shortened_sources=dict(
            f_reduced_coefficients=[encode(x) for x in f_reduced.coeffs()],
            g_reduced_coefficients=[encode(x) for x in g_reduced.coeffs()],
            r0_reduced_coefficients=[encode(x) for x in r0_reduced.coeffs()],
            r1_reduced_coefficients=[encode(x) for x in r1_reduced.coeffs()],
            low_polynomial_degree=low_head.degree(),
            label_shift_encoded=encode(label_shift),
            exact_identity="f|F9=(X6-beta6)/(X-beta)+(beta6-beta54)*g|F9",
            unique_codeword_pencil_label_for_dimensions_6_to_8=encode(unique_codeword_label),
            unique_codeword_affine_parameter_for_dimensions_6_to_8=encode(
                unique_codeword_affine_parameter
            ),
            source_r0_reciprocal_coefficient_nonzero=True,
            endpoint_and_common_agreement_for_dimensions_6_to_8="exactly the chosen dimension",
            high_agreement_label_count_for_dimensions_6_to_8=1,
            proof_scope="last source statements use the exact reciprocal root bound",
        ),
        scope=(
            "all 648 canonical witnesses restricted to the fixed F9 subfield; "
            "linear ranks over F6561 and support histograms; no subset optimization "
            "or all-codeword search, no preserved larger-domain source bound assumed"
        ),
        verifier_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,
        pass_all_checks=True,
    )
    (root/"receipt.json").write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
