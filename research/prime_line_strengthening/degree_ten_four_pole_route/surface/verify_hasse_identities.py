"""Independent standard-library replay of the two exact unit identities."""
import hashlib
import json
import math
from pathlib import Path

P = Path(__file__).parent
raw = (P / 'gauss_image_interpolation.json').read_bytes()
gate_raw = (P / 'hasse_multiplicity_gate.json').read_bytes()
gate = json.loads(gate_raw)
assert gate['input_sha256'] == hashlib.sha256(raw).hexdigest()
terms = [(tuple(e), int(v)) for e, v in json.loads(raw)['image_terms']]
assert all(sum(e) == 62 and 0 < v < 29 for e, v in terms)
assert len({e for e, v in terms}) == len(terms)

affine = {}
for row in gate['affine_certificate']:
    db, dc = row['derivative_b'], row['derivative_c']
    mb, mc = row['multiplier_b'], row['multiplier_c']
    assert min(db, dc, mb, mc) >= 0 and db + dc <= 14
    for (a, b, c), v in terms:
        if b < db or c < dc:
            continue
        e = (b - db + mb, c - dc + mc)
        add = row['coefficient'] * v * math.comb(b, db) * math.comb(c, dc)
        affine[e] = (affine.get(e, 0) + add) % 29
affine = {e: v for e, v in affine.items() if v}
assert affine == {(0, 0): 1}, affine

boundary = {}
for row in gate['boundary_certificate']:
    da, db = row['derivative_a'], row['derivative_b']
    assert min(da, db) >= 0 and da + db <= 14
    for (a, b, c), v in terms:
        if a != da or b < db:
            continue
        for k, coefficient in enumerate(row['multiplier_coefficients']):
            e = b - db + k
            boundary[e] = (boundary.get(e, 0) + coefficient * v * math.comb(b, db)) % 29
boundary = {e: v for e, v in boundary.items() if v}
assert boundary == {0: 1}, boundary

# At [0:1:0], dehomogenizing b gives distinct monomials a^i c^j;
# hence the least total degree is the exact local multiplicity.
endpoint_order = min(a + c for (a, b, c), v in terms)
assert endpoint_order == gate['endpoint_010_multiplicity'] < 15
result = {
    'status': 'PASS',
    'polynomial_sha256': hashlib.sha256(raw).hexdigest(),
    'certificate_sha256': hashlib.sha256(gate_raw).hexdigest(),
    'affine_identity_terms': len(gate['affine_certificate']),
    'boundary_identity_terms': len(gate['boundary_certificate']),
    'endpoint_order': endpoint_order,
    'scope': 'No multiplicity-at-least-15 point of the recorded homogeneous polynomial over F29 algebraic closure; no CAS or row reduction used.'
}
(P / 'hasse_multiplicity_gate.root_verified.json').write_text(json.dumps(result, indent=2))
print(result)
