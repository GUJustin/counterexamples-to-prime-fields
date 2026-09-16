"""Separate arithmetic audit of every exactly computed class certificate.

Uses coefficient sums instead of the closed binomial Fourier trace, and
histograms instead of the producer's expanded incidence arrays.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import json
from rational_circle_bounds import ln,ln2,div,entropy


@lru_cache(None)
def count(m,k,c):
    total=0;L=1
    while L<=m:
        # Expand (1-(-z)^L)^(m/L)/(1+z), without the hockey-stick identity.
        trace=sum((-1)**(k+j)*comb(m//L,j) for j in range(k//L+1))
        ram=1 if L==1 else L//2 if c%L==0 else -L//2 if c%(L//2)==0 else 0
        total+=trace*ram;L*=2
    assert total%m==0
    return total//m


def pairs(N,b):
    q,s=divmod(N,b)
    return (b*q*(q-1)+2*s*q)//2


def main():
    data=json.loads(Path('circle_product_dyadic_verification.json').read_text());p=data['p']
    assert data['status']=='passed'
    classes=certificates=0
    for row in data['exact_rows']:
        m,h,d,r=(row[k] for k in ('M','h','d','r'))
        assert len(row['product_classes'])==m.bit_length()
        weighted=0
        for option in row['product_classes']:
            c=option['product_exponent'];v=option['product_valuation']
            population=count(m,h-1,c);assert population==option['product_population']
            weighted+=population*(1 if c==0 else m>>(v+1))
            N=(population+p**(2*r)-1)//p**(2*r);assert N==option['N']
            if r==0:
                histogram=option['incidence_histogram']
                assert sum(multiplicity for s,multiplicity in histogram)==m
                assert sum(s*multiplicity for s,multiplicity in histogram)==N*h
                group=sum(multiplicity*(s*(s-1)//2+pairs(N-s,p-1)) for s,multiplicity in histogram)
            else:
                a,e=divmod(N*(h-1),m-1)
                def f(s):return s*(s-1)//2+pairs(N-s,p-1)
                group=N*(N-1)//2+(m-1-e)*f(a)+e*f(a+1)
            rest=(p+1-m)*pairs(N,p)
            budget=(d+1)*N*(N-1)//2-group-rest
            for kind,ext in (('CM31',2),('QM31',4)):
                cert=option['values'][kind];Q=p*p-p-1 if ext==2 else p**4-p*p
                collision_cap=budget//Q;J=cert['J']
                assert cert['on_G_lower']==group and cert['on_unit_rest_lower']==rest
                assert cert['off_circle_pair_budget']==budget and cert['poles']==Q
                assert cert['some_pole_pairs']==collision_cap
                assert pairs(N,J)<=collision_cap
                assert J==1 or pairs(N,J-1)>collision_cap
                rho=F(d,m);eta=F(2*r+3,m)-F(2,row['n'])
                logJ=div(ln(F(J)),ln2);H=div(entropy(rho),ln2)
                upper=logJ[1]-(row['n'].bit_length()-1)-H[0]/eta
                winner=data['winners'][kind]
                same=all(row[k]==winner[k] for k in ('M','B','d','r')) and J==winner['J']
                assert same or upper<F(winner['excess_lower'])
                certificates+=1
            classes+=1
        assert weighted==comb(m-1,h-1)
    for row in data['raw_exclusions']:
        assert all(F(row['excess_upper'])<F(w['excess_lower']) for w in data['winners'].values())
    result=dict(status='passed',exact_product_classes=classes,collision_certificates=certificates,
                raw_exclusions_checked=len(data['raw_exclusions']),
                independent_product_method='finite coefficient expansion of character generating functions',
                incidence_scope='Uses saved incidence histograms, whose formula and implementation were independently checked by exhaustive small supports and five earlier dynamic-program certificates.',
                coverage_scope='Complete dyadic-grid and reserve-tail coverage is certified separately by certify_circle_product_dyadic.py.')
    Path('circle_product_dyadic_output_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
