"""Bounded exact modular conic locus; sage -python, no parameter scan.

All coefficients of low-degree subresultants give NECESSARY conditions,
avoiding assumptions about the CAS's principal-subresultant indexing.
Degree-drop roots are retained and then tested homogeneously.
"""
import argparse,hashlib,json,time
from pathlib import Path
from sage.all import GF,PolynomialRing
ap=argparse.ArgumentParser()
ap.add_argument('--input',type=Path,default=Path(__file__).with_name('reconstruction.json'))
ap.add_argument('--output',type=Path,default=Path(__file__).with_name('conic_subresultants.json'))
args=ap.parse_args();raw=args.input.read_bytes();data=json.loads(raw)
assert data['p']==29 and data['interpolation_verified_at_all_190_nodes']
k=GF(29);A=PolynomialRing(k,'u');u=A.gen();PX=PolynomialRing(A,'X');X=PX.gen()
kappa=k(5);start=time.monotonic()
out={'input_sha256':hashlib.sha256(raw).hexdigest(),'p':29,
 'parameterization':'[a:b:c]=[5u^2:u:1]','endpoint':'[1:0:0]',
 'status':'started','scope':'All algebraic parameters on the modular conic; necessary rationality condition only.'}
def checkpoint():
 out['seconds']=time.monotonic()-start
 tmp=args.output.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2));tmp.replace(args.output)
def coeffs(f):return list(map(int,f.list()))
def factor_record(f):
 return [{'coefficients':coeffs(g),'degree':int(g.degree()),'exponent':int(e)} for g,e in f.factor()]
# Every saved residual coefficient homogenizes to parameter degree18.
cc=[]
for terms in data['residual_coefficient_terms']:
 cc.append(sum((k(c)*kappa**(18-i-j)*u**(36-i-2*j) for (i,j),c in terms),A.zero()))
f=PX(cc);assert f.degree()==48
lc=A(f[48]);out.update(stage='coefficients_ready',parameter_degree=int(max(c.degree() for c in cc)),
                      leading_coefficient=coeffs(lc),leading_factors=factor_record(lc));checkpoint()
seq=f.subresultants(f.derivative())
out['subresultant_profile']=[{'X_degree':int(g.degree()),'maximum_parameter_degree':int(max(c.degree() for c in g.list() if c))} for g in seq]
# Every subresultant is an integral polynomial combination of f and f'.
# If their specialized gcd has degree>=15, ANY combination whose X degree
# is <15 must vanish identically. Thus all its coefficients must vanish.
low=[g for g in seq if 0<=g.degree()<15]
h=A.zero()
for g in low:
 for c in g.list():h=h.gcd(c)
out.update(stage='subresultants_complete',low_polynomials=len(low),necessary_gcd=coeffs(h));checkpoint()
if not h:
 out.update(status='inconclusive',reason='No nonzero low-degree combination; generic conic may already satisfy the bound.');checkpoint();raise SystemExit
# Nonzero leading coefficient: all true candidates are roots of h.
# Leading-zero parameters are retained regardless of h, since infinity
# can contribute to the homogeneous gcd condition.
candidate=h*lc
out['candidate_factors']=factor_record(candidate);out['algebraic_tests']=[];checkpoint()
for fac,exponent in candidate.factor():
 if fac.degree()==1:
  E=k;root=-fac[0]/fac[1]
 else:
  E=k.extension(fac,'rho');root=E.gen()
 EX=PolynomialRing(E,'x');x=EX.gen();ff=EX([E(c(root)) for c in cc])
 if not ff:
  test={'factor':coeffs(fac),'status':'zero_discriminant_not_integral_separable_candidate'}
 else:
  gx=ff.derivative();gv=E(48)*ff-x*gx
  finite=int(gx.gcd(gv).degree())
  # A zero partial has vanishing order at infinity at least47; the other
  # determines the common order. Degrees -1 convention does not affect
  # min when the other partial is nonzero.
  infinity=min(47-int(gx.degree()),47-int(gv.degree()))
  gd=finite+infinity
  test={'factor':coeffs(fac),'degree':int(fac.degree()),'residual_X_degree':int(ff.degree()),
        'homogeneous_partial_gcd_degree':gd,'passes_necessary_bound':gd>=15}
 out['algebraic_tests'].append(test);checkpoint()
# At u=infinity the projective member is F0. Its homogeneous residual is
# obtained by setting (a,b,c)=(1,0,0), not by dropping an affine parameter.
ep=PX([sum((k(c) for (i,j),c in terms if i==0 and j==0),k.zero()) for terms in data['residual_coefficient_terms']])
EP=PolynomialRing(k,'x');ep=EP(ep.list());xx=EP.gen()
if ep:
 gx=ep.derivative();gv=k(48)*ep-xx*gx
 out['endpoint_test']={'member':'F0','residual_X_degree':int(ep.degree()),
  'homogeneous_partial_gcd_degree':int(gx.gcd(gv).degree())+min(47-int(gx.degree()),47-int(gv.degree())),
  'separate_known_scope':'The eigenmember has genus at least6 by the saved Kummer certificate.'}
else:out['endpoint_test']={'member':'F0','zero_discriminant':True}
out['status']='complete';checkpoint();print(json.dumps(out,indent=2),flush=True)
