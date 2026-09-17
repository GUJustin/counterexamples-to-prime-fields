"""Exact cutoff rank and the half-rank lemma for finite-length extension."""
from itertools import product
from math import comb
from fractions import Fraction as F
from pathlib import Path
import json
BASE=Path(__file__).resolve().parent

def formula(H,m,D,A):
 S={(u,b) for b,h in enumerate(H) for u in range(h) if m*A-D*(u+b)+b>0}
 G=sum(m*A-D*(u+b)+b for u,b in S)
 R=0;pieces=[]
 for q in range(max((u+b for u,b in S),default=-1)+1):
  U=sorted(u for u,b in S if u+b==q);L=m*A-(D-1)*q
  g=sum(max(0,L-u) for u in U)
  r=sum(min(sum(u<=ell for u in U),m-ell) for ell in range(max(0,min(m,L))))
  R+=r;pieces.append((q,L,g,r))
 return S,G,R,pieces

def matrix(H,m,D,A,p=1009):
 basis={}
 for b,h in enumerate(H):
  for u in range(h):
   for x in range(max(0,m*A-D*(u+b)+b)):
    col={}
    for j in range(u+1):
     i=x+u-j
     if i+2*j<m:col[(i,j,u-j+b)]=comb(u,j)%p
    while col:
     key=min(col)
     if key not in basis:
      inv=pow(col[key],-1,p);basis[key]={i:a*inv%p for i,a in col.items()};break
     f=col[key]
     for i,a in basis[key].items():
      v=(col.get(i,0)-f*a)%p
      if v:col[i]=v
      elif i in col:del col[i]
 return len(basis)

def main():
 half=0;maximum=F(0)
 for L in range(1,15):
  for mask in range(1,1<<L):
   U=[u for u in range(L) if mask>>u&1]
   G=sum(L-u for u in U)
   R=sum(min(sum(u<=ell for u in U),L-ell) for ell in range(L))
   assert G<=2*R
   maximum=max(maximum,F(G,R));half+=1
 matrices=0;dominations=0
 for H in product(range(4),repeat=3):
  for N in [12,16,20]:
   D=N//4-1
   for A in [N//4+1,N//2-1]:
    for m in range(1,6):
     S,G,R,pieces=formula(H,m,D,A)
     assert R==matrix(H,m,D,A);matrices+=1
     bad=[q for q,L,g,r in pieces if L<m]
     assert all(g<=2*r for q,L,g,r in pieces if q in bad)
     low={(u,b) for u,b in S if u+b not in bad}
     g0=sum(m*A-D*(u+b)+b for u,b in low)
     r0=sum(r for q,L,g,r in pieces if q not in bad)
     assert G-N*R<=g0-N*r0
     astar=F(A,N)+F(2*(A-1),N*(D-1))
     B=sum(m*astar-F(u+b,4) for u,b in low)
     assert B>=F(g0,N)
     assert all(m*astar>F(u+b,4) for u,b in low)
     assert astar==F(A*N-8,N*(N-8))
     dominations+=1
 out=dict(status='passed',half_rank_subsets=half,largest_dimension_rank_ratio=str(maximum),
  exact_cutoff_matrix_checks=matrices,finite_length_domination_checks=dominations,
  scope='Finite checks of the exact cutoff formula, half-rank inequality, and reduction. The uniform all-m theorem requires the separate injection and reduction proof.')
 (BASE/'finite_length_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
