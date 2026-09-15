"""Verify the compact degree25 factored certificate using exact integers."""
import json
from math import isqrt
from pathlib import Path

ROOT=Path(__file__).resolve().parent
ROOT_NUMERATORS=[734680,2391341,4113168,6361771,9106419,12322595,
                 15989086,20095283,24650528,29671516,35141871,41012408]
ROOT_DENOMINATOR=1000000


def certify_factored(data):
    D=data['Q_denominator']
    assert D==1884025
    a,b=851547,580691
    # H(T)=product_i(R_i D - 10^6 T), expanded afresh with integers.
    H=[1]
    for r in ROOT_NUMERATORS:
        new=[0]*(len(H)+1)
        for i,c in enumerate(H):
            new[i]+=r*D*c
            new[i+1]-=ROOT_DENOMINATOR*c
        H=new
    square=[0]*(2*len(H)-1)
    for i,c in enumerate(H):
        for j,e in enumerate(H): square[i+j]+=c*e
    W=[0]*(len(square)+1)
    for i,c in enumerate(square):
        W[i]+=a*D*c
        W[i+1]-=b*c
    numerator=sum(c*int(s) for c,s in zip(W,data['Q_numerator_moment_sums']))
    assert len(W)==26
    maxT=(a*D-1)//b
    denominator=0; sites=0
    for x in range(isqrt(maxT//341)+1):
        for y in range(isqrt((maxT-341*x*x)//5)+1):
            T=341*x*x+5*y*y
            h=1
            for r in ROOT_NUMERATORS: h*=r*D-ROOT_DENOMINATOR*T
            weight=(a*D-b*T)*h*h
            assert weight>=0
            multiplicity=(1 if x==0 else 2)*(1 if y==0 else 2)
            denominator+=multiplicity*weight
            sites+=multiplicity
    assert numerator>0 and denominator>0
    bound=(numerator+denominator-1)//denominator
    assert bound==5133798314667
    return {'n':64,'t':34,'computation_t':30,
            'D':D,'A_numerator':a,'A_denominator':b,
            'root_denominator':ROOT_DENOMINATOR,'root_numerators':ROOT_NUMERATORS,
            'radial_weight_degree':25,
            'H_T_integer_coefficients':[str(c) for c in H],
            'weight_T_integer_coefficients':[str(c) for c in W],
            'exact_numerator':str(numerator),'exact_denominator':str(denominator),
            'max_T':maxT,'positive_region_lattice_points':sites,
            'certified_class_lower_bound':bound}


if __name__=='__main__':
    data=json.loads((ROOT/'moments_degree50.json').read_text())
    saved=json.loads((ROOT/'certificate_factored.json').read_text())
    assert certify_factored(data)==saved
    print(json.dumps({'factored_certificate_verified':True,
                     'certified_class_lower_bound':saved['certified_class_lower_bound']},sort_keys=True))
