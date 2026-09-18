"""Independent power-sum and primitive-root replay of the r=5 support gate."""
import json,itertools,math,time
from pathlib import Path
from flint import fmpz_poly
from sympy import factorint,primitive_root
P=Path(__file__).parent;start=time.monotonic();d=json.loads((P/'exceptional_r5_supports.json').read_text());phi=fmpz_poly([1,0,-1,0,1,0,-1,0,1]);powers=[fmpz_poly([0]*j+[1])%phi for j in range(20)];covered=set();candidates=set();actual=[]
for rec in d['records']:
 sub=rec['support'];orb={tuple(sorted((a*j+4*b)%20 for j in sub)) for a in range(20) if math.gcd(a,20)==1 for b in range(5)}
 assert len(orb)==rec['orbit_size'];assert not (orb & covered);covered.update(orb)
 sums=[None]+[sum((powers[(j*k)%20] for j in sub),fmpz_poly([])) for k in range(1,6)];h=[fmpz_poly([1])]
 for k in range(1,6):
  v=sum((sums[j]*h[k-j] for j in range(1,k+1)),fmpz_poly([]))%phi
  assert all(int(c)%k==0 for c in v);h.append(fmpz_poly([int(c)//k for c in v]))
 eq=[h[3],h[4],h[5]-2];norms=[abs(int(e.resultant(phi))) for e in eq];assert norms==rec['norms'];g=math.gcd(*norms);assert g==rec['norm_gcd'] and g>0
 for p in factorint(g):
  p=int(p)
  if p%20!=1:continue
  candidates.add(p);z=pow(int(primitive_root(p)),(p-1)//20,p)
  for a in range(20):
   if math.gcd(a,20)!=1:continue
   x=pow(z,a,p)
   vals=[sum(int(c)*pow(x,j,p) for j,c in enumerate(e))%p for e in eq]
   if not any(vals):actual.append((sub,p,a))
assert len(covered)==math.comb(20,8)==d['support_count'];assert sorted(candidates)==d['split_prime_candidates'];assert not actual
out={'pass':True,'method':'Newton power-sum recurrence with exact integer coefficient division; explicit primitive-root evaluations rather than polynomial gcd','orbit_representatives':len(d['records']),'covered_supports':len(covered),'candidate_primes':sorted(candidates),'actual_exceptional_embeddings':actual,'seconds':time.monotonic()-start};(P/'exceptional_r5_supports.verified.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
