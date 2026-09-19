#!/usr/bin/env python3
"""Exact quadratic-pole label fibers for the saved odd-Gold parameter set."""

from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import fmpz_mod_poly_ctx, fq_default_ctx, fq_default_poly_ctx, nmod_mat


def main():
    started = time.monotonic()
    root = Path(__file__).resolve().parent
    p, n, q, d, D, k, T, source_upper = 3, 243, 59049, 90, 162, 102, 153, 135
    modulus_coefficients = [2,1,0,0,2,2,2,0,0,0,1]
    modulus = fmpz_mod_poly_ctx(p)(modulus_coefficients)
    assert modulus.is_irreducible()
    field = fq_default_ctx(modulus=modulus, var="z", fq_type="FQ_NMOD")
    polys = fq_default_poly_ctx(field)
    X, beta = polys.gen(), field.gen()
    assert q-1 == 2**3*11**2*61
    assert beta**(q-1) == 1
    assert all(beta**((q-1)//r) != 1 for r in (2,11,61))
    native_generator = beta**244
    assert native_generator**242 == 1
    assert native_generator**121 != 1 and native_generator**22 != 1
    assert beta**n != beta and beta**(n*n) == beta

    def encode(value):
        return sum(int(coefficient)*p**i for i,coefficient in enumerate(value.to_list()))

    def decode(value):
        return field([(value//p**i) % p for i in range(10)])

    def guard():
        if time.monotonic()-started > 110:
            raise RuntimeError("Stopped at the bounded 110-second internal cap")
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 512*1024**2:
            raise RuntimeError("Stopped at the 512 MiB memory cap")

    native = sorted([field.zero()]+[native_generator**i for i in range(242)],key=encode)
    assert len({encode(x) for x in native}) == n and all(x**n == x for x in native)
    good = [a for a in native if not a.is_zero() and a**121 == -field.one()]
    assert len(good) == 121
    exponents = [10,30,90,28,84]
    Lambda, delta = X**n-X, beta**n-beta
    cstar = (delta**2)**(p**9)
    assert cstar**p == delta**2 and not cstar.is_zero()

    # Finite evaluation-space rank: H has dimension11 over F3, E has dimension10.
    basis = [polys.one()]
    for i in range(5):
        linear = native_generator**i
        basis.append(sum(((linear*X)**(p**j) for j in range(5)), polys.zero()))
    for i in range(5):
        a = native_generator**i
        basis.append(sum((a**(p**j)*X**exponents[j] for j in range(5)), polys.zero()))
    coefficient_rows, evaluation_rows = [], []
    for polynomial in basis:
        row = []
        for exponent in range(d+1):
            code = encode(polynomial[exponent])
            row.extend((code//p**i) % p for i in range(10))
        coefficient_rows.append(row)
        value = encode(polynomial(beta))
        evaluation_rows.append([(value//p**i) % p for i in range(10)])
    assert nmod_mat(coefficient_rows,p).rank() == 11
    evaluation_rank = nmod_mat(evaluation_rows,p).rank()
    assert evaluation_rank == 10

    shifted = []
    for b in native:
        z = beta+b
        shifted.append((b,[z**e for e in exponents],z**3,z**9))
    fibers = defaultdict(list)
    records = []
    for a in good:
        coefficients = [a**(p**i) for i in range(5)]
        for b,powers,z3,z9 in shifted:
            G_beta = field.one()
            for coefficient,power in zip(coefficients,powers):
                G_beta += coefficient*power
            assert not G_beta.is_zero()
            F_beta = coefficients[4]*z3+coefficients[2]*z9
            label = delta*F_beta/G_beta
            assert label**p == delta**2*(1-G_beta**(-2))
            label_code = encode(label)
            parameter_code = None if label.is_zero() else encode(1-cstar/label)
            if parameter_code is not None:
                assert parameter_code not in (0,1)
            a_code,b_code = encode(a),encode(b)
            records.append([a_code,b_code,label_code,parameter_code])
            fibers[label_code].append([a_code,b_code])
        guard()
    assert len(records) == 29403 and len(fibers[0]) == 1
    assert encode(cstar) not in fibers
    histogram = Counter(len(members) for label,members in fibers.items() if label)
    assert all(size <= p for size in histogram)
    assert sum(size*count for size,count in histogram.items()) == 29402
    nonzero_count = len(fibers)-1
    assert nonzero_count >= (29402+2)//3 == 9801
    parameters = {record[3] for record in records if record[3] is not None}
    assert len(parameters) == nonzero_count

    # Test every witness in one deterministic collision fiber of each observed size,
    # as well as the unique zero-label witness.
    sample_labels = [0]+[
        min(label for label,members in fibers.items() if label and len(members)==size)
        for size in sorted(histogram)
    ]
    source_g = [(x-beta).inverse() for x in native]
    source_f = [(x**D-beta**D)*g for x,g in zip(native,source_g)]
    samples = []
    for label_code in sample_labels:
        label = decode(label_code)
        witness_signatures = set()
        for a_code,b_code in fibers[label_code]:
            a,b = decode(a_code),decode(b_code)
            Z = X+b
            coefficients = [a**(p**j) for j in range(5)]
            G = 1+sum((coefficients[j]*Z**exponents[j] for j in range(5)),polys.zero())
            F = coefficients[4]*Z**3+coefficients[2]*Z**9
            assert G.derivative() == F**p and G**p-G == Lambda*F**p
            quotient,remainder = divmod(Lambda,G)
            assert remainder.is_zero()
            P = F*quotient
            assert P.is_monic() and P.degree() == D and (P-X**D).degree() == k
            assert P(beta) == label
            witness,remainder = divmod(X**D-P+label-beta**D,X-beta)
            assert remainder.is_zero() and witness.degree() == k-1
            signature = tuple(encode(c) for c in witness.coeffs())
            assert signature not in witness_signatures
            witness_signatures.add(signature)
            matches = affine_matches = 0
            for x,f,g in zip(native,source_f,source_g):
                residual = f+label*g-witness(x)
                assert residual == P(x)*g
                matches += residual.is_zero()
                if label_code:
                    scale = cstar/label
                    parameter = 1-scale
                    residual_affine = (
                        (1-parameter)*(f+cstar*g)+parameter*cstar*g
                        -scale*witness(x)
                    )
                    assert residual_affine == scale*residual
                    affine_matches += residual_affine.is_zero()
            assert matches == T
            assert not label_code or affine_matches == T
            samples.append(dict(
                a=a_code,center=b_code,label=label_code,
                fiber_size=len(fibers[label_code]),witness_degree=witness.degree(),
                matches=matches,affine_matches=affine_matches if label_code else None,
            ))
        guard()

    bank_path = root/"parameters_and_labels.json"
    bank_path.write_text(json.dumps(dict(
        columns=["a","center_b","P(beta)","affine_parameter_or_null_at_zero_label"],
        encoding="base-3 polynomial coefficients in the displayed degree-10 modulus",
        records=records,
    ),indent=2)+"\n")
    output = dict(
        status="PASS",p=p,native_size=n,challenge_size=q,
        native_extension_degree=5,challenge_extension_degree=10,
        challenge_degree_over_native=2,
        modulus_coefficients_ascending=modulus_coefficients,
        modulus_irreducible=True,field_implementation="FLINT FQ_NMOD",
        beta_encoded=encode(beta),beta_native=False,
        challenge_generator_primitive=True,
        challenge_multiplicative_order_factorization={"2":3,"11":2,"61":1},
        native_generator_power_of_beta=244,
        native_generator_encoded=encode(native_generator),
        native_elements_encoded=[encode(x) for x in native],
        good_a_count=121,good_a_are_native_nonsquares=True,
        coefficient_space_basis_rank=11,
        coefficient_evaluation_rank=evaluation_rank,
        coefficient_evaluation_kernel_dimension=11-evaluation_rank,
        evaluated_bank_polynomial_count=len(records),
        zero_label_polynomial_count=len(fibers[0]),zero_label_parameters=fibers[0],
        nonzero_label_count=nonzero_count,
        nonzero_fiber_size_histogram=dict(sorted(histogram.items())),
        maximum_observed_fiber_size=max(histogram),
        lower_bound_nonzero_labels=9801,
        distinct_interior_affine_parameter_count=len(parameters),
        cstar_encoded=encode(cstar),cstar_cube_equals_delta_squared=True,
        cstar_outside_bank=True,endpoint_pair=["f+cstar*g","cstar*g"],
        code_dimension=k,threshold=T,
        source_r0_agreement_upper_by_proof=source_upper,
        source_r1_and_common_agreement_by_proof=k,
        source_bounds_verified_by_codeword_enumeration=False,
        full_polynomial_sample_count=len(samples),samples=samples,
        bank_sha256=hashlib.sha256(bank_path.read_bytes()).hexdigest(),
        verifier_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        scope=(
            "all29403 native bank evaluations at one fixed quadratic exterior pole, "
            "their exact label-fiber histogram and representative distinct witnesses; "
            "the universal polynomial classification and source bounds are proof-based; "
            "no challenge-field or all-codeword enumeration"
        ),
    )
    (root/"receipt.json").write_text(json.dumps(output,indent=2,sort_keys=True)+"\n")
    print(json.dumps({key:value for key,value in output.items()
                      if key not in ("native_elements_encoded","samples")},
                     indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
