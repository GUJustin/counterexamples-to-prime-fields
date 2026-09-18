"""Independent stdlib Hasse reconstruction and exact integer Bareiss minors."""
import hashlib,json,math,time
from pathlib import Path
P=Path(__file__).parent;start=time.monotonic()
raw=(P.parent/'gate.json').read_bytes()
bank=next(r for r in json.loads(raw) if r['bank']=='orbit2')
receipt=json.loads((P/'nonprimitive_norm_gate.json').read_text())
assert receipt['input_sha256']==hashlib.sha256(raw).hexdigest()
assert bank['p']==receipt['prime']==83
def determinant_integer(A):
    A=[row[:] for row in A];n=len(A);previous=1;sign=1
    for k in range(n-1):
        pivot=next(i for i in range(k,n) if A[i][k])
        if pivot!=k:A[k],A[pivot]=A[pivot],A[k];sign=-sign
        q=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=q*A[i][j]-A[i][k]*A[k][j]
                assert value%previous==0
                A[i][j]=value//previous
            A[i][k]=0
        previous=q
    return sign*A[-1][-1]
results=[]
for case in receipt['cases']:
    t=case['intermediate_degree'];assert t in (2,5,10)
    cap=34//t
    monomials=[(i,j) for j in range(10//t+1) for i in range(cap-3*j+1)]
    assert [list(e) for e in monomials]==case['columns']
    labels=[]
    for n in range(14):
        multiplicity=-(-(4 if n<7 else 6)//t)
        labels.extend((n,total-dy,dy) for total in range(multiplicity) for dy in range(total+1))
    assert [list(e) for e in labels]==case['row_labels']
    selected=case['selected_rows'];assert len(set(selected))==len(monomials)
    matrix=[]
    for row in selected:
        node,dx,dy=labels[row];x=bank['base'][node];y=bank['word'][node]
        matrix.append([(math.comb(i,dx)*math.comb(j,dy)*x**(i-dx)*y**(j-dy))%83
                       if i>=dx and j>=dy else 0 for i,j in monomials])
    det=determinant_integer(matrix)%83
    assert det==case['minor_determinant'] and det!=0
    results.append({'t':t,'rows':len(labels),'columns':len(monomials),'minor_mod83':det})
out={'status':'PASS','method':'independent Hasse entries, exact integer Bareiss determinant',
     'cases':results,'seconds':time.monotonic()-start}
(P/'nonprimitive_norm_gate.verified.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
