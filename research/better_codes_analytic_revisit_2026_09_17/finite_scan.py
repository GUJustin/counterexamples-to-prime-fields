"""Restricted exact scan of ePrint 2026/2056 Eqs61--63,57--58."""
from fractions import Fraction as F
from pathlib import Path
import json,math
n=262144;D=131071;p=2130706433;budget=p**6//2**128

def counts(m,b,A):
 B=(m*A+b-1)//D
 out=[]
 for t in range(B+1):
  hi=min(t,b);lo=max(0,D*t-m*A+1)
  N=(hi-lo+1)*(m*A-D*t)+(lo+hi)*(hi-lo+1)//2 if hi>=lo else 0
  L=max(0,t-b);top=min(m-1,m*A-(D-1)*t-1)
  # sum min(m-s,min(t,s)-L+1) on L<=s<=top
  cut=min(top,t,(m+L-1)//2)
  R=(cut-L+1)*(cut-L+2)//2 if cut>=L else 0
  l=max(L,cut+1);r=min(top,t)
  if r>=l:R+=(r-l+1)*m-(l+r)*(r-l+1)//2
  l=max(L,t+1);r=top;v=t-L+1
  cut=min(r,m-v)
  if cut>=l:R+=(cut-l+1)*v
  l=max(l,cut+1)
  if r>=l:R+=(r-l+1)*m-(l+r)*(r-l+1)//2
  out.append((N,R))
 return out

def direct(m,b,A):
 return [(sum(max(0,m*A-D*t+j) for j in range(min(t,b)+1)),sum(min(m-s,max(0,min(t,s)-max(0,t-b)+1)) for s in range(m) if s+(D-1)*t<m*A)) for t in range((m*A+b-1)//D+1)]

def evaluate(m,b,A,cut=None):
 rows=counts(m,b,A)
 if cut is not None:rows=rows[:cut+1]
 B=len(rows)-1
 diff=[N-n*R for N,R in rows];S=sum(diff)
 if S<=0:return None
 cumulative=0;weighted=0;H=None
 for h,d in enumerate(diff):
  cumulative+=d;weighted+=h*d
  if (h+1)*cumulative-weighted>0:H=h;break
 if H is None:H=max(B,weighted//S)
 assert sum((H-t+1)*d for t,d in enumerate(diff) if H>=t)>0
 assert H==0 or sum((H-t)*d for t,d in enumerate(diff) if H>t)<=0
 lam=F(n-D,A-D);bb=B*(2*b+1);hh=H*(2*b+1)
 ordinary=(2*bb-1)*hh+lam*(hh+bb+4*D*bb*hh)+(n-D-1)*bb
 regular=(48*D*D*H+16*D)*lam*lam*B*b+8*D*(n-D-1)*lam*B*b
 listbound=4*D*lam*B*b+2*B*b+B
 tau=2*D-3;u=1+tau*(B-1);v=min(u,tau*(b-1)+D)
 Freg=B*v+b*(u-v);J=H*(2*u*v-v*v)+2*(1+tau*H)*Freg
 C=A-D+1;NN=n-D;aa=lam*J*(n-A);bb0=Freg*NN*NN
 lo=1;hi=A-D
 while lo<hi:
  mid=(lo+hi)//2
  if aa*mid*mid>=bb0*(C-mid)**2:hi=mid
  else:lo=mid+1
 def rex(x):return F(NN+1-x,C-x)*lam*J+F((NN-x)*NN,x)*Freg
 x=min(set([lo,max(1,lo-1),min(A-D,lo+1)]),key=rex)
 exactreg=rex(x)
 return dict(m=m,b=b,B=B,H=H,surplus=S,exact_regular=str(exactreg),exact_regular_ratio=float(exactreg/budget),optimal_L=D+x,regular=str(regular),ordinary=str(ordinary),list=str(listbound),ratio=float((regular+ordinary+listbound)/budget),regular_ratio=float(regular/budget),ordinary_ratio=float(ordinary/budget))
if __name__=='__main__':
 for m in range(1,15):
  for b in range(m+1):assert counts(m,b,181284)==direct(m,b,181284)
 result={}
 for A in [183210,181284]:
  records=[];attempted=0
  for m in [8,12,16,20,24,28,32,48,64,96,128,192,256,384,512,768,1024,1536,2048]:
   for num in range(24,39):
    b=m*num//100;attempted+=1;r=evaluate(m,b,A)
    if r:records.append(r)
  result[str(A)]={'attempted':attempted,'feasible':len(records),'best':min(records,key=lambda r:r['ratio']) if records else None,'best_regular':min(records,key=lambda r:r['exact_regular_ratio']) if records else None}
 print(json.dumps(result,indent=2))
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
