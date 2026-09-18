"""Independent monomial-Vandermonde and five new resultant checks."""
import json,hashlib,time
from pathlib import Path
from flint import nmod_mat,nmod_poly,nmod_mpoly_ctx
P=Path(__file__).parent;raw=(P.parent/'gate.json').read_bytes();bank=next(x for x in json.loads(raw)if x['bank']=='paley');d=json.loads((P/'reconstruction.json').read_text());p=29
assert d['input_sha256']==hashlib.sha256(raw).hexdigest() and d['schema_version']==1 and d['p']==p and d['chart']=='F0+s F1+t F2'
assert d['parameter_degree_bound']==18 and d['residual_X_degree_bound']==48
pts=[(a,b)for a in range(19)for b in range(19-a)];mons=pts[:];seen={(r['s'],r['t']):r for r in d['evaluations']};assert len(seen)==len(d['evaluations'])==190 and set(seen)==set(pts)
V=nmod_mat([[pow(a,i,p)*pow(b,j,p)%p for i,j in mons]for a,b in pts],p)
Y=nmod_mat([seen[a,b]['coefficients']+[0]*(49-len(seen[a,b]['coefficients']))for a,b in pts],p)
coeff=V.inv()*Y;declared=[{tuple(e):z for e,z in c}for c in d['residual_coefficient_terms']];assert len(declared)==49
for k in range(49):
 assert {ij:int(coeff[r,k])for r,ij in enumerate(mons)if coeff[r,k]}==declared[k]
 for(a,b),z in declared[k].items():assert(k-2*a-4*b-2)%7==0 and a+b<=18
C=nmod_mpoly_ctx.get(['X','Y'],p);forms=[C.from_dict({tuple(ij):c for ij,c in zip(bank['columns'],v)if c})for v in bank['kernel']]
T=nmod_poly([1],p)
for i,x in enumerate(bank['base']):T*=nmod_poly([-x,1],p)**(12 if i<7 else 30)
def evaluate(a,b):return nmod_poly([sum(z*pow(a,i,p)*pow(b,j,p)for(i,j),z in c.items())%p for c in declared],p)
new=[(19,1),(20,2),(21,3),(22,4),(28,28)];checks=[]
for a,b in new:
 assert(a,b)not in seen;start=time.monotonic();f=forms[0]+a*forms[1]+b*forms[2];res=f.resultant(f.derivative('Y'),'Y');rc=res.to_dict();assert all(j==0 for i,j in rc)
 rr=nmod_poly([int(rc.get((i,0),0))for i in range(max(i for i,j in rc)+1)],p)
 fd=f.to_dict();lead=nmod_poly([int(fd.get((i,10),0))for i in range(5)],p)
 delta,rem=divmod(-rr,lead);assert not rem
 residual,rem=divmod(delta,T);assert not rem and residual==evaluate(a,b)
 gg=residual.gcd(residual.derivative());rec=dict(s=a,t=b,residual_degree=residual.degree(),derivative_gcd_degree=gg.degree(),seconds=time.monotonic()-start);checks.append(rec);print(rec,flush=True)
out=dict(status='PASS',input_sha256=d['input_sha256'],interpolation_method='independent dense monomial Vandermonde inversion',nodes=190,parameter_terms=sum(len(c)for c in declared),mu7_identity='k-2a-4b=2 mod7',new_checks=checks)
(P/'verify_reconstruction.json').write_text(json.dumps(out,indent=2));print('PASS independent reconstruction and five out-of-grid resultant checks')
