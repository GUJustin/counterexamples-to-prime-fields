import json,math
from pathlib import Path
from fractions import Fraction as F
D=Path(__file__).parent
r=json.loads((D/'rational_seed.json').read_text());s=json.loads((D/'local_search.json').read_text());p=17
red=lambda x:F(x).numerator*pow(F(x).denominator,-1,p)%p
u=list(map(F,r['affine_nodes']));w=list(map(F,r['affine_word']));q=[list(map(F,c)) for c in r['affine_polynomials']]
assert len({red(x) for x in u})==16
rad=[11-3*x for x in u];assert [red(x) for x in rad]==s['nodes'] and all(x for x in rad)
def compose(c,a,b):
 o=[0]*len(c)
 for j,v in enumerate(c):
  for k in range(j+1):o[k]=(o[k]+v*math.comb(j,k)*a**(j-k)*b**k)%p
 return o
old=[[ (a-b)%p for a,b in zip(c,s['polynomials'][3])] for c in s['polynomials']]
trans=[compose(c,11,-3) for c in old]
kappa=next(red(q[i][j])*pow(trans[i][j],-1,p)%p for i in range(8) for j in range(4) if trans[i][j])
assert all(red(q[i][j])==kappa*trans[i][j]%p for i in range(8) for j in range(4))
assert all(red(w[j])==kappa*(s['word'][j]-sum(a*pow(s['nodes'][j],k,p) for k,a in enumerate(s['polynomials'][3])))%p for j in range(16))
# Exact substitution U=(11-T²)/3, ascending degree-six coefficients.
sextics=[]
for c in q:
 out=[F(0)]*7
 for j,a in enumerate(c):
  for k in range(j+1):out[2*k]+=a*math.comb(j,k)*F(11,3)**(j-k)*F(-1,3)**k
 sextics.append(out)
assert all(red(c[2*k])==kappa*old[i][k]%p for i,c in enumerate(sextics) for k in range(4))
assert all(red(c[k])==0 for c in sextics for k in [1,3,5])
out=dict(pass_all=True,field_prime=p,kappa=kappa,modular_relation='q_i(U)=kappa*(P_i(11-3U)-P_3(11-3U))',rational_cover='U=(11-T^2)/3',radicands=[str(x) for x in rad],radicands_mod17=list(map(red,rad)),sextic_coefficients=[[str(a) for a in c] for c in sextics])
(D/'rational_cover.verified.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS kappa=',kappa)
