from sage.all import *
import argparse,json,time
ap=argparse.ArgumentParser();ap.add_argument('--case',type=int,default=0);ap.add_argument('--h',type=int,default=1);ap.add_argument('--output',required=True);args=ap.parse_args();start=time.monotonic()
K=NumberField(PolynomialRing(QQ,'z').gen()**4+1,'z');z=K.gen();R=PolynomialRing(K,names=('a','b','c'),order='degrevlex');aa=R.gens()
patterns=[[(1,3),(7,2),(7,2)],[(1,3),(7,2),(2,5)],[(7,1),(7,2),(7,2)],[(7,1),(7,2),(2,5)]]
# Monic cubic parity component, whose roots are the three paired squared coordinates.
e=[R.one()]
for a in aa:
 new=[R.zero()]*(len(e)+1)
 for k,v in enumerate(e):new[k]-=a*a*v;new[k+1]+=v
 e=new
shift=-1 if args.h==1 else 1
other=[-sum((e[k]/(1-z**(2*k-2*j+shift)) for k in range(4)),R.zero())/2 for j in range(4)]
E,B=(e,other) if args.h==1 else (other,e)
def ev(co,x):return sum((v*x**j for j,v in enumerate(co)),R.zero())
# Verify first skew roots exactly.
for s in range(4):assert ev(E,z**(2*s))+z**s*ev(B,z**(2*s))==0
guard=R.one()
for a in aa:guard*=a*(a**8-1)
for i in range(3):
 for j in range(i):guard*=aa[i]**8-aa[j]**8
polys=[];raw=[]
for a,pat in zip(aa,patterns[args.case]):
 for k in pat:
  om=z**k
  f=ev(E,om**2*a*a)+om*a*(ev(B,om**2*a*a)-ev(B,a*a)) if args.h==1 else ev(E,om**2*a*a)-om**2*ev(E,a*a)+om*a*ev(B,om**2*a*a)
  raw.append(f)
  while True:
   g=f.gcd(guard)
   if g.total_degree()==0:break
   f=f//g
  if f:f=f/f.lc()
  polys.append(f)
out={'case':args.case,'h':args.h,'patterns':patterns[args.case],'raw_equations':list(map(str,raw)),'equations':list(map(str,polys)),'degrees':[f.total_degree() for f in polys]}
def save():
 out['seconds']=time.monotonic()-start
 with open(args.output,'w') as fp:json.dump(out,fp,indent=2)
 print(json.dumps({k:v for k,v in out.items() if k not in('raw_equations','equations','basis','saturated_basis')}),flush=True)
save()
I=R.ideal(polys);gb=list(I.groebner_basis());out['basis']=list(map(str,gb));save()
target=R.one() if gb==[R.one()] else aa[0]
if I.reduce(target)==0:
 multipliers=target.lift(I)
 assert sum((f*m for f,m in zip(polys,multipliers)),R.zero())==target
 def encodepoly(f):
  return [[list(exp),[str(v) for v in K(co).list()]] for exp,co in f.dict().items()]
 out['certificate']={'equations':[encodepoly(f) for f in polys],'multipliers':[encodepoly(f) for f in multipliers],'target':encodepoly(target)}
 save()
if gb==[R.one()]:out['excluded']=True;save()
else:
 reduced=I.reduce(guard);out['reduced_guard']=str(reduced);save()
 S=PolynomialRing(K,names=('t','a','b','c'),order='degrevlex');t=S.gen(0);phi=R.hom(S.gens()[1:],S)
 J=S.ideal([phi(f) for f in gb]+[t*phi(reduced)-1]);sgb=list(J.groebner_basis());out['saturated_basis']=list(map(str,sgb));out['excluded']=sgb==[S.one()];save()
