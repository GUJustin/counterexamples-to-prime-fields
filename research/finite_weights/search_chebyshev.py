"""Discover polynomial weights in a stable basis; certify using integers."""
from pathlib import Path
from fractions import Fraction
from functools import reduce
from math import gcd
import json
import argparse
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, eye, hstack

ROOT = Path(__file__).parent
parser = argparse.ArgumentParser()
parser.add_argument('--moments',type=Path,default=ROOT/'moments40.json')
parser.add_argument('--degrees',type=int,nargs='+',default=[20,24,28,32,36,40])
parser.add_argument('--output',type=Path,default=ROOT/'chebyshev_certificates.json')
parser.add_argument('--method',default='highs',choices=['highs','highs-ipm','highs-ds'])
parser.add_argument('--no-presolve',action='store_true')
parser.add_argument('--form',default='weight',choices=['weight','distribution'])
parser.add_argument('--stride',type=int,default=1)
parser.add_argument('--time-limit',type=float,default=60)
args = parser.parse_args()
saved = json.loads(args.moments.read_text())
moments = saved['centered_moments']
count = moments[0]
scale = 4200
lo, hi = -4169, 3991
assert args.stride >= 1
points = np.arange(lo, hi + 1, args.stride, dtype=float) / scale
basis = [[1], [0, 1]]
for j in range(2, saved['degree'] + 1):
    new = [0] * (j + 1)
    for i, a in enumerate(basis[-1]):
        new[i + 1] += 2 * a
    for i, a in enumerate(basis[-2]):
        new[i] -= scale * scale * a
    basis.append(new)
expected = [float(Fraction(sum(a*m for a,m in zip(poly,moments)),
                           count * scale**j))
            for j,poly in enumerate(basis)]
out = []
for degree in args.degrees:
    assert degree <= saved['degree']
    powers = np.polynomial.chebyshev.chebvander(points, degree)
    if args.form == 'weight':
        A = hstack([csr_matrix(powers), -eye(len(points), format='csr')], format='csr')
        result = linprog(np.r_[np.zeros(degree+1), np.ones(len(points))],
            A_ub=A, b_ub=np.zeros(len(points)),
            A_eq=csr_matrix(np.r_[expected[:degree+1], np.zeros(len(points))].reshape(1,-1)),
            b_eq=[1.0], bounds=[(None,None)]*(degree+1)+[(0,None)]*len(points),
            method=args.method,options={'presolve':not args.no_presolve,'time_limit':args.time_limit})
    else:
        A = hstack([eye(len(points),format='csr'),csr_matrix(-np.ones((len(points),1)))],format='csr')
        result = linprog(np.r_[np.zeros(len(points)),1.0],
            A_ub=A,b_ub=np.zeros(len(points)),
            A_eq=hstack([csr_matrix(powers.T),csr_matrix((degree+1,1))],format='csr'),
            b_eq=1000*np.array(expected[:degree+1]),bounds=(0,None),
            method=args.method,options={'presolve':not args.no_presolve,'time_limit':args.time_limit})
    if not result.success:
        print(degree, result, flush=True)
        continue
    # The floating-point optimizer supplies a candidate only. Rounding all
    # basis coefficients and the remaining evaluation are exact integers.
    candidate = result.x[:degree+1] if args.form == 'weight' else result.eqlin.marginals
    candidate = candidate / np.max(np.abs(candidate))
    numerical_bound = (count/result.fun if args.form == 'weight' else count*result.fun/1000)/args.stride
    rounded = [int(round(c*10**15)) for c in candidate]
    coeff = [0]*(degree+1)
    for j, b in enumerate(rounded):
        for i, a in enumerate(basis[j]):
            coeff[i] += b * a * scale**(degree-j)
    common = reduce(gcd, coeff)
    coeff = [a//common for a in coeff]
    def evaluate(x):
        value = 0
        for a in reversed(coeff):
            value = value*x + a
        return value
    numerator = sum(a*m for a,m in zip(coeff,moments))
    denominator = sum(max(0,evaluate(x)) for x in range(lo,hi+1))
    assert numerator > 0 and denominator > 0
    bound = (numerator+denominator-1)//denominator
    item = dict(degree=degree,center=saved['center'],low=lo+saved['center'],
        high=hi+saved['center'],coefficients_ascending=coeff,numerator=numerator,
        denominator=denominator,list_lower_bound=bound,
        numerical_search_bound=numerical_bound,
        numerical_chebyshev_coefficients=candidate.tolist(),numerical_scale=scale)
    out.append(item)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(degree, bound, numerical_bound, flush=True)
