"""Small-field explicit pre-contact extraction rank sanity checks."""
import json
from math import comb
from pathlib import Path
p=101;n=5;m=4;D=12;w=2;S=1;L=3;R=1
nodes=list(range(n))
rows=[(a,r,f,j,z) for a in nodes for r in range(R+1) for f in range(r+1) for j in range(S+1) for z in range(L-f-j+1)]
index={row:k for k,row in enumerate(rows)}
cols=[(e,i,j,z) for i in range(R+1) for j in range(S+1) for z in range(L-i-j+1) for e in range(D-w*i-(w-1)*j)]
def matrix_rank(mat):
 rr=0
 for c in range(len(mat[0])):
  pivot=next((r for r in range(rr,len(mat)) if mat[r][c]),None)
  if pivot is None:continue
  mat[rr],mat[pivot]=mat[pivot],mat[rr]
  inv=pow(mat[rr][c],-1,p);mat[rr]=[(v*inv)%p for v in mat[rr]]
  for r in range(rr+1,len(mat)):
   if mat[r][c]:
    q=mat[r][c];mat[r]=[(a-q*b)%p for a,b in zip(mat[r],mat[rr])]
  rr+=1
  if rr==len(mat):break
 return rr
out=[]
for mode in ['zero','nonconstant']:
 mat=[[0]*len(cols) for _ in rows]
 for cc,(e,i,j,z) in enumerate(cols):
  for a in nodes:
   u0=0 if mode=='zero' else(a*a+3)%p;u1=0 if mode=='zero' else(2*a+7)%p
   for r in range(R+1):
    for f in range(min(i,r)+1):
     d=r-f
     if d>e:continue
     for k in range(i-f+1):
      row=(a,r,f,j,z+k)
      mat[index[row]][cc]+=comb(e,d)*pow(a,e-d,p)*comb(i,f)*comb(i-f,k)*pow(u0,i-f-k,p)*pow(u1,k,p)
      mat[index[row]][cc]%=p
 actual=matrix_rank(mat);assert actual==len(rows)
 out.append(dict(received_values=mode,rank=actual,rows=len(rows),columns=len(cols)))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
