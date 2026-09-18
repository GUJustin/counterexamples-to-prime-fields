"""Independent integer Bareiss replay of original modular minor receipts."""
import json
from pathlib import Path

here=Path(__file__).parent
data=json.loads((here/'elliptic_quadruple_cone_gate.json').read_text())
def determinant(A):
    A=[r[:] for r in A];N=len(A);old=1;sign=1
    for k in range(N-1):
        r=next((r for r in range(k,N) if A[r][k]),None)
        if r is None:return 0
        if r!=k:A[k],A[r]=A[r],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,N):
            for j in range(k+1,N):
                value=A[i][j]*pivot-A[i][k]*A[k][j]
                assert value%old==0
                A[i][j]=value//old
            A[i][k]=0
        old=pivot
    return sign*A[-1][-1]

receipts=[]
for field in data['field_results']:
    p=field['p'];full=[];linear=[];degenerate=[]
    for case in field['cases']:
        pair=[case['m'],case['n']]
        planes=case['planes']
        for plane,quad in zip(planes,case['quadruples']):
            assert len(set(None if v is None else tuple(v) for v in quad))==4
            for point in quad:
                if point is None:V=[0,0,0,1]
                else:
                    x,y=point
                    assert (y*y-x*x*x+x)%p==0
                    V=[1,x,y,x*x%p]
                assert sum(a*b for a,b in zip(plane,V))%p==0
        rank=case['quadratic_rank']
        if rank==10:
            rows=[]
            for index in case['independent_row_indices']:
                v=planes[index]
                rows.append([v[i]*v[j]%p for i,j in data['monomials']])
            det=determinant(rows)%p
            assert det
            full.append({'pair':pair,'determinant_mod_p':det})
        elif rank==6:
            j=3 if pair in [[-1,-1],[0,0]] else 2
            assert all(v[j]==0 for v in planes)
            assert len(case['kernel'])==4
            assert all(not a or j in mon for v in case['kernel']
                       for a,mon in zip(v,data['monomials']))
            columns=[mon for mon in data['monomials'] if j not in mon]
            rows=[[planes[index][a]*planes[index][b]%p for a,b in columns]
                  for index in case['independent_row_indices']]
            assert determinant(rows)%p
            linear.append({'pair':pair,'forced_plane_coefficient_zero':j,
                           'all_quadratic_relations_divisible_by_that_coordinate':True})
        else:
            assert rank==0 and not planes
            assert pair in [[-2,-1],[-1,-2],[0,1],[1,0]]
            degenerate.append(pair)
    assert len(full)==41 and len(linear)==4 and len(degenerate)==4
    receipts.append(dict(p=p,full_rank_minors=full,linear_cases=linear,
                         duplicate_point_cases=degenerate))
out=dict(status='PASS',field_results=receipts,
         scope='Two-prime necessary identity gate for this curve, tau=O and m,n in [-3,3]; no positive rank-three cone found.')
(here/'elliptic_quadruple_cone_verified.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 82 original 10x10 minors; 8 linear-only branches; 8 duplicate-point branches.')
