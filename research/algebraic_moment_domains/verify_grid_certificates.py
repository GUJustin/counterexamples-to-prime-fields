"""Independent standard-library verifier: no FLINT, HNF, or LLL calls."""
import json,math,time
from pathlib import Path
P=Path(__file__).parent

def mul(A,B):
    BT=list(zip(*B))
    return [[sum(a*b for a,b in zip(row,col)) for col in BT] for row in A]
def det(A):
    A=[r[:] for r in A]; n=len(A); old=1; sign=1
    for k in range(n-1):
      if not A[k][k]:
        z=next(i for i in range(k+1,n) if A[i][k]);A[k],A[z]=A[z],A[k];sign=-sign
      pivot=A[k][k]
      for i in range(k+1,n):
        for j in range(k+1,n):
          num=A[i][j]*pivot-A[i][k]*A[k][j]
          assert num%old==0
          A[i][j]=num//old
        A[i][k]=0
      old=pivot
    return sign*A[-1][-1]
results=[]
for m in [8,12,16]:
 for kind in ['gaussian','interval']:
    start=time.monotonic(); d=json.loads((P/f'{kind}_{m}.certificate.json').read_text());n=m*m
    if kind=='interval': expected=[[x**j for x in range(n)] for j in range(m+1)]
    else:
      expected=[[1]*n]
      for j in range(1,m+1):
        for parity in [0,1]:
          expected.append([sum(math.comb(j,l)*a**(j-l)*b**l*(-1)**((l-parity)//2) for l in range(parity,j+1,2)) for a in range(m) for b in range(m)])
    A,B,C,J,U,R=[d[k] for k in ['A','B','C','J','U','R']]
    assert A==expected
    assert det(B)!=0 and mul(B,C)==A and mul(A,J)==B
    assert abs(det(U))==1 and mul(U,C)==R
    widths=[]
    for row in R:
      ss=sorted(row); widths.append(sum(ss[n//2:])-sum(ss[:n//2]))
    assert widths==d['widths']
    signature_bound=math.prod(w+1 for w in widths); subsets=math.comb(n,n//2)
    gram=mul(C,list(map(list,zip(*C)))); gd=det(gram);assert gd>0
    results.append(dict(m=m,kind=kind,status='PASS',exact_signature_bound=str(signature_bound),exact_subset_count=str(subsets),positive_certificate=signature_bound<subsets,normalized_gram_log2_volume=math.log2(gd)/2,seconds=time.monotonic()-start))
print(json.dumps(results,indent=2));(P/'independent_verification.json').write_text(json.dumps(results,indent=2))
