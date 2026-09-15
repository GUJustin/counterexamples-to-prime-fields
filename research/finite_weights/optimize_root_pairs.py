"""Exact joint shifts of neighboring roots, avoiding single-root local traps."""
from pathlib import Path
from math import prod
import argparse
import json

ROOT = Path(__file__).parent
parser = argparse.ArgumentParser()
parser.add_argument('initial',type=Path)
parser.add_argument('output',type=Path)
parser.add_argument('--sweeps',type=int,default=12)
args = parser.parse_args()
saved = json.loads((ROOT/'moments40.json').read_text())
moments = saved['centered_moments']
cert = json.loads(args.initial.read_text())[0]
roots = cert['roots'][:]
lead = cert['coefficients_ascending'][-1]
lo,hi = -4169,3991
def coefficients(zeros):
    out = [lead]
    for r in zeros:
        new = [0]*(len(out)+1)
        for j,a in enumerate(out):
            new[j] -= r*a
            new[j+1] += a
        out = new
    return out
def score():
    c = coefficients(roots)
    return (sum(a*m for a,m in zip(c,moments)),
        sum(max(0,lead*prod(x-r for r in roots)) for x in range(lo,hi+1)))
num,den = score()
for sweep in range(args.sweeps):
    moves = 0
    for i in range(len(roots)-1):
        if roots[i+1]-roots[i] > 2:
            continue
        rest = roots[:i]+roots[i+2:]
        c = coefficients(rest)
        A = [sum(a*m for a,m in zip(c,moments[j:])) for j in range(3)]
        values = [max(0,lead*prod(x-r for r in rest)) for x in range(lo,hi+1)]
        B = [sum(p*x**j for x,p in zip(range(lo,hi+1),values)) for j in range(3)]
        lower = max(lo,roots[i-1]) if i else lo
        upper = min(hi-1,roots[i+2]-1) if i+2 < len(roots) else hi-1
        best_num,best_den,best_root = num,den,None
        for r in range(lower,upper+1):
            a = A[2]-(2*r+1)*A[1]+r*(r+1)*A[0]
            b = B[2]-(2*r+1)*B[1]+r*(r+1)*B[0]
            if a > 0 and b > 0 and a*best_den > best_num*b:
                best_num,best_den,best_root = a,b,r
        if best_root is not None:
            roots[i:i+2] = [best_root,best_root+1]
            num,den = best_num,best_den
            moves += 1
    assert score() == (num,den)
    cert.update(roots=roots[:],coefficients_ascending=coefficients(roots),
        numerator=num,denominator=den,list_lower_bound=(num+den-1)//den)
    args.output.write_text(json.dumps([cert],indent=2)+'\n')
    print('paired sweep',sweep,'moves',moves,'bound',cert['list_lower_bound'],flush=True)
    if moves == 0:
        break
