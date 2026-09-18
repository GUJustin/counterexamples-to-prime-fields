"""Exact pair-factor certificate; no replacement-subset or field scan."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from flint import fmpq_poly,fmpq
P=Path(__file__).parent;j=json.loads((P/'rational_seed.json').read_text())
f=[fmpq_poly([fmpq(a) for a in row]) for row in j['affine_polynomials']]
xs=[fmpq(a) for a in j['affine_nodes']];w=[fmpq(a) for a in j['affine_word']]
inc=[[a for a in range(8) if f[a](x)==w[i]] for i,x in enumerate(xs)]
assert min(map(len,inc))==2
assert max(Counter(str(q[3]) for q in f).values())==1

def strip(g):
 for x in xs:
  while g.degree()>0 and g(x)==0:g=g//fmpq_poly([-x,1])
 return g
edges=[]
for a,b in combinations(range(8),2):
 g=strip(f[a]-f[b])
 if g.degree()>0:edges.append({'pair':[a,b],'residual_degree':g.degree(),'residual_polynomial':[str(v) for v in g]})
assert [e['pair'] for e in edges]==[[0,1],[0,6],[0,7],[1,7]]
for a,b,c in combinations(range(8),3):assert strip((f[a]-f[b]).gcd(f[a]-f[c])).degree()==0
low=[{'node':i,'pair':s} for i,s in enumerate(inc) if len(s)==2]
assert [r['pair'] for r in low]==[[6,7],[0,4],[1,5],[0,3]]
weights=[2,2,2,4,4,4,3,3]
assert min(sum(weights[a] for a in row) for row in inc)==6
assert max(sum(weights[a] for a in e['pair']) for e in edges)==5
assert max(weights)==4
out={'weighted_separator':weights,'old_min_weight':6,'fresh_max_weight':5,'pass':True,'incumbent_column_sizes':list(map(len,inc)),'deletable_columns_under_equal_size_exchange':low,'fresh_pair_edges':edges,'fresh_triple_collisions':0,'infinity_max_bucket':1,'scope':'Fixed eight polynomials; retained old coordinates and values fixed; equal numbers of deleted and genuinely fresh added coordinates.'}
(P/'simultaneous_exchange.verified.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
