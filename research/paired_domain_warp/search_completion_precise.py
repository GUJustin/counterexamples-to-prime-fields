"""Bounded fixed-point search; every rounding is upward and uses integers."""
from math import comb
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def certify(b,r,n,t,budget=0,Cextra=2,conditioning=4):
 p=2**b-1;K=n//2;D=(K+1)//2;m=n//2-r-2*t;d=D-t
 if not (n%4==2 and 0<d<m and p>(n+1)**2):return None
 C=4*r+Cextra;L=comb(m,d);precision=r*b+64;scale=1<<precision
 num=p**r*(p-2*m*m)+L*(C**(2*r+2)+2*m*m);den=L*(p-2*m*m)
 up=lambda a,b:(a+b-1)//b
 u=up(num*scale*(1<<budget),den);seq=[u]
 if u>=scale:return None
 for _ in range(t):
  u=up((p*u*u+C*C*u*scale)*(1<<budget),(p-conditioning)*scale);seq.append(u)
  if u>=scale:return None
 if (p-1)**r*u>=scale:return None
 return dict(b=b,r=r,n=n,K=K,t=t,m0=m,D0=d,precision=precision,scaled_missing=[str(v) for v in seq],event_budget_bits=budget)

if __name__=='__main__':
 start=time.monotonic();rows=[]
 for b in [31,61,89,107,127]:
  r=1;first=None
  for n in range(2*b,3*b+1):
   if n%4!=2:continue
   p=2**b-1
   if n**3*2**n>=p**3:continue
   for t in range(1,16):
    row=certify(b,r,n,t)
    if row:first=row;break
   if first:break
  rows.append(dict(b=b,first=first))
 out=dict(status='completed',rows=rows,seconds=time.monotonic()-start,scope='Exact sufficient recurrence search; strict Elias checked separately before promotion.')
 (BASE/'precise_completion_search.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
