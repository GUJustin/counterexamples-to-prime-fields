"""Rebuild the explicit monic degree-40 certificate without an optimizer."""
from pathlib import Path
from math import prod
import json

ROOT = Path(__file__).parent
saved = json.loads((ROOT/'moments40.json').read_text())
assert (saved['n'],saved['t'],saved['q'],saved['center'],saved['degree']) == (64,34,1071,22138,40)
assert len(saved['centered_moments']) == 41
roots = [-4169,-3591,-3590,-3214,-3213,-2844,-2843,-2475,-2474,-2107,-2106,
         -1742,-1735,-1391,-1358,-1065,-968,-765,-565,-476,482,571,769,969,
         1065,1352,1385,1721,1729,2081,2082,2436,2437,2787,2788,3135,3136,
         3484,3485,4184]
assert len(roots) == 40
coeff = [1]
for r in roots:
    new = [0]*(len(coeff)+1)
    for j,a in enumerate(coeff):
        new[j] -= r*a
        new[j+1] += a
    coeff = new
numerator = sum(a*m for a,m in zip(coeff,saved['centered_moments']))
denominator = sum(max(0,prod(x-r for r in roots)) for x in range(-4169,3992))
assert numerator > 0 and denominator > 0
cert = dict(degree=len(roots),center=22138,low=17969,high=26129,roots=roots,
    coefficients_ascending=coeff,numerator=numerator,denominator=denominator,
    list_lower_bound=(numerator+denominator-1)//denominator)
assert cert['list_lower_bound'] == 5285900426578
(ROOT/'factored40_certificates.json').write_text(json.dumps([cert],indent=2)+'\n')
print(cert['list_lower_bound'])
