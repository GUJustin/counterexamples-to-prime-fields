"""All split-prime classification via safe affine/Galois support orbits."""
import itertools,json,time,math
from pathlib import Path
from flint import fmpz_poly,nmod_poly
from sympy import factorint
P=Path(__file__).parent;start=time.monotonic();phi=fmpz_poly([1,0,-1,0,1,0,-1,0,1]);roots=[fmpz_poly([0]*j+[1])%phi for j in range(20)];one=fmpz_poly([1]);units=[a for a in range(20) if math.gcd(a,20)==1];seen=set();records=[];good=[];char0=[];candidates=set();hist={}
for sub in itertools.combinations(range(20),8):
 if sub in seen:continue
 orbit={tuple(sorted((a*j+4*b)%20 for j in sub)) for a in units for b in range(5)};seen.update(orbit)
 h=[one]+[fmpz_poly([]) for _ in range(5)]
 for j in sub:
  for d in range(1,6):h[d]=(h[d]+roots[j]*h[d-1])%phi
 eq=[h[3],h[4],h[5]-2];norms=[abs(int(phi.resultant(e))) for e in eq];g=math.gcd(*norms);hist[str(g)]=hist.get(str(g),0)+1
 if not g:char0.append(sub);continue
 ps=[int(p) for p in factorint(g) if p%20==1];candidates.update(ps)
 for p in ps:
  gg=nmod_poly(list(map(int,phi)),p)
  for e in eq:gg=gg.gcd(nmod_poly(list(map(int,e)),p))
  if gg.degree()>0:good.append({'support_exponents':sub,'orbit_size':len(orbit),'prime':p,'norms':norms,'common_factor':list(map(int,gg))})
 records.append({'support':sub,'orbit_size':len(orbit),'norms':norms,'norm_gcd':g})
assert len(seen)==math.comb(20,8)
out={'r':5,'target_agreement':8,'support_count':len(seen),'orbit_representatives':len(records)+len(char0),'group':'j -> a*j+4*b, a in units(Z/20), b in Z/5','char0_supports':char0,'split_prime_candidates':sorted(candidates),'actual_exceptional_primes':sorted({r['prime'] for r in good}),'exceptional_support_embeddings':good,'norm_gcd_histogram':hist,'records':records,'seconds':time.monotonic()-start};(P/'exceptional_r5_supports.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items() if k not in ['records','exceptional_support_embeddings','norm_gcd_histogram']});print('exceptional_orbits',len(good))
