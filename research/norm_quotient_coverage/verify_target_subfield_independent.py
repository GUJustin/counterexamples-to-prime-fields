"""Independent exact uniform-cap check for the target-subfield second moment."""
from fractions import Fraction as F
from math import comb, isqrt
from pathlib import Path
import json
p=2130706433
n,J,m=262144,131072,1024
M=p**6-1
P=(p-1)//m-1
s=n//m-1
w=m-1
epsilon=F(6*(isqrt(p)+1)+1,P)
a=1-F(comb(s,2),P)
assert a>0
rows=[]
for e in [1,2,3,6]:
    r=(J-1-w)//m+e+1
    L=comb(s,r)
    first=sum((F(comb(r,u)*comb(s-r,u))*epsilon**(2*u) for u in range(min(r,s-r)+1)),F(0))
    second=sum((F(comb(r,u)*comb(s-r,u))*epsilon**(r+u) for u in range(min(r,s-r)+1)),F(0))
    bound=F(M-1,L)*(first+(M-2)*second)/a
    assert 0<bound<F(1,2**22)
    targets=p**(6//e)-1
    guaranteed=targets-targets//2**22
    rows.append(dict(relative_norm_degree=e,subfield_degree=6//e,native_alphabet_degree=6//e,auxiliary_extension_degree=6,
        s=s,r=r,w=w,missing_fraction_upper_bound="2^-22 (strict)",
        target_group_order=targets,guaranteed_nearby_labels=guaranteed,guaranteed_nearby_normalized_interiors=guaranteed-1,
        exact_common_and_polynomial_source_agreement=J+m-1,
        rational_direction_agreement_upper_bound=J+e*m-1,
        exact_nearby_agreement=J+(e+1)*m-1,
        capacity_margin_numerator=(e+1)*m-1,
        common_agreement_loss_numerator=e*m,
        minimum_endpoint_loss_numerator=m))
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(dict(status='PASS_EXACT_UNIFORM_CAP',
    scope='Selected base-field fiber domains; mathematical character and compiler lemmas are inputs; no explicit tag set or prescribed-domain assertion',
    prime=p,n=n,dimension=J,fiber_size=m,cases=rows),indent=2)+'\n')
print(json.dumps({'status':'PASS','cases':len(rows),'receipt':str(out)}))
