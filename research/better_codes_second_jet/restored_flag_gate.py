"""Replay restored flag arithmetic, then a bounded curvature-linear source gate."""
from pathlib import Path
import json
N=262144;w=131071;A=181275

def triangle(u):
 if u<0:return 0,0
 return (u+1)*(u+2)//2,u*(u+1)*(u+2)//3

def rect(a,b,u):
 c=t=0
 for shift,sign in ((0,1),(a,-1),(b,-1),(a+b,1)):
  x,y=triangle(u-shift);c+=sign*x;t+=sign*(y+shift*x)
 return c,t

def rankprofile(m,B,s,U):
 R=T=0
 for r in range(m):
  for h in range(s+1):
   c,t=rect(r+1,B-2*h+1,U-h);R+=c;T+=t+h*c
   q=max((m-r+1)//2,m-r-(s-h))
   if q<=r and m-r+2*h<=B:
    c,t=rect(r-q+1,B-2*h-q+1,U-h-q)
    R-=c;T-=t+(h+q)*c
 return R,T

def coefficients(m,B,s,U,k=0,n0=1,agreement=A):
 C=M=0
 for h in range(s+1):
  reserve=h if h<n0 else k
  cutoff=m*agreement-reserve*(agreement-(w-2))
  for r in range(B-2*h+1):
   b=cutoff-(w-2)*h-(w-1)*r
   q=min(U-h-r,(b-1)//w)
   if q<0:continue
   c=(q+1)*b-w*q*(q+1)//2
   C+=c;M+=b*q*(q+1)//2-w*q*(q+1)*(2*q+1)//6+(h+r)*c
 return C,M

def gate(m,B,s,U):
 R,T=rankprofile(m,B,s,U);C,M=coefficients(m,B,s,U)
 gap=C-N*R
 L=max(U,m+B+s,(M-N*T)//gap) if gap>0 else None
 return dict(m=m,B=B,s=s,U=U,k=0,n0=1,C=C,M=M,R=R,T=T,gap=gap,L=L,nullity=(L+1)*gap-M+N*T if L else None)

# Reproduce the actual restored source receipt before using its arithmetic.
R,T=rankprofile(114,47,21,155)
C,M=coefficients(114,47,21,155,5,7,181353)
assert 2256*R-T==5804271999
assert 2256*C-M==1521555139747342
samples=[]
for m in (72,96,117,128,140,160,192,256):
 B=round(.31*m)+2;U=(m*A+B-1)//w
 samples.append(gate(m,B,1,U))
# One explicitly bounded low-curvature family, no matrix search.
best=None;tested=0;active=[]
for m in range(48,321):
 for B in range(max(2,(27*m)//100),min(m,(35*m)//100+3)+1):
  U=(m*A+B-1)//w
  g=gate(m,B,1,U);tested+=1
  if g['L'] is not None:
   if best is None or g['L']<best['L']:best=g
   if g['L']<3261:active.append(g)
out={'pinned_receipt_checks':2,'tested_shapes':tested,'grid':'48<=m<=320, .27m<=B<=.35m+3, curvaturecap1,k0,n01,automaticU','samples':samples,'best_L':best,'active_at_critical':len(active),'scope':'Restored exact sufficient source-rank arithmetic only; target counting theorem port and retained-branch cost not yet checked.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
