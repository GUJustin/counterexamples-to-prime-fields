"""Independent exact cyclotomic-field interpolation of the search outputs."""
from pathlib import Path
from math import gcd,comb
from functools import reduce
from collections import Counter
from itertools import combinations,islice
import json
import sympy as s


def multiply(a,b,K):
    out=[K.zero]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def interp(nodes,values,K):
    out=[K.zero]*len(nodes)
    for i,x in enumerate(nodes):
        numerator=[K.one];denominator=K.one
        for j,y in enumerate(nodes):
            if i!=j:
                numerator=multiply(numerator,[-y,K.one],K)
                denominator*=x-y
        for j,c in enumerate(numerator):out[j]+=values[i]*c/denominator
    return out


def ev(c,x,K):
    out=K.zero
    for a in reversed(c):out=out*x+a
    return out


def serialize(c):
    return [[str(a) for a in v.to_list()] for v in c]


def field(n):
    X=s.symbols('X')
    K=s.QQ.alg_field_from_poly(s.Poly(s.cyclotomic_poly(n,X),X),alias='z')
    return K,K.unit


def main():
    base=Path(__file__).resolve().parent
    census=json.loads((base/'search.json').read_text());full=[]
    for row in census['fixtures']:
        n=row['n'];k=row['k'];K,z=field(n)
        assert s.isprime(row['split_prime'])
        assert row['supports_checked']==comb(n,k+1)
        nodes=[z**i for i in range(n)]
        values=[(x**k-K.one)**2/K(2) for x in nodes]
        bank={}
        for S in row['exact_supports']:
            I=S[:k];c=interp([nodes[i] for i in I],[values[i] for i in I],K)
            support=tuple(i for i in range(n) if ev(c,nodes[i],K)==values[i])
            assert set(S)<=set(support)
            key=tuple(tuple(v.to_list()) for v in c)
            bank[key]=(c,support)
        # Every (k+1)-subset of a found candidate's full support must have
        # been retained, and every retained subset belongs to one candidate.
        reconstructed=set()
        for c,S in bank.values():reconstructed.update(combinations(S,k+1))
        assert reconstructed==set(map(tuple,row['exact_supports']))
        full.append(dict(n=n,k=k,complete_above_capacity_list=len(bank),
                         agreement_histogram=dict(Counter(len(S) for c,S in bank.values())),
                         candidates=[dict(coefficients=serialize(c),support=S) for c,S in bank.values()]))
    restricted=[]
    for row in json.loads((base/'structured_search.json').read_text())['fixtures']:
        n=row['n'];k=row['k'];r=row['r'];A=row['A'];K,z=field(n)
        nodes=[z**i for i in range(n)];word=[(x**k-K.one)**2/K(2) for x in nodes]
        certified={};orbits=[]
        for item in row['candidates']:
            Z=item['zero_exponents'];I=item['determining_exponents']
            locator=[K.one]
            for i in Z:locator=multiply(locator,[-nodes[i],K.one],K)
            residual=interp([nodes[i] for i in I],[word[i]/ev(locator,nodes[i],K) for i in I],K)
            c=multiply(locator,residual,K)
            assert len(c)<=k
            support=[i for i in range(n) if ev(c,nodes[i],K)==word[i]]
            assert len(support)>=A
            orbit=set()
            for t in range(k):
                shifted=[v*z**(4*t*j) for j,v in enumerate(c)]
                key=tuple(tuple(v.to_list()) for v in shifted)
                orbit.add(key);certified[key]=shifted
            assert len(orbit)==item['finite_field_orbit_size']
            step=reduce(gcd,[j for j,v in enumerate(c) if j and v])
            orbits.append(dict(size=len(orbit),agreements=len(support),support=support,
                               composition_step=step,descended_domain_length=n//step,
                               coefficients=serialize(c)))
        assert len(certified)==row['finite_field_orbit_size_sum']
        restricted.append(dict(n=n,k=k,A=A,certified_characteristic_zero_list=len(certified),orbits=orbits,
                               scope='Verified lower bound from the shared-zero search, not an unrestricted complete list.'))
    result=dict(status='passed',coefficient_convention='Each coefficient is represented in descending powers of a primitive nth root, modulo its cyclotomic polynomial.',
                complete_small_censuses=full,shared_zero_certificates=restricted,
                scope='Finite characteristic-zero statements. The modular filter is exhaustive only for the enumerated support classes; no growing-length upper bound is asserted.')
    (base/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='passed',complete_small_censuses=[{k:v for k,v in r.items() if k!='candidates'} for r in full],shared_zero_certificates=[{k:v for k,v in r.items() if k!='orbits'} for r in restricted]),indent=2))


if __name__=='__main__':main()
