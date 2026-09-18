import json,math,itertools
from pathlib import Path
from flint import nmod_poly
P=Path(__file__).parent;source=json.loads((P.parent.parent/'gate.json').read_text())[0];p=29
basis=[{tuple(kl):a for kl,a in zip(source['columns'],v) if a} for v in source['kernel']]
charts=[]
for infx,infy in [(False,False),(False,True),(True,False),(True,True)]:
 charts.append([{((34-i-3*j) if infx else i,10-j if infy else j):a for (i,j),a in f.items()} for f in basis])
def coeff(f,x,y,i,j):
 return sum(a*math.comb(k,i)*math.comb(l,j)*pow(x,k-i,p)*pow(y,l-j,p) for(k,l),a in f.items() if k>=i and l>=j)%p
points=[]
for ch in range(4):
 xx=range(p) if ch<2 else [0]; yy=range(p) if ch%2==0 else [0]
 for x in xx:
  for y in yy:
   vals=[[coeff(f,x,y,i,j) for f in charts[ch]] for i,j in [(0,0),(1,0),(0,1)]]
   points.append((ch,x,y,vals))
assert len(points)==900
cache={}
def cone(ch,x,y,m,pars):
 key=(ch,x,y,m)
 if key not in cache:cache[key]=[[coeff(f,x,y,m-j,j) for f in charts[ch]] for j in range(m+1)]
 return [sum(a*b for a,b in zip(v,pars))%p for v in cache[key]]
old=json.loads((P/'count.json').read_text());oldmap={tuple(v['parameters']):v for v in old['results']};summary={}
for pars in [(1,a,b) for a in range(p) for b in range(p)]+[(0,1,a) for a in range(p)]+[(0,0,1)]:
 smooth=known=unknown=0;ords=[]
 for ch,x,y,vs in points:
  h,hx,hy=[sum(a*b for a,b in zip(v,pars))%p for v in vs]
  if h:continue
  if hx or hy:smooth+=1;known+=1;continue
  for m in range(2,12):
   co=cone(ch,x,y,m,pars)
   if any(co):break
  else:unknown+=1;continue
  f=nmod_poly(co,p);deg=f.degree();infty=m-deg
  squarefree=(infty<=1 and f.gcd(f.derivative()).degree()==0)
  if not squarefree:unknown+=1;continue
  branches=int(infty==1)+sum(int(f(t)==0) for t in range(p));known+=branches;ords.append([ch,x,y,m,branches])
 status='excluded_lower_bound' if known>30 else ('unresolved_nonordinary' if unknown else ('point_count_candidate' if known==30 else 'excluded_exact_count'))
 r=oldmap[pars]
 assert (known,smooth,unknown,status)==(r['known_normalization_points'],r['smooth_points'],len(r['unknown_singularities']),r['status']),(pars,known,r)
 assert ords==r['ordinary_singularities']
 summary[status]=summary.get(status,0)+1
# Independently verify that all nonsymmetric remaining points lie in four mu7 orbits.
zeta=16;reps=[(1,1,17),(1,4,1),(1,8,15),(1,8,20)]
orbits=[{(1,a*pow(zeta,2*j,p)%p,b*pow(zeta,4*j,p)%p) for j in range(7)} for _,a,b in reps]
remaining={pars for pars,r in oldmap.items() if r['status'] in ['point_count_candidate','unresolved_nonordinary']}
assert set.union(*orbits)|{(0,1,0)}==remaining
# Resolve simple directions of the exceptional nonordinary cone at (1,1).
co=cone(0,1,1,4,(1,8,15));f=nmod_poly(co,p);expected=11*nmod_poly([-9,1],p)**2*nmod_poly([-9,-6,1],p)
assert f==expected
assert pow(14,(p-1)//2,p)==p-1
out=dict(status='PASS',members=871,surface_points=900,summary=summary,orbits_verified=True,exceptional_cone=co,quadratic_discriminant=14,two_simple_F841_directions=True)
(P/'independent_count.json').write_text(json.dumps(out,indent=2));print(out)
