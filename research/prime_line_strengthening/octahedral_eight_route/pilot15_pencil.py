"""Exact sign-twisted octahedral gate over Q(i,sqrt(2)); no parameter scan."""
from sympy import QQ,I,sqrt
from sympy.polys.rings import ring
from itertools import combinations
from pathlib import Path
import json,time
start=time.monotonic();K=QQ.algebraic_field(I,sqrt(2));R,x=ring('x',K);z=K.zero;o=K.one;ii=K.from_sympy(I);s2=K.from_sympy(sqrt(2));P=Path(__file__).parent

def norm(m):
 a=next(a for a in m if a);return tuple(v/a for v in m)
def mm(a,b):return norm((a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
def act(m,a):
 if a is None:return None if not m[2] else m[0]/m[2]
 den=m[2]*a+m[3];return None if not den else (m[0]*a+m[1])/den
ident=(o,z,z,o);gens=[norm((ii,z,z,o)),norm((o,o,o,-o))];group={ident:1};queue=[ident]
for m in queue:
 for g in gens:
  n=mm(g,m);sg=-group[m]
  if n in group:assert group[n]==sg
  else:group[n]=sg;queue.append(n)
assert len(group)==24
h=norm((ii,o,-ii,o));assert h in group and group[h]==1;H=[ident,h,mm(h,h)];assert mm(H[-1],h)==ident
special=set(act(g,o+s2) for g in group);assert len(special)==12 and None not in special
orbits=[]
while special:
 a=next(iter(special));orb={act(g,a) for g in H};assert len(orb)==3;orbits.append(orb);special-=orb
reps=[];covered=set()
for g in group:
 if g not in covered:reps.append(g);covered|={mm(h,g) for h in H}
assert len(reps)==8 and reps[0]==ident
F8=x**8+14*x**4+1;F12=x**12-33*x**8-33*x**4+1;F6=x*(x**4-1)
def pull(f,m):
 a,b,c,d=m;return sum((R(c0)*(a*x+b)**k[0]*(c*x+d)**(8-k[0]) for k,c0 in f.items()),R.zero)
def det(m):return m[0]*m[3]-m[1]*m[2]
for g in group:assert pull(F8,g)==det(g)**4*F8
fixed=ii*x*x+(ii-o)*x+1;assert F8.rem(fixed)==0
outputs=[]
for j in range(4):
 cand=[]
 for k in range(4):
  if k==j:continue
  f=fixed
  for orb in [orbits[j],orbits[k]]:
   for a in orb:f*=x-a
  cand.append(f.monic())
 f0,f1=cand[:2];assert f0!=f1
 E0=[pull(f0,g)-group[g]*det(g)**4*f0 for g in reps]
 E1=[pull(f1,g)-group[g]*det(g)**4*f1 for g in reps]
 even=[k for k in range(1,8) if group[reps[k]]==1];odd=[k for k in range(8) if group[reps[k]]==-1];hits=[]
 for a in even:
  for b,c in combinations(odd,2):
   g=(E0[a]*E1[b]-E1[a]*E0[b]).gcd(E0[a]*E1[c]-E1[a]*E0[c]).gcd(E0[b]*E1[c]-E1[b]*E0[c])
   guard=F8*F12*F6
   while g.degree()>0:
    z=g.gcd(guard)
    if z.degree()==0:break
    g=g.exquo(z)
   if g.degree()>0:
    u=v=R.zero
    for row in [a,b,c]:
     u=E1[row].rem(g);v=-E0[row].rem(g)
     if u or v:break
    if u:
     ratio=v.LC/u.LC if v else K.zero
     constant=(v==ratio*u)
     candidate=f0+ratio*f1 if constant else None
    else:
     constant=bool(v);candidate=f1 if constant else None
    rankzero=g
    for row in [a,b,c]:rankzero=rankzero.gcd(E0[row]).gcd(E1[row])
    assert rankzero.degree()==0
    if constant:
     for row in [a,b,c]:assert (E0[row]+ratio*E1[row]).rem(g)==0 if u else E1[row].rem(g)==0
    stab=sum(pull(candidate,z)==group[z]*det(z)**4*candidate for z in group) if constant else None
    hits.append(dict(cosets=[a,b,c],gcd=str(g.as_expr()),degree=g.degree(),constant_candidate=constant,stabilizer=stab,candidate=str(candidate.as_expr()) if constant else None,basis=[str(f0.as_expr()),str(f1.as_expr())]))
 outputs.append(dict(special_orbit=j,hits=hits))
out=dict(field='Q(i,sqrt(2))',tests=72,target_agreement=15,seconds=time.monotonic()-start,candidates=outputs);(P/'pilot15_pencil.json').write_text(json.dumps(out,indent=2));print([(a['special_orbit'],[h['degree'] for h in a['hits']]) for a in outputs])
