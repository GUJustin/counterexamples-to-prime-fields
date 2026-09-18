"""Independent rational arithmetic verification of q8 ideal identities.

No CAS, Groebner basis, or floating-point arithmetic is used. This verifies
the supplied polynomial identities; the geometric equation reduction is
audited separately.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import time

ZERO = (F(0),) * 4
ONE = (F(1), F(0), F(0), F(0))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def mul(a, b):
    out = [F(0)] * 4
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if y:
                k = i + j
                out[k % 4] += x * y * (1 if k < 4 else -1)
    return tuple(out)


def decode(rows):
    out = {}
    for exp, co in rows:
        key = tuple(exp)
        assert len(key) == 3 and all(isinstance(i, int) and i >= 0 for i in key)
        assert len(co) <= 4 and key not in out
        val = tuple(map(F, co)) + (F(0),) * (4 - len(co))
        if val != ZERO:
            out[key] = val
    return out


def padd(a, b):
    out = dict(a)
    for e, c in b.items():
        v = add(out.get(e, ZERO), c)
        if v == ZERO:
            out.pop(e, None)
        else:
            out[e] = v
    return out


def pmul(a, b):
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            g = tuple(x + y for x, y in zip(e, f))
            out[g] = add(out.get(g, ZERO), mul(c, d))
    return {e: c for e, c in out.items() if c != ZERO}


def scale(a, c):
    return {e: v for e, x in a.items() if (v := mul(x, c)) != ZERO}


def power(a, k):
    out = {(0, 0, 0): ONE}
    for _ in range(k):
        out = pmul(out, a)
    return out


def zp(k):
    k %= 8
    out = [F(0)] * 4
    out[k % 4] = F(1 if k < 4 else -1)
    return tuple(out)


def ev(co, x):
    out = {}
    for v in reversed(co):
        out = padd(pmul(out, x), v)
    return out


def reconstruct(case, h):
    one = {(0, 0, 0): ONE}
    aa = [{tuple(int(j == i) for j in range(3)): ONE} for i in range(3)]
    e = [one]
    for a in aa:
        new = [{} for _ in range(len(e) + 1)]
        for k, v in enumerate(e):
            new[k] = padd(new[k], scale(pmul(power(a, 2), v), neg(ONE)))
            new[k + 1] = padd(new[k + 1], v)
        e = new
    shift = -1 if h == 1 else 1
    other = []
    for j in range(4):
        v = {}
        for k in range(4):
            # 1/(1-z^odd)=(1+z^odd+z^(2odd)+z^(3odd))/2.
            co = ZERO
            for m in range(4):
                co = add(co, zp((2*k - 2*j + shift)*m))
            co = tuple(-x/4 for x in co)
            v = padd(v, scale(e[k], co))
        other.append(v)
    E, B = (e, other) if h == 1 else (other, e)
    for s in range(4):
        x = {(0, 0, 0): zp(2*s)}
        assert not padd(ev(E, x), scale(ev(B, x), zp(s)))
    guard = one
    for a in aa:
        guard = pmul(guard, pmul(a, padd(power(a, 8), scale(one, neg(ONE)))))
    for i in range(3):
        for j in range(i):
            guard = pmul(guard, padd(power(aa[i], 8), scale(power(aa[j], 8), neg(ONE))))
    patterns = [[(1, 3), (7, 2), (7, 2)], [(1, 3), (7, 2), (2, 5)],
                [(7, 1), (7, 2), (7, 2)], [(7, 1), (7, 2), (2, 5)]]
    raw = []
    for a, pair in zip(aa, patterns[case]):
        a2 = power(a, 2)
        for k in pair:
            x = scale(a2, zp(2*k))
            if h == 1:
                diff = padd(ev(B, x), scale(ev(B, a2), neg(ONE)))
                f = padd(ev(E, x), pmul(scale(a, zp(k)), diff))
            else:
                f = padd(ev(E, x), scale(ev(E, a2), neg(zp(2*k))))
                f = padd(f, pmul(scale(a, zp(k)), ev(B, x)))
            raw.append(f)
    return raw, guard


def verify_metadata(path):
    start = time.monotonic()
    content = path.read_bytes()
    d = json.loads(content)
    raw, guard = reconstruct(d['case'], d['h'])
    assert raw == [decode(x) for x in d['raw_encoded']]
    normalized = [decode(x) for x in d['normalized_encoded']]
    for i in range(6):
        scalar = tuple(map(F, d['normalization_scalars'][i]))
        assert scalar != ZERO
        product = scale(normalized[i], scalar)
        factors = d['removed_factors'][i]
        quotients = d['removed_guard_quotients'][i]
        assert len(factors) == len(quotients)
        for f, q in zip(factors, quotients):
            factor, quotient = decode(f), decode(q)
            assert pmul(factor, quotient) == guard
            product = pmul(product, factor)
        assert product == raw[i]
    return {'file': path.name, 'sha256': hashlib.sha256(content).hexdigest(),
            'case': d['case'], 'h': d['h'], 'equations_reconstructed': True,
            'guarded_divisions_verified': True, 'seconds': time.monotonic()-start}


def verify(path):
    start = time.monotonic()
    raw = path.read_bytes()
    data = json.loads(raw)
    cert = data['certificate']
    eqs = [decode(x) for x in cert['equations']]
    metadata_path = path.with_name(f"metadata_c{data['case']}_h{data['h']}.json")
    if metadata_path.exists():
        metadata = json.loads(metadata_path.read_text())
        assert eqs == [decode(x) for x in metadata['normalized_encoded']]
    multipliers = [decode(x) for x in cert['multipliers']]
    target = decode(cert['target'])
    assert len(eqs) == len(multipliers) == 6
    expected = {(1, 0, 0): ONE} if data['h'] == 1 else {(0, 0, 0): ONE}
    assert target == expected
    total = {}
    for eq, multiplier in zip(eqs, multipliers):
        total = padd(total, pmul(eq, multiplier))
    assert total == target, 'Polynomial ideal identity failed'
    return {'file': path.name, 'sha256': hashlib.sha256(raw).hexdigest(),
            'case': data['case'], 'h': data['h'], 'identity_verified': True,
            'equation_terms': list(map(len, eqs)),
            'multiplier_terms': list(map(len, multipliers)),
            'seconds': time.monotonic() - start}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    results = [verify_metadata(p) if p.name.startswith('metadata_') else verify(p)
               for p in args.files]
    args.output.write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results, indent=2))
