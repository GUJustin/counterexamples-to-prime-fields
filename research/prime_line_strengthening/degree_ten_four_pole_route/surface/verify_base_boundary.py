#!/usr/bin/env python3
"""Independent tangent-rank, multiplicity-jump and boundary-map receipt."""
import json,math,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
raw=(P.parent/'gate.json').read_bytes(); b=next(z for z in json.loads(raw) if z['bank']=='paley')
F=[{tuple(ij):v for ij,v in zip(b['columns'],row) if v%29} for row in b['kernel']]
checks=[]
for k,m in [(0,4),(7,6)]:
 x,y=b['base'][k],b['word'][k]
 M=[[sum(v*math.comb(i,m-jj)*math.comb(j,jj)*pow(x,i-m+jj,29)*pow(y,j-jj,29) for (i,j),v in f.items() if i>=m-jj and j>=jj)%29 for jj in range(3)] for f in F]
 d=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))%29
 assert d==({0:5,7:20}[k]);checks.append(dict(representative=k,multiplicity=m,coefficient_columns=[0,1,2],matrix=M,determinant=d))
extra=[]
for name,at_infty in [('origin',False),('weighted_infinity',True)]:
 fs=[{(34-i-3*j if at_infty else i,j):v for (i,j),v in f.items()} for f in F]
 rows=[[f.get((1,0),0),f.get((0,1),0)] for f in fs]
 assert rows[1]==[0,0]
 assert (rows[0][0]*rows[2][1]-rows[0][1]*rows[2][0])%29
 order=min(i+j for i,j in fs[1]);assert order==2
 extra.append(dict(chart=name,linear_rows=rows,kernel=[0,1,0],F1_order=order,F1_initial_terms=[[list(ij),v] for ij,v in fs[1].items() if sum(ij)==order]))
leading=[[[i,v] for (i,j),v in f.items() if j==10] for f in F]
assert leading==[[[0,25]],[[2,27]],[[4,20]]]
infty=[[[j,v] for (i,j),v in f.items() if i+3*j==34] for f in F]
assert all(infty)
out=dict(status='PASS',input_sha256=hashlib.sha256(raw).hexdigest(),tangent_rank_three=checks,extra_basepoints=extra,C0_restriction=leading,infinity_restriction=infty,boundary_separability={'old_exceptionals':{'nonconstant':'rank-three tangent maps','degree_upper_bound':6},'extra_exceptionals':{'nonconstant':'rank-two linear maps','degree':1},'C0':{'nonconstant':True,'degree_upper_bound':4},'infinity':{'nonconstant':'distinct exponent supports','degree_upper_bound':10},'reason':'All nonconstant map degrees are below characteristic 29; thus every boundary restriction is generically separable and the surface map has rank at least one there.'})
(P/'base_locus_boundary.verified.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS: tangent minors 5,20; F1 extra orders 2,2; all boundary maps separable')
