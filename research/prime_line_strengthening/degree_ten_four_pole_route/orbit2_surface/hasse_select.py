"""Batched exact degree62 Hasse ideal certificate, no symmetry assumption."""
import json,hashlib,math,time,gc
from pathlib import Path
from flint import nmod_mat,nmod_poly
P=Path(__file__).resolve().parent;raw=(P/'gauss_image_interpolation.json').read_bytes();H=json.loads(raw)['image_terms'];p=83
cols=[(b,c) for b in range(63) for c in range(63-b)];ci={v:i for i,v in enumerate(cols)}
start=time.time();rows=[];metadata=[];derivs={}
for t in range(15):
 for db in range(t+1):
  dc=t-db;D=[(b-db,c-dc,v*math.comb(b,db)*math.comb(c,dc)%p) for (a,b,c),v in H if b>=db and c>=dc]
  for mb in range(t+1):
   for mc in range(t+1-mb):
    row=[0]*len(cols)
    for b,c,v in D:row[ci[b+mb,c+mc]]=v
    rows.append(row);metadata.append([db,dc,mb,mc])
    if len(rows)==2560:break
   if len(rows)==2560:break
  if len(rows)==2560:break
 if len(rows)==2560:break
M=nmod_mat(rows,p);T=M.transpose();del M,rows
R,rank=T.rref();del T
assert rank==2016
selected=[next(j for j in range(2560) if int(R[i,j])) for i in range(rank)]
out=dict(input_sha256=hashlib.sha256(raw).hexdigest(),rank=rank,rows=2560,columns=2016,basis_metadata=[metadata[j] for j in selected],selected_rows=selected,seconds=time.time()-start)
(P/'hasse_basis.json').write_text(json.dumps(out,indent=2)+'\n');print('SELECT PASS',rank,time.time()-start,flush=True)
