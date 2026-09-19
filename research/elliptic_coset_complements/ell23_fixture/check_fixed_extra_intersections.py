#!/usr/bin/env python3
"""One fixed-Z finite intersection census, not a counterexample search."""
import hashlib
import json
from pathlib import Path
from flint import nmod_mat

root=Path(__file__).resolve().parent
raw=(root/'fixture.json').read_bytes()
f=json.loads(raw)
p,ell,n,k=f['p'],f['ell'],f['n'],f['k']
d=5
Z=f['subgroups'][0]['kernel_x'][:d]
domain=[x for x in f['domain'] if x not in Z]
dim=k+d
r=len(domain)-dim
assert (p,ell,n,k,len(domain),r)==(1657,23,264,173,259,81)

def evaluate(poly,x):
    v=0
    for a in reversed(poly): v=(v*x+a)%p
    return v

weights=[]
for x in domain:
    product=1
    for y in domain:
        if y!=x: product=product*(x-y)%p
    weights.append(pow(product,-1,p))
parity=nmod_mat([[weights[j]*pow(x,i,p)%p for j,x in enumerate(domain)]
                for i in range(r)],p)
assert parity.rank()==r
# Verify the exact code being quotiented, including its highest monomial.
code=nmod_mat([[pow(x,j,p) for j in range(dim)] for x in domain],p)
assert (parity*code).rank()==0

syndromes={}
dimensions=[]
t=(ell-1)//2
for index,h in enumerate(f['subgroups']):
    if set(h['kernel_x'])&set(Z): continue
    rows=[]
    for x in domain:
        K=evaluate(h['K'],x)
        N=evaluate(h['N'],x)
        row=[]
        for i in range(3):
            e=0 if K==0 else pow(N,t-3+i,p)*pow(pow(K,2*i+1,p),-1,p)%p
            row.extend(e*pow(x,j,p)%p for j in range(d+1))
        rows.append(row)
    S=parity*nmod_mat(rows,p)
    rank=S.rank()
    assert rank==3*d+3
    syndromes[index]=[[int(S[i,j]) for j in range(3*d+3)] for i in range(r)]
    dimensions.append({'subgroup':index,'rank':rank})

pairs=[]
indices=sorted(syndromes)
for pos,h in enumerate(indices):
    for hh in indices[pos+1:]:
        A=nmod_mat([a+b for a,b in zip(syndromes[h],syndromes[hh])],p)
        rank=A.rank()
        pairs.append({'H':h,'H_prime':hh,'joined_rank':rank,
                      'intersection_dimension':2*(3*d+3)-rank})

hist={}
for rec in pairs:
    key=str(rec['intersection_dimension'])
    hist[key]=hist.get(key,0)+1
receipt={'status':'PASS','scope':'all clean subgroup pairs for ONE specified fixed extra set',
         'construction_established':False,'fixture_sha256':hashlib.sha256(raw).hexdigest(),
         'p':p,'ell':ell,'Z':Z,'punctured_length':len(domain),
         'quotient_code_dimension':dim,'syndrome_rows':r,
         'common_far_residue_space_removed':True,'residue_dimension':d,
         'clean_subgroup_dimensions':dimensions,'pairs_checked':len(pairs),
         'intersection_dimension_histogram':hist,'pairs':pairs,
         'limitation':'Does not cover other extra sets, variable extra sets, other curves or growing ell.'}
(root/'fixed_extra_intersections.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({key:value for key,value in receipt.items()
                  if key not in ('pairs','clean_subgroup_dimensions')},indent=2))
