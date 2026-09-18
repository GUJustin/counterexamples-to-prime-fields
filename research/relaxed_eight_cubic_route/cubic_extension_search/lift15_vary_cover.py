import json,runpy
from pathlib import Path
P=Path(__file__).parent
# Import only definitions before the actual source processing.
s=(P/'lift15.py').read_text();ns={};exec(s[s.index('class Ring:'):s.index('r=Ring(17)')],{'Fraction':__import__('fractions').Fraction},ns)
Ring=ns['Ring'];r=Ring(17);d=json.loads((P/'lift15.json').read_text());seed=json.loads((P.parent/'rational_seed.json').read_text());U=list(map(r.rat,seed['affine_nodes']));W=list(map(r.rat,seed['affine_word']))
def solve(mat):
 a=[[tuple(x) for x in row] for row in mat];n=len(a);m=len(a[0])-1;E=[[(int(i==j),0) for j in range(n)] for i in range(n)];piv=[];rank=0
 for c in range(m):
  z=next((i for i in range(rank,n) if a[i][c]!=(0,0)),None)
  if z is None:continue
  a[z],a[rank]=a[rank],a[z];E[z],E[rank]=E[rank],E[z];iv=r.inv(a[rank][c]);a[rank]=[r.mul(x,iv) for x in a[rank]];E[rank]=[r.mul(x,iv) for x in E[rank]]
  for i in range(n):
   if i!=rank:
    t=a[i][c];a[i]=[r.sub(x,r.mul(t,y)) for x,y in zip(a[i],a[rank])];E[i]=[r.sub(x,r.mul(t,y)) for x,y in zip(E[i],E[rank])]
  piv.append(c);rank+=1
 bad=[i for i in range(rank,n) if a[i][-1]!=(0,0)];cert=[]
 for i in bad:
  lam=E[i]
  for c in range(m):
   z=(0,0)
   for j in range(n):z=r.a(z,r.mul(lam[j],tuple(mat[j][c])))
   assert z==(0,0)
  cert.append({'left_null':lam,'rhs_pairing':a[i][-1]})
 return {'rank':rank,'variables':m,'consistent':not bad,'certificates':cert}
out=[]
for case in d['cases']:
 H=[tuple(a%17 for a in c) for c in case['normalized_lift_coefficients']];der=[r.mul((j,0),H[j]) for j in range(1,10)];rows=[]
 for k,i in enumerate(case['support']):
  t=tuple(a%17 for a in d['lifted_nodes'][i]);u=U[i//3];w=W[i//3];pw=[r.pow(t,j) for j in range(10)];dp=r.ev(der,t);invder=r.inv(r.n(pw[2]));fac=r.mul(dp,invder)
  # A'=-T² for A=(11-T³)/3. Node variation is -(dA-u*dB)/A'.
  coverA=[r.n(r.mul(fac,pw[j])) for j in range(4)];coverB=[r.mul(r.sub(r.mul(fac,u),r.mul((3,0),w)),pw[j]) for j in range(1,4)]
  rhs=r.n(tuple(case['residual_div17'][k]));rows.append(pw+coverA+coverB+[rhs])
 cyc=[[row[j] for j in list(range(10))+[10,16]]+[row[-1]] for row in rows]
 out.append({'raw_coefficients':case['raw_coefficients'],'support':case['support'],'cyclic_two_moduli':solve(cyc),'general_four_moduli':solve(rows),'general_matrix':rows})
(P/'lift15_vary_cover.json').write_text(json.dumps({'cases':out},indent=2)+'\n');print([(x['cyclic_two_moduli']['rank'],x['cyclic_two_moduli']['consistent'],x['general_four_moduli']['rank'],x['general_four_moduli']['consistent']) for x in out])
