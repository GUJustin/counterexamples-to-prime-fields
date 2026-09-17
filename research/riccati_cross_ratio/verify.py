"""Exact Riccati solution, cross-ratio, collision, and incidence checks."""
import importlib.util
import itertools
import json
from pathlib import Path
import random

BASE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'first_order_helpers', BASE.parent/'quasilinear_first_order'/'verify.py')
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
add, mul, scale = h.add, h.mul, h.scale
trim, evaluate, derivative = h.trim, h.evaluate, h.derivative


def subtract(a, b, p):
    return add(a, scale(b, -1, p), p)


def divide(a, b, p):
    a, b = trim(a), trim(b)
    assert b != [0]
    quotient = [0]*max(1, len(a)-len(b)+1)
    inverse = pow(b[-1], -1, p)
    while a != [0] and len(a) >= len(b):
        index, coefficient = len(a)-len(b), a[-1]*inverse % p
        quotient[index] = coefficient
        a = subtract(a, [0]*index+scale(b, coefficient, p), p)
    return trim(quotient), a


def equation_from_pencil(u, v, g, shift, p):
    w = subtract(u, v, p)
    n = mul(g, mul(u, v, p), p)
    a = mul(w, n, p)
    b1 = subtract(mul(w, derivative(n, p), p), mul(n, derivative(w, p), p), p)
    b2 = subtract(mul(derivative(u, p), v, p), mul(u, derivative(v, p), p), p)
    assert a != [0] and b2 != [0]
    b0 = add(subtract(mul(a, derivative(shift, p), p), mul(b1, shift, p), p),
             mul(b2, mul(shift, shift, p), p), p)
    shifted_b1 = subtract(b1, scale(mul(b2, shift, p), 2, p), p)
    return a, b0, shifted_b1, b2


def residual(candidate, equation, p):
    a, b0, b1, b2 = equation
    right = add(b0, add(mul(b1, candidate, p), mul(b2, mul(candidate, candidate, p), p), p), p)
    return subtract(mul(a, derivative(candidate, p), p), right, p)


def cross_ratio(polys, p):
    p0, p1, p2, p3 = polys
    numerator = mul(subtract(p3, p0, p), subtract(p2, p1, p), p)
    denominator = mul(subtract(p2, p0, p), subtract(p3, p1, p), p)
    assert numerator != [0] and denominator != [0]
    index = next(i for i, x in enumerate(denominator) if x)
    constant = numerator[index]*pow(denominator[index], -1, p) % p if index < len(numerator) else 0
    return numerator == scale(denominator, constant, p), constant, numerator, denominator


def check_collisions(candidates, p):
    m, count = len(candidates), 0
    for x in range(p):
        frequencies = {}
        for candidate in candidates:
            value = evaluate(candidate, x, p)
            frequencies[value] = frequencies.get(value, 0)+1
        assert max(frequencies.values()) == 1 or max(frequencies.values()) >= m-1
        count += 1
    return count


def check_sharp_lists():
    fixtures = []
    for m, p in [(3, 7), (3, 13), (3, 31), (4, 17), (4, 41),
                 (5, 31), (5, 101), (6, 37), (8, 97)]:
        assert all(p % d for d in range(2, int(p**0.5)+1))
        assert (p-1) % (2*m) == 0
        s = (p-1)//(2*m)
        image = sorted({pow(x, s, p) for x in range(1, p)})
        assert len(image) == 2*m
        roots, extra = image[:m], image[m:]
        r = h.locator(roots, p)
        monomial = [0]*(m-1)+[1]
        cs = []
        for root in roots:
            quotient, remainder = divide(r, [-root % p, 1], p)
            assert remainder == [0]
            cs.append(subtract(quotient, monomial, p))
        def compose(poly):
            out = [0]*((len(poly)-1)*s+1)
            for i, c in enumerate(poly):
                out[i*s] = c
            return trim(out)
        # R C' = R' C - C^2 - 2 T C + R'T - T^2 - RT'.
        b0 = subtract(subtract(mul(derivative(r, p), monomial, p),
                               mul(monomial, monomial, p), p),
                      mul(r, derivative(monomial, p), p), p)
        b1 = subtract(derivative(r, p), scale(monomial, 2, p), p)
        jacobian = [0]*(s-1)+[s % p]
        eq = (compose(r), mul(jacobian, compose(b0), p),
              mul(jacobian, compose(b1), p), scale(jacobian, -1, p))
        candidates = [compose(c) for c in cs]
        n, degree, agreement = p-1, (m-2)*s, m*s
        assert p > 2*degree
        assert len({tuple(c) for c in candidates}) == m
        assert all(len(c)-1 <= degree and residual(c, eq, p) == [0]
                   for c in candidates)
        word = {}
        for x in range(1, p):
            y = pow(x, s, p)
            word[x] = (-pow(y, m-1, p)) % p if y in roots else evaluate(cs[extra.index(y)], y, p)
        counts = [sum(evaluate(c, x, p) == word[x] for x in word) for c in candidates]
        assert counts == [agreement]*m
        assert m*(agreement-degree) == n
        for y in extra:
            assert len({evaluate(c, y, p) for c in cs}) == m
        fixtures.append(dict(p=p, M=m, s=s, n=n, D=degree, A=agreement,
                             agreements=counts, exact_equality=True))
    return fixtures


