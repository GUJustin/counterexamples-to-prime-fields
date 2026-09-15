"""Rebuild the explicit monic degree-24 certificate without an optimizer."""
from pathlib import Path
from math import prod
import json

ROOT = Path(__file__).parent
saved = json.loads((ROOT/'moments40.json').read_text())
roots = [-4169,-2943,-2942,-2376,-2375,-1853,-1847,-1375,-1325,-962,-778,-598,
         603,781,963,1319,1369,1829,1836,2339,2340,2876,2877,3991]
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
(ROOT/'factored_certificates.json').write_text(json.dumps([cert],indent=2)+'\n')
print(cert['list_lower_bound'])
