"""Batched exact degree62 Hasse ideal certificate, no symmetry assumption."""
import json,hashlib,math,time,gc
from pathlib import Path
from flint import nmod_mat,nmod_poly
P=Path(__file__).resolve().parent;raw=(P/'gauss_image_interpolation.json').read_bytes();H=json.loads(raw)['image_terms'];p=83
cols=[(b,c) for b in range(63) for c in range(63-b)];ci={v:i for i,v in enumerate(cols)}
start=time.time();selection=json.loads((P/'hasse_basis.json').read_text());assert selection['input_sha256']==hashlib.sha256(raw).hexdigest()
basis_meta=selection['basis_metadata'];basis=[];count=selection['rows'];log=[]
for db,dc,mb,mc in basis_meta:
 row=[0]*len(cols)
 for (a,b,c),v in H:
  if b>=db and c>=dc:row[ci[b-db+mb,c-dc+mc]]=v*math.comb(b,db)*math.comb(c,dc)%p
 basis.append(row)
rank=len(basis);assert rank==len(cols)
A=nmod_mat(basis,p);T=A.transpose();del A
rhs=nmod_mat([[int(c==(0,0))] for c in cols],p);solution=T.solve(rhs);del T,rhs
weights=[int(solution[i,0]) for i in range(rank)];del solution
v=[sum(a*r[j] for a,r in zip(weights,basis))%p for j in range(len(cols))];success=v==[int(c==(0,0)) for c in cols]
out=dict(input_sha256=hashlib.sha256(raw).hexdigest(),p=p,Hasse_orders=[0,14],affine_chart='a=1',degree_bound=62,matrix_rows=count,matrix_columns=len(cols),rank=rank,constant_in_span=success,batch_log=log)
if success:out['affine_certificate']=[dict(coefficient=w,derivative_b=m[0],derivative_c=m[1],multiplier_b=m[2],multiplier_c=m[3]) for w,m in zip(weights,basis_meta) if w]
(P/'hasse_multiplicity_gate.json').write_text(json.dumps(out,indent=2)+'\n');print('AFFINE',success,flush=True)
# Complete projective boundary: a=0,c=1 and the single remaining point.
g=nmod_poly([],p);rep={};jets=[];meta=[]
for t in range(15):
 for da in range(t+1):
  db=t-da;coeff=[0]*63
  for (a,b,c),v in H:
   if a==da and b>=db:coeff[b-db]=(coeff[b-db]+v*math.comb(b,db))%p
  f=nmod_poly(coeff,p)
  if f:jets.append(f);meta.append([da,db])
for j,f in enumerate(jets):
 gg,s,t=g.xgcd(f);rep={k:s*v for k,v in rep.items() if s*v};rep[j]=rep.get(j,nmod_poly([],p))+t;g=gg
 if g.degree()==0:break
assert sum((v*jets[k] for k,v in rep.items()),nmod_poly([],p))==g
out.update(boundary_empty=g.degree()==0,boundary_gcd_coefficients=[int(v) for v in g.coeffs()],boundary_certificate=[dict(derivative_a=meta[j][0],derivative_b=meta[j][1],multiplier_coefficients=[int(v) for v in f.coeffs()]) for j,f in rep.items() if f],endpoint_010_multiplicity=min(a+c for (a,b,c),v in H))
out['global_exclusion']=success and out['boundary_empty'] and out['endpoint_010_multiplicity']<15;out['seconds']=time.time()-start
(P/'hasse_multiplicity_gate.json').write_text(json.dumps(out,indent=2)+'\n');print('GLOBAL',out['global_exclusion'],'endpoint',out['endpoint_010_multiplicity'],'seconds',out['seconds'],flush=True)
