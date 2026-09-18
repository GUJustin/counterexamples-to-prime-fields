"""Independent flint-backed PRS and extension-field replay; no Sage."""
import json,hashlib,time
from pathlib import Path
from flint import nmod_poly,fq_default_ctx,fq_default_poly_ctx,fmpz_mod_poly_ctx
P=Path(__file__).parent;raw=(P/'reconstruction.json').read_bytes();d=json.loads(raw);saved=json.loads((P/'conic.json').read_text());assert saved['input_sha256']==hashlib.sha256(raw).hexdigest()
p=29;zero=nmod_poly([],p);one=nmod_poly([1],p)
def trim(f):
 while f and not f[-1]:f.pop()
 return f
def prem(f,g):
 r=f[:];m=len(g)-1;n=len(f)-1;remaining=n-m+1;lc=g[-1]
 while r and len(r)-1>=m:
  delta=len(r)-1-m;c=r[-1];r=[v*lc for v in r]
  for j,v in enumerate(g):r[j+delta]-=c*v
  trim(r);remaining-=1
 if remaining and r:r=[v*(lc**remaining) for v in r]
 return r
def exact_div(f,b):
 out=[]
 for v in f:
  q,r=divmod(v,b);assert not r;out.append(q)
 return trim(out)
f=[]
for terms in d['residual_coefficient_terms']:
 cc=[0]*37
 for (i,j),c in terms:cc[36-i-2*j]=(cc[36-i-2*j]+c*pow(5,18-i-j,p))%p
 f.append(nmod_poly(cc,p))
assert list(map(int,f[48].coeffs()))==saved['leading_coefficient']
# Independent projective-substitution checks at fixed parameters, including0.
for u in (0,1,2,7):
 for coeff,terms in zip(f,d['residual_coefficient_terms']):
  homogeneous=sum(c*pow(5*u*u,18-i-j,p)*pow(u,i,p) for (i,j),c in terms)%p
  assert int(coeff(u))==homogeneous
lc0=f[-1];g=trim([f[i]*i for i in range(1,len(f))]);a=f[:];b=g[:]
n,m=len(a)-1,len(b)-1;delta=n-m
h=[v*((-1)**(delta+1)) for v in prem(a,b)]
lc=b[-1];c=-(lc**delta);necessary=zero;profile=[];start=time.monotonic()
while h:
 k=len(h)-1;profile.append(k)
 if k<15:
  for v in h:necessary=necessary.gcd(v)
  # Stop as soon as every possible necessary root is a degree-drop root.
  rem=necessary
  while rem.degree()>0:
   common=rem.gcd(lc0)
   if common.degree()==0:break
   rem=rem//common
  if rem.degree()==0:break
 a,b,m,delta=b,h,k,m-k
 beta=-lc*(c**delta)
 h=exact_div(prem(a,b),beta)
 lc=b[-1]
 if delta>1:
  num=(-lc)**delta;den=c**(delta-1);c,rr=divmod(num,den);assert not rr
 else:c=-lc
assert necessary and rem.degree()==0, 'Coverage did not close on the leading locus'
# Verify the supplied candidate factors exhaust the leading polynomial.
unit,factors=lc0.factor();savedfac={tuple(v['coefficients']) for v in saved['leading_factors']}
assert {tuple(map(int,z.coeffs())) for z,e in factors}==savedfac
checks=[]
for fac,e in factors:
 if fac.degree()==1:
  root=-int(fac[0])*pow(int(fac[1]),-1,p)%p
  ff=nmod_poly([int(c(root)) for c in f],p);x=nmod_poly([0,1],p)
 else:
  F=fq_default_ctx(modulus=fmpz_mod_poly_ctx(29)(list(map(int,fac.coeffs()))),var='r');C=fq_default_poly_ctx(F);root=F.gen()
  vals=[]
  for c0 in f:
   v=F(0)
   for z in reversed(c0.coeffs()):v=v*root+int(z)
   vals.append(v)
  ff=C(vals);x=C([0,1])
 assert ff
 gx=ff.derivative();gv=48*ff-x*gx
 gd=gx.gcd(gv).degree()+min(47-gx.degree(),47-gv.degree())
 expected=next(v for v in saved['algebraic_tests'] if v['factor']==list(map(int,fac.coeffs())))
 assert gd==expected['homogeneous_partial_gcd_degree']<15
 checks.append({'factor_degree':fac.degree(),'residual_degree':ff.degree(),'homogeneous_gcd':gd})
ep=nmod_poly([sum(c for (i,j),c in terms if i==j==0)%p for terms in d['residual_coefficient_terms']],p);x=nmod_poly([0,1],p)
gx=ep.derivative();gv=48*ep-x*gx;egd=gx.gcd(gv).degree()+min(47-gx.degree(),47-gv.degree());assert egd==4
out={'status':'PASS','reconstruction_sha256':hashlib.sha256(raw).hexdigest(),'independent_PRS_degrees':profile,'necessary_gcd_coefficients':list(map(int,necessary.coeffs())),
 'all_necessary_roots_are_leading_degree_drop':True,'residue_checks':checks,'endpoint_homogeneous_gcd':egd,'seconds':time.monotonic()-start}
(P/'conic.independent.json').write_text(json.dumps(out,indent=2));print(out)
