"""Exact cubic factorization and scope data for the user's named fields."""
from flint import nmod_poly
from pathlib import Path
import json
rows=[]
for name,p in [('M31',2**31-1),('BabyBear',2**31-2**27+1),('Goldilocks',2**64-2**32+1)]:
 H=nmod_poly([1,3,2,1],p);unit,factors=H.factor(); roots=[];product=nmod_poly([int(unit)],p)
 for f,e in factors:
  product*=f**e
  if f.degree()==1:
   r=(-int(f[0])*pow(int(f[1]),-1,p))%p
   assert (r**3+2*r*r+3*r+1)%p==0;roots.append(r)
  if f.degree()==2:
   disc=(int(f[1])**2-4*int(f[0])*int(f[2]))%p
   assert pow(disc,(p-1)//2,p)==p-1
 assert product==H
 rows.append(dict(name=name,prime=p,cubic_factors=[dict(polynomial=str(f),multiplicity=e) for f,e in factors],scalar_missing_labels=roots,full_native_domain_size=p**5,domain_size_bits=(p**5).bit_length(),scope='Degree-five extension and full native evaluation domain; not a practical-parameter security bound.'))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
