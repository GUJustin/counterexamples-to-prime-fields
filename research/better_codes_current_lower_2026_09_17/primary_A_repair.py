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

A=181275; rows=[]
for m in range(1,116):
 q,r=divmod(A*m,w)
 for s in range(q+1):
  if r+s>w:continue
  lower=max(m+s-1,q); L=274277
  gap=coeff(A,m,L,s)-n*rank(m,L,s)
  slope=coeff(A,m,L+1,s)-n*rank(m,L+1,s)-gap
  lowgap=gap+slope*(lower-L)
  req=lower if lowgap>0 else max(lower,L+(-gap)//slope+1) if slope>0 else None
  if req is not None:
   assert coeff(A,m,req,s)>n*rank(m,req,s)
   if req>lower:assert coeff(A,m,req-1,s)<=n*rank(m,req-1,s)
  rows.append(dict(m=m,s=s,q=q,slope=slope,gap=gap,required_L=req))
feasible=[x for x in rows if x['required_L'] is not None]
out=dict(target=A,scope='all 1<=m<=115, 0<=s<=floor(mA/w), L>=max(m+s-1,q), one-residue formula',count=len(rows),feasible=feasible,same_q=[x for x in rows if x['q']==159],best_slope=max(rows,key=lambda x:x['slope']))
(ROOT/'primary_A_repair.json').write_text(json.dumps(out,indent=2)+'\n')
print('cases',len(rows),'feasible',len(feasible),'best',min(feasible,key=lambda x:x['required_L']) if feasible else None)
print('s35to37',[x for x in rows if x['m']==115 and x['s'] in [35,36,37]])
# Truncated weighted-degree escape: all m>=116 dominated by m=116,
# D<=160*w-s, as coefficient spaces are nested in D and constraints in m.
trunc=[]
for s in range(160):
 m=116;D=160*w-s;lower=max(m+s-1,D//w);L=274277
 gap=coeff(D,1,L,s)-n*rank(m,L,s)
 slope=coeff(D,1,L+1,s)-n*rank(m,L+1,s)-gap
 lowgap=gap+slope*(lower-L)
 req=lower if lowgap>0 else max(lower,L+(-gap)//slope+1) if slope>0 else None
 trunc.append(dict(m=m,s=s,D=D,gap=gap,slope=slope,required_L=req))
out['truncated_degree']=trunc
(ROOT/'primary_A_repair.json').write_text(json.dumps(out,indent=2)+'\n')
print('truncated feasible',[x for x in trunc if x['required_L'] is not None])
