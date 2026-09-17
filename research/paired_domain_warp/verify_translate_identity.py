"""Exact finite checks of the missing-set translate recurrence."""
from collections import Counter
from fractions import Fraction
from itertools import product
from random import Random
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def check(p,r,old):
 xs=list(range(1,r+1));excluded={0}
 for a in xs+old:excluded|={a,p-a}
 T=[a for a in range(p) if a not in excluded];N=len(T);V=(p-1)**r;C=4*r+2
 assert len(excluded)**2<p and N*2>=p
 vectors=[tuple((x*x-a*a)%p for x in xs) for a in T]
 ratios=Counter()
 for v in vectors:
  for w in vectors:ratios[tuple(a*pow(b,-1,p)%p for a,b in zip(v,w))]+=1
 identity=(1,)*r;assert ratios[identity]>=2*N
 universe=list(product(range(1,p),repeat=r));rng=Random(1729);rows=[]
 for size in sorted(set([0,1,5,20,min(100,V),V-20,V-5,V-1,V])):
  B=set(rng.sample(universe,size));small=B if size<=V//2 else set(universe)-B
  weighted=0
  for shift,c in ratios.items():
   inv=tuple(pow(a,-1,p) for a in shift)
   inter=sum(tuple(a*b%p for a,b in zip(v,inv)) in small for v in small)
   if size>V//2:inter=2*size-V+inter
   weighted+=c*inter
  h=Fraction(size,V);uncond=Fraction(weighted,N*N*V)
  cond=Fraction(weighted-2*N*size,N*(N-2)*V)
  assert cond>=0 and uncond<=h*h+Fraction(C*C,p)*h
  assert cond<=(h*h+Fraction(C*C,p)*h)/Fraction(p-4,p)
  assert cond<=uncond/Fraction(N-2,N)
  rows.append(dict(missing_size=size,unconditional=str(uncond),conditional=str(cond)))
 return dict(p=p,r=r,old_core_orbits=old,available=N,group_size=V,ordered_seed_pairs=N*N,rows=rows)

if __name__=='__main__':
 start=time.monotonic();out=dict(status='passed',cases=[check(257,1,[2,3,4]),check(127,2,[])],seconds=time.monotonic()-start,scope='Exact translate-intersection averages, exclusion of equal sign-orbits, and conservative Fourier/conditioning recurrence on finite missing sets. General Parseval argument is in the written proof.')
 (BASE/'translate_identity_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
