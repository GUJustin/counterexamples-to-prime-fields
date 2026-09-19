#!/usr/bin/env python3
"""Symbolic verification of the single Lattes-Schwarzian candidate."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s


def schwarzian(value, variable):
    first = s.diff(value, variable)
    return s.cancel(s.diff(value, variable, 3)/first -
                    s.Rational(3, 2)*(s.diff(value, variable, 2)/first)**2)


x, a, b = s.symbols("x a b")
assert schwarzian((x-a)/(x-b), x) == 0

# Treat the cubic values and their first two derivatives as independent jets.
# F*Y'^2=G(Y), differentiated twice, fixes Y'' and Y'''.
F, F1, F2, G1, G2, u = s.symbols("F F1 F2 G1 G2 u", nonzero=True)
G = F*u*u
v = (G1 - F1*u)/(2*F)
w = (G2*u - F2*u - 3*F1*v)/(2*F)
schwarzian_jet = w/u - s.Rational(3, 2)*(v/u)**2
C_F = -F2/(2*F) + 3*F1**2/(8*F**2)
C_G = -G2/(2*G) + 3*G1**2/(8*G**2)
assert s.cancel(schwarzian_jet - (C_F-u*u*C_G)) == 0

# The double-pole coefficient, and the next Laurent coefficient, are universal.
t, A0, A1, A2, A3 = s.symbols("t A0 A1 A2 A3", nonzero=True)
pole = A0/t**2 + A1/t + A2 + A3*t
S_pole = schwarzian(pole, t)
double_coefficient = s.limit(t*t*S_pole, t, 0)
simple_coefficient = s.limit(t*(S_pole+s.Rational(3, 2)/t**2), t, 0)
assert double_coefficient == -s.Rational(3, 2)
assert s.simplify(simple_coefficient-3*A1/(2*A0)) == 0

# Independent fixed-degree residual ledger for the common connection term.
A, B = s.symbols("A B")
cubic = x**3 + A*x + B
connection_numerator = s.expand(3*s.diff(cubic,x)**2 -
                                4*cubic*s.diff(cubic,x,2))
assert s.degree(connection_numerator, x) == 4
assert connection_numerator == 3*x**4 - 6*A*x*x - 24*B*x + 3*A*A

result = {
    "PASS": True,
    "scope": "Symbolic identities only; no elliptic curve, label, or locator search",
    "fractional_linear_schwarzian": "0",
    "normalized_isogeny_connection_identity": True,
    "double_pole_coefficient": "-3/2",
    "simple_pole_coefficient": "3*A1/(2*A0)",
    "connection_numerator": str(connection_numerator),
    "connection_numerator_degree": 4,
    "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
