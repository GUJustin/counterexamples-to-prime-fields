"""Exact small-field checks of cubic arrangement and collision identities."""
from itertools import combinations,product
from math import prod,isqrt
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent


def det(matrix,p):
 a=[list(row) for row in matrix];out=1
 for i in range(len(a)):
  j=next((j for j in range(i,len(a)) if a[j][i]%p),None)
  if j is None:return 0
  if j!=i:a[i],a[j]=a[j],a[i];out=-out
  v=a[i][i]%p;out=out*v%p
  for j in range(i+1,len(a)):
   c=a[j][i]*pow(v,-1,p)%p
   a[j]=[(x-c*y)%p for x,y in zip(a[j],a[i])]
 return out%p


def arrangement(p,u):
 A=list(range(u));B=list(range(u,2*u));nodes=A+B
 forms={a:(1,-a,-a*a,-a*a*a) for a in nodes}
 minors=0
 for xs in combinations(nodes,4):
  assert det([forms[x] for x in xs],p)!=0;minors+=1
 smooth=0
 if u>=2:
  for xs in combinations(nodes,3):
   if not(set(xs)&set(A) and set(xs)&set(B)):continue
   a,b,c=xs;point=(-a*b*c,-(a*b+a*c+b*c),a+b+c,-1)
   vals={x:sum(i*j for i,j in zip(forms[x],point))%p for x in nodes}
   assert {x for x,v in vals.items() if v==0}==set(xs)
   gradient=[(sum(forms[x][i]*prod(vals[y] for y in A if y!=x) for x in A)
              -sum(forms[x][i]*prod(vals[y] for y in B if y!=x) for x in B))%p
             for i in range(4)]
   assert any(gradient);smooth+=1
 points=0;good=0;outside=0
 for U,V in product(range(p),repeat=2):
  images={a:(a**3+V*a*a+U*a)%p for a in nodes}
  injective=len(set(images.values()))==2*u;good+=injective
  for X in range(p):
   equality=(prod((X-images[a])%p for a in A)-prod((X-images[a])%p for a in B))%p==0
   points+=equality
   if injective and X not in images.values():outside+=equality
 assert p>2*u*u
 upper=p*p+(u-1)*(u-2)*p*(isqrt(p)+1)+3*u**4*p
 assert points<=upper and outside<=points
 return dict(p=p,u=u,vandermonde_minors=minors,smooth_triple_points=smooth,
             hypersurface_points=points,point_count_upper=upper,
             injective_maps=good,outside_collisions=outside)


def locator(xs,p):
 coeff=[1]
 for x in xs:
  out=[0]*(len(coeff)+1)
  for j,v in enumerate(coeff):out[j]=(out[j]-x*v)%p;out[j+1]=(out[j+1]+v)%p
  coeff=out
 return coeff


def thue_morse():
 p=131;nodes=list(range(-16,1));anchor=0
 S=[i-16 for i in range(16) if i.bit_count()%2==0]+[anchor]
 T=[i-16 for i in range(16) if i.bit_count()%2==1]+[anchor]
 assert all(sum(x**j for x in S)==sum(x**j for x in T) for j in range(4))
 good=0;collisions=0;min_roots=100;max_roots=-1
 for U,V in product(range(p),repeat=2):
  images={x:(x**3+V*x*x+U*x)%p for x in nodes}
  if len(set(images.values()))!=len(nodes):continue
  good+=1
  FS=locator([images[x] for x in S],p);FT=locator([images[x] for x in T],p)
  assert FS[-2:]==FT[-2:] and FS[0]==FT[0]==0
  P=[(a-b)%p for a,b in zip(FS,FT)][1:]
  assert not any(P[7:]) and any(P)
  w=FS[1:];assert len(w)==9 and w[-1]==1
  ev=lambda coeff,x:sum(a*pow(x,j,p) for j,a in enumerate(coeff))%p
  core=[images[x] for x in nodes if x!=anchor]
  assert sum(ev(w,x)==ev(P,x) for x in core)==8
  roots=sum(ev(P,x)==0 for x in range(p) if x not in core and x!=0)
  # Zero is available for padding after anchor removal: P need not
  # vanish there. Include it in the outside collision total as well.
  roots+=ev(P,0)==0
  collisions+=roots;min_roots=min(min_roots,roots);max_roots=max(max_roots,roots)
 assert good>0
 return dict(p=p,seed_nodes=len(nodes),support_size=len(S),original_moments=3,
             transformed_moments=1,code_dimension=7,far_agreement=8,
             injective_maps=good,outside_pair_collisions=collisions,
             min_outside_roots=min_roots,max_outside_roots=max_roots)

if __name__=='__main__':
 start=time.monotonic()
 out=dict(status='passed',arrangements=[arrangement(p,u) for p,u in [(7,1),(17,2),(23,3),(37,4)]],
          moment_preservation=thue_morse(),seconds=time.monotonic()-start,
          scope='Finite checks of Vandermonde general position, smooth triple intersections, point-count bounds, moment preservation, and outside collision identities. Absolute irreducibility is proved in the written argument.')
 (BASE/'geometry_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
