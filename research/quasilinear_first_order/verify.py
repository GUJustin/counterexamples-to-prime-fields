"""Exact finite checks for the restricted first-order MCA theorem."""
import itertools
import json
from pathlib import Path
import random

BASE = Path(__file__).resolve().parent


def trim(a):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def add(a, b, p):
    return trim([((a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)) % p
                 for i in range(max(len(a), len(b)))])


def scale(a, c, p):
    return trim([v*c % p for v in a])


def mul(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i+j] = (out[i+j]+u*v) % p
    return trim(out)


def derivative(a, p):
    return trim([i*a[i] % p for i in range(1, len(a))] or [0])


def evaluate(a, x, p):
    y = 0
    for c in reversed(a):
        y = (y*x+c) % p
    return y


def locator(xs, p):
    out = [1]
    for x in xs:
        out = mul(out, [-x % p, 1], p)
    return out


def interpolate(xs, ys, p):
    out = [0]
    for i, (x, y) in enumerate(zip(xs, ys)):
        others = xs[:i]+xs[i+1:]
        basis = locator(others, p)
        out = add(out, scale(basis, y*pow(evaluate(basis, x, p), -1, p), p), p)
    return out


def bad_support(xs, g, support, degree, p):
    if len(support) <= degree+1:
        return False
    seed = support[:degree+1]
    candidate = interpolate([xs[i] for i in seed], [g[i] for i in seed], p)
    return any(evaluate(candidate, xs[i], p) != g[i] for i in support)


def equation(kind, degree, z, p):
    if kind == 'two_solution':
        w = locator(list(range(degree)), p)
        # A=W'P+P(P-W).
        a = [[0], add(derivative(w, p), scale(w, -1, p), p), [1]]
        return w, a
    if kind == 'three_solution':
        w = locator(list(range(degree)), p)
        # A=W'P+P(P-W)(P-2W).
        a = [[0], add(derivative(w, p), scale(mul(w, w, p), 2, p), p),
             scale(w, -3, p), [1]]
        return w, a
    if kind == 'moving_riccati':
        r = [p-1, z]+[0]*(degree-1)+[1]
        # R P'=R'P-P^2.
        return r, [[0], derivative(r, p), [p-1]]
    if kind == 'rank_drop':
        # z P' = P(P-1); z=0 is an identically-zero separant.
        return [z], [[0], [p-1], [1]]
    raise AssertionError(kind)


def residual(candidate, r, a, p):
    right, power = [0], [1]
    for coefficient in a:
        right = add(right, mul(coefficient, power, p), p)
        power = mul(power, candidate, p)
    return add(mul(r, derivative(candidate, p), p), scale(right, -1, p), p)


