#!/usr/bin/env python3
"""Targeted exact boundary checks for the conditional Galois theorem."""
from collections import Counter
import json
from pathlib import Path

p=7
D=list(range(1,p))
D3=[x for x in D if pow(x,3,p)==1]
perms={tuple(a*x%p for x in D3) for a in D3}
perms|={tuple(a*pow(x,-1,p)%p for x in D3) for a in D3}
assert len(perms)==6

# A raw nonsquare does not ensure every reflection is free.
alpha=3
assert alpha not in {x*x%p for x in D}
fixed=[x for x in D if 4*pow(x,-1,p)%p==x]
assert fixed==[2,5]
projected=pow(alpha,2,p)
assert projected in {x*x%p for x in D3}
bad_fibers=Counter((x*x+projected*pow(x*x,-1,p))%p for x in D)
assert sorted(bad_fibers.values())==[2,4]

# n=B=6, d=3, projected twist -1 in mu_2: one full simple fiber.
assert { (pow(x,3,p)-pow(pow(x,3,p),-1,p))%p for x in D }=={0}
assert all((6*pow(x,5,p))%p !=0 for x in D)
# Its deck group: rotations by mu_3 and reflections alpha*mu_3/X.
deck=[tuple(a*x%p for x in D) for a in D3]
deck += [tuple(alpha*a*pow(x,-1,p)%p for x in D) for a in D3]
assert len(set(deck))==6
assert all(all(y!=x for x,y in zip(D,g)) for g in deck if g!=tuple(D))

# X^4 is geometrically Galois in characteristic seven, but only two
# fourth-root rotations descend to F_7.
assert [x for x in D if pow(x,4,p)==1]==[1,6]

out=dict(status='all exact assertions passed',n3_stabilizer_order=6,
         raw_twist_counterexample_fixed_points=fixed,
         raw_twist_fiber_sizes=sorted(bad_fibers.values()),
         one_fiber_dihedral_group_order=6,
         arithmetic_deck_order_for_degree4_power_over_F7=2)
Path(__file__).with_name('galois_boundaries_verified.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
