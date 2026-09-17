"""Exact rational continuum ledger; five local derivative probes, not a grid."""
from fractions import Fraction as F
import json
A=181275;w=131071;n=262144;alpha=F(A,w);rho=F(n,w);d=F(A-w+1,w)
def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return c
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def scale(a,k):return [x*k for x in a]
def inte(a,lo,hi):return sum(x*(hi**(i+1)-lo**(i+1))/F(i+1) for i,x in enumerate(a))
def rank(l,s):
 c=2*l-1-s
 removed=6*s*s*c+3*(s-(1+2*s)*c)*s*s+2*(-1-2*s+2*c)*s**3+3*s**4
 return (s*(6*l-2-3*s)-removed)/12
def gap(l,s):
 b=[alpha,-(1-F(1,w))]
 C=inte(add(scale(mul([l,-1],mul(b,b)),F(1,2)),scale(mul(b,mul(b,b)),-F(1,6))),F(0),s)
 return C-rho*rank(l,s)
def thin(l,s,t=3261,y=55,r=12):
 T=[l,-F(t)];Y=[alpha+s/w,-F(y)];S=[s,-F(r)]
 Ypre=[alpha+s/w,-(y+d)];Ypost=[s/w,-F(r,w)]
 end=min(l/t,(alpha+s/w)/y,s/r);cuts={F(0),end}
 switch=alpha/(y+d-F(r,w))
 if 0<switch<end:cuts.add(switch)
 lines=[T,Y,S,Ypre,Ypost]
 for i,P in enumerate(lines):
  for Q in lines[:i]:
   if P[1]!=Q[1]:
    x=(Q[0]-P[0])/(P[1]-Q[1])
    if 0<x<end:cuts.add(x)
 cuts=sorted(cuts);total=F(0)
 for lo,hi in zip(cuts,cuts[1:]):
  mid=(lo+hi)/2;limit=Ypre if mid<switch else Ypost
  U=min([T,Y,limit],key=lambda P:P[0]+P[1]*mid)
  V=min([S,U],key=lambda P:P[0]+P[1]*mid)
  ch=add(add(mul(T,add(mul(V,U),scale(mul(V,V),-F(1,2)))),scale(mul(V,mul(U,U)),-F(1,2))),scale(mul(V,mul(V,V)),F(1,6)))
  total+=inte(ch,lo,hi)
 return d*total
rows=[]
for l,s in [(F(60),F(31,100)),(F(599,10),F(31,100)),(F(601,10),F(31,100)),(F(60),F(3099,10000)),(F(60),F(3101,10000))]:
 g=gap(l,s);th=thin(l,s)
 rows.append(dict(L_over_m=float(l),s_over_m=float(s),gap=float(g),thin=float(th),margin=float(g-th),relative_margin=float((g-th)/g),char_m_max=int(F(2130706432,1)/(163*l+9678*(alpha+s/w)))))
print(json.dumps(dict(scope='Continuum only; not a finite gate or certificate',rows=rows),indent=2))
