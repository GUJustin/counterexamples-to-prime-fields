#!/usr/bin/env python3
"""Exact classification and degree-section checks for quadratic powers."""
import itertools
import json
from pathlib import Path
from poly import add, mul, scale, deriv, trim, eval_poly


def power(P, e, p):
    out = [1]
    for _ in range(e):
        out = mul(out, P, p)
    return out


def equation(P, e, p):
    P1 = deriv(P, p)
    P2 = deriv(P1, p)
    P3 = deriv(P2, p)
    return add(add(scale(mul(mul(P, P, p), P3, p), e*e, p),
                   scale(mul(mul(P, P1, p), P2, p), 3*e*(1-e), p), p),
               scale(mul(mul(P1, P1, p), P1, p), (1-e)*(1-2*e), p), p)


def run():
    records = []
    tested = 0
    solutions = 0
    for p, e in [(5, 1), (7, 2), (11, 2), (7, 3)]:
        expected = set()
        for degree in range(3):
            for coeffs in itertools.product(range(p), repeat=degree):
                H = list(coeffs)+[1]
                expected.add(tuple(power(H, e, p)))
        found = set()
        for degree in range(2*e+1):
            for coeffs in itertools.product(range(p), repeat=degree):
                P = list(coeffs)+[1]
                tested += 1
                if equation(P, e, p) == [0]:
                    found.add(tuple(P))
        assert found == expected
        assert len(found) == 1+p+p*p
        solutions += len(found)
        records.append({"p": p, "e": e, "degree_cap": 2*e,
                        "monic_solutions": len(found)})
    sections = []
    for p, e in [(101, 2), (101, 4), (101, 5), (101, 10), (101, 20),
                 (1009, 3), (1009, 6), (1009, 8), (1009, 12), (1009, 24)]:
        assert p>2*e and (p-1) % e == 0
        roots = [a for a in range(1, p) if pow(a, e, p) == 1]
        assert len(roots) == e
        polys = set()
        for u, v in itertools.product(roots, repeat=2):
            # Interpolate H(0)=u, H(1)=1, H(2)=v.
            a = (u+v-2)*pow(2, -1, p) % p
            b = (1-u-a) % p
            H = trim([u, b, a])
            P = power(H, e, p)
            assert all(eval_poly(P, x, p) == 1 for x in (0, 1, 2))
            assert equation(P, e, p) == [0]
            assert e*pow(u, e-1, p) % p and e*pow(v, e-1, p) % p
            polys.add(tuple(P))
        assert len(polys) == e*e
        sections.append({"p": p, "e": e, "reduced_section_points": len(polys)})
    result = {"status": "PASS", "monic_polynomials_checked": tested,
              "classified_solutions": solutions, "classification_fixtures": records,
              "degree_sections": sections,
              "scope": "Classification and e-squared proper reduced sections; no nearby-line or MCA lower bound."}
    Path(__file__).with_name("quadratic_power_family_verification.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ("classification_fixtures", "degree_sections")}, indent=2))


if __name__ == "__main__":
    run()
