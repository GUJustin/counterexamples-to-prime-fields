"""Single surviving wedge candidate with safe quotient-cap erosion."""
import json
from pathlib import Path
from wedge_probe import C,rank,W,A,N

def slab(D,L,S,H,k,width):
 if min(D-1,L,S,H)<0:return 0
 ans=0
 for j in range(min(S,L,H//k)+1):
  d=D-(W-1)*j
  end=min(L-j,H-k*j,(d-1)//W)
  if end<0:continue
  full=min(end,(d-width)//W)
  if full>=0:
   nn=full+1;ans+=width*(nn*(L+1-j)-full*nn//2)
  for i in range(max(0,full+1),end+1):
   ans+=(L+1-i-j)*min(width,max(0,d-W*i))
 return ans

def band(m,L,S,H,k,r,y,t,actual_weighted_degree=None):
 D=m*A;delta=A-W+1;Y=(D+S-1)//W
 # deg_(1,k)(F)>=max(deg_YS(F),k*deg_R(F)).
 dH=max(y,k*r) if actual_weighted_degree is None else actual_weighted_degree
 assert max(y,k*r)<=dH<=y+(k-1)*r
 dc=W*y-r
 fuel=min(L//t,S//r,Y//y,H//dH)
 total=0
 for h in range(1,fuel+1):
  Dh=max(0,D-h*dc-(h-1)*delta)
  total+=slab(Dh,L-h*t,S-h*r,H-h*dH,k,delta)
 return total

if __name__=='__main__':
 checks=0
 for k in [1,2,3]:
  for D in [17,W-3,W+41,3*W+4]:
   for H in [2,5,12]:
    assert slab(D,8,5,H,k,50205)==C(D,8,5,H,k)-C(max(0,D-50205),8,5,H,k)
    checks+=1
 m,L,S=1000,60000,310;rows=[]
 for k,H in [(1,1383),(2,1538)]:
  gap=C(m*A,L,S,H,k)-N*rank(m,L,S,H,k)
  for z in [2975,3206]:
   b=band(m,L,S,H,k,12,55,z+55)
   rows.append(dict(kappa=k,H=H,z=z,gap=gap,slab=b,margin=gap-b))
 out=dict(slab_difference_checks=checks,rows=rows,scope='Fixed small-scale shape; quotient weighted-cap erosion uses only guaranteed max(y,k*r), not assumed maximal factor weighted degree. Requires wedge-source and wedge-band formal lemmas; no helper/count certificate.')
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
