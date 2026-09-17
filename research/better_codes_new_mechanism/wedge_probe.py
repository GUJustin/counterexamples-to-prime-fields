"""Independent weighted-YS support, with exact enclosing-block contact rank.
H controls i+kappa*j, whereas L controls i+j+z.
"""
import json
from pathlib import Path
W=131071;A=181275;N=262144

def B(M,L,S,H,k):
 if min(M,L,S,H)<0:return 0
 ans=0
 for b in range(min(S,L,H//k)+1):
  a=min(M,L-b,H-k*b);nn=a+1
  ans+=nn*(L+1-b)-a*nn//2
 return ans

def rank(m,L,S,H,k):
 ans=0
 for r in range(m):
  h=m-r;M=min(r,L)
  ans+=B(M,L,S,H,k)
  if h<=min(M,L,S) and k*h<=H:
   ans-=B(M-h,L-h,S-h,H-k*h,k)
 return ans

def C(D,L,S,H,k):
 ans=0
 for b in range(min(S,L,H//k)+1):
  d=D-(W-1)*b
  if d<=0:continue
  nn=min(L-b,H-k*b,(d-1)//W)+1
  c=L+1-b
  ans+=nn*d*c+W*nn*(nn-1)*(2*nn-1)//6-(d+W*c)*nn*(nn-1)//2
 return ans

if __name__=='__main__':
 checks=0
 for k in [1,2,3]:
  for H in range(10):
   for M,L,S in [(3,5,4),(6,4,2),(2,8,5)]:
    brute=sum(L+1-a-b for a in range(M+1) for b in range(S+1) if a+b<=L and a+k*b<=H)
    assert B(M,L,S,H,k)==brute;checks+=1
 cchecks=0
 for k in [1,2,3]:
  for H in range(8):
   DD=3*W+17;LL=5;SS=4
   brute=sum((LL+1-i-j)*max(DD-W*i-(W-1)*j,0) for j in range(SS+1) for i in range(LL-j+1) if i+k*j<=H)
   assert C(DD,LL,SS,H,k)==brute;cchecks+=1
 m,L,S=1000,60000,310;D=m*A;automaticY=(D+S-1)//W
 rows=[]
 for k,H in [(1,automaticY),(2,automaticY),(2,automaticY+S//2),(2,automaticY+S),(3,automaticY),(3,automaticY+S),(3,automaticY+2*S)]:
  c=C(D,L,S,H,k);r=rank(m,L,S,H,k)
  rows.append(dict(kappa=k,H=H,C=c,rank=r,nullity_lower_bound=c-N*r,positive=c>N*r))
 out=dict(shape=dict(m=m,L=L,S=S,D=D),B_brute_checks=checks,C_brute_checks=cchecks,rows=rows,scope='One finite weighted-support feasibility gate; rank is exact for enclosing local block, upper bound for extraction. No routing/certificate claim.')
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
