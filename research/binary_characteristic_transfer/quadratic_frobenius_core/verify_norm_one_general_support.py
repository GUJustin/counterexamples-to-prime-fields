"""Bounded exact replay of general support formulas; no word/domain search."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

def ceil(x):return -((-x.numerator)//x.denominator)
def prime_above(x):
 p=max(3,x+1)
 if p%2==0:p+=1
 while any(p%d==0 for d in range(3,isqrt(p)+1,2)):p+=2
 return p
rows=[]
for c in (F(3,2),F(7,4),F(19,10)):
 delta=c*c-2;h=ceil(8/delta);s=ceil(F(8*h)/delta);kap=ceil(4*c*c/delta)
 R=h*(h+1)*(6*s+2*h+7)//6
 crit=F(2*R,(s+1)*h*h)
 assert crit==2+F(2,h)+F((h+1)*(2*h+1),3*h*(s+1))<=2+delta/2<c*c
 # Original coefficient/local-rank sums at the smallest convenient active cap.
 T0=ceil(F(2*h+s,h));B0=h*T0
 gd=sum(max(2*h*T0-2*t+b,0) for t in range(B0+1) for b in range(min(t,s)+1))
 rd=sum(int(a+t<2*h*T0)*min(2*h-a,max(0,min(t,a)-max(0,t-s)+1)) for a in range(2*h) for t in range(B0+1))
 assert gd==(s+1)*B0*F(2*B0+2-s,2) and rd==R
 g2=(s+1)*h*h*c*c;g1=(s+1)*h*(F(s,2)-1)*c
 a2=(kap-1)*g2-2*kap*R;a1=(kap-1)*g1+2*kap*R;a0=2*kap*R
 C=h*(2*s+1);d0=2*C-s*(s+1);cor=2*max(d0,0)+2*h*(2*s-1)
 bound=max(F(s),3/(c-1),F(2*h+s)/(h*c),F(1),(a1+a0)/a2,F(cor,2))
 p=prime_above(ceil(bound));N=2*(p*p+p+1);T=ceil(c*p);B=h*T;H=kap*B
 G=(s+1)*B*F(2*B+2-s,2)
 assert a2>0 and p>s and B>=2*h+s
 inner=(kap-1)*G-kap*N*R
 assert inner>=a2*p*p-a1*p-a0>0
 surplus=(H-B+1)*G-(H+1)*N*R
 assert surplus>0
 lam=F(N-2,T-2);upper=lam*((2*s+1)*B-s*(s+1))+(2*s-1)*B-s*s
 assert upper<=C*N+cor*p<=(C+1)*N
 assert p+1<T<=2*p+2
 rows.append(dict(c=str(c),h=h,derivative_cap=s,kappa=kap,critical_squared=str(crit),direct_test_T=T0,direct_G=gd,direct_R=rd,p=p,N=N,T=T,coefficient_count=int(G),local_rank=R,graded_surplus=int(surplus),uniform_multiplier=C+1,list_bound=str(upper)))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
