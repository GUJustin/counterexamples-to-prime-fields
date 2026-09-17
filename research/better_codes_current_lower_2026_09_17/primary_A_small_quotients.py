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
for qcap in [160,161,162,163]:
 for m in range(115,120):
  for s in range(qcap+1):
   D=min(181275*m,(qcap+1)*w-s)
   q,r=divmod(D,w)
   if s>q or r+s>w:continue
   lower=max(m+s-1,q);L=274277
   gap=coeff(D,1,L,s)-n*rank(m,L,s)
   slope=coeff(D,1,L+1,s)-n*rank(m,L+1,s)-gap
   lowgap=gap+slope*(lower-L)
   req=lower if lowgap>0 else max(lower,L+(-gap)//slope+1) if slope>0 else None
   if req is not None:
    assert coeff(D,1,req,s)>n*rank(m,req,s)
    if req>lower:assert coeff(D,1,req-1,s)<=n*rank(m,req-1,s)
   rows.append(dict(qcap=qcap,m=m,s=s,D=D,slope=slope,required_L=req))
(ROOT/'primary_A_small_quotients.json').write_text(json.dumps(rows,indent=2)+'\n')
for q in [160,161,162,163]:
 for scap in [35,36,q]:
  good=[x for x in rows if x['qcap']==q and x['s']<=scap and x['required_L'] is not None]
  print(q,scap,'best',min(good,key=lambda x:x['required_L']) if good else None)
