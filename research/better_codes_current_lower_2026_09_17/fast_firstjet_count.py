"""Exact O(number of residue crossings) coefficient count for L>=floor((D+s-1)/w)."""
from math import comb

def coefficient_count(D,L,s,w=131071):
 q,r=divmod(D,w)
 assert 0<=s<=q and (D+s-1)//w<=L
 cuts={0,s+1}
 for k in range((r+s)//w+1):
  j=k*w-r+1
  if 0<j<=s:cuts.add(j)
 total=0;cuts=sorted(cuts)
 for lo,end in zip(cuts,cuts[1:]):
  e=(r+lo+w-1)//w
  def term(j):
   d=D-(w-1)*j;C=L+1-j;nn=q-j+e
   return nn*d*C+w*nn*(nn-1)*(2*nn-1)//6-(d+w*C)*nn*(nn-1)//2
  dif=[term(lo+j) for j in range(4)];length=end-lo
  for degree in range(4):
   total+=comb(length,degree+1)*dif[0]
   dif=[b-a for a,b in zip(dif,dif[1:])]
 return total
