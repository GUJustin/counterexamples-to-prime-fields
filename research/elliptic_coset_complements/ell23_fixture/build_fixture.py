"""Exact six-twist census and normalized Velu fixture; standard library only."""
from pathlib import Path
import json, math, time, hashlib
start=time.monotonic(); root=Path(__file__).parent
p=1657; ell=23
trial=list(range(2,math.isqrt(p)+1))
assert all(p%d for d in trial)
factors=[2,3,23]; assert 2**3*3**2*23==p-1
g=next(g for g in range(2,p) if all(pow(g,(p-1)//q,p)!=1 for q in factors))
squares={}
for y in range(p): squares.setdefault(y*y%p,[]).append(y)
def add(U,V):
 if U is None:return V
 if V is None:return U
 x,y=U;z,w=V
 if x==z and (y+w)%p==0:return None
 slope=((w-y)*pow(z-x,-1,p) if x!=z else 3*x*x*pow(2*y,-1,p))%p
 xx=(slope*slope-x-z)%p
 return xx,(slope*(x-xx)-y)%p
def mul(U,n):
 V=None
 while n:
  if n&1: V=add(V,U)
  U=add(U,U);n>>=1
 return V
def pmul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return c
def peval(a,x):
 y=0
 for v in reversed(a):y=(y*x+v)%p
 return y
def loc(roots):
 a=[1]
 for x in roots:a=pmul(a,[-x%p,1])
 return a
census=[];chosen=None
for j in range(6):
 b=pow(g,j,p)
 points=[None]+[(x,y) for x in range(p) for y in squares.get((x**3+b)%p,[])]
 torsion=[P for P in points if mul(P,ell) is None]
 census.append({'twist_exponent':j,'b':b,'curve_point_count':len(points),'ell_torsion_count':len(torsion)})
 if len(torsion)==ell*ell and chosen is None:chosen=(b,points,torsion)
assert chosen is not None, census
b,points,torsion=chosen
assert all(P is None or (P[1]**2-P[0]**3-b)%p==0 for P in torsion)
U=next(P for P in torsion if P is not None)
span={mul(U,a) for a in range(ell)}
V=next(P for P in torsion if P not in span)
labelpoints={(a,c):add(mul(U,a),mul(V,c)) for a in range(ell) for c in range(ell)}
assert len(set(labelpoints.values()))==ell*ell
assert set(labelpoints.values())==set(torsion)
domain=sorted({P[0] for P in torsion if P is not None});assert len(domain)==264
subgroups=[];checked=0
for direction in [(1,a) for a in range(ell)]+[(0,1)]:
 generator=labelpoints[direction]
 H=[mul(generator,j) for j in range(ell)]
 assert len(set(H))==ell
 roots=sorted({P[0] for P in H if P is not None});assert len(roots)==11
 K=loc(roots);B=pmul(K,K);N=[0]+B
 for x in roots:
  quotient=loc([z for z in roots if z!=x]);q2=pmul(quotient,quotient)
  term=pmul(q2,[(4*(x**3+b)-6*x**3)%p,6*x*x%p])
  for j,v in enumerate(term):N[j]=(N[j]+v)%p
 assert len(N)==24 and N[-1]==1 and all(peval(N,x) for x in roots)
 tags={}
 for x in domain:
  if x in roots:continue
  y=next(y for y in squares[(x**3+b)%p])
  P=(x,y)
  direct=(x+sum(add(P,T)[0]-T[0] for T in H if T is not None))%p
  tag=peval(N,x)*pow(peval(B,x),-1,p)%p
  assert tag==direct
  tags.setdefault(tag,[]).append(x);checked+=1
 assert len(tags)==11 and all(len(xs)==23 for xs in tags.values())
 Phi=loc(domain); product=K
 for tag,xs in sorted(tags.items()):
  F=N.copy()
  for j,v in enumerate(B):F[j]=(F[j]-tag*v)%p
  assert F==loc(xs)
  product=pmul(product,F)
 assert product==Phi
 subgroups.append({'direction':direction,'generator':generator,'points':H,'kernel_x':roots,'K':K,'B':B,'N':N,'fibers':[{'tag':a,'x':xs} for a,xs in sorted(tags.items())]})
assert len({tuple(H['kernel_x']) for H in subgroups})==24
assert sum(len(H['kernel_x']) for H in subgroups)==len(domain)
assert set().union(*(set(H['kernel_x']) for H in subgroups))==set(domain)
fixture={'p':p,'ell':ell,'curve':{'a':0,'b':b},'primitive_element':g,'curve_point_count':len(points),'torsion_points':torsion,'torsion_basis':[U,V],'torsion_coordinates':[{'a':a,'c':c,'point':P} for (a,c),P in labelpoints.items()],'domain':domain,'n':264,'k':173,'threshold':213,'polynomial_coefficient_order':'ascending','infinity_encoding':None,'subgroups':subgroups}
f=root/'fixture.json';f.write_text(json.dumps(fixture,indent=2)+'\n')
receipt={'status':'PASS','prime_check':'trial division by every integer 2..40','p_minus_one_factorization':{'2':3,'3':2,'23':1},'primitive_element':g,'six_twists':census,'chosen_b':b,'torsion_count':len(torsion),'subgroup_count':len(subgroups),'direct_velu_evaluations':checked,'all_24_domain_factorizations_checked':True,'all_torsion_points_scalar_multiplied_by_23':True,'torsion_basis_grid_bijective':True,'johnson_squared_difference':213**2-264*(173-1),'fixture_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
(root/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
