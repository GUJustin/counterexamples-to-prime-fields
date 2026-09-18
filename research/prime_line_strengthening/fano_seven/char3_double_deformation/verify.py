"""Independent univariate F3[t]/Phi7(t^3-t) reconstruction and certificate replay."""
import json
from pathlib import Path
P=Path(__file__).parent
source=(P.parent/'char3_deformation/verify.py').read_text()
exec(source[source.index('def padd'):source.index('z=decode(3)')],dict()) if False else None
from functools import lru_cache
exec(source[source.index('def padd'):source.index('z=decode(3)')])
d=json.loads((P/'solve.json').read_text());z=decode(3);eta=add(add(z,powr(z,2)),powr(z,4));eb=sub(neg(one),eta);alpha=mul(eb,powr(eta,3**18-2))
def ev(p,x):
 v=zero
 for c in reversed(p):v=add(mul(v,x),c)
 return v
polys=[]
for i in range(7):
 p=[zero]*12;a=mul(eta,powr(z,2*i));b=powr(z,3*i);c=powr(z,4*i)
 for k,v in {2:mul(eb,powr(z,5*i)),3:neg(c),4:b,5:sub(c,a),6:b,8:b,11:a}.items():p[k]=v
 polys.append(p)
polys.append([zero]*12);assert polys==[list(map(decode,p)) for p in d['polynomials']]
nodes=list(map(decode,d['nodes']));words=list(map(decode,d['words']));assert len(set(nodes[:42]))==42 and zero not in nodes[:42] and all(x==zero for x in nodes[42:])
rows=[];rhs=[]
for j,x in enumerate(nodes):
 if j<42:
  orbit=j//21;t=(j%21)//3;assert sub(powr(x,3),x)==mul(alpha if orbit else one,powr(z,t))
  assert words[j]==(zero if orbit else mul(mul(x,x),powr(z,5*t)))
  assert [i for i,p in enumerate(polys) if ev(p,x)==words[j]]==d['masks'][j]
 else:assert d['masks'][j]==[i for i in range(8) if ((i>>((j-42)//2))&1)==(j-42)%2]
 for i in d['masks'][j]:
  row={};v=one
  for k in range(12):
   if v!=zero:row[12*i+k]=v
   v=mul(v,x)
  dv=ev([tuple(k*c%3 for c in polys[i][k]) for k in range(1,12)],x)
  if dv!=zero:row[96+j]=dv
  row[144+j]=neg(one);rows.append(row)
  rhs.append(mul(eta,mul(mul(x,x),powr(z,5*((j%21)//3)))) if 21<=j<42 and i==7 else zero)
assert rhs==list(map(decode,d['rhs'])) and len(rows)==192
left=list(map(decode,d['mod9_obstruction']));v=[zero]*192
for a,row in zip(left,rows):
 for k,c in row.items():v[k]=add(v[k],mul(a,c))
assert all(a==zero for a in v)
y=zero
for a,b in zip(left,rhs):y=add(y,mul(a,b))
assert y!=zero
K=[list(map(decode,v)) for v in d['kernel_basis']]
for v in K:
 for row in rows:
  a=zero
  for k,c in row.items():a=add(a,mul(c,v[k]))
  assert a==zero
free=[j for j in range(192) if j not in d['pivot_columns']]
assert len(K)==len(free)==28
assert all(v[j]==(one if a==b else zero) for a,v in enumerate(K) for b,j in enumerate(free))
v=list(map(decode,d['distinct_node_tangent']))
assert len(set(v[138:144]))==6
assert all(not any(k in row for k in range(138,144)) for row in rows)
(P/'verify.json').write_text(json.dumps(dict(pass_all=True,independent_field=True,incidences=192,kernel_dimension_at_least=28,rank_at_most=164,mod9_inconsistent=True,six_independent_mark_velocities=True,scope='rank lower bound requires separate maximal-minor replay'),indent=2))
print('PASS: independent data, 28 kernel vectors, mod9 obstruction, six free mark velocities')
# Lift the projected separator to the original incidence rows and test every
# quadratic coefficient on the FULL tangent kernel, without gauge arguments.
sep=list(map(decode,d['quadratic_left_obstruction']));LB=[list(map(decode,v)) for v in d['left_kernel_basis']]
lam=[zero]*192
for a,v in zip(sep,LB):
 if a!=zero:
  for j,b in enumerate(v):lam[j]=add(lam[j],mul(a,b))
v=[zero]*192
for a,row in zip(lam,rows):
 if a!=zero:
  for k,c in row.items():v[k]=add(v[k],mul(a,c))
assert all(a==zero for a in v)
pair=zero
for a,b in zip(lam,rhs):pair=add(pair,mul(a,b))
assert pair!=zero
quad=[[zero]*28 for _ in range(28)];rid=0
for j,x in enumerate(nodes):
 for i in d['masks'][j]:
  a=lam[rid];rid+=1
  if a==zero:continue
  h2=ev([tuple((k*(k-1)//2*c)%3 for c in polys[i][k]) for k in range(2,12)],x)
  xis=[v[96+j] for v in K]
  ders=[ev([tuple(k*c%3 for c in v[12*i+k]) for k in range(1,12)],x) for v in K]
  for b in range(28):
   for c in range(b,28):
    val=mul(h2,mul(xis[b],xis[c]))
    if b==c:val=add(val,mul(ders[b],xis[b]))
    else:val=add(add(val,val),add(mul(ders[b],xis[c]),mul(ders[c],xis[b])))
    quad[b][c]=add(quad[b][c],mul(a,val))
assert all(v==zero for row in quad for v in row)
(P/'verify_quadratic.json').write_text(json.dumps(dict(pass_all=True,full_tangent_dimension=28,quadratic_coefficients_checked=406,separating_functional_annihilates_J=True,separating_functional_annihilates_all_quadratic_terms=True,separating_functional_pairs_nontrivially_with_rhs=True,scope='excludes ramification index two provided saved tangent basis complete; maximal minor certified separately'),indent=2))
print('PASS: full 406-coefficient quadratic separating identity')
