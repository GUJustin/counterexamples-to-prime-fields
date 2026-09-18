"""Complete all-prime support-norm sieve for r3,M5; no prime cutoff."""
import itertools,json,time,math
from pathlib import Path
from flint import fmpz_poly,nmod_poly
from sympy import factorint
P=Path(__file__).parent;start=time.monotonic();phi=fmpz_poly([1,0,-1,0,1]);roots=[fmpz_poly([0]*j+[1])%phi for j in range(12)];one=fmpz_poly([1]);records=[];good=[];char0=[];candidates=set()
for sub in itertools.combinations(range(12),5):
 h=[one,fmpz_poly([]),fmpz_poly([]),fmpz_poly([])]
 for j in sub:
  a=roots[j]
  for d in range(1,4):h[d]=(h[d]+a*h[d-1])%phi
 eq=[h[2],h[3]-2];norms=[abs(int(phi.resultant(e))) for e in eq];g=math.gcd(*norms)
 if not g:char0.append(sub);continue
 ps=[int(p) for p in factorint(g) if p%12==1];candidates.update(ps)
 for p in ps:
  gcd=nmod_poly(list(map(int,phi)),p)
  for e in eq:gcd=gcd.gcd(nmod_poly(list(map(int,e)),p))
  if gcd.degree()>0:
   row={'support_exponents':sub,'prime':p,'norms':norms,'common_factor':list(map(int,gcd))};good.append(row)
 records.append({'support':sub,'norm_gcd':g})
out={'r':3,'target_agreement':5,'support_count':792,'char0_supports':char0,'split_prime_candidates':sorted(candidates),'actual_exceptional_primes':sorted({r['prime'] for r in good}),'exceptional_support_embeddings':good,'seconds':time.monotonic()-start};(P/'exceptional_r3_supports.json').write_text(json.dumps(out,indent=2));print(out)
