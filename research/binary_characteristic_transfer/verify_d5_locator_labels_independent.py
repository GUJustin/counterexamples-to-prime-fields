"""Independent, bounded d5 label audit through actual three-space locators.

Only p=3,5 are enumerated.  The primary calculation uses recursive subspace
polynomials; trace-dual Plucker coordinates are checked afterward for each W.
No use is made of the two-space enumerator in check_d5_theta_one.py.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import json
import time

from flint import fq_default_ctx


def rref_spaces(p, dimension):
    for pivots in combinations(range(5), dimension):
        slots = [(r, c) for r, pivot in enumerate(pivots)
                 for c in range(pivot + 1, 5) if c not in pivots]
        for values in product(range(p), repeat=len(slots)):
            mat = [[0] * 5 for _ in range(dimension)]
            for r, pivot in enumerate(pivots):
                mat[r][pivot] = 1
            for (r, c), value in zip(slots, values):
                mat[r][c] = value
            yield mat


def nullspace(mat, p):
    mat = [row[:] for row in mat]
    pivots = []
    for c in range(5):
        r = len(pivots)
        k = next((k for k in range(r, len(mat)) if mat[k][c] % p), None)
        if k is None:
            continue
        mat[r], mat[k] = mat[k], mat[r]
        inv = pow(mat[r][c], -1, p)
        mat[r] = [(v * inv) % p for v in mat[r]]
        for k in range(len(mat)):
            if k != r:
                multiplier = mat[k][c]
                mat[k] = [(v - multiplier * w) % p
                          for v, w in zip(mat[k], mat[r])]
        pivots.append(c)
    out = []
    for c in range(5):
        if c not in pivots:
            row = [0] * 5
            row[c] = 1
            for r, pivot in enumerate(pivots):
                row[pivot] = -mat[r][c] % p
            out.append(row)
    return out


def evaluate_linearized(coeffs, x, p):
    value = x * 0
    power = x
    for coefficient in coeffs:
        value += coefficient * power
        power = power ** p
    return value


def subspace_locator(basis, F, p):
    coeffs = [F(1)]
    for x in basis:
        value = evaluate_linearized(coeffs, x, p)
        assert value != 0
        multiplier = value ** (p - 1)
        new = [-multiplier * coefficient for coefficient in coeffs] + [F(0)]
        for j, coefficient in enumerate(coeffs):
            new[j + 1] += coefficient ** p
        coeffs = new
    assert len(coeffs) == 4 and coeffs[-1] == 1 and coeffs[0] != 0
    assert all(evaluate_linearized(coeffs, x, p) == 0 for x in basis)
    return coeffs


def key(x):
    values = list(map(int, x.to_list()))
    return tuple(values + [0] * (5 - len(values)))


def run():
    started = time.monotonic()
    archived = json.loads(Path(__file__).with_name('check_d5_theta_one.json').read_text())
    archived = {row['p']: row for row in archived}
    rows = []
    for p in (3, 5):
        row_start = time.monotonic()
        F = fq_default_ctx(p, 5, 'a')
        coordinate_basis = [F([int(i == j) for i in range(5)]) for j in range(5)]

        def trace(x):
            total = F(0)
            for _ in range(5):
                total += x
                x = x ** p
            values = key(total)
            assert values[1:] == (0, 0, 0, 0)
            return values[0]

        gram = [[trace(x * y) for y in coordinate_basis] for x in coordinate_basis]
        assert len(nullspace(gram, p)) == 0
        counts = Counter()
        spaces = 0
        for mat in rref_spaces(p, 3):
            basis = list(map(F, mat))
            a3, a2, a1, _ = subspace_locator(basis, F, p)
            z = a1 + a2 ** p - a1 ** (p + 1)
            counts[key(z)] += 1

            trace_rows = [[sum(mat[r][k] * gram[k][j] for k in range(5)) % p
                           for j in range(5)] for r in range(3)]
            dual = nullspace(trace_rows, p)
            assert len(dual) == 2
            x, y = map(F, dual)
            assert all(trace(w * u) == 0 for w in basis for u in (x, y))
            X, Y = [x], [y]
            for _ in range(4):
                X.append(X[-1] ** p)
                Y.append(Y[-1] ** p)

            def P(i, j):
                return X[i] * Y[j] - X[j] * Y[i]

            denominator = P(3, 4)
            assert denominator != 0
            assert a1 == P(2, 4) / denominator
            assert a2 == P(1, 4) / denominator
            assert a3 == P(0, 4) / denominator
            assert z == (P(2, 4) - P(2, 3)) / denominator
            spaces += 1

        expected = (p ** 5 - 1) * (p ** 4 - 1) // ((p ** 2 - 1) * (p - 1))
        missing = [list(v) for v in product(range(p), repeat=5) if v not in counts]
        histogram = dict(sorted(Counter(counts.values()).items()))
        assert spaces == expected
        assert sum(k * v for k, v in histogram.items()) == spaces
        assert sum(histogram.values()) == len(counts)
        original = archived[p]
        assert original['spaces'] == spaces and original['labels'] == len(counts)
        assert original['missing'] == missing
        assert {int(k): v for k, v in original['fiber_histogram'].items()} == histogram
        row = dict(p=p, field=str(F), actual_three_spaces=spaces,
                   directly_constructed_locators=spaces, trace_dual_checks=spaces,
                   labels=len(counts), alphabet=p ** 5, missing=missing,
                   fiber_histogram=histogram, archived_receipt_matches=True,
                   seconds=round(time.monotonic() - row_start, 4), passed=True)
        rows.append(row)
        print(json.dumps(row), flush=True)

    # A bounded algebraic countercertificate to the proposed missing-label
    # equation z^2-z-1=0; no p=11 subspace enumeration is performed.
    locator, quotient, p = [8, 5, 8, 1], [4, 3, 1], 11
    product_coeffs = [0] * 6
    for i, a in enumerate(locator):
        for j, b in enumerate(quotient):
            product_coeffs[i + j] = (product_coeffs[i + j] + a * b) % p
    assert product_coeffs == [10, 0, 0, 0, 0, 1]
    z = (locator[2] + locator[1] - locator[2] ** 2) % p
    assert z == 4 and (z * z - z - 1) % p == 0
    counterexample = dict(p=p, label=z, locator_coefficients=locator,
                         composition_quotient_coefficients=quotient,
                         composition_coefficients=product_coeffs,
                         locator_separable=locator[0] != 0,
                         root_space_dimension=3,
                         proposed_missing_equation_value=0, passed=True)
    receipt = dict(method='recursive subspace locators on RREF three-spaces, followed by trace-dual checks',
                   rows=rows, p11_prediction_counterexample=counterexample,
                   total_seconds=round(time.monotonic() - started, 4), passed=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(receipt, indent=2) + '\n')
    return receipt


if __name__ == '__main__':
    run()
