"""Closed binary-square-factor modular screen; degenerations are retained."""
import json,itertools,time
from fractions import Fraction
from pathlib import Path
from flint import nmod_mat,nmod_poly
P=Path(__file__).parent;p=47;start=time.monotonic();d=json.loads((P/'rational_seed.json').read_text());fr=json.loads((P/'pair_padding_gate.json').read_text())['candidates']
def red(s):
 q=Fraction(s);return q.numerator*pow(q.denominator,-1,p)%p
def ev(c,x):return sum(a*pow(x,j,p) for j,a in enumerate(c))%p
X=list(map(red,d['affine_nodes']))+[3,17];W=list(map(red,d['affine_word']));Q=list(map(red,fr[0]['coefficients']));W +=[ev(Q,x) for x in X[16:]]
assert len(set(X))==18
norm=[[w*pow(x,i,p)%p for i in range(4)]+[pow(x,i,p) for i in range(7)]+[-w*w%p] for x,w in zip(X,W)]
full=[[[pow(x,i,p) for i in range(4)]+[0]*7+[-2*w%p],[0]+[i*w*pow(x,i-1,p)%p for i in range(1,4)]+[0]+[i*pow(x,i-1,p)%p for i in range(1,7)]+[0]] for x,w in zip(X,W)]
def solve(rows):
 global coefficient_rank
 A,r=nmod_mat(rows,p).rref();piv=[];coefficient_rank=r
 for i in range(r):
  c=next(j for j in range(12) if A[i,j])
  if c==11:
   coefficient_rank=r-1;return None
  piv.append(c)
 v=[0]*11
 for i,c in enumerate(piv):v[c]=int(A[i,11])
 free=[j for j in range(11) if j not in piv];basis=[]
 for j in free:
  z=[0]*11;z[j]=1
  for i,c in enumerate(piv):z[c]=-int(A[i,j])%p
  basis.append(z)
 return v,basis
cache={};accepted=[];unresolved=[];counts={};rank_exceptional=[]
def consider(v,origin):
 key=tuple(v)
 if key not in cache:
  E=nmod_poly([-a*pow(2,-1,p)%p for a in v[:4]],p);J=E*E-nmod_poly(v[4:],p)
  odd=0 if J.is_zero() else sum(f.degree() for f,e in J.factor()[1] if e%2)+(6-J.degree())%2
  cache[key]=odd
 if cache[key]<=2:accepted.append(dict(origin,B=v[:4],C=v[4:],binary_odd_degree=cache[key]))
for size in [12,11]:
 for sub in itertools.combinations(range(18),size):
  rows=[norm[j] for j in sub];sol=solve(rows)
  if coefficient_rank<11:rank_exceptional.append({'subset':sub,'modular_coefficient_rank':coefficient_rank})
  if sol is None:continue
  v,basis=sol
  if size==12:
   if basis:unresolved.append({'subset':sub,'dimension':len(basis)})
   else:consider(v,{'subset':sub})
  elif not basis:
   good=[j for j in sub if all(sum(a*b for a,b in zip(row[:11],v))%p==row[11] for row in full[j])]
   if len(good)>=2:consider(v,{'subset':sub,'full_pair':good[:2]})
  else:
   for pair in itertools.combinations(sub,2):
    ss=solve(rows+[row for j in pair for row in full[j]])
    if ss is None:continue
    vv,bb=ss
    if bb:unresolved.append({'subset':sub,'full_pair':pair,'dimension':len(bb)})
    else:consider(vv,{'subset':sub,'full_pair':pair})
out={'prime':p,'nodes':X,'word':W,'accepted_systems':accepted,'unresolved_systems':unresolved,'rank_exceptional_systems':rank_exceptional,'norms_tested':len(cache),'accepted_distinct_norms':len({tuple(r['B']+r['C']) for r in accepted}),'seconds':time.monotonic()-start}
(P/'ten_quadratic_norm_screen.json').write_text(json.dumps(out,indent=2));print({k:(len(v) if isinstance(v,list) else v) for k,v in out.items()})
