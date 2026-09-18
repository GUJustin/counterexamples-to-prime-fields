"""Direct finite support replay, separate from the original 22N receipt."""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json
rows=[]
for p in (401,4099,8191):
 N=2*(p*p+p+1)
 lo=isqrt(3*p*p)+1
 for T in (lo,2*p+2):
  m,s,B,H=16,8,8*T,800*T
  G=sum(max(m*T-2*t+b,0) for t in range(B+1) for b in range(min(t,s)+1))
  rs=[sum(int(a+t<m*T)*min(m-a,max(0,min(t,a)-max(0,t-s)+1)) for t in range(B+1)) for a in range(m)]
  R=sum(rs)
  assert G==9*B*B-27*B and R==852
  inner=99*G-100*N*R
  assert inner>=672*p*p-213168*p-213168>0
  surplus=(H-B+1)*G-(H+1)*N*R
  assert surplus==B*inner+(G-N*R)>0
  lam=Fraction(N-2,T-2)
  upper=lam*(17*B-72)+15*B-64
  assert upper==136*N+200*lam+120*T-336
  assert upper<=136*N+640*p-96<=137*N and p>8
  rows.append(dict(p=p,T=T,N=N,G=G,R=R,local_ranks=rs,graded_surplus=surplus,upper_numerator=upper.numerator,upper_denominator=upper.denominator,uniform_upper=137*N))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
print('PASS',len(rows),'endpoint profiles; all intermediate T follow monotonicity and the stated inequalities')
