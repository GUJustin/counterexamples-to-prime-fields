#!/usr/bin/env python3
"""Exact algebra/parameter gate; the finite example is canonical padding."""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json
import sympy as sp
from flint import nmod_poly

X, Y, pole, kap = sp.symbols('X Y pole kap')
C, B, Cz, Bz = sp.symbols('C B Cz Bz')
L = (Y*Y-pole*pole+kap)*C+(Y-pole)*B
Lz = (Y*Y-pole*pole+kap)*Cz+(Y-pole)*Bz
assert sp.expand(Lz*C-L*Cz-(Y-pole)*(Bz*C-B*Cz)) == 0
assert sp.expand(L-Y*Y*C-((Y-pole)*B+(kap-pole*pole)*C)) == 0

z = sp.symbols('z')
cc = sp.symbols('c0:5')
bb = sp.symbols('b0:6')
Cp = X**5+sum(cc[i]*X**i for i in range(5))
Bp = sum(bb[i]*X**i for i in range(6))
rotation = sp.Poly(sp.expand(Bp.subs(X,z*X)*Cp-Bp*Cp.subs(X,z*X)),X)
assert rotation.degree()==9
assert rotation.coeff_monomial(1)==0

s = sp.symbols('s')
m = 2*s
n = s*m
k = n-4*m+1
T = n-2*m-5
rho, agreement = k/n, T/n
curve = (8-rho)*agreement**2-6*rho*agreement+rho*(4*rho-5)
numerator = 48*s**4-16*s**3+742*s**2+160*s-25
assert sp.cancel(curve-numerator/(8*s**6))==0
assert sp.expand(T*T-n*(k-1)-(-4*s*s+40*s+25))==0
positive_curve_shift = sp.Poly(sp.expand(numerator.subs(s,s+16)),s)
assert all(c>0 for c in positive_curve_shift.all_coeffs())
positive_johnson_shift = sp.Poly(sp.expand((4*s*s-40*s-25).subs(s,s+16)),s)
assert all(c>0 for c in positive_johnson_shift.all_coeffs())

# Complete, small finite algebra fixture. It intentionally has gcd degree 5.
p=65537
assert all(p%j for j in range(2,isqrt(p)+1))
generator=3
assert pow(generator,(p-1)//2,p)==p-1
ss=16; mm=32; nn=512; kk=385; threshold=443; source_agreement=416
omega=pow(generator,(p-1)//nn,p)
domain=[pow(omega,j,p) for j in range(nn)]
assert len(set(domain))==nn and pow(omega,nn//2,p)!=1
tags=sorted({pow(x,mm,p) for x in domain})
assert len(tags)==ss
b=generator
assert b not in tags
alpha,beta=tags[:2]
padding=[]
for x in domain:
    if pow(x,mm,p) not in (alpha,beta):
        padding.append(x)
        if len(padding)==5:
            break

xx=nmod_poly([0,1],p)
yy=xx**mm
cp=nmod_poly([1],p)
for x in padding:
    cp*=xx-x
bp=-(alpha+beta)*cp
kappa=((b-alpha)*(b-beta))%p
assert kappa
lp=(yy**2-b*b+kappa)*cp+(yy-b)*bp
domain_poly=xx**nn-1
quotient,remainder=divmod(domain_poly,lp)
assert not remainder
gcd=cp.gcd(bp)
assert gcd.degree()==5
cleared=quotient*cp
label=(pow(b,ss,p)-1)*pow(kappa,-1,p)%p
witness,remainder=divmod(xx**(nn-2*mm)-pow(b,ss-2,p)+label-cleared,yy-b)
assert not remainder and witness.degree()==kk-1
agreement_points=[]
for x in domain:
    y=pow(x,mm,p)
    value=(pow(y,ss-2,p)-pow(b,ss-2,p)+label)*pow((y-b)%p,-1,p)%p
    if int(witness(x))==value:
        agreement_points.append(x)
assert len(agreement_points)==nn-2*mm==448
assert lp.degree()==2*mm+5 and cleared.degree()==nn-2*mm
assert all(int(cleared[i])==0 for i in range(nn-3*mm+1,nn-2*mm))

arc=nmod_poly([1],p)
for j in range(2*mm+5):
    arc*=xx-pow(omega,j,p)
assert arc.degree()==2*mm+5
assert all(int(arc[i])!=0 for i in range(arc.degree()+1))

rr=Fraction(kk,nn); aa=Fraction(threshold,nn)
curve_value=(8-rr)*aa*aa-6*rr*aa+rr*(4*rr-5)
assert curve_value>0 and nn*(kk-1)-threshold**2>0
receipt={
    'status':'PASS',
    'positive_outsider_found':False,
    'scope':'exact equivalence and canonical-padding rejection; no search',
    'primitive_target':{'m':'2s','n':'2s^2','deficit':5,'C_degree':5,
                        'B_degree_at_most':5,'gcd_C_B':1,
                        'error_locator_degree':'4s+5','field_parameter_count':12},
    'rotation_numerator_degree':rotation.degree(),
    'rotation_numerator_constant_term':int(rotation.coeff_monomial(1)),
    'nontrivial_rotation_intersection_bound':8,
    'opposite_pair_bound':4,
    'curve_numerator_after_s_plus_16':str(positive_curve_shift.as_expr()),
    'johnson_slack_after_s_plus_16':str(positive_johnson_shift.as_expr()),
    'finite_parameters':{'p':p,'s':ss,'m':mm,'n':nn,'dimension':kk,
                         'source_and_common_agreement':source_agreement,
                         'tested_agreement':threshold,'curve_polynomial':str(curve_value),
                         'squared_johnson_slack':nn*(kk-1)-threshold**2},
    'padding_fixture':{'generator':generator,'domain_generator':omega,'pole':b,
                       'omitted_full_fiber_tags':[alpha,beta],'padding_roots':padding,
                       'kappa':kappa,'label':label,'gcd_degree':gcd.degree(),
                       'witness_degree':witness.degree(),
                       'verified_agreements':len(agreement_points),
                       'is_genuine_outsider':False},
    'single_progression':{'length':arc.degree(),'all_coefficients_nonzero':True},
}
destination=Path(__file__).with_name('outsider_system_receipt.json')
destination.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
