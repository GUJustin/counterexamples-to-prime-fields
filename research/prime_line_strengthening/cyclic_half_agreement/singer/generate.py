"""Exact Singer trace-zero supports in F_(2^m), with verified primitive basis."""
import json,itertools,math
from pathlib import Path
r=Path(__file__).parent;out=[]
for m,poly in [(3,0b1011),(4,0b10011),(5,0b100101),(6,0b1000011),(7,0b10000011)]:
 q=(1<<m)-1
 def mul(a,b):
  c=0
  while b:
   if b&1:c^=a
   b>>=1;a<<=1
   if a&(1<<m):a^=poly
  return c
 def power(a,e):
  b=1
  while e:
   if e&1:b=mul(b,a)
   a=mul(a,a);e>>=1
  return b
 powers=[power(2,i) for i in range(q)]
 assert len(set(powers))==q and set(powers)==set(range(1,q+1)) and power(2,q)==1
 # Every nonzero residue is a power of X and thus invertible: the quotient
 # is a field, and X is primitive. This verifies the supplied polynomial.
 def trace(a):
  s=0
  for _ in range(m):s^=a;a=mul(a,a)
  assert s in [0,1]
  return s
 D=[i for i,a in enumerate(powers) if trace(a)==0];assert len(D)==(q-1)//2
 # Singer difference-set identity; multiplicities uniform off zero.
 differences=[sum((a-b)%q==d for a in D for b in D) for d in range(1,q)]
 assert len(set(differences))==1 and differences[0]==(q-3)//4
 S=sorted(set(range(q))-{(-i)%q for i in D});assert len(S)==(q+1)//2
 def canon(S):
  candidates=[tuple(sorted((i+t)%q for i in S)) for t in range(q)]
  return min(candidates,key=lambda T:sum(1<<i for i in T))
 classes={}
 units=[k for k in range(1,q) if math.gcd(k,q)==1]
 for k in units:
  Dk=sorted(k*i%q for i in D);Sk=sorted(set(range(q))-{(-i)%q for i in Dk});key=canon(Sk)
  if key not in classes:classes[key]={'representative_multiplier':k,'multipliers':[],'trace_zero_D':Dk,'support_S':Sk,'rotation_canonical_support':list(key),'rotation_canonical_mask_decimal':str(sum(1<<i for i in key))}
  classes[key]['multipliers'].append(k)
 assert len(classes)==len(units)//m and all(len(v['multipliers'])==m for v in classes.values())
 row={'q':q,'m':m,'unit_multipliers':units,'natural_h':(3*q-1)//4,'natural_h_coprime':math.gcd((3*q-1)//4,q)==1,'binary_polynomial_integer':poly,'binary_polynomial_exponents':[i for i in range(m+1) if poly>>i&1],'primitive_element':2,'primitive_powers':powers,'trace_zero_D':D,'support_S':S,'support_csv':','.join(map(str,S)),'difference_multiplicity':differences[0],'multiplier_classes':list(classes.values())}
 out.append(row);(r/f'q{q}.json').write_text(json.dumps(row,indent=2)+'\n')
 for j,cl in enumerate(classes.values()):(r/f'q{q}_class{j}.support').write_text(','.join(map(str,cl['rotation_canonical_support']))+'\n')
assert out[0]['trace_zero_D']==[1,2,4] and out[0]['support_S']==[0,1,2,4]
(r/'manifest.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{'q':a['q'],'primitive_polynomial':a['binary_polynomial_exponents'],'D_size':len(a['trace_zero_D']),'S_size':len(a['support_S']),'multiplier_classes':len(a['multiplier_classes']),'difference_multiplicity':a['difference_multiplicity']} for a in out],indent=2))
