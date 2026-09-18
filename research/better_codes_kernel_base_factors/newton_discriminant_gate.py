"""Exact finite supporting-line certificate; no optimization library."""
from fractions import Fraction as Q
import json
from pathlib import Path
n=262144; w=131071; q=43; r=12; t=3261; C=6802316684345

def box(a,b,h): return a*b*(t+1-h)-b*a*(a-1)//2-a*b*(b-1)//2

def rank(a):
 return sum(box(k+1,r+1,0)-box(max(k+1-(a-k),0),max(r+1-(a-k),0),a-k) for k in range(a))

def phi(a): return sum(max(0,a-j,2*(a-j-r)) for j in range(1,q))
slope=Q(27,715793); intercept=-Q(5633856,55061); loss=Q(640622,55061)
rows=[]
for a in range(68):
 b=max(0,(a-q+1)//2)
 slack=phi(a)-slope*rank(a)-intercept+loss*b
 assert slack>=0
 rows.append(dict(a=a,rank=rank(a),phi=phi(a),minimum_B_order=b,slack=str(slack)))
bound=slope*(C-1)+n*intercept-12*loss
lower=-(-bound.numerator//bound.denominator)
upper=q*(q-1)*w+(2*q-2)*12
out=dict(slope=str(slope),intercept=str(intercept),loss=str(loss),rational_lower=str(bound),lower=lower,upper=upper,residual=upper-lower,rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='rows'})
