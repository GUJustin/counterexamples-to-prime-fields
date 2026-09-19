#!/usr/bin/env python3
"""Exact parameter receipt; no construction of the enormous extension."""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json

p=257
assert all(p%d for d in range(2,isqrt(p)+1))
n0=(5*p*p-1)//2
k0=3
A0=2*p
T0=isqrt(5*p*p-2)
B=(p+1)*(p*p-1)
assert T0*T0 < 2*n0 and T0>A0
t=n0-6
h=A0-k0+1
assert h<=T0-k0
blocks=(t+h-1)//h
N=n0+t
dimension=k0+t
A=A0+t
T=T0+t
assert 2*dimension==N
assert A-dimension+1==h
assert T-dimension==T0-k0
assert 3*T<2*N
assert 9*6>7*7  # (1+sqrt(6))/5 > 2/3.
assert (blocks-1)*h<t<=blocks*h

# The ideal composition/padding gap bound follows by cross multiplication.
# M*delta/(M*n0+t) <= delta/n0 for M>0,t>=0,delta>0.
relative_loss=Fraction(T-A,T-dimension)
absolute_loss=Fraction(T-A,N)
assert relative_loss==Fraction(T0-A0,T0-k0)
receipt={
    'status':'PASS',
    'scope':'exact half-rate padding ledger; all-witness justification is the conjugate-descent lemma',
    'target_constant_absolute_fractional_gap_achieved':False,
    'p':p,
    'seed':{'length':n0,'dimension':k0,'source_and_common_agreement':A0,
            'near_threshold':T0,'certified_singleton_labels':B},
    'padding':{'total_roots':t,'maximum_roots_per_step':h,'quadratic_extension_steps':blocks,
               'last_step_roots':t-(blocks-1)*h},
    'result':{'length':N,'dimension':dimension,'rate':'1/2',
              'source_and_common_agreement':A,'near_threshold':T,
              'certified_singleton_labels':B,'absolute_fractional_gap':str(absolute_loss),
              'loss_to_capacity_margin':str(relative_loss),
              'alphabet_size':f'{p}^(4*2^{blocks})',
              'extension_degree_over_prime':4*2**blocks,
              'threshold_below_two_thirds':True,
              'first_order_curve_at_half_rate_above_two_thirds':True},
    'large_extension_instantiated':False,
}
destination=Path(__file__).with_name('half_rate_padding_receipt.json')
destination.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
