import json
from pathlib import Path
from flint import nmod_poly,nmod_mat
P=Path(__file__).resolve().parent;b=next(z for z in json.loads((P.parent/'gate.json').read_text()) if z['bank']=='orbit2');bank=json.loads((P.parent.parent/'quadratic_one_pole_route/orbit2_bank83.json').read_text());p=83;x=nmod_poly([0,1],p)
F=[{tuple(ij):v for ij,v in zip(b['columns'],row) if v} for row in b['kernel']]
def subst(f,q,derivative=False):
 out=nmod_poly([],p)
 for (i,j),v in f.items():
  if derivative and not j:continue
  out+=v*(j if derivative else 1)*x**i*q**(j-1 if derivative else j)
 return out
receipts=[]
for k,row in enumerate(bank['polynomials']):
 q=nmod_poly(row,p);rr=[subst(f,q) for f in F];M=nmod_mat([[int(f[j]) for f in rr] for j in range(35)],p);R,rank=M.rref();assert rank==1
 pivot=next(j for j in range(3) if int(R[0,j]));null=[]
 for j in range(3):
  if j==pivot:continue
  v=[0]*3;v[j]=1;v[pivot]=-int(R[0,j])%p;null.append(v)
 D=nmod_poly([1],p);agreement=[]
 for i,(a,y) in enumerate(zip(b['base'],b['word'])):
  if int(q(a))==y:D*=(x-a)**((4 if i<7 else 6)-1);agreement.append(i)
 assert len(agreement)==7 and D.degree()==27
 fy=[subst(f,q,True) for f in F];quartics=[]
 for v in null:
  pol=sum((a*f for a,f in zip(v,fy)),nmod_poly([],p));pol,rem=divmod(pol,D);assert not rem;quartics.append(pol)
 assert quartics[0].gcd(quartics[1]).degree()==0 and max(f.degree() for f in quartics)==4
 receipts.append(dict(old_graph=k,parameter_line=[int(R[0,j]) for j in range(3)],line_basis=null,agreement=agreement,forced_degree=27,normal_quartics=[[int(v) for v in f.coeffs()] for f in quartics],Gauss_degree=4))
(P/'old_graph_degrees.json').write_text(json.dumps(dict(status='PASS',prime=p,graphs=receipts),indent=2)+'\n');print('PASS: all seven normal maps are degree four and separable')
