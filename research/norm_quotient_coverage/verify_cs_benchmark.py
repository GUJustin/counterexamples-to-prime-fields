"""Rigorous Arb evaluation of the CS sufficient condition at benchmark parameters."""
from pathlib import Path
import json
from flint import arb, ctx

ctx.prec = 256
p, n, k = 2130706433, 262144, 131072
q = p**6

def evaluate(t):
    x = arb(n-t)/n
    entropy = (x*arb(q-1).log()-x*x.log()-(1-x)*(1-x).log())/arb(q).log()
    a = n*entropy-(n-t)
    residual = n*(1-entropy)+2+a.sqrt()-k
    return a, residual

records = []
for t in (132442, 132443, 139782):
    a, residual = evaluate(t)
    assert (residual < 0) if t == 132442 else (residual > 0)
    records.append(dict(agreement=t, entropy_auxiliary=str(a),
                        condition_residual=str(residual),
                        condition_passes=(t == 132442)))

# A'(T)=log((n-T)/T)/log(q)-log(1-1/q)/log(q) is decreasing.
# It is negative at the left endpoint of the comparison interval.
left = k+2
derivative_left = (arb(n-left)/left).log()/arb(q).log()-(1-arb(1)/q).log()/arb(q).log()
assert derivative_left < 0
assert evaluate(139782)[0] > arb(1)/4
# Thus A decreases but stays above 1/4, and F'=1-A'(1-1/(2sqrt(A)))>1.
score = -128*(arb(132442)/n).log()/arb(2).log()
result = dict(prime=p, alphabet=str(q), length=n, dimension=k,
              arithmetic='Arb real balls, 256-bit precision',
              records=records, derivative_left=str(derivative_left),
              largest_passing_threshold_in_interval=132442,
              interval=[left,139782],
              capacity_margin='1370/262144', score_expression=str(score),
              scope='CS sufficient-condition comparison only; no Lean certificate or improved benchmark')
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
