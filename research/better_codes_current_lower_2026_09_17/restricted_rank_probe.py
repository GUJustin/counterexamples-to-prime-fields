"""Explicit YS-cap source using the audited restricted local-block rank bound."""
import json
from pathlib import Path
from capped_source_count import count
from affine_local_source_gate import rank as oldrank

def F(K,L):
 return 0 if K<0 else (K+1)*(K+2)*(3*(L+1)-2*K)//6

def B(M,L,S,Y):
 if min(M,L,S,Y)<0:return 0
 K=min(Y,L)
 return F(K,L)-F(K-M-1,L-M-1)-F(K-S-1,L-S-1)+F(K-M-S-2,L-M-S-2)

def rank(m,L,S,Y):
 ans=0
 for r in range(m):
  M=min(r,L);h=m-r
  ans+=B(M,L,S,Y)
  if h<=min(M,L,S,Y):ans-=B(M-h,L-h,S-h,Y-h)
 return ans

if __name__=='__main__':
 checks=0
 for M in range(7):
  for L in range(7):
   for S in range(7):
    for Y in range(7):
     brute=sum(L+1-a-b for a in range(M+1) for b in range(S+1) if a+b<=min(L,Y))
     assert B(M,L,S,Y)==brute;checks+=1
 m,L,S=64000,3840000,19840;A=181275;n=262144;D=m*A;Y0=(D+S-1)//131071
 R0=rank(m,L,S,Y0);assert R0==oldrank(m,L,S),(R0,oldrank(m,L,S))
 rows=[]
 for Y in [Y0,m+S-2,m-1,7*m//8,3*m//4,m//2,m//4,S]:
  C=count(D,L,Y,S);R=rank(m,L,S,Y)
  rows.append(dict(Y=Y,C=C,rank=R,rank_saved=R0-R,nullity_lower_bound=C-n*R,positive=C>n*R))
 out=dict(shape=dict(m=m,L=L,S=S,D=D,automaticY=Y0),brute_B_checks=checks,uncapped_rank_regression=R0,rows=rows,scope='Exact enclosing local-block rank; valid upper bound on restricted constraint extraction. One fixed source profile. Negative lower bound is failure of dimension certificate, not nonexistence.')
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
