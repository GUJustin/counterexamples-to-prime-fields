"""Stdlib replay of Q(eta) equations; no Sage and no algebraic-field CAS."""
import hashlib,json,math
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).parent;raw=(P/'exact_kernel.json').read_bytes();receipt=json.loads(raw)
bankraw=(P/'gate.json').read_bytes();bank=next(x for x in json.loads(bankraw) if x['bank']=='paley')
assert receipt['gate_sha256']==hashlib.sha256(bankraw).hexdigest()
zero=(Q(0),Q(0));one=(Q(1),Q(0))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-2*a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def scale(a,c):return(a[0]*c,a[1]*c)
def powers(a,n):
 out=[one]
 for _ in range(n):out.append(mul(out[-1],a))
 return out
def mod29(a):
 d=math.lcm(a[0].denominator,a[1].denominator);num=[int(z*d) for z in a]
 e=0;unit=d
 while unit%29==0:e+=1;unit//=29
 root=7;mod=29
 for _ in range(e):
  root+=mod*(-((root*root+root+2)//mod)*pow(2*root+1,-1,29)%29);mod*=29
 v=(num[0]+num[1]*root)%mod;assert v%(29**e)==0
 return (v//(29**e))*pow(unit,-1,29)%29
def rank_mod(A):
 A=[r[:] for r in A];r=0
 for c in range(len(A[0])):
  pivot=next((i for i in range(r,len(A)) if A[i][c]),None)
  if pivot is None:continue
  A[r],A[pivot]=A[pivot],A[r];u=pow(A[r][c],-1,29);A[r]=[v*u%29 for v in A[r]]
  for i in range(r+1,len(A)):
   u=A[i][c]
   if u:A[i]=[(v-u*z)%29 for v,z in zip(A[i],A[r])]
  r+=1
  if r==len(A):break
 return r
alpha=(Q(-1,2),Q(1,2));cv=(Q(9,4),Q(3,4));results=[]
for idx,rec in enumerate(receipt['components']):
 char=(1,3,5)[idx];assert rec['character']==char
 coeff={(i,j):tuple(map(Q,c)) for i,j,c in rec['terms']}
 assert all((i+5*j)%7==char and i+3*j<=34 and j<=10 for i,j in coeff)
 assert coeff[2*idx,10]==(Q((25,27,20)[idx]),Q(0))
 columns=[(i,j) for i,j in bank['columns'] if (i+5*j)%7==char];matrix=[];conditions=0
 for x,y,m in [(one,one,4),(alpha,cv,6)]:
  xp,yp=powers(x,34),powers(y,10)
  for total in range(m):
   for dx in range(total+1):
    dy=total-dx;v=zero;row=[]
    for i,j in columns:
     entry=scale(mul(xp[i-dx],yp[j-dy]),math.comb(i,dx)*math.comb(j,dy)) if i>=dx and j>=dy else zero
     row.append(mod29(entry));v=add(v,mul(entry,coeff.get((i,j),zero)))
    assert v==zero,(char,dx,dy,v);matrix.append(row);conditions+=1
 assert rank_mod(matrix)==31
 reduced=[mod29(coeff.get(tuple(ij),zero)) for ij in bank['columns']]
 assert reduced==bank['kernel'][idx]
 results.append({'character':char,'exact_jets_verified':conditions,'rank_mod29':31,'reduction_matches':True})
assert len(results)==3
out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),'components':results,
     'scope':'Exact representative jets, eigenweights, normalization, and independent rank31 modular witnesses; equivariance gives all14 points.'}
(P/'exact_kernel.verified.json').write_text(json.dumps(out,indent=2));print(out)
