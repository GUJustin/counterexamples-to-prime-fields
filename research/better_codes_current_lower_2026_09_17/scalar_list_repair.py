"""Bounded exact seedless scalar-list source repair at A181275."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent;A=181275;n=262144;w=131071;p=2130706433

def inp(M,L,s):
 a=min(M,L);full=min(a+1,max(0,L-s+1));rest=a+1-full
 return full*(s+1)+rest*(L+1)-(full+a)*rest//2

def rank(m,L,s):
 total=0
 for r in range(m):
  M=min(r,L);h=m-r
  total+=inp(M,L,s)-(inp(M-h,L-h,s-h) if h<=min(M,L,s) else 0)
 return total

def coeff(D,L,s):
 total=0
 for j in range(min(s,L)+1):
  v=D-(w-1)*j;k=min(L-j,(v-1)//w)
  if k>=0:total+=(k+1)*v-w*k*(k+1)//2
 return total

def budget(Y,s):
 capY=1+2*w*Y;capR=w*(2*s-1);gap=A-w
 num=(n-w)*(capY*s+capR*Y)+(2*s-1)*Y*gap
 return num//gap+1,num,capY,capR
assert coeff(115*181284,159,35)==47864396310 and rank(115,159,35)==182580
assert 47864396310-n*182580==2144790
rows=[];cases=0
for m in range(95,161):
 q=(m*A)//w
 for s in range(20,56):
  for Y in range(max(s,q-12),q+1):
   cases+=1;C=coeff(m*A,Y,s);R=rank(m,Y,s)
   if C<=n*R:continue
   B,num,cy,cr=budget(Y,s)
   assert num<B*(A-w) and m<p and Y<p and 0<s<p
   rows.append(dict(m=m,Y=Y,s=s,D=m*A,coefficients=C,rank=R,nullity=C-n*R,list_budget=B,list_numerator=num,capY=cy,capR=cr))
rows.sort(key=lambda x:(x['list_budget'],x['m'],x['Y'],x['s']))
out=dict(target_A=A,scope='m95..160,s20..55,Y=floor(mA/w)-12..floor(mA/w),Y>=s; exact seedless counts',tested=cases,feasible=len(rows),best=rows[:20],original_target_gap=coeff(115*A,159,35)-n*rank(115,159,35))
(ROOT/'scalar_list_repair.json').write_text(json.dumps(out,indent=2)+'\n')
print('cases',cases,'feasible',len(rows),'best',rows[0] if rows else None)
