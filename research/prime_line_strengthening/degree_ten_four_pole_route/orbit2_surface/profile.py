import json,math,itertools,time,hashlib
from pathlib import Path
from flint import nmod_mpoly_ctx,nmod_poly,nmod_mat
P=Path(__file__).resolve().parent;raw=(P.parent/'gate.json').read_bytes();B=next(b for b in json.loads(raw) if b['bank']=='orbit2');p=83
C=nmod_mpoly_ctx.get(['X','Y'],p);X,Y=C.gens();F=[C.from_dict({tuple(ij):v for ij,v in zip(B['columns'],row) if v}) for row in B['kernel']];x=nmod_poly([0,1],p)
basis_change=[[1,0,1],[0,1,2],[0,0,1]]
F=[F[0]+F[2],F[1]+2*F[2],F[2]]
assert F[0].gcd(F[1]).total_degree()==0 and F[0].gcd(F[2]).total_degree()==0
out=dict(input_sha256=hashlib.sha256(raw).hexdigest(),prime=p,basis_change=basis_change)
def save(): (P/'profile.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
def univar(f):
 d=f.to_dict();assert all(j==0 for i,j in d);return nmod_poly([int(d.get((i,0),0)) for i in range(max(i for i,j in d)+1)],p)
forced=nmod_poly([1],p)
for k,a in enumerate(B['base']):forced*=(x-a)**((4 if k<7 else 6)**2)
res=[]
for j in [1,2]:
 rr=univar(F[0].resultant(F[j],'Y'));q,r=divmod(rr,forced);assert not r;res.append(q)
 out.setdefault('resultants',[]).append(dict(degree=rr.degree(),residual=[int(v) for v in q.coeffs()]));save()
g=res[0].gcd(res[1]);out['residual_gcd']=[int(v) for v in g.coeffs()];out['residual_gcd_factorization']=[([int(v) for v in q.coeffs()],int(e)) for q,e in g.factor()[1]];save()
# Leading boundary and infinity common restrictions.
def polyY(d):return nmod_poly([sum(int(v) for (i,j),v in d.items() if i==0 and j==k)%p for k in range(11)],p)
lead=[nmod_poly([sum(int(v) for (i,j),v in f.to_dict().items() if i==k and j==10)%p for k in range(5)],p) for f in F]
inf=[polyY({(34-i-3*j,j):v for (i,j),v in f.to_dict().items()}) for f in F]
out['leading']=[[int(v) for v in q.coeffs()] for q in lead];out['leading_gcd']=[int(v) for v in lead[0].gcd(lead[1]).gcd(lead[2]).coeffs()]
out['infinity']=[[int(v) for v in q.coeffs()] for q in inf];out['infinity_gcd']=[int(v) for v in inf[0].gcd(inf[1]).gcd(inf[2]).coeffs()]
checks=[]
for k,(a,b) in enumerate(zip(B['base'],B['word'])):
 m=4 if k<7 else 6;cones=[]
 for f in F:
  cones.append([sum(int(v)*math.comb(i,m-jj)*math.comb(j,jj)*pow(a,i-m+jj,p)*pow(b,j-jj,p) for (i,j),v in f.to_dict().items() if i>=m-jj and j>=jj)%p for jj in range(m+1)])
 polys=[nmod_poly(row,p) for row in cones];checks.append(dict(index=k,rank=nmod_mat(cones,p).rank(),cone_gcd=[int(v) for v in polys[0].gcd(polys[1]).gcd(polys[2]).coeffs()],infinity_direction_common=all(row[-1]==0 for row in cones),cones=cones))
out['prescribed_tangents']=checks;save();print('base profile',out['residual_gcd_factorization'],'leading',out['leading_gcd'],'infinity',out['infinity_gcd'],flush=True)
rows=[F,[f.derivative('X') for f in F],[f.derivative('Y') for f in F]]
h=C.constant(0)
for a,b in itertools.combinations(range(3),2):
 for c,d in itertools.combinations(range(3),2):h=h.gcd(rows[a][c]*rows[b][d]-rows[a][d]*rows[b][c])
out['jet_minors_gcd']=[[int(i),int(j),int(v)] for (i,j),v in h.to_dict().items()];save()
J=C.constant(0)
for perm in itertools.permutations(range(3)):
 sign=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3));J+=sign*rows[0][perm[0]]*rows[1][perm[1]]*rows[2][perm[2]]
out['Jacobian']={'degrees':list(map(int,J.degrees())),'weighted_degree':max(i+3*j for i,j in J.to_dict()),'terms':len(J)}
bank=json.loads((P.parent.parent/'quadratic_one_pole_route/orbit2_bank83.json').read_text());G=C.constant(1)
for row in bank['polynomials']:G*=Y-sum(v*X**i for i,v in enumerate(row))
H,r=divmod(J,G);assert not r
out['quotient']={'degrees':list(map(int,H.degrees())),'weighted_degree':max(i+3*j for i,j in H.to_dict()),'terms':len(H)};save();print('Gauss before factor',out['Jacobian'],out['quotient'],flush=True)
unit,factors=H.factor();out['quotient']['unit']=int(unit);out['quotient']['factors']=[dict(degrees=list(map(int,f.degrees())),exponent=int(e),terms=[[int(i),int(j),int(v)] for (i,j),v in f.to_dict().items()]) for f,e in factors];out['status']='PROFILE_COMPLETE';save();print('factorization',[(list(map(int,f.degrees())),int(e)) for f,e in factors],flush=True)
