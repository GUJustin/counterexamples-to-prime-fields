"""Independent arithmetic in F3[t]/Phi7(t^3-t), no tower multiplication tables."""
import json
import sys
CUBIC="--cubic" in sys.argv
from functools import lru_cache
from pathlib import Path
P=Path(__file__).parent;d=json.loads((P/'solve.json').read_text())
def padd(a,b):return tuple(((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%3 for i in range(max(len(a),len(b))))
def pmul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%3
 return tuple(c)
g=(1,);v=(1,);zraw=(0,2,0,1)
for i in range(1,7):v=pmul(v,zraw);g=padd(g,v)
assert len(g)==19 and g[-1]==1
zero=(0,)*18;one=(1,)+(0,)*17

def red(a):
 a=list(a)+[0]*max(0,18-len(a))
 for i in range(len(a)-1,17,-1):
  c=a[i]
  if c:
   for j in range(18):a[i-18+j]=(a[i-18+j]-c*g[j])%3
 return tuple(a[:18])
def add(a,b):return tuple((x+y)%3 for x,y in zip(a,b))
def neg(a):return tuple(-x%3 for x in a)
def sub(a,b):return add(a,neg(b))
@lru_cache(maxsize=100000)
def mul(a,b):return red(pmul(a,b))
def powr(a,n):
 z=one
 while n:
  if n&1:z=mul(z,a)
  a=mul(a,a);n//=2
 return z
@lru_cache(None)
def decode(x):
 ans=zero
 for j in range(3):
  b=x%729;x//=729;v=one
  for k in range(6):
   c=b%3;b//=3
   if c:ans=add(ans,red((0,)*j+tuple(c*t%3 for t in v)))
   v=mul(v,red(zraw))
 return ans
z=decode(3);eta=add(add(z,powr(z,2)),powr(z,4));eb=sub(neg(one),eta);alpha=mul(eb,powr(eta,3**18-2))
assert eta==decode(d['eta']) and alpha==decode(d['alpha']);assert powr(z,7)==one
nodes=list(map(decode,d['nodes']));words=list(map(decode,d['words']));assert len(set(nodes))==42 and zero not in nodes
polys=[]
for i in range(7):
 p=[zero]*11;a=mul(eta,powr(z,2*i));b=powr(z,3*i);c=powr(z,4*i)
 for k,v in {1:mul(eb,powr(z,5*i)),2:neg(c),3:b,4:sub(c,a),5:b,7:b,10:a}.items():p[k]=v
 polys.append(p)
polys.append([zero]*11)
def ev(p,x):
 v=zero
 for c in reversed(p):v=add(mul(v,x),c)
 return v
for j,x in enumerate(nodes):
 orbit=j//21;t=(j%21)//3;base=mul(alpha if orbit else one,powr(z,t));assert sub(powr(x,3),x)==base
 assert words[j]==(zero if orbit else mul(x,powr(z,5*t)))
 assert [i for i,p in enumerate(polys) if ev(p,x)==words[j]]==d['core_masks'][j]
reports=[]
for case in d['cases']:
 mask=case['triple_mask']|128;rows=[];rhs=[]
 for j in range(44):
  x=nodes[j] if j<42 else zero
  ids=d['core_masks'][j] if j<42 else [i for i in range(8) if bool(mask>>i&1)==(j==42)]
  for i in ids:
   row={};v=one
   for k in range(11):
    if v!=zero:row[11*i+k]=v
    v=mul(v,x)
   dv=ev([tuple((k*c)%3 for c in polys[i][k]) for k in range(1,11)],x)
   if dv!=zero:row[88+j]=dv
   row[132+j]=neg(one);rows.append(row)
   rhs.append(mul(eta,mul(x,powr(z,5*((j%21)//3)))) if 21<=j<42 and i==7 else zero)
 assert len(rows)==176
 def combine(values):
  out=[zero]*176
  for a,row in zip(values,rows):
   if a==zero:continue
   for k,v in row.items():out[k]=add(out[k],mul(a,v))
  return out
 left=list(map(decode,case['left_obstruction']));assert all(x==zero for x in combine(left))
 pairing=zero
 for a,b in zip(left,rhs):pairing=add(pairing,mul(a,b))
 assert pairing!=zero
 split=list(map(decode,case['split_row_certificate']));v=combine(split)
 assert all(x==(one if k==130 else neg(one) if k==131 else zero) for k,x in enumerate(v))
 # Check the obstruction functional annihilates every Hasse-quadratic tangent term.
 kernels=[list(map(decode,v)) for v in case['kernel_basis']]
 for v in kernels:
  for row in rows:
   value=zero
   for k,c in row.items():value=add(value,mul(c,v[k]))
   assert value==zero
 # Their distinguished free coordinates give an immediate independence check.
 piv=[];basis=[]
 for raw in kernels:
  v=raw[:]
  for k,b in zip(piv,basis):
   if v[k]!=zero:
    cf=v[k];v=[sub(x,mul(cf,y)) for x,y in zip(v,b)]
  k=next(k for k,x in enumerate(v) if x!=zero)
  iv=powr(v[k],3**18-2);v=[mul(x,iv) for x in v];piv.append(k);basis.append(v)
 assert len(piv)==20
 if not CUBIC:
  quad=[[zero]*20 for _ in range(20)];rowid=0
  for j in range(44):
   x=nodes[j] if j<42 else zero
   ids=d['core_masks'][j] if j<42 else [i for i in range(8) if bool(mask>>i&1)==(j==42)]
   for i in ids:
    lam=left[rowid];rowid+=1
    if lam==zero:continue
    h2=ev([tuple((k*(k-1)//2*c)%3 for c in polys[i][k]) for k in range(2,11)],x)
    xis=[v[88+j] for v in kernels]
    ders=[ev([tuple(k*c%3 for c in v[11*i+k]) for k in range(1,11)],x) for v in kernels]
    for a in range(20):
     for b in range(a,20):
      value=mul(h2,mul(xis[a],xis[b]))
      if a==b:value=add(value,mul(ders[a],xis[a]))
      else:value=add(add(value,value),add(mul(ders[a],xis[b]),mul(ders[b],xis[a])))
      quad[a][b]=add(quad[a][b],mul(lam,value))
  assert all(x==zero for r in quad for x in r)
 if CUBIC:
  comp=[list(map(decode,v)) for v in case['kernel_complement']]
  second=[list(map(decode,v)) for v in case['second_order_correction']]
  from itertools import combinations_with_replacement
  pairs=list(combinations_with_replacement(range(5),2));triples=list(combinations_with_replacement(range(5),3));tid={x:i for i,x in enumerate(triples)}
  cubic_rows=[];qrows=[];rowid=0
  for j in range(44):
   x=nodes[j] if j<42 else zero
   ids=d['core_masks'][j] if j<42 else [i for i in range(8) if bool(mask>>i&1)==(j==42)]
   for i in ids:
    h2=ev([tuple((k*(k-1)//2*c)%3 for c in polys[i][k]) for k in range(2,11)],x)
    h3=ev([tuple((k*(k-1)*(k-2)//6*c)%3 for c in polys[i][k]) for k in range(3,11)],x)
    xi=[v[88+j] for v in comp];et=[v[88+j] for v in second]
    rd=[ev([tuple(k*c%3 for c in v[11*i+k]) for k in range(1,11)],x) for v in comp]
    r2=[ev([tuple((k*(k-1)//2*c)%3 for c in v[11*i+k]) for k in range(2,11)],x) for v in comp]
    sd=[ev([tuple(k*c%3 for c in v[11*i+k]) for k in range(1,11)],x) for v in second]
    row=[zero]*35;quad=[]
    for a in range(5):row[tid[(a,a,a)]]=mul(h3,powr(xi[a],3))
    for zc,(b,c) in enumerate(pairs):
     val=mul(h2,mul(xi[b],xi[c]))
     if b==c:val=add(val,mul(rd[b],xi[b]))
     else:val=add(add(val,val),add(mul(rd[b],xi[c]),mul(rd[c],xi[b])))
     check=val
     for k,coeff in rows[rowid].items():check=add(check,mul(coeff,second[zc][k]))
     assert check==zero
     for a in range(5):
      xisq=mul(xi[b],xi[c]);xisq=xisq if b==c else add(xisq,xisq)
      twice=mul(h2,xi[a]);twice=add(twice,twice)
      value=add(mul(add(twice,rd[a]),et[zc]),add(mul(r2[a],xisq),mul(sd[zc],xi[a])))
      k=tid[tuple(sorted((a,b,c)))];row[k]=add(row[k],value)
    cubic_rows.append(row);rowid+=1
  # Directly check all20 left-kernel projected cubic rows (all35 monomials).
  for li,encoded in enumerate(case['left_kernel_basis']):
   lam=list(map(decode,encoded));project=[zero]*35
   for a,row in zip(lam,cubic_rows):
    if a!=zero:
     for k,value in enumerate(row):project[k]=add(project[k],mul(a,value))
   assert all(value==zero for value in project)
   assert project==list(map(decode,case['cubic_projection'][li][:35]))
 reports.append({'triple_mask':case['triple_mask'],'left_null_verified':True,'quadratic_obstruction_functional_zero_on_20_tangents':not CUBIC,'full_cubic_projection_verified':CUBIC,'nonzero_defect_pairing':list(pairing),'split_functional_in_rowspace':True})
out={'field_modulus':list(g),'original_incidence_verified':True,'certificates':reports,'scope':'No independent rank recomputation; both obstruction identities checked directly in different field presentation.'}
(P/('verify_cubic.json' if CUBIC else 'verify.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
