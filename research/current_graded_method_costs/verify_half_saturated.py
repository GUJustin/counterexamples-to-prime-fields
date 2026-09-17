from fractions import Fraction as F
from pathlib import Path
import json
checks=0
for m in range(2,81):
 for b in range(m//2+1):
  for Q in {m+b-1,2*m-2}:
   if Q<m+b-1:continue
   direct=sum(max(0,m-u-v,(m-u+1)//2) for v in range(b+1) for u in range(Q-v+1))
   formula=sum(F(m*m+m,2)-m*v+v*v for v in range(b+1))
   assert direct==formula
   a=F(139,200)
   G=sum((Q-v+1)*(m*a-F(Q+v,4)) for v in range(b+1))
   bracket=m*m*(a*a-F(1,2))+m*(1-a)*F(b-1,2)-F(b*(b+1),4)+F(1,16)
   assert G-direct<=(b+1)*bracket
   assert bracket<=m*m*(5*a*a-2*a-1)/4-F(3,4)*m*(1-a)+F(1,8)
   checks+=1
for m in range(32,513):
 a=F(139,200);b=F(m,8)
 bracket=m*m*(a*a-F(1,2))+m*(1-a)*(b-1)/2-b*(b+1)/4+F(1,16)
 assert bracket<0
n=262144;A=181284;a=F(A*n-4,n*(n-4));ff=(5*a*a-2*a-1)/4
assert all(m*m*ff-F(3,4)*m*(1-a)+F(1,8)<=0 for m in range(1,114))
assert 114**2*ff-F(3,4)*114*(1-a)+F(1,8)>0
out={'rank_and_surplus_cases':checks,'small_width_checks':481,'benchmark_saturated_necessary_m':114,'status':'passed; Riemann and continuity arguments remain analytic'}
Path(__file__).with_name('half_saturated_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
