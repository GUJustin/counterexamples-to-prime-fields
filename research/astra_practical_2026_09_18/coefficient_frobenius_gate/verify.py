#!/usr/bin/env python3
"""Actual-prime sextic checks and finite ledger for coefficient Frobenius."""

import json
import math
from pathlib import Path


P = 2130706433
ZERO = (0,) * 6
ONE = (1, 0, 0, 0, 0, 0)
ALPHA = (0, 1, 0, 0, 0, 0)


def trim(v):
    while len(v) > 1 and v[-1] == 0:
        v.pop()
    return v


def gcd_fp(a, b):
    a, b = trim(a[:]), trim(b[:])
    while b != [0]:
        r = a[:]
        inv = pow(b[-1], -1, P)
        while len(r) >= len(b) and r != [0]:
            t, scale = len(r) - len(b), r[-1] * inv % P
            for i, value in enumerate(b):
                r[t + i] = (r[t + i] - scale * value) % P
            trim(r)
        a, b = b, r
    return [x * pow(a[-1], -1, P) % P for x in a]


class Extension:
    def __init__(self, constant):
        self.c = constant

    @staticmethod
    def base(x):
        return (x % P, 0, 0, 0, 0, 0)

    @staticmethod
    def add(a, b):
        return tuple((x + y) % P for x, y in zip(a, b))

    @staticmethod
    def neg(a):
        return tuple(-x % P for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    @staticmethod
    def scale(a, c):
        return tuple(x * c % P for x in a)

    def mul(self, a, b):
        out = [0] * 11
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i + j] += x * y
        for j in range(10, 5, -1):
            value = out[j] % P
            out[j - 6] -= self.c * value
            out[j - 4] -= value
        return tuple(x % P for x in out[:6])

    def power(self, a, n):
        out = ONE
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out

    def inverse(self, a):
        assert a != ZERO
        answer = self.power(a, P ** 6 - 2)
        assert self.mul(answer, a) == ONE
        return answer

    def div(self, a, b):
        return self.mul(a, self.inverse(b))

    def product(self, values):
        answer = ONE
        for value in values:
            answer = self.mul(answer, value)
        return answer

    def polynomial(self, coefficients, value):
        answer = ZERO
        for c in reversed(coefficients):
            answer = self.add(self.mul(answer, value), c)
        return answer


def select_field():
    for constant in range(1, 65):
        field = Extension(constant)
        conjugates = [ALPHA]
        for _ in range(6):
            conjugates.append(field.power(conjugates[-1], P))
        minimal = [constant, 0, 1, 0, 0, 0, 1]
        if conjugates[6] != ALPHA:
            continue
        checks = [gcd_fp(minimal, list(field.sub(conjugates[j], ALPHA)))
                  for j in [2, 3]]
        if checks == [[1], [1]]:
            assert conjugates[3] == field.neg(ALPHA)
            return field, conjugates[:6]
    raise AssertionError("No irreducible candidate in the stated bound")


def polynomial_fp(roots):
    coefficients = [1]
    for x in roots:
        coefficients.append(0)
        for j in range(len(coefficients) - 1, 0, -1):
            coefficients[j] = (coefficients[j] - x * coefficients[j - 1]) % P
    return list(reversed(coefficients))


