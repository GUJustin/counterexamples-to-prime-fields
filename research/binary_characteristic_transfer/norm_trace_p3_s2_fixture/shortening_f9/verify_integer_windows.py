#!/usr/bin/env python3
"""Exact first-order/strict-Johnson window check at lengths 9 and 27."""

from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path


def verify_length(n):
    rows = [dict(k=1, no_nonnegative_threshold_strictly_below_johnson=True)]
    for k in range(2, n):
        maximum = isqrt(n * (k - 1) - 1)
        rho, alpha = Fraction(k, n), Fraction(maximum, n)
        # Since 11-rho is positive, this is exactly rho >= 11-3sqrt(13).
        high_branch = (11-rho)**2 <= 117
        row = dict(k=k, largest_integer_strictly_below_johnson=maximum)
        if high_branch:
            value = (8-rho)*alpha**2-6*rho*alpha+rho*(4*rho-5)
            assert value < 0
            row.update(branch="high", first_order_polynomial=str(value))
        elif alpha**2 <= rho/2:
            # The full low branch strictly exceeds sqrt(rho/2).
            row.update(
                branch="low",
                comparison="alpha <= sqrt(rho/2) < a1(rho)",
                leading_squared_slack=str(rho/2-alpha**2),
            )
        else:
            # Let b=sqrt(rho/2), u0=alpha/b-1 > 0.
            # u0^2(u0+3)<b is equivalent to rho*b < R below.
            R = rho**2/4-alpha**3+3*alpha*rho/2
            square_slack = R**2-rho**3/2
            assert R > 0 and square_slack > 0
            row.update(
                branch="low",
                comparison="u0^2(u0+3) < sqrt(rho/2)",
                positive_rational_side=str(R),
                positive_squared_slack=str(square_slack),
            )
        row["maximal_threshold_strictly_below_first_order"] = True
        rows.append(row)
    return dict(
        length=n,
        dimensions_checked=list(range(1, n)),
        rows=rows,
        integer_windows_above_first_order_and_strictly_below_johnson=0,
    )


def main():
    reports = [verify_length(n) for n in (9, 27)]
    expected_n9 = [
        (2, 2, "-602/729"), (3, 4, "-145/243"),
        (4, 5, "-424/729"), (5, 5, "-800/729"),
        (6, 6, "-26/27"), (7, 7, "-532/729"),
        (8, 7, "-824/729"),
    ]
    actual_n9 = [
        (row["k"], row["largest_integer_strictly_below_johnson"],
         row["first_order_polynomial"])
        for row in reports[0]["rows"][1:]
    ]
    assert actual_n9 == expected_n9
    output = dict(
        pass_all_checks=True,
        arithmetic="exact integers and rational numbers only",
        strict_dimension_convention="degree < k",
        finite_johnson_threshold="sqrt(n*(k-1))",
        branch_boundary="11-3sqrt(13)",
        reports=reports,
        full_dimension_note="k=n is the full ambient code and cannot have far sources",
        scope=(
            "a parameter obstruction for any construction at lengths 9 and 27; "
            "not a statement about other lengths or thresholds outside this window"
        ),
        verifier_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    )
    path = Path(__file__).with_name("integer_windows.json")
    path.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
