"""Small complete RREF census; secondary/primary locator-label overlap."""
import itertools
import json
from pathlib import Path
from flint import fq_default_ctx

p = 3
K = fq_default_ctx(p, 5, 't')
t = K.gen()
powers = [t**j for j in range(5)]

def encode(a):
    return tuple(int(c) for c in a.to_list())

def spaces(k):
    for pivots in itertools.combinations(range(5), k):
        positions = [(i,j) for i in range(k) for j in range(pivots[i]+1,5) if j not in pivots]
        for values in itertools.product(range(p), repeat=len(positions)):
            basis = [powers[j] for j in pivots]
            for (i,j),c in zip(positions,values):
                basis[i] += c*powers[j]
            yield basis

def locator(basis):
    coeff = [K(1)]
    for b in basis:
        value = sum((c*b**(p**i) for i,c in enumerate(coeff)), K(0))
        assert value
        scalar = value**(p-1)
        new = [K(0)]*(len(coeff)+1)
        for i,c in enumerate(coeff):
            new[i] -= scalar*c
            new[i+1] += c**p
        coeff = new
    for b in basis:
        assert sum((c*b**(p**i) for i,c in enumerate(coeff)), K(0)) == 0
    return coeff

sets=[]
for dim in [2,3]:
    labels={}
    for basis in spaces(dim):
        coeff=locator(basis)
        if dim==2:
            a,c=coeff[1]**p,coeff[0]**p
        else:
            a,c=coeff[2],coeff[1]
        key=(encode(a),encode(c))
        assert key not in labels
        labels[key]=dict(basis=[encode(v) for v in basis],locator=[encode(v) for v in coeff])
    assert len(labels)==1210
    sets.append(labels)
overlap=set(sets[0]) & set(sets[1])
result=dict(p=p,field=str(K),secondary=len(sets[0]),primary=len(sets[1]),overlap=len(overlap),
            union=len(set(sets[0])|set(sets[1])),
            example=None if not overlap else {str(i):sets[i][next(iter(overlap))] for i in range(2)})
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
