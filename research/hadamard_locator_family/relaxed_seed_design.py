"""A combinatorially feasible relaxed gluing pattern, not a realization."""
import itertools,json
from pathlib import Path
verts=range(8)
def block(bits,groups=range(4)):return tuple(2*g+b for g,b in zip(groups,bits))
quads=[block(v) for v in [(0,0,0,0),(1,1,1,1),(0,0,1,1),(1,1,0,0)]]
options=[]
for missing in range(4):
 groups=[g for g in range(4) if g!=missing]
 pairs=[]
 for bits in itertools.product(range(2),repeat=2):
  b=(0,)+bits;pairs.append((block(b,groups),block(tuple(1-x for x in b),groups)))
 options.append([sum((list(pairs[i]) for i in choice),[]) for choice in itertools.combinations(range(4),2)])
for choice in itertools.product(*options):
 blocks=quads+sum((list(x) for x in choice),[])
 degrees=[sum(v in b for b in blocks) for v in verts]
 counts={(i,j):sum(i in b and j in b for b in blocks) for i,j in itertools.combinations(verts,2)}
 if degrees==[8]*8 and max(counts.values())<=4 and all(not set(t)<=set(q) for t in blocks[4:] for q in quads):
  break
else:raise AssertionError('No feasible pattern')
assert len(set(blocks))==20
assert all(not ({2*g,2*g+1}<=set(b)) for b in blocks for g in range(4))
out={'new_blocks':blocks,'new_vertex_degrees':degrees,'new_pair_counts':[[i,j,c] for (i,j),c in counts.items()],'new_node_count':20,'fourfold_blocks':4,'triple_blocks':16,'old_nodes':12,'total_nodes':32,'agreement_per_candidate':14,'scope':'Only a feasible incidence pattern for preserved four-quadratic-seed gluing. Polynomial compatibility and node distinctness remain unproved.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'blocks':blocks,'degrees':degrees,'max_pair_count':max(counts.values())}))
