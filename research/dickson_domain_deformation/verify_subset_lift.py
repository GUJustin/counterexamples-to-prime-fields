"""Certify a smooth ten-candidate subbank of the obstructed p41 seed."""
from math import comb
from pathlib import Path
import json
BASE=Path(__file__).resolve().parent


def ev(c,x,m):
 a=0
 for v in reversed(c):a=(a*x+v)%m
 return a


def determinant(a,p):
 a=[row[:] for row in a];det=1
 for c in range(len(a)):
  r=next((r for r in range(c,len(a)) if a[r][c]%p),None)
  if r is None:return 0
  if r!=c:a[r],a[c]=a[c],a[r];det=-det
  d=a[c][c]%p;det=det*d%p;inv=pow(d,-1,p)
  for r in range(c+1,len(a)):
   f=a[r][c]*inv%p
   for j in range(c+1,len(a)):a[r][j]=(a[r][j]-f*a[c][j])%p
 return det%p


def main():
 p=41;n=40;k=10;labels=[3,8,10,11,12,13,16,17,18,20]
 cs=[[comb(21,2*j+1)*pow(a,20-2*j,p)%p for j in range(k)] for a in labels]
 xs=list(range(1,p))
 word=[((1+(1 if pow(x,20,p)==1 else -1))//2-pow(x,k,p))%p for x in xs]
 supports=[[u for u,x in enumerate(xs) if ev(c,x,p)==word[u]] for c in cs]
 assert all(len(s)==15 for s in supports)
 equations=[];J=[];rhs=[];v=n+len(cs)*k
 for u,x in enumerate(xs):
  inc=[i for i,s in enumerate(supports) if u in s];assert inc
  ref=inc[0]
  for i in inc[1:]:
   equations.append((u,i,ref));row=[0]*v
   row[u]=sum(t*(cs[i][t]-cs[ref][t])*pow(x,t-1,p) for t in range(1,k))%p
   for t in range(k):row[n+i*k+t]=pow(x,t,p);row[n+ref*k+t]=-pow(x,t,p)%p
   J.append(row)
   residual=(ev(cs[i],x,p*p)-ev(cs[ref],x,p*p))%(p*p)
   assert residual%p==0
   rhs.append(-residual//p%p)
 M=[row+[b] for row,b in zip(J,rhs)];piv=[];rank=0
 for col in range(v):
  r=next((r for r in range(rank,len(M)) if M[r][col]%p),None)
  if r is None:continue
  M[r],M[rank]=M[rank],M[r]
  inv=pow(M[rank][col],-1,p);M[rank]=[a*inv%p for a in M[rank]]
  for r in range(len(M)):
   if r!=rank and M[r][col]:
    fac=M[r][col];M[r]=[(a-fac*b)%p for a,b in zip(M[r],M[rank])]
  piv.append(col);rank+=1
  if rank==len(M):break
 assert rank==len(J)==110
 minor_det=determinant([[row[c] for c in piv] for row in J],p)
 assert minor_det
 correction=[0]*v
 for i,c in enumerate(piv):correction[c]=M[i][-1]
 assert all(sum(a*b for a,b in zip(row,correction))%p==b for row,b in zip(J,rhs))
 lifted_x=[(x+p*correction[u])%(p*p) for u,x in enumerate(xs)]
 lifted_c=[[(a+p*correction[n+i*k+t])%(p*p) for t,a in enumerate(c)] for i,c in enumerate(cs)]
 assert all(ev(lifted_c[i],lifted_x[u],p*p)==ev(lifted_c[r],lifted_x[u],p*p) for u,i,r in equations)
 lifted_word=[]
 for u,x in enumerate(lifted_x):
  ref=next(i for i,s in enumerate(supports) if u in s)
  lifted_word.append(ev(lifted_c[ref],x,p*p))
 assert all([u for u,x in enumerate(lifted_x) if ev(c,x,p*p)==lifted_word[u]]==supports[i] for i,c in enumerate(lifted_c))
 result=dict(status='passed',p=p,n=n,k=k,selected_labels=labels,list_size=10,agreements_each=15,
  equations=len(J),variables=v,rank=rank,pivot_columns=piv,minor_determinant=minor_det,
  first_correction=correction,lifted_nodes=lifted_x,lifted_polynomials=lifted_c,
  scope='Full-row-rank minor and direct mod1681 replay certify this ten-candidate subbank. Hensel gives a characteristic-zero lift and algebraic specialization gives large splitting primes. No complete-list or maximum-agreement assertion.')
 (BASE/'subset_lift_verification.json').write_text(json.dumps(result,indent=2)+'\n')
 print({a:b for a,b in result.items() if not isinstance(b,list)})
if __name__=='__main__':main()
