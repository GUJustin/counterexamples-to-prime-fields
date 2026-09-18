#!/usr/bin/env python3
"""Independent Vandermonde replay; no Lagrange interpolation code imported."""
import json,hashlib,itertools,math,time
from pathlib import Path
from fractions import Fraction as Q
P=Path(__file__).resolve().parent;raw=(P/'padded_eight_certificate.json').read_bytes();d=json.loads(raw)
source_raw=(P.parent/'prime_line_strengthening/fano_seven/orbit2_independent_field_audit.json').read_bytes();src=json.loads(source_raw)
p=d['avoidance_prime'];r=d['field_root_mod_prime'];assert p==10847 and all(p%a for a in range(2,math.isqrt(p)+1));assert (r**3-10*r*r+3*r+1)%p==0

def red(v):
 out=0
 for i,c in enumerate(v):
  c=Q(c);assert c.denominator%p;out+=c.numerator*pow(c.denominator,-1,p)*pow(r,i,p)
 return out%p
x=[red(v) for v in src['affine_nodes']];w=[red(v) for v in src['affine_word']];q=tuple(red(v) for v in d['new_cubic']);fresh=d['fresh_integer_nodes'];assert fresh==[1,2,3]
assert len(set(x+fresh))==17

def evaluate(c,z):
 out=0
 for a in reversed(c):out=(out*z+a)%p
 return out

def solve(ids,xx,ww):
 A=[[1,xx[i],xx[i]**2%p,xx[i]**3%p,ww[i]] for i in ids]
 for j in range(4):
  k=next(k for k in range(j,4) if A[k][j]);A[j],A[k]=A[k],A[j]
  v=pow(A[j][j],-1,p);A[j]=[a*v%p for a in A[j]]
  for k in range(4):
   if k!=j:
    v=A[k][j];A[k]=[(a-v*b)%p for a,b in zip(A[k],A[j])]
 return tuple(A[j][4] for j in range(4))
start=time.time();matches=[i for i in range(14) if evaluate(q,x[i])==w[i]];assert matches==d['old_matches']==[2,6,7,11]
others=0;avoidance=0;unique_old=set()
for S in itertools.combinations(range(14),4):
 c=solve(S,x,w);unique_old.add(c)
 if list(S)==matches:assert c==q
 else:
  assert c!=q;others+=1
  for z in fresh:assert evaluate(c,z)!=evaluate(q,z);avoidance+=1
assert others==1000 and avoidance==3000
old_counts={c:sum(evaluate(c,z)==v for z,v in zip(x,w)) for c in unique_old};assert max(old_counts.values())==7 and sum(n==7 for n in old_counts.values())==7
neww=[evaluate(q,z) for z in fresh];assert neww==[red(v) for v in d['fresh_exact_values']]
# Independently decode EVERY four-point support on the padded domain.
xx=x+fresh;ww=w+neww;unique=set(solve(S,xx,ww) for S in itertools.combinations(range(17),4))
counts={c:sum(evaluate(c,z)==v for z,v in zip(xx,ww)) for c in unique};maximum=max(counts.values());nearest=sorted(c for c,n in counts.items() if n==maximum)
assert maximum==7 and len(nearest)==8 and q in nearest
rho=Q(10,51);a=Q(21,51);margin=(8-rho)*a*a-6*rho*a+rho*(4*rho-5);assert margin==Q(536,44217)
# rho > 11-3sqrt13: both sides in the squared comparison are positive.
assert (11-rho)>0 and (11-rho)**2<117
out=dict(status='PASS',certificate_sha256=hashlib.sha256(raw).hexdigest(),source_sha256=hashlib.sha256(source_raw).hexdigest(),method='independent 4x4 Vandermonde Gauss-Jordan, all2380 padded supports',prime=p,field_root=r,old_supports=1001,avoidance_checks=avoidance,padded_supports=math.comb(17,4),distinct_padded_interpolants=len(unique),maximum_agreement=maximum,complete_nearest_list_size=len(nearest),nearest_coefficients=nearest,first_order_polynomial_margin=str(margin),seconds=time.time()-start)
(P/'padded_eight_certificate.verified.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
