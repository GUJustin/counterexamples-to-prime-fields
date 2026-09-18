import json,math,time,sys
from pathlib import Path
from flint import fmpz_mat
m=int(sys.argv[1]); out=Path(__file__).parent

def rows(M): return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def make(kind):
    n=m*m;s=m
    if kind=='interval': return [[x**j for x in range(n)] for j in range(s+1)]
    cols=[]
    for a in range(m):
      for b in range(m):
        re,im=1,0; col=[1]
        for j in range(1,s+1):
          re,im=re*a-im*b,re*b+im*a;col.extend([re,im])
        cols.append(col)
    return list(map(list,zip(*cols)))
report=[]
for kind in ['gaussian','interval']:
    start=time.monotonic(); aa=make(kind); A=fmpz_mat(aa); k=A.nrows();n=A.ncols()
    H,T=A.transpose().hnf(transform=True)
    assert all(H[i,j]==0 for i in range(k,n) for j in range(k))
    B=fmpz_mat([[H[j,i] for j in range(k)] for i in range(k)])
    J=fmpz_mat([[T[j,i] for j in range(k)] for i in range(n)])
    cq=B.solve(A); C=fmpz_mat([[int(cq[i,j]) if cq[i,j].denominator==1 else (_ for _ in ()).throw(ValueError('noninteger')) for j in range(n)] for i in range(k)])
    assert B*C==A and A*J==B
    R,U=C.lll(transform=True,delta=.99)
    assert U*C==R and abs(int(U.det()))==1
    def widths(M):
      return [sum(sorted(row)[n//2:])-sum(sorted(row)[:n//2]) for row in rows(M)]
    wb,wr=widths(C),widths(R)
    ent=math.log2(math.comb(n,n//2)); cost=sum(math.log2(1+x) for x in wr)
    data=dict(kind=kind,m=m,n=n,s=m,A=aa,B=rows(B),J=rows(J),C=rows(C),U=rows(U),R=rows(R),widths=wr)
    (out/f'{kind}_{m}.certificate.json').write_text(json.dumps(data))
    rec=dict(kind=kind,m=m,n=n,s=m,rank=k,entropy_bits=ent,width_cost_bits=cost,certified_log_list_bits=ent-cost,unreduced_width_bits=sum(math.log2(1+x) for x in wb),normalized_gram_log2_volume=math.log2(int((C*C.transpose()).det()))/2,lattice_log2_covolume=math.log2(abs(int(B.det()))),seconds=time.monotonic()-start)
    report.append(rec); print(json.dumps(rec),flush=True)
(out/f'gate_{m}.json').write_text(json.dumps(report,indent=2))
