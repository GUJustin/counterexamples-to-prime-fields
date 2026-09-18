"""Proved rank upper bound, exact arithmetic coefficient sums; no routing claim."""
from pathlib import Path
import json
N=262144;W=131071;A=181275

def first_rank(m,s):
    return (s+1)*(3*m*m+3*(1-s)*m+s*(2*s+1))//6

def counts(m,s,K,J):
    C=M=0
    for k in range(K+1):
      for j in range(s+1):
        b=m*A-(W-1)*j-(W-2)*k
        q=min(J-j-k,(b-1)//W)
        if q<0:continue
        c=(q+1)*b-W*q*(q+1)//2
        moment=b*q*(q+1)//2-W*q*(q+1)*(2*q+1)//6
        C+=c;M+=moment+(j+k)*c
    return C,M

def gate(m,K):
    s=max(1,round(.31*m));J=(m*A+s+2*K-1)//W
    assert m>=2*s and J>=m+s-3
    R0=first_rank(m,s)
    saving=s*(2*m-s-3)//2
    R=R0 if K==0 else 2*R0-saving
    C,M=counts(m,s,K,J);gap=C-N*R
    L=max(J,M//gap) if gap>0 else None
    return dict(m=m,S=s,J=J,K=K,numerator_degree_bound=m*A,
                coefficient_count=C,local_rank_upper=R,kernel_lower=gap,
                extra_kernel_saving=saving if K else 0,
                conservative_line_L=L,
                conservative_line_kernel_lower=(L+1)*gap-M if L is not None else None)

checks=0
exact=json.loads(Path(__file__).with_name('restricted_curvature_rank.json').read_text())
for r in exact['rows']:
    g=gate(r['m'],r['curvature_cap'])
    assert g['coefficient_count']==r['coefficient_slope']
    assert g['local_rank_upper']==r['local_rank']
    checks+=1
rows={K:[gate(m,K) for m in range(2,513)] for K in (0,1)}
first={K:next(r for r in rows[K] if r['kernel_lower']>0) for K in rows}
samples={K:[gate(m,K) for m in (64,96,128,256)] for K in rows}
out=dict(n=N,w=W,A=A,exact_matrix_regressions=checks,
         shape='S=max(1,round(.31m)), automaticJ; m2..512, one fixed shape family',
         first_positive=first,samples=samples,
         scope='Proved sufficient source gate only. L uses conservative (L+1)*localrank; second-jet routing and characteristic gates not certified.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
