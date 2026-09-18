import p2,json
from functools import reduce
rr=p2.G[tuple(p2.out[0]['head_line'])]
def span(rows):
 s={0}
 for r in rows:s|={v^r for v in s.copy()}
 return s
sets=[span(r['rows']) for r in rr]
common=set.intersection(*sets);union=set.union(*sets)
print('common',sorted(common),'union_size',len(union),'span_size',len(span(list(union))))
print('pair_intersections',sorted(set(len(a&b) for i,a in enumerate(sets) for b in sets[i+1:])))
print('locators', [r['locator'] for r in rr])
