from pathlib import Path
import json
from functools import lru_cache
P=Path(__file__).parent
s=(P.parent/'char3_deformation/verify.py').read_text();exec(s[s.index('def padd'):s.index('z=decode(3)')])
c=list(map(decode,[188,111,704,564,333,37,247,0]))
def code(v):return sum(a*3**i for i,a in enumerate(v))
def inv(v):assert v!=zero;return powr(v,3**18-2)
def solve(A,b):
 determinant=sub(mul(A[0][0],A[1][1]),mul(A[0][1],A[1][0]));assert determinant!=zero
 return [mul(sub(mul(b[0],A[1][1]),mul(b[1],A[0][1])),inv(determinant)),mul(sub(mul(A[0][0],b[1]),mul(A[1][0],b[0])),inv(determinant))],determinant
def ci(a,b,k):return c[a+2*b+4*k]
def diff(b,k):return sub(ci(0,b,k),ci(1,b,k))
# C0*d(b,0)-C1*d(b,1)=c(1,b,1)-c(1,b,0)
C,detC=solve([[diff(b,0),neg(diff(b,1))] for b in range(2)],[sub(ci(1,b,1),ci(1,b,0)) for b in range(2)])
B,detB=solve([[diff(0,k),neg(diff(1,k))] for k in range(2)],[sub(ci(1,1,k),ci(1,0,k)) for k in range(2)])
nodes=[zero,one,*B,*C];collisions=[(i,j) for i in range(6) for j in range(i+1,6) if nodes[i]==nodes[j]]
words=[zero,zero]
for b,x in enumerate(B):words.append(mul(mul(x,sub(x,one)),add(mul(C[0],diff(b,0)),ci(1,b,0))))
for k,x in enumerate(C):words.append(mul(mul(x,sub(x,one)),add(mul(B[0],diff(0,k)),ci(1,0,k))))
checks=[]
if not collisions:
 for i in range(8):
  ids=[(i&1),2+((i>>1)&1),4+((i>>2)&1)];lead=zero
  for j in ids:
   denom=one
   for k in ids:
    if k!=j:denom=mul(denom,sub(nodes[j],nodes[k]))
   lead=add(lead,mul(words[j],inv(denom)))
  assert lead==c[i];checks.append(True)
out=dict(encoding='univariate F3[t]/Phi7(t^3-t)',detB=code(detB),detC=code(detC),nodes=list(map(code,nodes)),words=list(map(code,words)),collisions=collisions,all_eight_leading_coefficients_verified=len(checks)==8)
(P/'fixed_c_faces.json').write_text(json.dumps(out,indent=2));print(out)
