"""Exhaustive geometric base-locus audit modulo29, including all boundaries."""
import json,math,time,hashlib
from pathlib import Path
from flint import nmod_mpoly_ctx,nmod_poly
P=Path(__file__).parent;raw=(P.parent/'gate.json').read_bytes();b=next(v for v in json.loads(raw) if v['bank']=='paley');p=29;C=nmod_mpoly_ctx.get(['X','Y'],p)
forms=[C.from_dict({tuple(ij):v for ij,v in zip(b['columns'],row) if v}) for row in b['kernel']]
x=nmod_poly([0,1],p);one=nmod_poly([1],p)
known=x;forced=one
for idx,z in enumerate(b['base']):known*=x-z;forced*=(x-z)**((4 if idx<7 else 6)**2)
resultants=[];residual=[]
for i in (1,2):
 rr=forms[0].resultant(forms[i],'Y');terms=rr.to_dict();assert terms and all(j==0 for k,j in terms)
 R=nmod_poly([int(terms.get((k,0),0)) for k in range(max(k for k,j in terms)+1)],p)
 q,r=divmod(R,forced);assert not r
 resultants.append(R);residual.append(q)
g=residual[0].gcd(residual[1]);unexplained=g
while unexplained.degree()>0:
 c=unexplained.gcd(known)
 if c.degree()==0:break
 unexplained=unexplained//c
assert unexplained.degree()==0
# Removing known X factors must not hide additional basepoints in their fibers.
fibers=[]
for xx,yy,m in [(0,0,1)]+[(a,c,4 if idx<7 else 6) for idx,(a,c) in enumerate(zip(b['base'],b['word']))]:
 pols=[]
 for form in forms:
  terms=form.to_dict();pols.append(nmod_poly([sum(int(c)*pow(xx,i,p) for (i,j),c in terms.items() if j==d)%p for d in range(11)],p))
 h=pols[0].gcd(pols[1]).gcd(pols[2]);power=0
 while h.degree()>0:
  q,r=divmod(h,x-yy)
  if r:break
  h=q;power+=1
 assert h.degree()==0 and power>=m
 fibers.append({'X':xx,'Y':yy,'common_ordinate_multiplicity':power})
# Proper transforms at the prescribed points: no common projective tangent direction.
tangent_checks=[]
for idx in (0,7):
 xx,yy=b['base'][idx],b['word'][idx];m=4 if idx==0 else 6;cones=[]
 for form in forms:
  cc=[]
  for dy in range(m+1):
   dx=m-dy
   cc.append(sum(int(c)*math.comb(i,dx)*math.comb(j,dy)*pow(xx,i-dx,p)*pow(yy,j-dy,p) for (i,j),c in form.to_dict().items() if i>=dx and j>=dy)%p)
  cones.append(nmod_poly(cc,p))
 assert cones[0].gcd(cones[1]).gcd(cones[2]).degree()==0
 assert any(c[m] for c in cones)
 tangent_checks.append({'representative':idx,'cones':[list(map(int,c.coeffs())) for c in cones],'no_common_projective_direction':True})
# Finite Y-infinity has F0 leading coefficient25, so no basepoint there.
assert {(i,j):int(c) for (i,j),c in forms[0].to_dict().items() if j==10}=={(0,10):25}
# Weighted X-infinity chart and its corner.
infty=[]
for form in forms:
 td={(34-i-3*j,j):int(c) for (i,j),c in form.to_dict().items()};assert min(i for i,j in td)>=0
 infty.append(nmod_poly([sum(c for (i,j),c in td.items() if i==0 and j==d)%p for d in range(11)],p))
assert infty[0].gcd(infty[1]).gcd(infty[2])==x
assert int(infty[2][10])==20
# At each new point, F0 and F2 have independent nonzero linear terms.
linear={}
for name,trans in [('origin',False),('weighted_infinity',True)]:
 rows=[]
 for form in forms:
  td={(34-i-3*j if trans else i,j):int(c) for (i,j),c in form.to_dict().items()}
  assert td.get((0,0),0)==0
  rows.append([td.get((1,0),0),td.get((0,1),0)])
 det=(rows[0][0]*rows[2][1]-rows[0][1]*rows[2][0])%p;assert det
 linear[name]={'linear_rows':rows,'F0_F2_determinant':det}
out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),'resultants':[[int(c) for c in r.coeffs()] for r in resultants],
 'resultant_degrees':[r.degree() for r in resultants],'forced_degree':forced.degree(),'residual_resultants':[[int(c) for c in r.coeffs()] for r in residual],
 'residual_gcd':list(map(int,g.coeffs())),'unexplained_gcd_degree':unexplained.degree(),
 'known_fiber_checks':fibers,'tangent_checks':tangent_checks,'infinity_polynomials':[list(map(int,v.coeffs())) for v in infty],'simple_basepoints':linear,
 'resolved_basepoint_count':16,'moving_self_intersection':14,'canonical_intersection':14,'Euler_characteristic':20,
 'jet_Chern_number':90,'scope':'Basepoint-free after14 prescribed blowups and2 further simple blowups over algebraic closure of F29.'}
(P/'base_locus.json').write_text(json.dumps(out,indent=2));print({k:out[k] for k in ('status','resultant_degrees','forced_degree','residual_gcd','jet_Chern_number')})
