"""Exact enlarged-box graded rank bound; source gate only."""
import json
from pathlib import Path
exec(Path(__file__).with_name('curvature_upper_gate.py').read_text().split('checks=0')[0])
def moments(m,s):
    rank=moment=0
    for r in range(m):
        size=(r+1)*(s+1)
        mom=size*(r+s)//2
        h=m-r
        if h<=min(r,s):
            removed=(r-h+1)*(s-h+1)
            mom-=removed*(r+s)//2
            size-=removed
        rank+=size;moment+=mom
    assert rank==first_rank(m,s)
    saving=s*(2*m-s-3)//2
    sm=0
    for b in range(1,s+1):
        num=m+s-3*b
        sm+=num*b+num*(num-1)//2
    return rank,moment,saving,sm
rows=[]
for m in (72,96,117,128,256):
 for K in (0,1):
    g=gate(m,K);s=g['S'];J=g['J'];r,t,sv,sm=moments(m,s)
    R=r if K==0 else 2*r-sv
    T=t if K==0 else 2*t+r-sm
    C,M=counts(m,s,K,J);gap=C-N*R
    # All enlarged-box nonzero image degrees <= m+S for curvature.
    L=max(J,m+s,M//gap) if gap>0 else None
    sharp=max(J,m+s,(M-N*T)//gap) if gap>0 else None
    g.update(rank_upper_profile_degree_moment=T,source_degree_moment=M,
             graded_line_L=sharp,graded_line_kernel_lower=(sharp+1)*gap-M+N*T if sharp is not None else None)
    rows.append(g)
out={'scope':'Enlarged graded box rank upper bound, L>=m+S; no routing or characteristic certificate. Restricting source by J can only reduce rank; no need J include entire box.', 'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
