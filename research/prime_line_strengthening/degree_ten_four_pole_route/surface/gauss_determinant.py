"""Gauss determinant and divisorial jet-rank audit, modulo29."""
import json,itertools,time,math
from pathlib import Path
from flint import nmod_mpoly_ctx
P=Path(__file__).parent;B=next(v for v in json.loads((P.parent/'gate.json').read_text()) if v['bank']=='paley');C=nmod_mpoly_ctx.get(['X','Y'],29);X,Y=C.gens()
F=[C.from_dict({tuple(ij):v for ij,v in zip(B['columns'],row) if v}) for row in B['kernel']]
rows=[F,[f.derivative('X') for f in F],[f.derivative('Y') for f in F]]
gcd=C.constant(0);minors=[]
for a,b in itertools.combinations(range(3),2):
 for c,d in itertools.combinations(range(3),2):
  h=rows[a][c]*rows[b][d]-rows[a][d]*rows[b][c];gcd=gcd.gcd(h);minors.append(h)
assert gcd.total_degree()==0
J=sum(((-1)**i)*F[i]*(rows[1][(i+1)%3]*rows[2][(i+2)%3]-rows[1][(i+2)%3]*rows[2][(i+1)%3])*((-1)**i) for i in range(3))
# Independent six-permutation determinant formula.
J2=C.constant(0)
for perm in itertools.permutations(range(3)):
 sign=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
 J2+=sign*rows[0][perm[0]]*rows[1][perm[1]]*rows[2][perm[2]]
assert J==J2 and J
orders=[]
for idx in (0,7):
 xx,yy=B['base'][idx],B['word'][idx];expected=3*(4 if idx==0 else 6)-1
 found=None
 for total in range(expected+5):
  cone=[]
  for dx in range(total+1):
   dy=total-dx
   cone.append(sum(int(c)*math.comb(int(i),dx)*math.comb(int(j),dy)*pow(xx,int(i)-dx,29)*pow(yy,int(j)-dy,29) for (i,j),c in J.to_dict().items() if i>=dx and j>=dy)%29)
  if any(cone):found=total;break
 assert found==expected
 orders.append({'representative':idx,'Jacobian_order':found,'expected':expected,'first_cone':cone})
origin_order=min(int(i+j) for i,j in J.to_dict())
infty_order=min(int(97-i-3*j+j) for i,j in J.to_dict())
assert origin_order==infty_order==2
old=json.loads((P.parent/'residual_discriminant'/'old_graph_lines.json').read_text());G=C.constant(1)
for row in old['lines']:G*=Y-sum(c*X**i for i,c in enumerate(row['cubic']))
H,rem=divmod(J,G);assert not rem and H
unit,factors=H.factor();rebuild=C.constant(int(unit))
for f,e in factors:rebuild*=f**e
assert rebuild==H
out={'status':'PASS','all_2x2_minors_gcd':str(gcd),'Jacobian_degrees':list(map(int,J.degrees())),
 'Jacobian_weighted_degree':int(max(i+3*j for i,j in J.to_dict())),'old_graphs_divide':True,
 'quotient_weighted_degree':int(max(i+3*j for i,j in H.to_dict())),'quotient_degrees':list(map(int,H.degrees())),
 'quotient_terms':len(H),'unit':int(unit),'factors':[{'degrees':list(map(int,f.degrees())),'exponent':int(e),'terms':[[int(i),int(j),int(c)] for (i,j),c in f.to_dict().items()]} for f,e in factors]}
out.update(prescribed_exceptional_orders=orders,origin_Jacobian_order=origin_order,
           weighted_infinity_Jacobian_order=infty_order,no_exceptional_ramification_components=True)
(P/'gauss_determinant.json').write_text(json.dumps(out,indent=2));print({k:out[k] for k in ('status','Jacobian_degrees','Jacobian_weighted_degree','quotient_degrees','quotient_weighted_degree','quotient_terms')});print('factors',[(list(map(int,f.degrees())),int(e)) for f,e in factors])
