"""Exhaust all degree <=2 codeword graphs in small RS examples.

Checks the quantitative incidence bound from either a far direction
or a far line point, including a point away from parameter zero.
"""
from itertools import product
from pathlib import Path
import json,time


def run():
 start=time.monotonic();p=5;domain=tuple(range(p));n=len(domain)
 words=[tuple((a+b*x)%p for x in domain) for a,b in product(range(p),repeat=2)]
 square=tuple(x*x%p for x in domain)
 directions=[tuple(1 for x in domain),tuple(x%2 for x in domain),square]
 rows=[];total=0
 for mode in ('point','direction'):
  for seed in directions:
   g=seed if mode=='point' else square
   z0=2
   f=tuple((square[j]-z0*g[j])%p for j in range(n)) if mode=='point' else seed
   far=tuple((f[j]+z0*g[j])%p for j in range(n)) if mode=='point' else g
   a0=max(sum(a==b for a,b in zip(far,w)) for w in words)
   assert a0==2
   line=[tuple((f[j]+z*g[j])%p for j in range(n)) for z in range(p)]
   for e in (1,2):
    maxima={T:0 for T in range(a0+1,n+1)}
    for coeffs in product(words,repeat=e+1):
     graph=[tuple(sum(pow(z,t,p)*coeffs[t][j] for t in range(e+1))%p
                  for j in range(n)) for z in range(p)]
     agreements=[sum(a==b for a,b in zip(w,v)) for w,v in zip(line,graph)]
     a=sum(f[j]==coeffs[0][j] and g[j]==coeffs[1][j]
           and all(coeffs[t][j]==0 for t in range(2,e+1)) for j in range(n))
     assert a<=a0
     assert sum(agreements)<=p*a+e*(n-a)
     for T in maxima:
      count=sum(v>=T for v in agreements)
      assert count*(T-a)<=e*(n-a)
      assert count<=e*(n-a0)//(T-a0)
      maxima[T]=max(maxima[T],count)
     total+=1
    rows.append(dict(mode=mode,seed=seed,degree=e,far_agreement=a0,maxima=maxima))
 return dict(status='passed',p=p,n=n,K=2,graphs_enumerated=total,rows=rows,
             seconds=time.monotonic()-start,
             scope='Exhaustive small-field incidence checks; the general result is proved by coordinate root counting.')

if __name__=='__main__':
 out=run()
 Path(__file__).with_name('far_concurrency_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