def main():
    rng = random.Random(160920261947)
    cases = []
    for p, degree in [(7, 2), (7, 3), (11, 3)]:
        a = h.locator(list(range(degree+1)), p)
        shift = trim([1, p-1]+[0]*(degree-2)+[1])
        b1, b2 = derivative(a, p), [p-1]
        b0 = subtract(subtract(mul(a, derivative(shift, p), p), mul(b1, shift, p), p),
                      mul(shift, shift, p), p)
        shifted_b1 = add(b1, scale(shift, 2, p), p)
        expected = [shift]
        for root in range(degree+1):
            quotient, remainder = divide(a, [-root % p, 1], p)
            assert remainder == [0]
            expected.append(add(shift, quotient, p))
        cases.append((f'sharp_shifted_D{degree}_p{p}', p, degree,
                      (a, b0, shifted_b1, b2), expected))
    for p, degree in [(7, 3), (11, 4)]:
        u, v = [0, 1], [1, 2]
        g = mul(add(scale(u, 3, p), scale(v, -2, p), p),
                add(scale(u, 4, p), scale(v, -3, p), p), p)
        cases.append((f'constant_denominator_D{degree}', p, degree,
                      equation_from_pencil(u, v, g, [0], p), None))
    for i in range(8):
        p, degree = 7, 2
        while True:
            u = trim([rng.randrange(p) for _ in range(degree+1)])
            v = trim([rng.randrange(p) for _ in range(degree+1)])
            if (u != [0] and v != [0] and u != v and
                subtract(mul(derivative(u, p), v, p), mul(u, derivative(v, p), p), p) != [0]):
                break
        shift = trim([rng.randrange(p) for _ in range(degree+1)])
        cases.append((f'random_pencil_{i}', p, degree,
                      equation_from_pencil(u, v, [1], shift, p), None))

    results = []
    enumerated = cross_ratios = collision_coordinates = received_lines = 0
    ordinary_incidence_cases = nonempty_bad_lines = 0
    for name, p, degree, equation, expected in cases:
        assert p > 2*degree
        candidates = []
        for coefficients in itertools.product(range(p), repeat=degree+1):
            enumerated += 1
            candidate = trim(coefficients)
            if residual(candidate, equation, p) == [0]:
                candidates.append(candidate)
        assert 3 <= len(candidates) <= degree+2
        if expected is not None:
            assert sorted(candidates) == sorted(expected)
        for quadruple in itertools.combinations(candidates, 4):
            constant, value, _, _ = cross_ratio(quadruple, p)
            assert constant and value not in (0, 1)
            cross_ratios += 1
        collision_coordinates += check_collisions(candidates, p)
        xs = list(range(p))
        values = [[evaluate(c, x, p) for x in xs] for c in candidates]
        thresholds = range(degree+1, p+1)
        lines = [([rng.randrange(p) for _ in xs], [rng.randrange(p) for _ in xs])
                 for _ in range(32)]
        # Plant common values where they exist and distribute the other
        # coordinates across candidates, exercising lists of size >=3.
        for offset in range(2*len(candidates)):
            word, fresh = [], 0
            for x in xs:
                frequencies = {}
                for row in values:
                    frequencies[row[x]] = frequencies.get(row[x], 0)+1
                common, frequency = max(frequencies.items(), key=lambda item: item[1])
                if frequency >= 2:
                    word.append(common)
                else:
                    word.append(values[(fresh+offset) % len(candidates)][x])
                    fresh += 1
            lines.append((word, [0]*p))
        for row in values:
            lines.append((row, [0]*p))
            direction = [0]*p
            direction[-1] = 1
            lines.append((row, direction))
        for f, direction in lines:
            for threshold in thresholds:
                delta = threshold-degree
                bad_labels = set()
                persistent_counts = [sum(direction[x] == 0 and row[x] == f[x] for x in xs)
                                     for row in values]
                heavy = sum(2*(count-degree) >= delta for count in persistent_counts)
                assert heavy*delta <= 2*p
                for z in range(p):
                    supports = [[x for x in xs if row[x] == (f[x]+z*direction[x]) % p]
                                for row in values]
                    indices = [i for i, support in enumerate(supports) if len(support) >= threshold]
                    m = len(indices)
                    assert m*delta <= p
                    if m >= 3:
                        matches = [sum(x in supports[i] for i in indices) for x in xs]
                        high = [x for x, count in enumerate(matches) if count >= 2]
                        assert all(matches[x] >= m-1 for x in high)
                        assert len(high)*(m-2) <= degree*m
                        assert threshold*m <= p+(m-1)*len(high)
                        ordinary_incidence_cases += 1
                    for i in indices:
                        if h.bad_support(xs, direction, supports[i], degree, p):
                            bad_labels.add(z)
                assert len(bad_labels)*delta <= 2*p*(p+degree+2)
                nonempty_bad_lines += bool(bad_labels)
            received_lines += 1
        results.append(dict(name=name, p=p, degree=degree,
                            coefficient_degrees=[len(c)-1 for c in equation],
                            solutions=len(candidates), received_lines=len(lines)))

    # p>D alone does not make all cross ratios constant. At p=3,D=2,
    # U=1+X+X^2, V=X+X^2, W=1+X give a Frobenius cross ratio.
    p, degree = 3, 2
    u, v, w = [1, 1, 1], [0, 1, 1], [1, 1]
    equation = equation_from_pencil(u, v, [1], [0], p)
    negative = [[0], u, v, w]
    assert p > degree and p <= 2*degree
    assert all(residual(c, equation, p) == [0] for c in negative)
    is_constant, _, numerator, denominator = cross_ratio(negative, p)
    assert not is_constant
    derivative_numerator = subtract(mul(derivative(numerator, p), denominator, p),
                                    mul(numerator, derivative(denominator, p), p), p)
    assert derivative_numerator == [0]
    values_at_zero = [evaluate(c, 0, p) for c in negative]
    assert sorted(values_at_zero) == [0, 0, 1, 1]
    negative_all = [trim(c) for c in itertools.product(range(p), repeat=degree+1)
                    if residual(trim(c), equation, p) == [0]]

    assert len(negative_all) == 5 > degree+2
    sharp_lists = check_sharp_lists()
    result = dict(status='PASS', sharp_list_fixtures=sharp_lists, fixtures=results, polynomials_enumerated=enumerated,
                  constant_cross_ratios=cross_ratios, collision_coordinates=collision_coordinates,
                  received_lines=received_lines, ordinary_incidence_cases=ordinary_incidence_cases,
                  nonempty_bad_line_threshold_cases=nonempty_bad_lines,
                  characteristic_negative_control=dict(p=3, degree=2, values_at_zero=values_at_zero,
                      numerator=numerator, denominator=denominator,
                      total_bounded_degree_solutions=len(negative_all)),
                  scope='Exact bounded-degree classifications, cross-ratio constants, collision '
                        'structure, ordinary lists, and fixed-equation full-support incidences. '
                        'Finite checks supplement the proof; challenge-dependent MCA remains open.')
    temporary = BASE/'verification.tmp'
    temporary.write_text(json.dumps(result, indent=2)+'\n')
    temporary.replace(BASE/'verification.json')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
