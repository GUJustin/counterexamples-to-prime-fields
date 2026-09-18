#!/usr/bin/env python3
"""Replay explicit identities only; no elimination or matrix construction."""
import json,hashlib,math,time
from pathlib import Path
from collections import defaultdict
p=Path(__file__).resolve().parent
start=time.time()
raw=(p/'gauss_image_interpolation.json').read_bytes()
h=json.loads(raw)['image_terms'];g=json.loads((p/'hasse_multiplicity_gate.json').read_text())
assert hashlib.sha256(raw).hexdigest()==g['input_sha256']
assert all(sum(ex)==62 for ex,v in h)
out=defaultdict(int)
for row in g['affine_certificate']:
 r,s=row['derivative_b'],row['derivative_c'];assert r+s<15
 for (a,b,c),v in h:
  if b>=r and c>=s:
   key=(b-r+row['multiplier_b'],c-s+row['multiplier_c'])
   out[key]=(out[key]+row['coefficient']*v*math.comb(b,r)*math.comb(c,s))%83
assert {k:v for k,v in out.items() if v}=={(0,0):1}
out=defaultdict(int)
for row in g['boundary_certificate']:
 r,s=row['derivative_a'],row['derivative_b'];assert r+s<15
 for (a,b,c),v in h:
  if a==r and b>=s:
   for j,m in enumerate(row['multiplier_coefficients']):
    out[b-s+j]=(out[b-s+j]+m*v*math.comb(b,s))%83
assert {k:v for k,v in out.items() if v}=={0:1}
# At [0:1:0], dehomogenize b=1. Distinct (a,c) remain distinct.
endpoint=min(a+c for (a,b,c),v in h if v%83)
assert endpoint==0 and endpoint<15
receipt=dict(status='PASS',algorithm='stdlib coefficient summation, no RREF',affine_identity='1',boundary_identity='1',endpoint_010_multiplicity=endpoint,seconds=time.time()-start,input_sha256=hashlib.sha256(raw).hexdigest(),certificate_sha256=hashlib.sha256((p/'hasse_multiplicity_gate.json').read_bytes()).hexdigest())
(p/'hasse_multiplicity_gate.verified.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
