"""Independent full signed-lattice moment evaluation, standard library only."""
import json
from pathlib import Path
from fractions import Fraction
from math import isqrt

ROOT=Path(__file__).resolve().parent


def crosscheck(data,certificate):
    D=data['Q_denominator']; A=Fraction(*certificate['A_rational'])
    H=list(map(int,certificate['H_T_integer_coefficients']))
    W=list(map(int,certificate['weight_T_integer_coefficients']))
    cs=[Fraction(*p) for p in certificate['h_z_rational']]
    scale=Fraction(H[0],1)/cs[0]
    for k,c in enumerate(H):
        assert Fraction(c)==scale*cs[k]/(D*A)**k

    def ev(coeff,T):
        value=0
        for c in reversed(coeff): value=value*T+c
        return value

    for T in [0,1,D,certificate['max_T'],certificate['max_T']+1,10*D]:
        assert ev(W,T)==(A.numerator*D-A.denominator*T)*ev(H,T)**2

    # Full signed coordinates and expanded moments, unlike verify.py's
    # quadrant symmetry and direct evaluation of the square.
    limit=certificate['max_T']; lattice_moments=[0]*len(W); points=0
    for x in range(-isqrt(limit//341),isqrt(limit//341)+1):
        edge=isqrt((limit-341*x*x)//5)
        for y in range(-edge,edge+1):
            T=341*x*x+5*y*y
            power=1
            for k in range(len(W)):
                lattice_moments[k]+=power
                power*=T
            points+=1
    den=sum(c*s for c,s in zip(W,lattice_moments))
    num=sum(c*int(s) for c,s in zip(W,data['Q_numerator_moment_sums']))
    assert den==int(certificate['exact_denominator'])
    assert num==int(certificate['exact_numerator'])
    assert points==certificate['positive_region_lattice_points']
    assert (num+den-1)//den==certificate['certified_class_lower_bound']
    return {'full_signed_lattice_points':points,
            'lattice_moment_degree':len(W)-1,
            'exact_denominator_crosscheck':True,
            'rational_to_integer_coefficient_crosscheck':True}


if __name__=='__main__':
    data=json.loads((ROOT/'moments_degree50.json').read_text())
    saved=json.loads((ROOT/'certificate_degree12.json').read_text())
    print(json.dumps(crosscheck(data,saved),sort_keys=True))
