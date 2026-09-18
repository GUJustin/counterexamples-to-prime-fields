"""Exact small combinatorial gate; no field or polynomial search."""
import itertools,json
from collections import Counter
from pathlib import Path

def hadamard(L):
 return sorted(sum(1<<x for x in range(L)if (a&x).bit_count()%2==b)for a in range(1,L)for b in range(2))
def permute(H,p):return sorted(sum(1<<p[i]for i in range(len(p))if B>>i&1)for B in H)
H=hadamard(8);copies={}
for p in itertools.permutations(range(8)):
 G=tuple(permute(H,p));copies.setdefault(G,p)
assert len(copies)==30
hist=Counter(len(set(H)&set(G))for G in copies)
p=(0,1,2,4,3,6,7,5);blocks=H+permute(H,p)
assert len(set(blocks))==28
checks=[]
for L in [4,8,16]:
 pp=p if L==8 else tuple(range(L))
 bs=hadamard(L)+permute(hadamard(L),pp)
 assert len(bs)==4*(L-1)
 assert all(B.bit_count()==L//2 for B in bs)
 assert all(sum(B>>i&1 for B in bs)==2*(L-1)for i in range(L))
 assert all(sum((B>>i&1)*(B>>j&1)for B in bs)==L-2 for i in range(L)for j in range(i))
 checks.append({'L':L,'n':len(bs),'D':L-2,'A':2*(L-1)})
locators={str(i):[q for q,B in enumerate(blocks)if B&1 and B>>i&1]for i in range(1,8)}
rows=[]
for q,B in enumerate(blocks):
 if B&1:continue
 labels=[i for i in range(1,8)if B>>i&1];j=labels[0]
 for i in labels[1:]:rows.append({'node':q,'positive_column':i,'negative_column':j})
assert len(rows)==42 and all(len(v)==6 for v in locators.values())
out={'status':'PASS','Hadamard_labeled_copies':30,'intersection_histogram':dict(sorted(hist.items())),
 'family_parameter_checks':checks,'L8_second_permutation':p,'L8_blocks_as_masks':blocks,
 'locator_H0i_node_indices':locators,'matrix_rows':rows,
 'entry_rule':'row(node q,+i,-j): +product_{r in H0i}(xq-xr) in column i and negative analogous product in column j',
 'guards':'28 distinct nodes; kernel leading coefficients 0,lambda1,...,lambda7 pairwise distinct',
 'scope':'exact design and compatibility target only; no polynomial realization found'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items()if k not in ['matrix_rows','locator_H0i_node_indices','L8_blocks_as_masks']})
