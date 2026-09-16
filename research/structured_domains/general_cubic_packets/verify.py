"""Check the archived exhaustive cubic search; --full reruns all general pencils."""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess
import tempfile

BASE = Path(__file__).resolve().parent


def domain(p, n):
    generator = next(pow(a, (p-1)//n, p) for a in range(2, p)
                     if pow(pow(a, (p-1)//n, p), n//2, p) != 1)
    return [pow(generator, i, p) for i in range(n)]


def independent_small(p, n):
    points = []
    for roots in itertools.combinations(domain(p, n), 3):
        a, b, c = roots
        points.append(((a+b+c) % p, (a*b+a*c+b*c) % p, a*b*c % p, roots))
    maxima = [0, 0]
    for i, a in enumerate(points):
        counts = [{}, {}]
        for b in points[i+1:]:
            d1, d2, d3 = [(b[j]-a[j]) % p for j in range(3)]
            if any((-d1*x*x+d2*x-d3) % p == 0 for x in a[3]):
                continue
            if d3:
                inv = pow(d3, -1, p)
                key, kind = (d1*inv % p, d2*inv % p), 1
            elif d1:
                key, kind = (1, d2*pow(d1, -1, p) % p), 0
            else:
                assert d2
                key, kind = (0, 1), 0
            counts[kind][key] = counts[kind].get(key, 0)+1
        for kind in (0, 1):
            maxima[kind] = max(maxima[kind], max(counts[kind].values(), default=0)+1)
    return dict(constant_product_maximum=maxima[0], nonconstant_product_maximum=maxima[1])


def witness(row):
    p, n = row['p'], row['n']
    a1, a2 = row['witness_anchor']
    s1, s2 = row['witness_slopes']
    fibers, roots = {}, []
    for x in domain(p, n):
        if (x**3-a1*x*x+a2*x-1) % p == 0:
            roots.append(x)
        numerator = (x**3+(s1-a1)*x*x+(a2-s2)*x) % p
        denominator = (s1*x*x-s2*x+1) % p
        if not denominator:
            assert numerator
            value = 'infinity'
        else:
            value = numerator*pow(denominator, -1, p) % p
        fibers.setdefault(value, []).append(x)
    assert len(roots) == 3
    assert all((s1*x*x-s2*x+1) % p for x in roots)
    assert max(map(len, fibers.values())) <= 3
    actual = sum(len(v) == 3 for v in fibers.values())
    assert actual == row['maximum_examined_full_fibers']
    return actual


def call(binary, *args):
    return json.loads(subprocess.check_output([str(binary), *map(str, args)], text=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--full', action='store_true', help='rerun the 29.7-billion-pair general search')
    args = parser.parse_args()
    record = json.loads((BASE/'verification.json').read_text())
    archive = json.loads((BASE/'checkpoints.json').read_text())
    digest = hashlib.sha256((BASE/'verify_general.cpp').read_bytes()).hexdigest()
    assert record['status'] == 'PASS' and archive['source_sha256'] == digest
    assert record['source_sha256'] == digest and archive['bucket_size'] == 256
    p, n = record['p'], record['n']
    assert p == 2130706433 and n == 256
    assert all(p % d for d in range(2, math.isqrt(p)+1))
    triples = (n-1)*(n-2)//6
    start, pairs, max_witness = 0, 0, 0
    for row in archive['chunks']:
        assert row['p'] == p and row['n'] == n and row['bucket_size'] == n
        assert row['anchor_start'] == start and row['anchor_end'] > start
        assert row['pairs_examined'] == (row['anchor_end']-start)*triples*(n-1)
        start = row['anchor_end']
        pairs += row['pairs_examined']
        max_witness = max(max_witness, witness(row))
    assert start == triples and pairs == triples*triples*(n-1)
    assert pairs == record['pairs_examined'] and max_witness == record['maximum_examined_full_fibers']
    assert record['general_cubic_upper_bound'] == max(2, max_witness, 3)
    small_checks = []
    with tempfile.TemporaryDirectory(prefix='cubic-packets-') as temporary:
        binaries = {}
        for kind in ('general', 'constant'):
            binary = Path(temporary)/kind
            subprocess.run(['c++', '-O3', '-std=c++17', str(BASE/f'verify_{kind}.cpp'),
                            '-o', str(binary)], check=True)
            binaries[kind] = binary
        for prime, size in ((97, 8), (193, 16)):
            expected = independent_small(prime, size)
            general = call(binaries['general'], prime, size, size)
            constant = call(binaries['constant'], prime, size)
            assert general['complete_scan']
            assert general['nonconstant_product_upper_bound'] == expected['nonconstant_product_maximum']
            assert constant['constant_product_max_complete_fibers'] == expected['constant_product_maximum']
            witness(general)
            small_checks.append(dict(p=prime, n=size, **expected))
        constant = call(binaries['constant'], p, n)
        assert constant['constant_product_max_complete_fibers'] == 3
        full = None
        if args.full:
            full = call(binaries['general'], p, n, n)
            assert full['complete_scan'] and full['pairs_examined'] == pairs
            assert full['nonconstant_product_upper_bound'] == record['nonconstant_product_upper_bound']
            witness(full)
    # Exact arithmetic for the strengthened dyadic consequence of Theorem 2.8.
    dyadic = []
    for degree, expected in [(513, (426, 43606)), (514, (426, 43180)), (516, (424, 43360))]:
        count = min(262144//degree, 1+218452//degree)
        uncovered = 262144-degree*count
        assert (count, uncovered) == expected
        dyadic.append(dict(degree=degree, maximum_complete_fibers=count,
                           minimum_uncovered_points=uncovered))
    result = dict(status='PASS', archived_general_pairs=pairs,
                  archived_general_witnesses_checked=len(archive['chunks']),
                  independent_small_checks=small_checks,
                  pinned_constant_product=constant,
                  full_general_rerun=full, dyadic_arithmetic=dyadic,
                  scope='Default checks archived coverage and witnesses, independent '
                        'small cases, and reruns the complete constant-product search. '
                        '--full also repeats the full general cubic enumeration.')
    temporary = BASE/'checks.tmp'
    temporary.write_text(json.dumps(result, indent=2)+'\n')
    temporary.replace(BASE/'checks.json')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
