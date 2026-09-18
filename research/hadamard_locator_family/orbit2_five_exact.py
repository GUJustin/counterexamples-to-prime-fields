"""Characteristic-zero replay of modular five-point survivors."""
from pathlib import Path
import json
base=Path(__file__).resolve().parents[1]/'prime_line_strengthening/fano_seven'
src=(base/'orbit7_independent_field_audit.py').read_text().split('w=K(')[0]
src=src.replace('c[j-1]-=2*c[j];c[j-2]+=c[j];c[j-3]+=c[j]','c[j-1]+=10*c[j];c[j-2]-=3*c[j];c[j-3]-=c[j]')
exec(src)
data=json.loads((base/'orbit2_independent_field_audit.json').read_text())
x=[K(v) for v in data['affine_nodes']];w=[K(v) for v in data['affine_word']]
def ev(c,t):
 y=K(0)
 for a in reversed(c):y=y*t+a
 return y
def mul(a,b):
 c=[K(0)]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):c[i+j]=c[i+j]+u*v
 return c
def interpolate(S):
 c=[K(0)]*4
 for i in S:
  t=[K(1)];d=K(1)
  for j in S:
   if i!=j:t=mul(t,[-x[j],K(1)]);d=d*(x[i]-x[j])
  c=[a+b*w[i]/d for a,b in zip(c,t)]
 return c
p=83
def red(z):return sum((v.numerator%p)*pow(v.denominator,-1,p)*pow(4,i,p) for i,v in enumerate(z.a))%p
banks=json.loads((base.parent/'degree_ten_four_pole_route/gate.json').read_text())
bank=next(b for b in banks if b['p']==83)
assert [red(v) for v in x]==bank['base'] and [red(v) for v in w]==bank['word']
subsets=[[2,6,7,11,13],[4,6,8,12,13]]
records=[]
for S in subsets:
 c=interpolate(S[:4]);matches=[i for i in range(14) if ev(c,x[i])==w[i]]
 records.append({'screen_subset':S,'exact_matches':matches,'coefficients':[v.out() for v in c],'fifth_residual':(ev(c,x[S[4]])-w[S[4]]).out()})
out={'field':'q^3-10q^2+3q+1','modular_order_verified':True,'cases':records,'scope':'Exact characteristic-zero interpolation and all14 evaluations; no padding or pullback claim in this script.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'cases':[{'subset':r['screen_subset'],'matches':r['exact_matches']} for r in records]}))
