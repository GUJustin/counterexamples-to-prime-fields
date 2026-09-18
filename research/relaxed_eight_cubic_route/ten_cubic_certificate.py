import json
from fractions import Fraction as F
from pathlib import Path
import sympy as S
P=Path(__file__).parent;d=json.loads((P/'rational_seed.json').read_text());p=json.loads((P/'pair_padding_gate.json').read_text());X=S.Symbol('X');g=S.Poly(358*X**2+125*X-25,X);cs=d['affine_polynomials']+[a['coefficients'] for a in p['candidates']]
def poly(c):return S.Poly(sum(S.Rational(a)*X**i for i,a in enumerate(c)),X)
Q=poly(p['candidates'][0]['coefficients']);rows=[]
for i,c in enumerate(cs):
 f=poly(c);old=sum(f.eval(S.Rational(x))==S.Rational(y) for x,y in zip(d['affine_nodes'],d['affine_word']));rem=(f-Q).rem(g);new=2 if rem.is_zero else 0
 rows.append({'index':i,'old_matches':old,'new_matches':new,'total':old+new,'remainder':list(map(str,rem.all_coeffs()))})
assert all(r['new_matches']==0 for r in rows[:8]);assert [r['index'] for r in rows if r['new_matches']]==[8,11];assert max(r['total'] for r in rows)==7
assert S.discriminant(g.as_expr(),X)==55**2*17;assert all(g.eval(S.Rational(x)) for x in d['affine_nodes'])
out={'field':'Q(sqrt(17))','new_node_polynomial':[358,125,-25],'discriminant':51425,'new_nodes':'(-125 +/- 55 sqrt(17))/716','new_word_remainder':list(map(str,Q.rem(g).all_coeffs())),'new_candidate_coefficients':[p['candidates'][i]['coefficients'] for i in [0,3]],'all_old_ge5_candidates':rows,'maximum_agreement':7,'complete_nearest_list':10,'reason':'Any >=7 match cubic on18 nodes matches>=5 rational old nodes, so is one of the exactly enumerated16 old >=5 interpolants. Irreducible quadratic means each rational candidate matches both fresh nodes or neither.'}
(P/'ten_cubic_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
