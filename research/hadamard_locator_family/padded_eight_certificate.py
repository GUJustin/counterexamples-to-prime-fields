"""Explicit finite complete eight-cubic bank via generic padding."""
import json,itertools
from pathlib import Path
from fractions import Fraction as F
base=Path(__file__).resolve().parents[1]/'prime_line_strengthening/fano_seven'
data=json.loads((base/'orbit2_independent_field_audit.json').read_text())
source=json.loads(Path(__file__).with_name('orbit2_five_exact.json').read_text())
qcoeff=source['cases'][0]['coefficients']; S=source['cases'][0]['exact_matches'];assert len(S)==4
p=10847;r=100
assert all(p%d for d in range(2,int(p**.5)+1))
assert (r**3-10*r*r+3*r+1)%p==0

def red(v):
 out=0
 for i,a in enumerate(v):
  a=F(a);assert a.denominator%p
  out+=a.numerator*pow(a.denominator,-1,p)*pow(r,i,p)
 return out%p
x=[red(v) for v in data['affine_nodes']];w=[red(v) for v in data['affine_word']];Q=[red(v) for v in qcoeff]
assert len(set(x))==14

def ev(c,t):return sum(a*pow(t,i,p) for i,a in enumerate(c))%p
def interpolate(S):
 c=[0]*4
 for i in S:
  poly=[1];den=1
  for j in S:
   if i==j:continue
   z=[0]*(len(poly)+1)
   for k,a in enumerate(poly):z[k]=(z[k]-x[j]*a)%p;z[k+1]=(z[k+1]+a)%p
   poly=z;den=den*(x[i]-x[j])%p
  m=w[i]*pow(den,-1,p)%p;c=[(a+m*b)%p for a,b in zip(c,poly)]
 return c
others=[]
for T in itertools.combinations(range(14),4):
 c=interpolate(T)
 if list(T)==S:assert c==Q
 else:assert c!=Q;others.append(c)
fresh=[]
for t in range(1,p):
 if t not in x and all(ev(c,t)!=ev(Q,t) for c in others):fresh.append(t)
 if len(fresh)==3:break
assert len(fresh)==3
unique={tuple(c) for c in others+[Q]}
old_counts={c:sum(ev(c,t)==v for t,v in zip(x,w)) for c in unique}
assert max(old_counts.values())==7 and sum(v==7 for v in old_counts.values())==7
assert sum(ev(Q,t)==v for t,v in zip(x,w))==4
# Exact appended values using already audited rational cubic-field arithmetic.
src=(base/'orbit7_independent_field_audit.py').read_text().split('w=K(')[0]
src=src.replace('c[j-1]-=2*c[j];c[j-2]+=c[j];c[j-3]+=c[j]','c[j-1]+=10*c[j];c[j-2]-=3*c[j];c[j-3]-=c[j]')
exec(src)
def exact_ev(c,t):
 a=K(0)
 for v in reversed(c):a=a*t+K(v)
 return a
out={'field':'q^3-10q^2+3q+1','source':'orbit2_independent_field_audit.json','new_cubic':qcoeff,'old_matches':S,'fresh_integer_nodes':fresh,'fresh_exact_values':[exact_ev(qcoeff,t).out() for t in fresh],'avoidance_prime':p,'field_root_mod_prime':r,'distinct_old_nodes_mod_prime':14,'other_four_point_interpolants_checked':len(others),'fresh_avoidance_checks':3*len(others),'old_modular_max_agreement':7,'old_modular_complete_list_size':7,'new_modular_complete_list_size':8,'source_parameters':{'n':17,'k':4,'agreement':7,'complete_nearest_list_size':8},'cubic_pullback_parameters':{'n':51,'k':10,'agreement':21,'list_size_lower_bound':8,'complete_list_claim':False},'first_order_polynomial_margin':'536/44217','scope':'Finite baseline only; no growing-list or better.codes claim.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'fresh':fresh,'checks':len(others)*3,'source':out['source_parameters'],'pullback':out['cubic_pullback_parameters']}))
