"""Replay the saved set; no random search and no inverse-coordinate formula."""
import collections
import json
import math
import sys
from pathlib import Path

here = Path(__file__).parent
source = sys.argv[1] if len(sys.argv)>1 else 'pilot.json'
data = json.loads((here / source).read_text())
best = data.get('best', data)
p, L = data['p'], data['L']
assert all(p % d for d in range(2, math.isqrt(p) + 1))
primes = []
v = 2
while len(primes) < L:
    if all(v % d for d in range(2, math.isqrt(v) + 1)):
        primes.append(v)
    v += 1
assert p > 2 * primes[-1] ** 2
polys = [(a*a % p, pow(a*a, -1, p)) for a in primes]
core = {}
for i in range(L):
    for j in range(i):
        for sign in (-1, 1):
            x = sign * primes[i] * primes[j] % p
            assert x not in core
            core[x] = (primes[i]**2 + primes[j]**2) % p
assert len(core) == L*(L-1)
nodes = best['nodes']
assert len(nodes) == len(set(nodes)) == len(core)+1
assert not (set(nodes) & (set(core) | {0}))
core_hits = [sum((c+d*x*x-y) % p == 0 for x,y in core.items())
             for c,d in polys]
assert core_hits == [2*(L-1)]*L
hist = collections.Counter()
by_label = collections.defaultdict(collections.Counter)
for x in nodes:
    values = []
    for i,(c,d) in enumerate(polys):
        value = ((c+d*x*x-pow(x,4,p))*pow(pow(x,3,p),-1,p)) % p
        assert value not in (0,1)
        values.append(value)
        hist[value] += 1
        by_label[value][i] += 1
    assert len(set(values)) == L
singles = sum(count == 1 for count in hist.values())
assert singles == best['singletons']
if 'distinct_labels' in best:
    assert len(hist) == best['distinct_labels']
assert sum(hist.values()) == L*len(nodes)
if 'max_multiplicity' in best:
    assert max(hist.values()) == best['max_multiplicity']
mapped = {(z*pow(1-z,-1,p)) % p for z in hist}
assert len(mapped) == len(hist) and 0 not in mapped and p-1 not in mapped
assert L+4 <= 2*(L-1) and 5 < 2*L-1
out = dict(status='PASS', source=source, p=p, L=L, fresh_nodes=len(nodes),
           core_nodes=len(core), incidences=sum(hist.values()),
           finite_singleton_labels=singles, finite_distinct_bad_labels=len(hist),
           total_bad_labels_including_infinity=len(hist)+1,
           guaranteed_singleton_labels_including_infinity=singles+1,
           exact_singleton_threshold_lists_including_infinity=1+sum(len(v)==1 for v in by_label.values()),
           maximum_threshold_list_size=max(map(len,by_label.values())),
           max_incidence_multiplicity=max(hist.values()),
           collision_pairs=sum(v*(v-1)//2 for v in hist.values()),
           note='Singleton count counts incidence multiplicity one; additional singleton lists may exist.')
output = 'independent_replay.json' if source == 'pilot.json' else Path(source).stem+'.independent_replay.json'
(here/output).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