def main():
    fixtures = []
    polynomial_challenges = uniqueness_checks = line_checks = 0
    rng = random.Random(16092026)
    for p, degree, kind, jet_degree, height, r_degree in [
        (7, 2, 'two_solution', 2, 0, 2),
        (7, 3, 'two_solution', 2, 0, 3),
        (7, 2, 'three_solution', 3, 0, 2),
        (7, 3, 'three_solution', 3, 0, 3),
        (7, 2, 'moving_riccati', 2, 1, 3),
        (11, 2, 'moving_riccati', 2, 1, 3),
        (7, 2, 'rank_drop', 2, 1, 0),
    ]:
        xs, by_label = list(range(p)), {}
        for z in range(p):
            r, a = equation(kind, degree, z, p)
            solutions = []
            for coeffs in itertools.product(range(p), repeat=degree+1):
                polynomial_challenges += 1
                candidate = trim(coeffs)
                if residual(candidate, r, a, p) == [0]:
                    solutions.append(candidate)
            by_label[z] = solutions
            if r != [0]:
                for x in xs:
                    if evaluate(r, x, p):
                        values = [evaluate(c, x, p) for c in solutions]
                        assert len(values) == len(set(values))
                        uniqueness_checks += len(values)
            if kind == 'two_solution':
                assert sorted(solutions) == sorted([[0], locator(list(range(degree)), p)])
            if kind == 'three_solution':
                w = locator(list(range(degree)), p)
                assert sorted(solutions) == sorted([[0], w, scale(w, 2, p)])
        threshold = max(degree, r_degree)+1
        tau = max(0, 2*degree-3)
        b = 1+tau*(jet_degree-1)
        k = height+jet_degree*(b+tau*height)
        q = jet_degree+height
        bound = (height + q*k*((p-degree)/(threshold-degree) +
                 3*p/(threshold-r_degree)) + 2*p*p/(threshold-r_degree))
        bad_counts = []
        lines = [([rng.randrange(p) for _ in xs], [rng.randrange(p) for _ in xs])
                 for _ in range(16)]
        # Lines anchored at actual solutions exercise persistent supports too.
        for candidate in by_label[0][:3]:
            f = [evaluate(candidate, x, p) for x in xs]
            lines.append((f, [0]*p))
            g = [0]*p
            g[-1] = 1
            lines.append((f, g))
        for f, g in lines:
            bad_labels = set()
            for z, solutions in by_label.items():
                nearby = []
                for candidate in solutions:
                    support = [i for i, x in enumerate(xs)
                               if evaluate(candidate, x, p) == (f[i]+z*g[i]) % p]
                    if len(support) >= threshold:
                        nearby.append(candidate)
                        if bad_support(xs, g, support, degree, p):
                            bad_labels.add(z)
                r, _ = equation(kind, degree, z, p)
                if r != [0]:
                    actual_r = sum(evaluate(r, x, p) == 0 for x in xs)
                    assert len(nearby)*(threshold-actual_r) <= p-actual_r
            assert len(bad_labels) <= bound
            bad_counts.append(len(bad_labels))
            line_checks += 1
        fixtures.append(dict(p=p, degree=degree, kind=kind,
                             solutions_per_label=[len(by_label[z]) for z in range(p)],
                             received_lines=len(lines), maximum_bad_labels=max(bad_counts)))

    lower = []
    for s, p in [(1, 17), (2, 29), (3, 37), (4, 53), (8, 97)]:
        n, degree, threshold = 12*s, 3*s, 6*s
        xs = list(range(n))
        w = locator(xs[:degree], p)
        f, g = [0]*n, [0]*n
        for i in range(6*s, 9*s):
            f[i] = evaluate(w, xs[i], p)
        for j, i in enumerate(range(9*s, n), 1):
            value = evaluate(w, xs[i], p)
            f[i], g[i] = 3*j*value % p, value
        expected = {(c-3*j) % p for c in (0, 1) for j in range(1, 3*s+1)}
        assert len(expected) == n//2
        bad_labels = set()
        for z in range(p):
            for c in (0, 1):
                candidate = scale(w, c, p)
                r, a = equation('two_solution', degree, z, p)
                assert residual(candidate, r, a, p) == [0]
                support = [i for i, x in enumerate(xs)
                           if evaluate(candidate, x, p) == (f[i]+z*g[i]) % p]
                assert threshold <= len(support) <= threshold+1
                if bad_support(xs, g, support, degree, p):
                    bad_labels.add(z)
        assert bad_labels == expected
        lower.append(dict(s=s, p=p, n=n, degree=degree, threshold=threshold,
                          bad_labels=len(bad_labels)))

    # Implicit first-order examples exercise the stronger local theorem,
    # including actual surfaces and separants that depend on the solution.
    implicit = []
    for kind, height in [('parabola', 0), ('moving_parabola', 1), ('two_slopes', 2)]:
        p, degree, n, threshold, jet_degree = 7, 2, 7, 4, 2
        xs = list(range(n))
        by_label = {}
        for z in range(p):
            solutions = []
            for coeffs in itertools.product(range(p), repeat=degree+1):
                polynomial_challenges += 1
                candidate = trim(coeffs)
                deriv = derivative(candidate, p)
                if kind == 'parabola':
                    q_value = add(mul(deriv, deriv, p), scale(candidate, -4, p), p)
                elif kind == 'moving_parabola':
                    q_value = add(mul(deriv, deriv, p), scale(add(candidate, [z], p), -4, p), p)
                else:
                    q_value = add(mul(deriv, deriv, p), [-z*z % p], p)
                if q_value == [0]:
                    solutions.append((candidate, scale(deriv, 2, p)))
            by_label[z] = solutions
        if kind in ('parabola', 'moving_parabola'):
            assert all(len(v) == p+1 for v in by_label.values())
        else:
            assert len(by_label[0]) == p
            assert all(len(by_label[z]) == 2*p for z in range(1, p))
        tau = max(0, 2*degree-3)
        t0 = 1+tau*(jet_degree-1+height)
        k, q = height+jet_degree*t0, jet_degree+height
        local_bound = q*k+q*t0*(n-degree)/(threshold-degree)+q*n
        positive_cases = 0
        for _ in range(24):
            f = [rng.randrange(p) for _ in xs]
            g = [rng.randrange(p) for _ in xs]
            witnesses, coordinate_labels = {}, [set() for _ in xs]
            for z, solutions in by_label.items():
                for candidate, separant in solutions:
                    support = [i for i, x in enumerate(xs)
                               if evaluate(candidate, x, p) == (f[i]+z*g[i]) % p]
                    if len(support) < threshold or not bad_support(xs, g, support, degree, p):
                        continue
                    nonsingular = [i for i in support if evaluate(separant, xs[i], p)]
                    witnesses.setdefault(z, []).append(nonsingular)
                    for i in nonsingular:
                        coordinate_labels[i].add(z)
            assert all(len(v) <= local_bound for v in coordinate_labels)
            for ell in range(1, threshold+1):
                labels = {z for z, lists in witnesses.items() if any(len(v) >= ell for v in lists)}
                assert len(labels)*ell <= n*local_bound
                # Direct double count on one witness per label, independently
                # of the large universal constant in the theorem.
                selected = [next(v for v in witnesses[z] if len(v) >= ell) for z in labels]
                incidences = sum(map(len, selected))
                assert len(labels)*ell <= incidences <= sum(map(len, coordinate_labels))
                positive_cases += bool(labels)
            line_checks += 1
        implicit.append(dict(kind=kind, p=p, degree=degree,
                             solutions_per_label=[len(by_label[z]) for z in range(p)],
                             received_lines=24, nonempty_label_threshold_cases=positive_cases))

    # Without p>D, P'=0 admits 0 and X^p with the same value at zero.
    p = 3
    frobenius = [0]*p+[1]
    assert derivative(frobenius, p) == [0] and evaluate(frobenius, 0, p) == 0
    result = dict(status='PASS', fixtures=fixtures,
                  polynomial_challenges=polynomial_challenges,
                  nonsingular_value_uniqueness_checks=uniqueness_checks,
                  received_lines=line_checks, sharp_linear_lower_fixtures=lower,
                  implicit_first_order_fixtures=implicit,
                  characteristic_negative_control=True,
                  scope='Finite checks of uniqueness, lists, classified examples, full '
                        'agreement supports, and the sharp linear family. These do not '
                        'replace the algebraic-geometric proof of the uniform theorem.')
    temporary = BASE/'verification.tmp'
    temporary.write_text(json.dumps(result, indent=2)+'\n')
    temporary.replace(BASE/'verification.json')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
