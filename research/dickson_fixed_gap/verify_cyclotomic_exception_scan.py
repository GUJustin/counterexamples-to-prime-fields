"""Independent exact replay and coverage audit of the C++ exception scan."""
from pathlib import Path
from math import gcd
import json,time
from check_cyclotomic_lift import supports,rank,prime,generator

start=time.monotonic();base=Path(__file__).resolve().parent
rows=json.loads((base/'cyclotomic_exceptions_scan.json').read_text());out=[]
for row in rows:
 p0,n,k,limit=(row[x] for x in ['seed_prime','n','K','limit'])
 primes=[p for p in range(n+1,limit+1,n) if prime(p)]
 units=[a for a in range(1,n) if gcd(a,n)==1]
 assert len(primes)==row['primes'] and len(primes)*len(units)==row['embeddings']
 sets=supports(p0);g=generator(p0)
 for exc in row['exceptions']:
  q,z=exc['p'],exc['root'];assert q in primes
  assert len({pow(z,j,q) for j in range(n)})==n
  nodes={pow(g,j,p0):pow(z,j,q) for j in range(n)}
  r,_,_=rank(sets,n,k,q,nodes);assert r==exc['rank']<n-k
 assert len(row['exceptions'])==row['native_hits']==2
 assert all(x['p']==p0 for x in row['exceptions'])
 # Independently replay two full-rank new characteristics, including the largest.
 samples=[next(p for p in primes if p>p0),primes[-1]]
 for q in samples:
  z=pow(generator(q),(q-1)//n,q)
  nodes={pow(g,j,p0):pow(z,j,q) for j in range(n)}
  r,_,_=rank(sets,n,k,q,nodes);assert r==n-k
 out.append(dict(seed_prime=p0,primes=len(primes),embeddings=row['embeddings'],
                 exception_replays=len(row['exceptions']),full_rank_samples=samples))
result=dict(status='passed',results=out,total_embeddings=sum(x['embeddings'] for x in out),seconds=time.monotonic()-start,
            scope='Independent exception and sample rank replay, plus exact prime/embedding-count coverage. The full bounded census is C++; no beyond-cutoff claim except the separate n16 integral certificate.')
(base/'cyclotomic_exceptions_verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
