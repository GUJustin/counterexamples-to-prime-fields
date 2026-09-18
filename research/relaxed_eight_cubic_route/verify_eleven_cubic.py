import json,runpy,time
from pathlib import Path
from fractions import Fraction as F
D=Path(__file__).parent;v=runpy.run_path(str(D/'verify_ten_cubic.py'));seen=v['seen'];X=v['X'];W=v['W'];ev=v['ev'];seed=v['s']
cs=[list(map(F,c['coefficients'])) for c in json.loads((D/'pair_padding_gate.json').read_text())['candidates']]
r=F(-80,163);s=F(-135,262);g=[F(4525,15304),F(4175,3826),F(1)]
def rem(c):
 a=list(c)
 while len(a)>2:
  lead=a.pop()
  a[-1]-=lead*g[1];a[-2]-=lead*g[0]
 return tuple(a+[F(0)]*(2-len(a)))
assert ev(cs[0],r)==ev(cs[2],r) and ev(cs[0],s)==ev(cs[5],s) and rem([a-b for a,b in zip(cs[2],cs[5])])==(0,0)
assert r not in X and s not in X and r!=s and all(ev(g,x)!=0 for x in X+[r,s])
assert g[1]**2-4*g[0]==F(55**2*39,3826**2)
vr=rem(cs[2]);hits={};hist={}
for c,old in seen.items():
 support=old[:]
 if ev(c,r)==ev(cs[0],r):support.append(16)
 if ev(c,s)==ev(cs[0],s):support.append(17)
 if rem(c)==vr:support.append(18)
 hist[len(support)]=hist.get(len(support),0)+1
 if len(support)>=7:hits[c]=support
expected={tuple(map(F,c)) for c in seed['affine_polynomials']}|{tuple(cs[i]) for i in [0,2,5]}
assert set(hits)==expected and max(hist)==7
rho=F(40,247);a=F(7,19);t=rho/2;K=3*a*t+t*t-a**3;gap=4*t**3-K*K
assert gap==F(4666871,1343677407241) and a*a>t and K>0 and gap>0
out=dict(pass_all=True,complete_list_size=11,maximum_agreement=7,old_four_interpolants=len(seen),histogram=hist,quadratic_word=list(map(str,vr)),low_branch_gap=str(gap),selected_supports=[{'coefficients':list(map(str,c)),'support':ss} for c,ss in hits.items()])
(D/'eleven_cubic_certificate.verified.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='selected_supports'})
