#!/usr/bin/env python3
"""Symbolic identity checks for the coset/Dickson gate; no finite-field scan."""
import json
from pathlib import Path
import sympy as sp

T, e, kappa, h, alpha, j = sp.symbols("T e kappa h alpha j")
A = (2*e+2*kappa-1)*h
B = -(e+2*kappa)*h*h-4*(e-1)*alpha
residual_bracket = ((e-1)*(T*T-4*alpha)
                    +(2*kappa+1)*T*(T-h)
                    -(e+2*kappa)*(T-h)**2)
assert sp.expand(residual_bracket-(A*T+B)) == 0
derivative_bracket = (e-2)*(A*T+B)+(T-h)*A
assert sp.expand(derivative_bracket-((e-1)*A*T+(e-2)*B-A*h)) == 0

diagonal = (e-2*j)*(e-2*j-1)+(2*kappa+1)*(e-2*j)-e*(e+2*kappa)
assert sp.expand(diagonal+4*j*(e+kappa-j)) == 0
ratio = -alpha*(e-2*j+2)*(e-2*j+1)/(j*(e+kappa-j))
assert sp.cancel(diagonal*ratio-4*alpha*(e-2*j+2)*(e-2*j+1)) == 0
assert sp.simplify(ratio.subs({j:1,kappa:0})+e*alpha) == 0
assert sp.simplify(ratio.subs({j:1,kappa:1})+(e-1)*alpha) == 0

result = {
    "status": "PASS: symbolic identities, not a parameter scan",
    "operator": "(T^2-4alpha)d^2 +(2kappa+1)T d -e(e+2kappa)",
    "checks": ["power-contact residual", "derivative linear factor",
               "coefficient diagonal", "coefficient recurrence cancellation",
               "first-kind second coefficient", "second-kind second coefficient"],
    "proposition_scope": "e>=7, characteristic p>2e+2, nonzero Dickson parameter; either kind; arbitrary Mobius-cleared whole fiber",
    "proof_file": "BALANCED_SPLIT_LOCATOR_COSET_DICKSON_GATE.md"
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
