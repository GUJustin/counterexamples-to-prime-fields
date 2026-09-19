#!/usr/bin/env python3
"""Bounded exact test of the one prescribed isogeny-norm label kappa."""

import hashlib
import json
from pathlib import Path
import resource
import time

from flint import nmod_mat, nmod_poly


def main():
    started = time.monotonic()
    root = Path(__file__).resolve().parent
    fixture_path = root.parent / "fixture.json"
    raw_fixture = fixture_path.read_bytes()
    fixture = json.loads(raw_fixture)
    p, ell, n, k = (fixture[key] for key in ("p", "ell", "n", "k"))
    R, omitted = n-k, 2*ell+5
    row_count, unknown_count = R-omitted, 2*R
    assert (p, ell, n, k, R, omitted, row_count, unknown_count) == (
        1657, 23, 264, 173, 91, 51, 40, 182
    )
    domain = set(fixture["domain"])
    coordinates = {
        (item["a"], item["c"]): item["point"]
        for item in fixture["torsion_coordinates"]
    }
    representatives = {}
    for pair, point in sorted(coordinates.items()):
        if point is not None:
            representatives.setdefault(point[0], (pair, point))
    representatives = [representatives[x] for x in sorted(representatives)]
    assert len(representatives) == n
    extra_multipliers = (1, 2, 4, 5, 6)

    def evaluate(poly, x):
        value = 0
        for coefficient in reversed(poly):
            value = (value*x+coefficient) % p
        return value

    def locator(roots):
        result = nmod_poly([1], p)
        for x in roots:
            result *= nmod_poly([-x % p, 1], p)
        return result

    eligible = []
    for h in fixture["subgroups"]:
        kernel = set(h["kernel_x"])
        eligible.append([
            item for item in representatives if item[1][0] not in kernel
        ])
    assert all(len(items) == ell*(ell-1)//2 for items in eligible)

    basis_rows, all_rows, records = [], [], []
    rank = 0
    timed_out = False
    for point_index in range(ell*(ell-1)//2):
        if rank == unknown_count or timed_out:
            break
        for h_index, h in enumerate(fixture["subgroups"]):
            pair, point = eligible[h_index][point_index]
            multiples = {}
            for j in (*extra_multipliers, 3, 7):
                multiple = coordinates[(j*pair[0] % ell, j*pair[1] % ell)]
                assert multiple is not None
                multiples[j] = multiple[0]
            extra = sorted(multiples[j] for j in extra_multipliers)
            assert len(set(extra)) == 5
            tags = []
            for j in (3, 7):
                denominator = evaluate(h["B"], multiples[j])
                assert denominator
                tags.append(evaluate(h["N"], multiples[j])
                            * pow(denominator, -1, p) % p)
            assert tags[0] != tags[1]
            fiber_dictionary = {entry["tag"]: entry["x"] for entry in h["fibers"]}
            first, second = (fiber_dictionary[tag] for tag in tags)
            support = sorted(set(first) | set(second) | set(extra))
            assert len(support) == omitted and set(support) <= domain
            assert not set(extra) & (set(first) | set(second))

            K = h["K"]
            label = 1
            for x in extra:
                label = label*evaluate(K, x) % p
            assert label
            J = locator(extra)
            N, B = nmod_poly(h["N"], p), nmod_poly(h["B"], p)
            U = (N-tags[0]*B)*(N-tags[1]*B)*J
            assert U == locator(support)
            coefficients = [int(value) for value in U.coeffs()]
            assert len(coefficients) == omitted+1 and coefficients[-1] == 1
            rows = []
            for shift in range(row_count):
                left = [0]*R
                left[shift:shift+len(coefficients)] = coefficients
                rows.append(left + [(label*value) % p for value in left])
            reduced, new_rank = nmod_mat(basis_rows+rows, p).rref()
            basis_rows = [
                [int(reduced[i, j]) for j in range(unknown_count)]
                for i in range(new_rank)
            ]
            all_rows.extend(rows)
            records.append(dict(
                subgroup=h_index, point_index=point_index,
                torsion_coordinates=list(pair), point=point,
                extra_x=extra, tags_3_and_7=tags,
                full_support=support, label_kappa=label,
                locator_coefficients_ascending=coefficients,
                rank_before=rank, rank_after=new_rank,
            ))
            rank = new_rank
            if rank == unknown_count:
                break
            if time.monotonic()-started >= 50:
                timed_out = True
                break

    independent_rows = []
    square_matrix_hash = None
    if rank == unknown_count:
        transposed_rref, transposed_rank = nmod_mat(all_rows, p).transpose().rref()
        assert transposed_rank == unknown_count
        pivots = []
        for i in range(unknown_count):
            pivot = next(j for j in range(len(all_rows)) if transposed_rref[i, j])
            pivots.append(pivot)
        assert len(set(pivots)) == unknown_count
        square_rows = [all_rows[pivot] for pivot in pivots]
        square = nmod_mat(square_rows, p)
        assert square.rank() == unknown_count and int(square.det()) != 0
        independent_rows = [
            dict(stacked_row=pivot, support_index=pivot//row_count,
                 recurrence_shift=pivot % row_count)
            for pivot in pivots
        ]
        square_matrix_hash = hashlib.sha256(
            json.dumps(square_rows, separators=(",", ":")).encode()
        ).hexdigest()

    selected = dict(
        fixture_sha256=hashlib.sha256(raw_fixture).hexdigest(),
        p=p, ell=ell, n=n, k=k, redundancy=R,
        unknown_order="[s_f[0..90],s_g[0..90]]",
        label_formula="product K_H(x(jP)), j in {1,2,4,5,6}",
        records=records,
        independent_rows=independent_rows,
        independent_matrix_sha256=square_matrix_hash,
    )
    selected_path = root / "selected_supports.json"
    selected_path.write_text(json.dumps(selected, indent=2, sort_keys=True)+"\n")
    receipt = dict(
        status="FULL_RANK" if rank == unknown_count else "BOUNDED_PARTIAL",
        p=p, ell=ell, n=n, k=k, threshold=n-omitted,
        redundancy=R, errors_per_support=omitted,
        recurrence_rows_per_support=row_count,
        global_syndrome_unknowns=unknown_count,
        selected_support_count=len(records),
        subgroup_indices=sorted({item["subgroup"] for item in records}),
        distinct_selected_label_count=len({item["label_kappa"] for item in records}),
        final_rank=rank, nullity=unknown_count-rank,
        stopped_immediately_at_full_rank=rank == unknown_count,
        fifty_second_cap_triggered=timed_out,
        independent_square_row_count=len(independent_rows),
        independent_matrix_sha256=square_matrix_hash,
        fixture_sha256=hashlib.sha256(raw_fixture).hexdigest(),
        selected_supports_sha256=hashlib.sha256(selected_path.read_bytes()).hexdigest(),
        verifier_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        scope=(
            "the specified ell23 curve, support family, and norm label kappa; "
            "full rank excludes even a nonzero common syndrome pair for these "
            "selected supports, hence excludes the whole prescribed labelled bank; "
            "it does not exclude subbanks omitting constraints, other label maps, "
            "other curves or all moving quintics"
        ),
        no_counterexample_claim=True,
        no_inverse_or_projective_reparameter_rerun=True,
    )
    (root / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n")
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
