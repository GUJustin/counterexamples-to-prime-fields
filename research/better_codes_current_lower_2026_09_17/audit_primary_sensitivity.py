import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parent;n=262144;w=131071

def rectangle(a,b,h,L):
 if a==0 or b==0:return 0
 assert h+a+b-2<=L
 return a*b*(L+1-h)-b*a*(a-1)//2-a*b*(b-1)//2

def rank(m,L,s):
 assert m+s<=L+1
 return sum(rectangle(r+1,s+1,0,L)-rectangle(max(0,r+1-min(r+1,m-r)),max(0,s+1-min(r+1,m-r)),min(r+1,m-r),L) for r in range(m))
def choose(a,b):return math.comb(a,b) if a>=b else 0

def coeff(A,m,L,s):
 q,r=divmod(A*m,w);assert s<=q<=L and r+s<=w
 U=L+1-q;c1=U*(r+q);c2=U*(w-2)+r+q+w-1;c3=2*w-3
 return sum(c*(choose(q+2,j)-choose(q+1-s,j)) for j,c in [(2,c1),(3,c2),(4,c3)])
rows=[]
for name,m0,L0,s0,C0,R0 in [('A',115,274277,35,13125118927898685,50068355280),('B',134,18992,40,1405157241467798,5360249390),('TCap',226,9281,70,3312623460539726,12636646882)]:
 assert coeff(181284,m0,L0,s0)==C0 and rank(m0,L0,s0)==R0
 target=coeff(181275,m0,L0,s0)-n*R0;allrows=[];qcap=(181284*m0)//w
 for s in range(s0+1):
  for m in range(max(1,2*s),m0+1):
   if (181275*m)//w>qcap:continue
   try:
    R=rank(m,L0,s);C=coeff(181275,m,L0,s)
    slope=coeff(181275,m,L0+1,s)-C-n*(rank(m,L0+1,s)-R)
   except AssertionError:continue
   gap=C-n*R
   lower=max(m+s-1,(181275*m)//w)
   lowgap=gap+slope*(lower-L0)
   req=lower if lowgap>0 else (max(lower,L0+(-gap)//slope+1) if slope>0 else None)
   if req is not None:
    assert coeff(181275,m,req,s)>n*rank(m,req,s)
    if req>lower:assert coeff(181275,m,req-1,s)<=n*rank(m,req-1,s)
   allrows.append(dict(m=m,s=s,required_L=req,surplus_at_old_L=gap,slope=slope,surplus_at_min_L=lowgap))
 feasible=[a for a in allrows if a['required_L'] is not None];best=min(feasible,key=lambda z:z['required_L']) if feasible else None;winners=[a for a in feasible if a['required_L']<=L0]
 rows.append(dict(name=name,original=dict(m=m0,L=L0,s=s0,q=qcap),target_surplus=target,tested=len(allrows),positive_slope=sum(a['slope']>0 for a in allrows),best=best,nonworsening=winners))
 print(name,'old target',target,'best',best,'winners',len(winners),flush=True)
(ROOT/'primary_sensitivity.json').write_text(json.dumps(dict(A=181275,complete=True,scope='Dimension positivity only; m<=oldm,s<=olds,floor(mA/w)<=oldq, one-residue closed counts.',rows=rows),indent=2)+'\n')
