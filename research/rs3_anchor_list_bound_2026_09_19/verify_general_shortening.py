#!/usr/bin/env python3
"""Exact formula/cell audit; no anchor-count or field scan."""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

import sympy as sp


def main():
    n, D, T, j = sp.symbols("n D T j")
    delta = (T - j) ** 2 - (D - j) * (n - j)
    affine = T * T - D * n + j * (n + D - 2 * T)
    assert sp.expand(delta - affine) == 0
    assert sp.expand((n - j) * (T - D) - delta - (T - j) * (n - T)) == 0
    one_anchor = (n / T) * (n - 1) * (T - 2) / delta.subs({D: 2, j: 1})
    previous = n * (n - 1) * (T - 2) / (T * ((T - 1) ** 2 - (n - 1)))
    assert sp.cancel(one_anchor - previous) == 0

    cells = []
    nv, dv = 262144, 131071
    for tv, expected_j in ((181275, 48879), (181284, 48801)):
        deficit = dv * nv - tv * tv
        slope = nv + dv - 2 * tv
        assert deficit > 0 and slope > 0 and dv < tv <= nv
        jmin = deficit // slope + 1
        assert jmin == expected_j and 1 <= jmin <= dv
        before = -deficit + (jmin - 1) * slope
        after = -deficit + jmin * slope
        assert before <= 0 < after
        square_gap = nv * nv - 2 * tv * tv
        assert square_gap > 0
        factor = Fraction((nv - jmin) * (tv - dv), after)
        assert factor > 1
        cells.append({
            "n": nv,
            "degree_bound_D": dv,
            "dimension": dv + 1,
            "agreement_T": tv,
            "Dn_minus_T_squared": deficit,
            "denominator_slope": slope,
            "minimum_admissible_j": jmin,
            "denominator_at_previous_j": before,
            "denominator_at_minimum_j": after,
            "n_squared_minus_2T_squared": square_gap,
            "Johnson_factor_at_minimum_j": str(factor),
            "all_admissible_j_bound_log2_strictly_greater_than": str(Fraction(jmin, 2)),
        })

    here = Path(__file__).resolve().parent
    result = {
        "status": "PASS",
        "scope": "Two frozen cells; no claim about current website parameters.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "sympy_version": sp.__version__,
        "formula": "binom(n,j)/binom(T,j)*(n-j)*(T-D)/((T-j)^2-(D-j)*(n-j))",
        "hypotheses": "0<=j<=D<T<=n; denominator>0; integer parameters; distinct coordinates",
        "symbolic_checks": {
            "denominator_affine_identity": True,
            "Johnson_factor_at_least_one_identity": True,
            "RS3_one_anchor_specialization": True,
        },
        "cells": cells,
        "conclusion": "Every admissible displayed bound exceeds 2^24400; this formula does not improve the practical benchmark.",
    }
    output = here / "general_shortening_receipt.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "receipt": str(output), "cells": cells}, indent=2))


if __name__ == "__main__":
    main()