def finite_checks(field, conjugates):
    for b in range(2, 100):
        zeta = pow(b, (P - 1) // 32, P)
        if pow(zeta, 16, P) != 1:
            break
    assert pow(zeta, 32, P) == 1
    nodes = [pow(zeta, j, P) for j in range(32)]
    tags = [pow(zeta, 2 * j, P) for j in range(16)]
    records = []
    for d in [1, 2, 3, 6]:
        r = 6 // d
        orbit = [conjugates[d * i] for i in range(r)]
        basis = [field.power(conjugates[d % 6], j) for j in range(6)]

        def tau(value):
            result = ZERO
            for c, v in zip(value, basis):
                result = field.add(result, field.scale(v, c))
            return result

        def raw_trace(value):
            result, current = ZERO, value
            for _ in range(r):
                result, current = field.add(result, current), tau(current)
            return result

        gamma = None
        for j in range(6):
            candidate = raw_trace(field.power(ALPHA, j))
            if candidate != ZERO and (d == 1 or any(candidate[1:])):
                gamma = candidate
                break
        assert gamma is not None and tau(gamma) == gamma
        extra = tags[1:r]
        selected = tags[r:r + 9]
        assert len(selected) == 9 and set(extra).isdisjoint(selected)
        weights = []
        for i, root in enumerate(orbit):
            numerator = field.product(field.sub(root, field.base(x)) for x in extra)
            derivative = field.product(field.sub(root, other)
                                       for j, other in enumerate(orbit) if i != j)
            weights.append(field.div(numerator, derivative))

        def linearized(value):
            result, current = ZERO, value
            for weight in weights:
                result = field.add(result, field.mul(weight, current))
                current = tau(current)
            return result

        # P0(alpha)=gamma, so delta(Y)=Y*P0(Y) has delta(alpha)=alpha*gamma.
        p0 = list(gamma) + [1]
        p0[0] = (p0[0] + field.c) % P
        p0[2] = (p0[2] + 1) % P
        assert field.polynomial([field.base(x) for x in p0], ALPHA) == gamma
        divided = [field.base(x) for x in p0]
        divided[0] = field.sub(divided[0], gamma)
        q = [ZERO] * 6
        q[-1] = divided[-1]
        for j in range(4, -1, -1):
            q[j] = field.add(divided[j + 1], field.mul(ALPHA, q[j + 1]))
        assert field.add(divided[0], field.mul(ALPHA, q[0])) == ZERO
        q_after = [linearized(c) for c in q]
        matches = 0
        locator = polynomial_fp(selected)
        for x in nodes:
            y = x * x % P
            ey, R = field.base(y), field.base(x - 1)
            vu = field.polynomial([field.base(c) for c in locator], ey)
            delta = field.mul(ey, field.polynomial([field.base(c) for c in p0], ey))
            v0 = field.add(vu, delta)
            pole = field.sub(ey, ALPHA)
            f = field.div(field.mul(R, v0), field.mul(ey, pole))
            g = field.neg(field.div(R, pole))
            F, G = linearized(f), linearized(g)
            H = field.mul(R, field.polynomial(q_after, ey))
            residual = field.sub(field.add(F, field.mul(gamma, G)), H)
            cvalue = field.product(field.sub(ey, field.base(c)) for c in extra)
            normvalue = field.product(field.sub(ey, a) for a in orbit)
            expected = field.div(field.mul(field.mul(R, vu), cvalue),
                                 field.mul(ey, normvalue))
            assert residual == expected
            assert tau(F) == F and tau(G) == G and tau(H) == H
            assert linearized(field.mul(gamma, f)) == field.mul(gamma, F)
            matches += residual == ZERO
        assert matches == 1 + 2 * (9 + r - 1)
        records.append({"subfield_degree": d, "relative_degree": r,
                        "extra_packets": r - 1, "domain_length": 32,
                        "row_dimension": 16, "witness_degree_upper": 11,
                        "exact_agreements": matches,
                        "far_direction_agreement_upper": 15 + 2 * r,
                        "nonbase_label": any(gamma[1:])})
    # Independent paired-support trace identities, with alpha^(p^3)=-alpha.
    a = field.mul(ALPHA, ALPHA)
    for y in tags:
        ey = field.base(y)
        z = field.mul(ey, ey)
        plus = field.inverse(field.mul(ey, field.sub(ey, ALPHA)))
        minus = field.inverse(field.mul(ey, field.add(ey, ALPHA)))
        symmetric = field.scale(field.add(plus, minus), pow(2, -1, P))
        antisymmetric = field.div(field.sub(plus, minus), field.scale(ALPHA, 2))
        assert symmetric == field.inverse(field.sub(z, a))
        assert antisymmetric == field.div(ey, field.mul(z, field.sub(z, a)))
    return records


def ledger():
    total = math.comb(255, 136)
    records = []
    for d in [1, 2, 3, 6]:
        r, head = 6 // d, 7 - 6 // d
        exponent = head + 6 - d
        denominator = 256 * P ** exponent
        fixed_denominator = denominator * P ** d
        records.append({"subfield_degree": d, "relative_degree": r,
                        "head_coordinates": head, "off_subfield_coordinates": 6 - d,
                        "total_field_coordinates": exponent,
                        "mean_fiber": total / denominator,
                        "guaranteed_supports": (total + denominator - 1) // denominator,
                        "guaranteed_fixed_word_list":
                            (total + fixed_denominator - 1) // fixed_denominator,
                        "challenge_subfield_size": str(P ** d),
                        "distinct_labels_not_automatically_certified": True})
    return records


if __name__ == "__main__":
    field, conjugates = select_field()
    result = {"status": "PASS", "prime": P,
              "irreducible_polynomial": f"X^6+X^2+{field.c}",
              "irreducibility": "Rabin: Frobenius^6 identity; gcd tests at powers2,3",
              "alpha_frobenius_cubed_equals_negative_alpha": True,
              "relative_trace_compilers": finite_checks(field, conjugates),
              "practical_ledger": ledger()}
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "prime": P,
                      "irreducible_polynomial": result["irreducible_polynomial"],
                      "relative_trace_compilers": len(result["relative_trace_compilers"]),
                      "actual_prime_domain_points_per_fixture": 32,
                      "output": str(output)}))
