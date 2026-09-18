"""Exact characteristic-zero omitted-root rank classification.
Three global phase shifts and seven cyclic rotations reduce2187 assignments
to105 orbits. Coefficients are exact inQ[z]/Phi21, no numerical embedding.
"""
import itertools,json,time
from pathlib import Path
import sympy as s
z=s.Symbol('z');f=s.Poly(s.cyclotomic_poly(21,z),z,domain=s.QQ)
K=s.QQ.algebraic_field((f,z));Z=K([1,0]);zp=[K.one]
for i in range(21):zp.append(zp[-1]*Z)
assert zp[21]==K.one and zp[7]!=K.one and zp[3]!=K.one

def orbit(a):return {tuple((a[(j-k)%7]+b)%3 for j in range(7)) for k in range(7) for b in range(3)}
allseq=set(itertools.product(range(3),repeat=7));reps=[]
while allseq:
 a=min(allseq);O=orbit(a);assert O<=allseq
 reps.append((a,len(O)));allseq-=O
assert len(reps)==105 and sum(n for _,n in reps)==2187

def encode(a):return [str(x) for x in a.to_list()]
def rref(A):
 A=[row[:] for row in A];piv=[];row=0
 for col in range(4):
  ix=next((i for i in range(row,5) if A[i][col]),None)
  if ix is None:continue
  A[row],A[ix]=A[ix],A[row]
  inv=K.exquo(K.one,A[row][col]);A[row]=[x*inv for x in A[row]]
  for i in range(5):
   if i!=row and A[i][col]:
    c=A[i][col];A[i]=[x-c*y for x,y in zip(A[i],A[row])]
  piv.append(col);row+=1
 return A,piv
out=[];start=time.time();path=Path(__file__).with_name('rank21.json')
for a,n in reps:
 F=[sum((zp[(3*k*j+7*a[j])%21] for j in range(7)),K.zero) for k in range(7)]
 G=[sum((zp[(3*k*j+14*a[j])%21] for j in range(7)),K.zero) for k in range(7)]
 A=[[F[(d+5-l)%7] for d in range(3)]+[K.convert(-7 if l==5 else 0)] for l in (4,5,6)]
 A += [[G[(d+10-l)%7] for d in range(3)]+[K.zero] for l in (4,6)]
 R,piv=rref(A);rank=sum(c<3 for c in piv);consistent=3 not in piv
 row={'phases':a,'orbit_size':n,'rank':rank,'augmented_rank':len(piv),'consistent':consistent}
 if consistent:
  point=[K.zero]*3
  for i,col in enumerate(piv):point[col]=R[i][3]
  free=[i for i in range(3) if i not in piv];basis=[]
  for j in free:
   v=[K.zero]*3;v[j]=K.one
   for i,col in enumerate(piv):v[col]=-R[i][j]
   basis.append(v)
  assert all(sum((v*x for v,x in zip(ar[:3],point)),K.zero)==ar[3] for ar in A)
  for v in basis:assert all(sum((b*x for b,x in zip(ar[:3],v)),K.zero)==K.zero for ar in A)
  row['particular']=[encode(v) for v in point];row['nullspace']=[[encode(v) for v in b] for b in basis]
 out.append(row)
 path.write_text(json.dumps({'field_polynomial':str(f.as_expr()),'cases':out,'complete':False,'elapsed':time.time()-start},indent=2))
print(json.dumps({'orbits':len(out),'assignments':sum(x['orbit_size'] for x in out),'consistent_orbits':sum(x['consistent'] for x in out),'singular_consistent':[(x['phases'],x['orbit_size'],x['rank']) for x in out if x['consistent'] and x['rank']<3],'seconds':time.time()-start}),flush=True)
path.write_text(json.dumps({'field_polynomial':str(f.as_expr()),'cases':out,'complete':True,'elapsed':time.time()-start},indent=2))
