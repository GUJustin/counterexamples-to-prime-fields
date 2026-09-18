"""Tiny independent polynomial determinant check, not a parameter survey."""
from itertools import permutations
from math import factorial
from pathlib import Path
import json
p=1000003;n=7

def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return c

def entry(i,j,h):
 f=[1]
 for a in range(h-1):
  shifts=(pow(4,-1,p),3*pow(4,-1,p)) if a<i else (1,3*pow(2,-1,p))
  for s in shifts:f=mul(f,[(j*n+a+s)%p,1])
 return f

rows=[]
for h in (2,3,4):
 ans=[0]*(2*h*(h-1)+1)
 for perm in permutations(range(h)):
  sign=(-1)**sum(perm[i]>perm[j] for i in range(h) for j in range(i+1,h))
  f=[1]
  for i,j in enumerate(perm):f=mul(f,entry(i,j,h))
  for d,c in enumerate(f):ans[d]=(ans[d]+sign*c)%p
 while ans and ans[-1]==0:ans.pop()
 expected=pow(n,h*(h-1)//2,p)
 for i in range(h):
  poch=1
  for j in range(i):poch=poch*(3*pow(2,-1,p)+j)%p
  expected=expected*poch*factorial(i)%p
 assert len(ans)-1==h*(h-1)
 assert ans[-1]==expected
 rows.append(dict(h=h,degree=len(ans)-1,leading=ans[-1],predicted=expected,permutations=factorial(h)))
out=dict(p=p,n=n,checks=rows,result='PASS',scope='Exact polynomial determinant at h2,3,4; independent validation of the analytic formula, not a subgroup scan.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
