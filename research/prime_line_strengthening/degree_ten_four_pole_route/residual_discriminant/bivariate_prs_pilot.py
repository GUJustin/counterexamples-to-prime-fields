"""Bounded direct Brown subresultant PRS over F29[s,t], not a determinant job.

Only a cost pilot unless the degree14 remainder is reached. Exact divisions
and independent field-specialized PRS comparisons are checked at each stage.
"""
import argparse,hashlib,json,time
from pathlib import Path
from flint import nmod_mpoly_ctx,nmod_poly
ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=Path(__file__).with_name('reconstruction.json'));ap.add_argument('--output',type=Path,default=Path(__file__).with_name('bivariate_prs_pilot.json'));ap.add_argument('--term-limit',type=int,default=300000);ap.add_argument('--seconds',type=float,default=50);args=ap.parse_args()
raw=args.input.read_bytes();D=json.loads(raw);assert D['p']==29
C=nmod_mpoly_ctx.get(['s','t'],29);zero=C.constant(0);one=C.constant(1)
f=[C.from_dict({tuple(e):int(c) for e,c in terms}) for terms in D['residual_coefficient_terms']]
def trim(a):
 while a and not a[-1]:a.pop()
 return a
f=trim(f);assert len(f)==49
g=trim([i*f[i] for i in range(1,len(f))])
out={'status':'running','input_sha256':hashlib.sha256(raw).hexdigest(),'algorithm':'Brown fraction-free subresultant PRS over F29[s,t]','term_limit':args.term_limit,'steps':[],'exact_coefficient_divisions':0,'scope':'Cost pilot; no boundary strata discarded and no global exclusion inferred.'};start=time.monotonic()
def checkpoint():
 out['seconds']=time.monotonic()-start;tmp=args.output.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2));tmp.replace(args.output)
class SoftStop(Exception):pass
def guard(polys=None):
 if time.monotonic()-start>args.seconds:raise SoftStop('soft time budget reached')
 if polys is not None and sum(len(v) for v in polys)>4*args.term_limit:raise SoftStop('intermediate coefficient term budget reached')
def prem(a,b):
 r=a[:];m=len(b)-1;remaining=len(a)-len(b)+1;lc=b[-1]
 while r and len(r)-1>=m:
  guard(r);delta=len(r)-1-m;c=r[-1];r=[v*lc for v in r]
  for j,v in enumerate(b):r[j+delta]-=c*v
  trim(r);remaining-=1;guard(r)
 if remaining and r:r=[v*(lc**remaining) for v in r]
 return r
def exactdiv(a,b):
 ret=[]
 for v in a:
  q,r=divmod(v,b);assert not r,'nonexact Brown division';ret.append(q);out['exact_coefficient_divisions']+=1
 return trim(ret)
def scalar_prs(a,b):
 n,m=a.degree(),b.degree();delta=n-m;lc=int(b.leading_coefficient());c=-pow(lc,delta,29)%29
 h=(a%b)*pow(lc,delta+1,29)*((-1)**(delta+1));ret=[]
 while h:
  k=h.degree();ret.append(h);a,b,m,delta=b,h,k,m-k
  beta=-lc*pow(c,delta,29)%29;assert beta
  h=(a%b)*pow(int(b.leading_coefficient()),a.degree()-b.degree()+1,29)*pow(beta,-1,29)
  lc=int(b.leading_coefficient())
  if delta>1:c=pow(-lc,delta,29)*pow(pow(c,delta-1,29),-1,29)%29
  else:c=-lc%29
 return ret
refs={}
for pt in [(20,2),(2,3),(3,2),(4,7),(7,4),(11,13),(13,11),(1,1),(2,1),(1,2),(5,8),(8,5)]:
 a=nmod_poly([int(v(*pt)) for v in f],29);b=nmod_poly([int(v(*pt)) for v in g],29)
 if a.degree()==48 and b.degree()==47:refs[pt]=scalar_prs(a,b)
assert refs
checkpoint()
try:
 a,b=f,g;m=len(b)-1;delta=len(a)-len(b)
 h=[v*((-1)**(delta+1)) for v in prem(a,b)];lc=b[-1];c=-(lc**delta)
 while h:
  k=len(h)-1;step=len(out['steps']);checks=[]
  for pt,seq in refs.items():
   if len(seq)<=step or [v.degree() for v in seq[:step+1]]!=[v['X_degree'] for v in out['steps']]+[k]:continue
   specialized=nmod_poly([int(v(*pt)) for v in h],29)
   assert specialized==seq[step],('specialization mismatch',pt,k)
   checks.append(list(pt))
  assert checks,'all fixed nonsingular comparison points exhausted'
  rec={'X_degree':k,'coefficient_total_terms':sum(len(v) for v in h),'maximum_coefficient_terms':max(len(v) for v in h),'maximum_parameter_total_degree':int(max(v.total_degree() for v in h)),'specialization_checks':checks,'elapsed_seconds':time.monotonic()-start}
  out['steps'].append(rec);checkpoint();print(rec,flush=True)
  if k<=14:
   out.update(status='target_reached',note='Degree14 polynomial reached; no coefficient-ideal analysis yet.');break
  if rec['coefficient_total_terms']>args.term_limit:raise SoftStop('completed-remainder term budget reached')
  guard();a,b,m,delta=b,h,k,m-k
  beta=-lc*(c**delta);h=exactdiv(prem(a,b),beta);lc=b[-1]
  if delta>1:
   c,r=divmod((-lc)**delta,c**(delta-1));assert not r
  else:c=-lc
 if not h:out.update(status='complete_zero_remainder')
except SoftStop as exc:out.update(status='bounded_stop',reason=str(exc))
checkpoint();print(json.dumps({'status':out['status'],'steps':len(out['steps']),'seconds':out['seconds']}),flush=True)
