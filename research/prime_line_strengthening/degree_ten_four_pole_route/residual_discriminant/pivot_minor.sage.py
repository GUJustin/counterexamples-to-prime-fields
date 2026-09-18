"""One bordered minor only: bounded cost pilot in the chart c-a=1."""
import argparse,hashlib,json,time
from pathlib import Path
from sage.all import GF,PolynomialRing,matrix
ap=argparse.ArgumentParser()
ap.add_argument('--input',type=Path,default=Path(__file__).with_name('reconstruction.json'))
ap.add_argument('--output',type=Path,default=Path(__file__).with_name('pivot-minor.json'))
ap.add_argument('--compute-minor',action='store_true')
args=ap.parse_args();raw=args.input.read_bytes();d=json.loads(raw)
assert d['p']==29 and d['mu7_sparsity_verified']
k=GF(29);R=PolynomialRing(k,('u','v'));u,v=R.gens()
# Parameter homogenization [a:b:c]=[u:v:u+1].
cc=[sum(k(z)*u**(18-a-b)*v**a*(u+1)**b for (a,b),z in terms)
    for terms in d['residual_coefficient_terms']]
cc=[R(c) for c in cc]
# Binary partial coefficients in X^i V^(47-i), then multiplication by degree32.
fx=[k(i+1)*cc[i+1] for i in range(48)]
fv=[k(48-i)*cc[i] for i in range(48)]
rows=[[R.zero() for _ in range(66)] for _ in range(80)]
for j in range(33):
    for i in range(48):rows[i+j][j]=fx[i];rows[i+j][33+j]=fv[i]
M=matrix(R,rows);E=matrix(k,[[c(0,0) for c in row] for row in rows])
assert E.rank()==66
selected=list(E.transpose().pivots())
assert len(selected)==66
# The first65 independent rows determine65 independent columns.
pivot_rows=selected[:65]
pivot_cols=list(E.matrix_from_rows(pivot_rows).pivots())
assert len(pivot_cols)==65
remaining_col=next(j for j in range(66) if j not in pivot_cols)
remaining_rows=[i for i in range(80) if i not in pivot_rows]
border_row=selected[65]
out={'input_sha256':hashlib.sha256(raw).hexdigest(),'chart':'[u:v:u+1]',
     'matrix_shape':[80,66],'entry_degree_bound':18,
     'evaluation_parameter':[0,0,1],'evaluation_rank':66,
     'pivot_rows':pivot_rows,'pivot_columns':pivot_cols,
     'remaining_column':remaining_col,'remaining_rows':remaining_rows,
     'pilot_border_row':border_row,'status':'matrix-ready'}
def checkpoint():args.output.write_text(json.dumps(out,indent=2))
checkpoint();print('80x66 matrix and65x65 pivot ready',flush=True)
if args.compute_minor:
    out['status']='computing-one-minor';checkpoint();start=time.monotonic()
    minor=M.matrix_from_rows_and_columns(pivot_rows+[border_row],pivot_cols+[remaining_col]).determinant()
    assert minor and minor(0,0)!=0
    out.update(status='one-minor-complete',seconds=time.monotonic()-start,
               degree=int(minor.total_degree()),term_count=len(minor.dict()),
               minor_terms=[[list(map(int,e)),int(z)] for e,z in minor.dict().items()])
    checkpoint();print('Minor degree',out['degree'],'terms',out['term_count'],flush=True)
