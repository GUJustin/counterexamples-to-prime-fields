"""Exact product-key distribution for 136-subsets of mu_256 minus one."""
import json
import math
from pathlib import Path

m,h,p=256,136,2130706433
dp=[[0]*m for _ in range(h+1)]
dp[0][0]=1
for exponent in range(1,m):
    for size in range(min(h,exponent),0,-1):
        old=dp[size-1]
        new=dp[size]
        for residue in range(m):
            new[(residue+exponent)%m] += old[residue]
counts=dp[h]
assert sum(counts)==math.comb(m-1,h)
# Independent roots-of-unity filter, evaluated by integer Ramanujan sums.
fourier=[]
for residue in range(m):
    numerator=0
    for d in [1,2,4,8,16,32,64,128,256]:
        r=h//d
        coefficient=(-1)**(h+r)*math.comb(m//d-1,r)
        ramanujan=(1 if d==1 else d//2 if residue%d==0
                   else -d//2 if residue%(d//2)==0 else 0)
        numerator+=coefficient*ramanujan
    assert numerator%m==0
    fourier.append(numerator//m)
assert fourier==counts
maximum=max(counts)
excess_numerator=maximum*m-sum(counts)
assert excess_numerator*10**35 < sum(counts)
guarantee=(maximum+p**6-1)//p**6
required=p**6//2**128+1
assert guarantee < required
result=dict(M=m,h=h,minimum=str(min(counts)),maximum=str(maximum),
            total=str(sum(counts)),max_to_mean=maximum*m/sum(counts),
            max_to_mean_excess_numerator=str(excess_numerator),
            max_to_mean_excess_denominator=str(sum(counts)),
            excess_less_than_1e_minus_35=True,
            independent_ramanujan_check=True,
            strongest_product_then_six_coefficient_guarantee=str(guarantee),
            required=str(required),counts=[str(x) for x in counts])
Path(__file__).with_name('product_distribution.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='counts'},indent=2))
