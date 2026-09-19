#!/usr/bin/env python3
"""A fixed exact RS embedding of the 17-root multiplicative grid.

This checks only the stated bank, not all p^3 quadratics, and does not
claim the external subgroup theorem's unspecified onset at t=17.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations_with_replacement
from math import isqrt
from pathlib import Path
import json
import sympy as sp


def evaluate(coefficients, x, p):
    a, b, c = coefficients
    return (a * x * x + b * x + c) % p


def main():
    p, t = 131071, 17
    assert all(p % a for a in range(2, isqrt(p) + 1))
    assert all(t % a for a in range(2, isqrt(t) + 1))
    assert pow(2, t, p) == 1 and 2 != 1
    H = sorted({pow(2, j, p) for j in range(t)})
    assert len(H) == t and all(pow(a, t, p) == 1 for a in H)
    assert (p - 1) not in H

    coordinates = []
    seen_x = set()
    for u, v in combinations_with_replacement(H, 2):
        x, value = (u + v) % p, u * v % p
        assert x != 0 and x not in seen_x
        seen_x.add(x)
        coordinates.append({"x": x, "value": value, "pair": [u, v]})
    coordinates.sort(key=lambda item: item["x"])
    n = len(coordinates)
    assert n == t * (t + 1) // 2 == 153

    bank = []
    for a in H:
        bank.append({"family": "row", "parameter": a, "coefficients": [0, a, -a * a % p]})
    for a in H:
        bank.append({"family": "product", "parameter": a, "coefficients": [0, 0, a]})
    ratio_parameters = {}
    for zeta in H:
        coefficient = zeta * pow((1 + zeta) ** 2 % p, -1, p) % p
        ratio_parameters.setdefault(coefficient, []).append(zeta)
    assert len(ratio_parameters) == (t + 1) // 2 == 9
    for coefficient, parameters in sorted(ratio_parameters.items()):
        assert len(parameters) in (1, 2)
        if len(parameters) == 1:
            assert parameters == [1]
        else:
            assert parameters[0] * parameters[1] % p == 1
        bank.append({"family": "ratio", "parameters": parameters, "coefficients": [coefficient, 0, 0]})
    assert len(bank) == (5 * t + 1) // 2 == 43
    assert len({tuple(item["coefficients"]) for item in bank}) == len(bank)

    owners = {item["x"]: [] for item in coordinates}
    by_family = {}
    for index, item in enumerate(bank):
        matches = [point["x"] for point in coordinates if evaluate(item["coefficients"], point["x"], p) == point["value"]]
        expected = (t + 1) // 2 if item["family"] == "product" else t
        assert len(matches) == expected
        item["agreement"] = len(matches)
        item["matching_coordinates"] = matches
        by_family.setdefault(item["family"], []).append(len(matches))
        for x in matches:
            owners[x].append(index)

    for point in coordinates:
        u, v = point["pair"]
        assert len(owners[point["x"]]) == (3 if u == v else 4)
        assert len(owners[point["x"]]) <= 4
    owner_histogram = dict(sorted(Counter(map(len, owners.values())).items()))
    assert owner_histogram == {3: 17, 4: 136}
    total_incidences = sum(item["agreement"] for item in bank)
    assert total_incidences == sum(map(len, owners.values())) == 595

    # Four explicitly selected bank points have three independent differences.
    inverse_four = pow(4, -1, p)
    affine_basis = [(0, 0, 1), (0, 0, 2), (inverse_four, 0, 0), (0, 1, p - 1)]
    coefficient_set = {tuple(item["coefficients"]) for item in bank}
    assert all(a in coefficient_set for a in affine_basis)
    difference_matrix = sp.Matrix([
        [(v - u) % p for u, v in zip(affine_basis[0], row)]
        for row in affine_basis[1:]
    ])
    affine_determinant = int(difference_matrix.det()) % p
    assert affine_determinant != 0

    # General formal identities used in the obstruction note.
    u, v, y, a, b, c, zeta = sp.symbols("u v y a b c zeta")
    F = u * v - a * (u + v) ** 2 - b * (u + v) - c
    inverted = u * v - a * (u + v) ** 2 - b * u * v * (u + v) - c * u ** 2 * v ** 2
    assert sp.cancel(u ** 2 * v ** 2 * F.subs({u: 1 / u, v: 1 / v}, simultaneous=True) - inverted) == 0
    monomial_pullback = u * y - b * u ** 2 - b * y - c * u
    assert sp.expand(u * F.subs(a, 0).subs(v, y / u) - monomial_pullback) == 0
    assert sp.expand(F.subs({a: 0, c: -b ** 2}) - (u - b) * (v - b)) == 0
    assert sp.expand(F.subs(v, zeta * u) - ((zeta - a * (1 + zeta) ** 2) * u ** 2 - b * (1 + zeta) * u - c)) == 0
    xi = sp.symbols("xi")
    assert sp.expand(zeta * (1 + xi) ** 2 - xi * (1 + zeta) ** 2 - (zeta - xi) * (1 - zeta * xi)) == 0

    fixture = {"p": p, "t": t, "subgroup": H, "coordinates": coordinates, "bank": bank}
    base = Path(__file__).parent
    fixture_text = json.dumps(fixture, indent=2, sort_keys=True) + "\n"
    (base / "fixture.json").write_text(fixture_text)
    receipt = {
        "status": "PASS",
        "scope": "One fixed canonical-bank embedding; not an all-quadratic list census",
        "p": p, "prime_trial_division_limit": isqrt(p),
        "subgroup_generator": 2, "subgroup_order": t,
        "length_n": n, "bank_size": len(bank),
        "family_agreement_histograms": {name: dict(sorted(Counter(values).items())) for name, values in by_family.items()},
        "owner_histogram": owner_histogram, "total_incidences": total_incidences,
        "affine_coefficient_dimension": 3, "affine_basis": affine_basis,
        "affine_difference_determinant_mod_p": affine_determinant,
        "generic_algebraic_identities_verified": ["double inversion", "product monomial change", "row factorization", "ratio component", "ratio coefficient deduplication"],
        "external_size_condition_16t4_le_p3": 16 * t ** 4 <= p ** 3,
        "external_theorem_c0_onset_verified": False,
        "fixture_sha256": sha256(fixture_text.encode()).hexdigest(),
    }
    (base / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
