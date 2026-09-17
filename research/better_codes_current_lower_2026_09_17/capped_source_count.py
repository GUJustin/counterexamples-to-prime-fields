"""Exact monomial count with independent total, YS, and slope caps.
No source existence or local-rank claim is made by this arithmetic module.
"""
def count(D,L,Y,S,w=131071):
 if min(D-1,L,Y,S)<0:return 0
 total=0
 for j in range(min(L,Y,S)+1):
  d=D-(w-1)*j
  if d<=0:continue
  nn=min(L-j,Y-j,(d-1)//w)+1
  if nn<=0:continue
  C=L+1-j
  total+=nn*d*C+w*nn*(nn-1)*(2*nn-1)//6-(d+w*C)*nn*(nn-1)//2
 return total
