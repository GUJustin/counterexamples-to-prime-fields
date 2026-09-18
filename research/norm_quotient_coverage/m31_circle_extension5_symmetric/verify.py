#!/usr/bin/env python3
"""Exact completion arithmetic for the M31 degree-five symmetric circle space."""
from decimal import Decimal,getcontext
from fractions import Fraction
from math import comb
from pathlib import Path
import json,resource,time

started=time.monotonic()
getcontext().prec=70
p=2**31-1
assert all(31%d for d in range(2,6))
ll=4
for _ in range(29): ll=(ll*ll-2)%p
assert ll==0 and 46340**2<p<46341**2
q=p**5; M=q-1; m=512; n=262144
circle_order=p+1; subgroup_size=circle_order//m
trace_image_size=subgroup_size//2+1
P=trace_image_size-3  # Exclude both branch traces and one regular reserved tag.
assert P==2**21-2
character_numerator=5*46341+2
epsilon=Fraction(character_numerator,P)
s,r,t=255,129,22
s0,r0=s-2*t,r-t
a=1-Fraction(comb(s0,2),P)
assert a>0 and 0<r0<s0 and s<=P
L0=comb(s0,r0)
overlaps=sum(Fraction(comb(r0,u)*comb(s0-r0,u))*epsilon**(2*u)
             for u in range(min(r0,s0-r0)+1))
seed=(M-1)*overlaps/(a*L0)
grid=2**320
def up(v):
    numerator=(v.numerator*grid+v.denominator-1)//v.denominator
    result=Fraction(numerator,grid)
    assert result>=v
    return numerator,result
def decimal(v):
    v=Fraction(v)
    return str(Decimal(v.numerator)/Decimal(v.denominator))
def log2(v):
    v=Fraction(v)
    return str((Decimal(v.numerator).ln()-Decimal(v.denominator).ln())/Decimal(2).ln())
seed_numerator,h=up(seed)
steps=[]
for j in range(t):
    Pj=P-s0-2*j
    gamma=Fraction(character_numerator+s0+2*j,Pj)
    numerator,h=up((h*h+gamma*gamma*h)/(1-Fraction(1,Pj)))
    steps.append({"step":j+1,"remaining_population":Pj,
                  "gamma_numerator":gamma.numerator,"gamma_denominator":gamma.denominator,
                  "hole_numerator_over_grid":numerator,"log2_hole_bound_display":log2(h),
                  "group_times_hole_bound_display":decimal(M*h)})
assert M*h<1

laurent_degree=(r-2)*m+(m-1)
dimension=2*laurent_degree+1
source_agreement=2*((r-1)*m+m-1)
near_agreement=2*(r*m+m-1)
assert laurent_degree==65535 and dimension==131071
assert source_agreement==132094 and near_agreement==133118
assert n==(s+1)*2*m
assert near_agreement-dimension==2047
# Complete-fiber counting ceiling at the next power-of-two fiber size.
next_fiber=4*m
max_full_fibers=n//next_fiber
assert max_full_fibers==128 and 2**max_full_fibers<M

receipt={
 "status":"PASS_EXACT_EXISTENCE_ON_SYMMETRIC_CIRCLE_SPACE_ONLY",
 "p":p,"primality":"Lucas-Lehmer with prime exponent31 and29 iterations",
 "extension_degree":5,"alphabet_and_challenge_field_size":q,"product_group_order":M,
 "circle_order":circle_order,"power_exponent":m,"regular_fiber_size":2*m,
 "power_subgroup_size":subgroup_size,"trace_image_size":trace_image_size,
 "excluded_tags":"the two branch traces +2,-2 and one regular reserved tag",
 "population_size":P,"character_numerator":character_numerator,
 "character_bias_denominator":P,"character_bias_display":decimal(epsilon),
 "circle_mixed_sum_bound":"10 sqrt(p)","regular_trace_population_sum_bound":"5 sqrt(p)+2",
 "final_tag_count":s,"product_cardinality":r,"completion_pairs":t,
 "seed_tag_count":s0,"seed_product_cardinality":r0,"seed_support_count":L0,
 "distinct_probability_lower_numerator":a.numerator,"distinct_probability_lower_denominator":a.denominator,
 "rounding_denominator":grid,"seed_hole_numerator_over_grid":seed_numerator,
 "seed_log2_hole_bound_display":log2(Fraction(seed_numerator,grid)),"steps":steps,
 "final_exact_integer_left":M*steps[-1]["hole_numerator_over_grid"],
 "final_exact_integer_right":grid,
 "final_exact_integer_slack":grid-M*steps[-1]["hole_numerator_over_grid"],
 "domain_length":n,"laurent_degree_bound":laurent_degree,"code_dimension":dimension,
 "exact_both_source_and_common_agreement":source_agreement,"exact_nonzero_pencil_agreement":near_agreement,
 "nonzero_near_labels":M,"source_to_near_gap":near_agreement-source_agreement,
 "capacity_margin":str(Fraction(near_agreement-dimension,n)),
 "next_full_fiber_size":next_fiber,"max_complete_fibers_at_next_size":max_full_fibers,
 "all_subsets_of_those_fibers":2**max_full_fibers,
 "next_fiber_has_fewer_supports_than_labels":True,
 "scope":"selected full trace fibers, fixed core, real Laurent circle space of dimension131071; no implementation equivalence",
 "elapsed_seconds":time.monotonic()-started,
 "peak_rss_platform_units":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
}
out=Path(__file__).with_name("receipt.json")
out.write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({"status":receipt["status"],"receipt":str(out),"M_times_h_final":decimal(M*h),
                  "code_dimension":dimension,"source_agreement":source_agreement,"near_agreement":near_agreement}))
