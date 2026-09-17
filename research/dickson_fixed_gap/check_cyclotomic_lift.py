"""Exact rank obstruction to the natural root-of-unity lift of seed supports."""
from pathlib import Path
from math import isqrt
import json,time
from check_integer_lift import supports


def prime(p):return p>=2 and all(p%d for d in range(2,isqrt(p)+1))
def generator(p):
 factors=[];n=p-1;d=2
 while d*d<=n:
  if n%d==0:
   factors.append(d)
   while n%d==0:n//=d
  d+=1
 if n>1:factors.append(n)
 return next(g for g in range(2,p) if all(pow(g,(p-1)//d,p)!=1 for d in factors))


def rank(sets,n,k,q,nodes):
 assert len(set(nodes.values()))==n
 pivots={};count=0;first_full=None
 for si,S in enumerate(sets,1):
  anchors=S[:k]
  invden=[pow(__import__('math').prod((nodes[a]-nodes[b])%q for b in anchors if b!=a)%q,-1,q) for a in anchors]
  for x in S[k:]:
   row=[0]*n;row[x-1]=1
   prod=__import__('math').prod((nodes[x]-nodes[a])%q for a in anchors)%q
   for a,v in zip(anchors,invden):row[a-1]=-prod*pow((nodes[x]-nodes[a])%q,-1,q)*v%q
   count+=1
   for col in range(n):
    v=row[col]
    if not v:continue
    if col in pivots:
     basis=pivots[col]
     for j in range(col,n):row[j]=(row[j]-v*basis[j])%q
    else:
     inv=pow(v,-1,q);pivots[col]=[(z*inv)%q for z in row];break
   assert len(pivots)<=n-k
   if len(pivots)==n-k:
    first_full=si
    return len(pivots),count,first_full
 return len(pivots),count,first_full


def main():
 start=time.monotonic();out=[]
 for p in [17,41,97,193]:
  n=p-1;k=n//4;sets=supports(p);g=generator(p)
  q=((65536+n-1)//n)*n+1
  while not prime(q):q+=n
  z=pow(generator(q),(q-1)//n,q)
  nodes={pow(g,j,p):pow(z,j,q) for j in range(n)}
  rk,count,prefix=rank(sets,n,k,q,nodes)
  assert rk==n-k
  native,_,_=rank(sets,n,k,p,{x:x for x in range(1,p)})
  assert native==n-k-1
  out.append(dict(seed_prime=p,n=n,K=k,seed_generator=g,auxiliary_prime=q,
                  primitive_nth_root=z,native_rank=native,cyclotomic_rank=rk,
                  rows_used=count,support_prefix_sufficing=prefix,
                  characteristic_zero_kernel_dimension=k))
 result=dict(status='passed',results=out,seconds=time.monotonic()-start,
             scope='Same seed supports on their natural cyclotomic lifts. Auxiliary modular rank certifies characteristic-zero rank; new received words and witnesses allowed. Does not exclude arbitrary moving nodes or selected other sublists.')
 Path(__file__).with_name('cyclotomic_lift_verification.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
