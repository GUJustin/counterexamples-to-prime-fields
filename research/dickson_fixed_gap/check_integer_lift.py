"""Test preservation of Dickson agreement supports on integer nodes.

Ranks modulo an auxiliary prime certify lower bounds on rational ranks.
This does NOT test moving nodes or every possible characteristic-zero lift.
"""
from math import comb
from pathlib import Path
import json


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def supports(p):
    k, e = (p-1)//4, (p+1)//2
    word = {}
    for x in range(1,p):
        chi = pow(x,(p-1)//2,p)
        word[x] = ((1 + (1 if chi == 1 else -1))//2-pow(x,k,p))%p
    answer = []
    for a in range(1,(p-1)//2+1):
        coefficients = [comb(e,2*j+1)*pow(a,e-2*j-1,p)%p for j in range(k)]
        support = []
        for x in range(1,p):
            v = 0
            for c in reversed(coefficients):
                v = (v*x+c)%p
            if v == word[x]:
                support.append(x)
        require(len(support) == 3*(p-1)//8, 'seed agreement')
        answer.append(support)
    return answer


def rank_constraints(sets, n, k, modulus):
    pivots = {}
    rows = 0
    for support in sets:
        anchor = support[:k]
        denominators = []
        for a in anchor:
            denominator = 1
            for b in anchor:
                if b != a:
                    denominator = denominator*(a-b)%modulus
            denominators.append(pow(denominator,-1,modulus))
        for x in support[k:]:
            row = [0]*n
            row[x-1] = 1
            product = 1
            for a in anchor:
                product = product*(x-a)%modulus
            for a, inverse in zip(anchor, denominators):
                row[a-1] = -product*pow(x-a,-1,modulus)*inverse%modulus
            rows += 1
            for col in range(n):
                value = row[col]
                if not value:
                    continue
                if col in pivots:
                    basis = pivots[col]
                    for j in range(col,n):
                        row[j] = (row[j]-value*basis[j])%modulus
                else:
                    inverse = pow(value,-1,modulus)
                    pivots[col] = [(entry*inverse)%modulus for entry in row]
                    break
    return len(pivots), rows


if __name__ == '__main__':
    results = []
    for p in (17,41,97,193):
        n, k = p-1,(p-1)//4
        sets = supports(p)
        native, rows = rank_constraints(sets,n,k,p)
        auxiliary, same_rows = rank_constraints(sets,n,k,65537)
        require(rows == same_rows, 'identical incidence systems')
        require(native < n-k, 'native non-codeword exists')
        require(auxiliary <= n-k, 'global codeword kernel')
        results.append(dict(p=p,n=n,k=k,constraints=rows,native_rank=native,
                            auxiliary_prime=65537,auxiliary_rank=auxiliary,
                            rational_rank_certified_exact=(auxiliary == n-k),
                            nontrivial_integer_node_lift_excluded=(auxiliary == n-k)))
    result = dict(status='PASS',scope='same supports on integer representatives; not moving nodes',results=results)
    Path(__file__).with_name('integer_lift_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
