"""Exact sparse mu7 quotient of the residual polynomial on a*b != 0."""
import json,hashlib
from pathlib import Path
P=Path(__file__).parent;raw=(P/'reconstruction.json').read_bytes();d=json.loads(raw)
out=[]
for k,terms in enumerate(d['residual_coefficient_terms']):
 for (i,j),c in terms:
  e=3*k+i+2*j-6
  assert e%7==0 and e>=0
  out.append([[k,j,e//7],c])
# Identity: D(b^3 Z; b, U b^2) = b^6 E(Z,U,b^7).
# Replay in the Laurent polynomial ring: each term recovers its original i.
assert len({tuple(e) for e,c in out})==len(out)
for (k,j,v),c in out:
 i=6+7*v-3*k-2*j
 assert i>=0 and i+j<=18
 assert [[i,j],c] in d['residual_coefficient_terms'][k]
rec={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
 'field':29,'variables':['Z','U','V'],'chart':'a=1,b!=0',
 'identity':'D(b^3 Z; b, U b^2) = b^6 E(Z,U,b^7)',
 'quotient_coordinates':'U=c/b^2, V=b^7; V!=0',
 'terms':out,'degrees':[max(e[i]for e,c in out)for i in range(3)],
 'scope':'Equivalent homogeneous binary-gradient-gcd test after invertible fiber scaling; a=0 and b=0 need separate charts.'}
(P/'invariant_quotient.json').write_text(json.dumps(rec,indent=2))
print({k:v for k,v in rec.items()if k!='terms'})
