"""Exact finite Fourier orthogonality and joint-image collision checks."""
from itertools import product,combinations
from collections import Counter
from math import prod
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def mul(a,b):
 n=len(a);out=[0]*n
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:out[(i+j)%n]+=x*y
 return out

def reduce_poly(a,phi):
 a=list(a);d=len(phi)-1
 for j in range(len(a)-1,d-1,-1):
  c=a[j]
  for k,x in enumerate(phi):a[j-d+k]-=c*x
 return a[:d]

def fourier(p,r,u,phi):
 U=p-1;V=U**r;xs=tuple(range(1,r+1));excluded={0}|{x for x in xs}|{-x%p for x in xs}
 allowed=[a for a in range(p) if a not in excluded]
 vecs=[tuple((x*x-a*a)%p for x in xs) for a in allowed]
 g=next(g for g in range(2,p) if len({pow(g,k,p) for k in range(U)})==U)
 logs={pow(g,k,p):k for k in range(U)}
 dist=Counter({(1,)*r:1})
 for _ in range(u):
  new=Counter()
  for v,c in dist.items():
   for w in vecs:new[tuple(a*b%p for a,b in zip(v,w))]+=c
  dist=new
 collision=sum(c*c for c in dist.values())
 total=[0]*U
 for chi in product(range(U),repeat=r):
  f=[0]*U
  for v in vecs:f[sum(k*logs[x] for k,x in zip(chi,v))%U]+=1
  star=[f[-j%U] for j in range(U)]
  square=mul(f,star);power=[1]+[0]*(U-1)
  for _ in range(u):power=mul(power,square)
  total=[a+b for a,b in zip(total,power)]
 residue=reduce_poly(total,phi)
 assert residue==[V*collision]+[0]*(len(phi)-2)
 assert sum(dist.values())==len(allowed)**u
 return dict(p=p,r=r,u=u,characters=V,allowed_seeds=len(allowed),product_vectors=len(dist),collision_pairs=collision,identity='sum_character_power = group_size * exact_collision_count, reduced modulo cyclotomic polynomial')

def images(p,r,m,D):
 xs=tuple(range(1,r+1));reps=range(r+1,(p+1)//2)
 cores=0;energy=0;collisions=Counter()
 for seed in combinations(reps,m):
  supp=list(combinations(seed,D));vectors=[tuple(prod((x*x-a*a)%p for a in I)%p for x in xs) for I in supp]
  hist=Counter(vectors);energy+=sum(c*c for c in hist.values());cores+=1
  for i,j in combinations(range(len(supp)),2):
   u=len(set(supp[i])-set(supp[j]))
   if vectors[i]==vectors[j]:assert u>r;collisions[u]+=1
 return dict(p=p,r=r,m=m,D=D,cores=cores,total_energy=energy,collisions_by_support_difference=dict(collisions))

if __name__=='__main__':
 start=time.monotonic()
 out=dict(status='passed',fourier=[fourier(11,2,3,[1,-1,1,-1,1]),fourier(11,3,4,[1,-1,1,-1,1]),fourier(19,2,3,[1,0,0,-1,0,0,1])],images=[images(23,2,6,3),images(29,3,8,4)],seconds=time.monotonic()-start,scope='Exact integer group convolutions and cyclotomic reductions verify Fourier identities; exhaustive cores verify zero collisions for support difference <= block size. The Weil estimate remains a cited theorem.')
 (BASE/'joint_image_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
