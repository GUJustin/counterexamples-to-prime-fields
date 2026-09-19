#!/usr/bin/env python3
"""Numerical target only; does not certify any received line or counterexample."""
import json
from fractions import Fraction
from pathlib import Path
import sympy as s

ell, d = s.symbols('ell d')
n = (ell**2-1)/2
k = n-4*ell+1
T = n-2*ell-d
assert s.expand(n*(k-1)-T**2-((d-4)*ell**2-4*d*ell-d**2-d)) == 0
a, rho = T/n, k/n
F = (8-rho)*a*a-6*rho*a+rho*(4*rho-5)
num = (6*ell**4-4*ell**3+387*ell**2+196*ell-291)/2
assert s.cancel((n**3*F).subs(d,5)-num)==0
assert s.expand(2*num-(2*ell**3*(3*ell-2)+387*(ell**2-1)+196*(ell-1)+292))==0
assert s.expand(k-n/2-(ell**2-16*ell+3)/4)==0
v=23; nn=(v*v-1)//2; kk=nn-4*v+1; tt=nn-2*v-5
aa, rr=Fraction(tt,nn),Fraction(kk,nn)
ff=(8-rr)*aa**2-6*rr*aa+rr*(4*rr-5)
assert 0<kk<tt<nn and rr>Fraction(1,2) and ff>0
assert nn*(kk-1)-tt*tt==39
receipt={'status':'PASS','construction_established':False,
         'scope':'symbolic threshold window only',
         'minimum_odd_prime_in_proved_window':23,
         'example':{'ell':v,'n':nn,'k':kk,'T':tt,
                    'indexed_choices':(v+1)*(v-1)*(v-3)//8,
                    'squared_johnson_slack':39,'first_order_polynomial':str(ff)}}
Path(__file__).with_suffix('.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
