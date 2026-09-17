"""Independent integer audit of the archived equal-fiber counting frontier.

Pure finite combinatorics; no protocol execution or submission.
"""
import json
import math
from decimal import Decimal, localcontext
from pathlib import Path

p = 2130706433
n = 262144
required = p**6 // 2**128 + 1
with localcontext() as ctx:
    ctx.prec = 70
    def score(a):
        return -Decimal(128) * (Decimal(a)/n).ln()/Decimal(2).ln()
    target = next(a for a in range(139775, 139800) if score(a) <= Decimal('116.12'))
    boundary = {str(a): str(score(a)) for a in [139775,target-1,target]}

rows = []
for j in range(1,19):
    b = 2**j
    m = n//b
    H = (target+1+b-1)//b
    h = H-1
    r = max(0,H-m//2-3)
    if h>m-1:
        continue
    numerator = math.comb(m-1,h)
    denominator = m*p**r
    count = (numerator+denominator-1)//denominator
    assert count < required
    rows.append(dict(B=b,M=m,H=H,r=r,agreement=H*b-1,
                     certified_count=str(count),
                     sufficient=numerator > denominator*(required-1),
                     missing_bits=math.log2(required)-math.log2(count)))
best=max(rows,key=lambda row:int(row['certified_count']))
result=dict(p=p,n=n,required_count=str(required),target_agreement=target,
            boundary_scores=boundary,rows=rows,best_failed_alternative=best)
Path(__file__).with_name('frontier.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(target=target,required=str(required),best=best,boundary=boundary),indent=2))
