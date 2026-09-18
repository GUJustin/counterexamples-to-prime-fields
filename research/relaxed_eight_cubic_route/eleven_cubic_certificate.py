"""Complete eleven-cubic list on nineteen coordinates over a quadratic field."""
import json,itertools,time
from pathlib import Path
from flint import fmpq,fmpq_poly
P=Path(__file__).parent;start=time.monotonic();d=json.loads((P/'rational_seed.json').read_text());fresh=json.loads((P/'pair_padding_gate.json').read_text())['candidates'];xs=list(map(fmpq,d['affine_nodes']));ws=list(map(fmpq,d['affine_word']));polys=[fmpq_poly(list(map(fmpq,c))) for c in d['affine_polynomials']];fs=[fmpq_poly(list(map(fmpq,r['coefficients']))) for r in fresh]
r=fmpq('-80/163');s=fmpq('-135/262');g=fmpq_poly([fmpq('4525/15304'),fmpq('4175/3826'),1]);v=fs[2]%g
assert r!=s and r not in xs and s not in xs and g(r) and g(s) and all(g(x) for x in xs)
assert fs[0](r)==fs[2](r) and fs[0](s)==fs[5](s) and (fs[2]-fs[5])%g==0
assert g.derivative().gcd(g).degree()==0
# Discriminant has nonsquare numerator 117975=25*4719=25*3*11^2*13.
assert g[1]**2-4*g[0]==fmpq('117975/14638276')
def interp(I):
 ans=fmpq_poly([])
 for i in I:
  term=fmpq_poly([1]);den=fmpq(1)
  for j in I:
   if j!=i:term*=fmpq_poly([-xs[j],1]);den*=xs[i]-xs[j]
  ans+=term*(ws[i]/den)
 return ans
unique={}
for I in itertools.combinations(range(16),4):
 q=interp(I);unique[tuple(map(str,q))]=q
records=[];maxmatch=0;hist={}
for key,q in unique.items():
 sup=[i for i,x in enumerate(xs) if q(x)==ws[i]]
 if q(r)==fs[0](r):sup.append(16)
 if q(s)==fs[0](s):sup.append(17)
 if q%g==v:sup.append(18)
 hist[len(sup)]=hist.get(len(sup),0)+1;maxmatch=max(maxmatch,len(sup))
 if len(sup)>=7:records.append({'coefficients':key,'support':sup})
expected={tuple(map(str,q)) for q in polys+[fs[i] for i in [0,2,5]]}
assert {tuple(r['coefficients']) for r in records}==expected and len(records)==11 and maxmatch==7
# Exact low/high branch threshold tests.
def test(m):
 rho=fmpq(3*m+1,19*m);a=fmpq(7,19)
 if (11-rho)**2<117:return ((8-rho)*a*a-6*rho*a+rho*(4*rho-5))>0,'high',None
 t2=rho/2;K=3*a*t2+t2*t2-a**3;gap=4*t2**3-K*K
 return a*a>t2 and (K<=0 or gap>0),'low',str(gap)
threshold=next(m for m in range(1,10000) if test(m)[0]);assert all(not test(m)[0] for m in range(1,threshold))
out={'field':'Q(sqrt(39))','new_rational_nodes':[str(r),str(s)],'new_quadratic_minpoly':list(map(str,g)),'new_quadratic_word':list(map(str,v)),'four_subsets':1820,'distinct_interpolants':len(unique),'max_agreement':maxmatch,'nearest_list':records,'histogram':hist,'minimum_pullback_degree':threshold,'pullback_n':19*threshold,'pullback_k':3*threshold+1,'pullback_A':7*threshold,'threshold_test':test(threshold),'seconds':time.monotonic()-start}
(P/'eleven_cubic_certificate.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items() if k not in ['nearest_list','histogram']})
