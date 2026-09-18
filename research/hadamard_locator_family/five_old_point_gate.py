"""Bounded modular screening for a fresh cubic through five old received points."""
import itertools,json,time
from pathlib import Path
base=Path(__file__).resolve().parents[1]/'prime_line_strengthening/degree_ten_four_pole_route'
banks=json.loads((base/'gate.json').read_text());out=[];start=time.monotonic()
def det(A,p):
 A=[row[:] for row in A];v=1
 for j in range(len(A)):
  pivot=next((i for i in range(j,len(A)) if A[i][j]%p),None)
  if pivot is None:return 0
  if pivot!=j:A[pivot],A[j]=A[j],A[pivot];v=-v
  z=A[j][j]%p;v=v*z%p;inv=pow(z,-1,p)
  for i in range(j+1,len(A)):
   c=A[i][j]*inv%p
   for k in range(j,len(A)):A[i][k]=(A[i][k]-c*A[j][k])%p
 return v%p
for bank in banks:
 p=bank['p'];nodes=bank['base'];word=bank['word'];polys=bank['polynomials'] if 'polynomials' in bank else None
 surv=[];old=0;seen={}
 for subset in itertools.combinations(range(14),5):
  A=[[pow(nodes[i],j,p) for j in range(4)]+[word[i]] for i in subset]
  if not det(A,p):
   B=[row[:] for row in A[:4]]
   for j in range(4):
    k=next(k for k in range(j,4) if B[k][j]%p);B[j],B[k]=B[k],B[j]
    v=pow(B[j][j],-1,p);B[j]=[z*v%p for z in B[j]]
    for k in range(4):
     if k!=j:
      v=B[k][j];B[k]=[(z-v*w)%p for z,w in zip(B[k],B[j])]
   coeff=tuple(B[j][4] for j in range(4))
   matches=[i for i in range(14) if sum(coeff[j]*pow(nodes[i],j,p) for j in range(4))%p==word[i]]
   if len(matches)>=7:old+=1;continue
   surv.append(list(subset));seen[coeff]=matches
 out.append({'bank':bank['bank'],'p':p,'old_member_subsets':old,'fresh_survivor_subsets':surv,'count':len(surv),'distinct_fresh_cubics':[{'coefficients':list(c),'matches':v} for c,v in seen.items()]})
result={'cases':out,'seconds':time.monotonic()-start,'scope':'Necessary modular five-point determinant test; survivors require characteristic-zero verification.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
