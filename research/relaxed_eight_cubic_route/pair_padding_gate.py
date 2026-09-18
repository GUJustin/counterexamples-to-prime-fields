import json,itertools
from fractions import Fraction as F
from pathlib import Path
import sympy as S
P=Path(__file__).parent;d=json.loads((P/'rational_seed.json').read_text());xs=list(map(F,d['affine_nodes']));ys=list(map(F,d['affine_word']));X=S.Symbol('X')
def ev(c,x):return sum(a*x**j for j,a in enumerate(c))
def interp(I):
 ans=S.interpolate([(S.Rational(xs[i].numerator,xs[i].denominator),S.Rational(ys[i].numerator,ys[i].denominator)) for i in I],X);return tuple(F(ans.expand().coeff(X,j)) for j in range(4))
# Persistent supports supply exact candidates, then independently recount all matches.
a=json.loads((P/'canonical_lift_interpolants.json').read_text());cs=[]
for r in a['persistent_fresh']:
 c=interp(r['support'][:4]);sup=[i for i,x in enumerate(xs) if ev(c,x)==ys[i]];assert len(sup)==5;cs.append((c,sup))
rows=[];hits=[]
for i,j in itertools.combinations(range(8),2):
 f=S.Poly(sum(S.Rational((cs[i][0][k]-cs[j][0][k]).numerator,(cs[i][0][k]-cs[j][0][k]).denominator)*X**k for k in range(4)),X);outside=f
 old=[]
 for k,x in enumerate(xs):
  if ev(tuple(F(t) for t in reversed(f.all_coeffs())),x)==0:
   old.append(k);outside=outside.exquo(S.Poly(X-S.Rational(x.numerator,x.denominator),X))
 sf=outside.sqf_part();simple=outside.exquo(S.gcd(outside,outside.diff()))
 # A root is simple in original iff not a root of gcd(f,f').
 simple=f.exquo(S.gcd(f,f.diff())); simple=simple.exquo(S.gcd(simple,S.gcd(f,f.diff())))
 for x in xs:
  lin=S.Poly(X-S.Rational(x.numerator,x.denominator),X)
  if simple.rem(lin).is_zero:simple=simple.exquo(lin)
 row={'pair':[i,j],'difference':str(S.factor(f.as_expr())),'old_root_indices':old,'simple_outside_degree':simple.degree(),'simple_outside_factor':str(S.factor(simple.as_expr()))};rows.append(row)
 if simple.degree()>=2:hits.append(row)
out={'candidates':[{'coefficients':list(map(str,c)),'support':sup} for c,sup in cs],'pairs':rows,'hits':hits};(P/'pair_padding_gate.json').write_text(json.dumps(out,indent=2)+'\n');print('hits',len(hits));print(*hits,sep='\n')
