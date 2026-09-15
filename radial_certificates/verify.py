"""Exact integer certificate for rational compactly supported radial weights."""
import json
from pathlib import Path
from fractions import Fraction
from math import lcm,isqrt

ROOT=Path(__file__).resolve().parent


def certify(moments,candidate):
    D=moments['Q_denominator']
    A=Fraction(*candidate['A_rational'])
    cs=[Fraction(*c) for c in candidate['h_z_rational']]
    # z=Q/A=T/(D*A); clear denominators in h(z).
    ht=[c/(D*A)**i for i,c in enumerate(cs)]
    scale=lcm(*(c.denominator for c in ht))
    H=[int(c*scale) for c in ht]
    hsquare=[0]*(2*len(H)-1)
    for i,c in enumerate(H):
        for j,e in enumerate(H): hsquare[i+j]+=c*e
    W=[0]*(len(hsquare)+1)
    for i,c in enumerate(hsquare):
        W[i]+=A.numerator*D*c
        W[i+1]-=A.denominator*c
    ms=[int(v) for v in moments['Q_numerator_moment_sums']]
    assert len(W)<=len(ms)
    numerator=sum(c*ms[i] for i,c in enumerate(W))
    maxT=(A.numerator*D-1)//A.denominator
    denominator=0
    points=0
    for x in range(isqrt(maxT//341)+1):
        xpart=341*x*x
        for y in range(isqrt((maxT-xpart)//5)+1):
            T=xpart+5*y*y
            hv=0
            for c in reversed(H): hv=hv*T+c
            w=(A.numerator*D-A.denominator*T)*hv*hv
            assert w>=0
            multiplicity=(1 if x==0 else 2)*(1 if y==0 else 2)
            denominator+=multiplicity*w
            points+=multiplicity
    assert numerator>0 and denominator>0
    return {'degree':candidate['degree'],'A_rational':candidate['A_rational'],
            'h_z_rational':candidate['h_z_rational'],'H_T_integer_coefficients':[str(c) for c in H],
            'weight_T_integer_coefficients':[str(c) for c in W],
            'exact_numerator':str(numerator),'exact_denominator':str(denominator),
            'certified_class_lower_bound':(numerator+denominator-1)//denominator,
            'positive_region_lattice_points':points,'max_T':maxT}


def main():
    data=json.loads((ROOT/'moments_degree50.json').read_text())
    saved=json.loads((ROOT/'certificate_degree12.json').read_text())
    result=certify(data,saved)
    assert result==saved
    print(json.dumps({'exact_saved_moment_verification':True,
                     'certified_class_lower_bound':result['certified_class_lower_bound']},sort_keys=True))


if __name__=='__main__': main()
