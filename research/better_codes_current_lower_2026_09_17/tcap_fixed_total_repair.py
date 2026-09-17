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

def smallcoeff(D,L,s):
 ans=0
 for j in range(min(s,L)+1):
  v=D-(w-1)*j
  k=min(L-j,(v-1)//w)
  if k<0:continue
  z=L+1-j
  ans+=(k+1)*z*v-(z*w+v)*k*(k+1)//2+w*k*(k+1)*(2*k+1)//6
 return ans

def cdiff(D,u,s):
 # C(u+1)-C(u), exact including the newly available diagonals.
 ans=0
 for j in range(min(s,u+1)+1):
  v=D-(w-1)*j;k=min(u+1-j,(v-1)//w)
  if k>=0:ans+=(k+1)*v-w*k*(k+1)//2
 return ans

def solve(m,s,T):
 D=181275*m;q,r=divmod(D,w)
 if s>q or r+s>w:return None
 low=max(m+s-1,q);base=max(low,T+1)
 c=coeff(181275,m,base,s);rank0=rank(m,base,s)
 G=c-n*rank0
 slope=coeff(181275,m,base+1,s)-n*rank(m,base+1,s)-G
 def gap(L):return G+slope*(L-base)
 def strong(L):return gap(L)-smallcoeff(D,L-T-1,s)
 # Above quotient degree q all coefficient increments have reached saturation.
 ulo=base-T-1;uhi=max(ulo,q+2)
 lo=ulo;hi=uhi
 while lo<hi:
  mid=(lo+hi)//2
  if cdiff(D,mid,s)<slope:lo=mid+1
  else:hi=mid
 peak=T+1+lo;peakgap=strong(peak)
 req=None
 # If L<=T, ordinary positivity already forces total common-divisor degree<=T.
 if low<=T:
  if gap(low)>0:req=low
  elif slope>0 and gap(T)>0:req=max(low,base+(-G)//slope+1)
 if req is None and peakgap>0:
  lo2=base;hi2=peak
  while lo2<hi2:
   mid=(lo2+hi2)//2
   if strong(mid)>0:hi2=mid
   else:lo2=mid+1
  req=lo2
  assert strong(req)>0
  if req>base:assert strong(req-1)<=0
 return dict(m=m,s=s,q=q,T=T,slope=slope,min_total_cap=(T+(-peakgap)//slope+1 if peakgap<=0 and slope>0 else T if peakgap>0 else None),peak_L=peak,peak_strong_gap=peakgap,required_L=req,nullity=gap(req) if req is not None else None,quotient_count=smallcoeff(D,req-T-1,s) if req is not None and req>T else None)
# Independent exact small-box and difference sanity checks.
for D in [17,131071*3+7,40968150]:
 for u in [0,1,5,50,312]:
  for s in [0,3,70]:
   direct=sum((u+1-i-j)*max(0,D-w*i-(w-1)*j) for i in range(u+1) for j in range(min(s,u-i)+1))
   assert smallcoeff(D,u,s)==direct
   assert cdiff(D,u,s)==smallcoeff(D,u+1,s)-smallcoeff(D,u,s)
rows=[]
for m in range(1,261):
 for s in range(0,91):
  if m>226 and (m<220 or s<50):continue
  z=solve(m,s,9275)
  if z is not None:rows.append(z)
feas=[x for x in rows if x['required_L'] is not None]
oldbox=[x for x in feas if x['m']<=226 and x['s']<=70]
print('cases',len(rows),'feasible',len(feas),'oldbox',len(oldbox))
print('bestold',min(oldbox,key=lambda x:x['required_L']) if oldbox else None)
print('best',min(feas,key=lambda x:x['required_L']) if feas else None)
print('same',[x for x in rows if x['m']==226 and x['s']==70])
(ROOT/'tcap_fixed_total_repair.json').write_text(json.dumps(dict(target=181275,total_cap=9275,rows=rows),indent=2)+'\n')

near=[x for x in rows if x['min_total_cap'] is not None];print('nearesttotal',min(near,key=lambda x:x['min_total_cap']))
print('nearestsameq',min([x for x in near if x['q']<=312 and x['s']<=70],key=lambda x:x['min_total_cap']))
