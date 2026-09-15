"""Exact coordinate ascent for a monic integer-root polynomial certificate."""
from pathlib import Path
from math import prod
import json
import argparse

ROOT = Path(__file__).parent
parser = argparse.ArgumentParser()
parser.add_argument('--initial',type=Path)
parser.add_argument('--output',type=Path,default=ROOT/'integer28_certificates.json')
parser.add_argument('--sweeps',type=int,default=12)
args = parser.parse_args()
saved = json.loads((ROOT/'moments40.json').read_text())
moments = saved['centered_moments']
lo,hi = -4169,3991
roots = [-4169,-3153,-3149,-2641,-2637,-2161,-2157,-1697,-1685,-1273,-1209,
         -901,-709,-561,567,711,903,1207,1271,1671,1683,2127,2131,2587,2591,
         3071,3075,3991]
leading = 1
if args.initial:
    initial = json.loads(args.initial.read_text())[0]
    roots = initial['roots'][:]
    leading = initial['coefficients_ascending'][-1]
assert leading in [-1,1]

def coefficients(zeros):
    coeff = [leading]
    for r in zeros:
        new = [0]*(len(coeff)+1)
        for j,a in enumerate(coeff):
            new[j] -= r*a
            new[j+1] += a
        coeff = new
    return coeff

def save():
    coeff = coefficients(roots)
    num = sum(a*m for a,m in zip(coeff,moments))
    den = sum(max(0,leading*prod(x-r for r in roots)) for x in range(lo,hi+1))
    cert = dict(degree=len(roots),center=22138,low=17969,high=26129,roots=roots[:],
        coefficients_ascending=coeff,numerator=num,denominator=den,
        list_lower_bound=(num+den-1)//den)
    args.output.write_text(json.dumps([cert],indent=2)+'\n')
    return cert['list_lower_bound']

print('initial',save(),flush=True)
for sweep in range(args.sweeps):
    moves = 0
    for i,old_root in enumerate(roots):
        if not lo <= old_root <= hi:
            continue
        rest = roots[:i]+roots[i+1:]
        coeff = coefficients(rest)
        A0 = sum(a*m for a,m in zip(coeff,moments))
        A1 = sum(a*m for a,m in zip(coeff,moments[1:]))
        values = [leading*prod(x-r for r in rest) for x in range(lo,hi+1)]
        pos0 = sum(max(0,p) for p in values)
        pos1 = sum(x*max(0,p) for x,p in zip(range(lo,hi+1),values))
        left_pos0 = left_pos1 = left_neg0 = left_neg1 = 0
        lower = roots[i-1] if i else lo
        upper = roots[i+1] if i+1 < len(roots) else hi
        best_num = best_den = best_root = None
        old_num = old_den = None
        for r,p in zip(range(lo,hi+1),values):
            if p >= 0:
                left_pos0 += p
                left_pos1 += r*p
            else:
                left_neg0 -= p
                left_neg1 -= r*p
            if not lower <= r <= upper:
                continue
            num = A1-r*A0
            den = pos1-left_pos1-r*(pos0-left_pos0)+r*left_neg0-left_neg1
            if r == old_root:
                old_num,old_den = num,den
            if num > 0 and den > 0 and (best_num is None or num*best_den > best_num*den):
                best_num,best_den,best_root = num,den,r
        assert old_num is not None and old_den > 0
        if best_num*old_den > old_num*best_den:
            roots[i] = best_root
            moves += 1
    print('sweep',sweep,'moves',moves,'bound',save(),flush=True)
    if moves == 0:
        break
