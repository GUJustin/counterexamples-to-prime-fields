"""Independent FLINT reconstruction of every saved common-z candidate."""
import json
from pathlib import Path
from flint import nmod_poly as Poly
P=Path(__file__).parent
out={}
for p in (29,43):
 d=json.loads((P/f'inversion_p{p}.json').read_text());hist={};examples=[]
 for row in d['positive_gcds']:
  assert len(row['gcd'])==2
  b,c,q=(row[x]for x in ('b','c','q'));z=-row['gcd'][0]*pow(row['gcd'][1],-1,p)%p
  inv=lambda a:pow(a%p,-1,p)
  edge={(0,1):1,(0,2):b,(0,3):c,(1,2):q*inv(c)%p,(1,3):q*inv(b)%p,(2,3):q};x=lambda i,j:edge[tuple(sorted((i,j)))];beta=[0,(q-b*c)%p,(q-c)%p,(q-b)%p];N=(b*c+b*q+c*q+q)%p;M=(b*b*c*c-b*b*c*q+b*b*c-b*b*q-b*c*c*q+b*c*c+b*q*q-b*q-c*c*q+c*q*q-c*q+q*q)%p;t=-N*inv(q*M)%p;a=[1]+[(1+t*beta[i]*(sum(beta)-2*beta[i]))%p for i in range(1,4)];pp=-q*(b*c+b+c+q)*inv(N)%p;k=(q-b*b)*(q-c*c)*(q-1)*inv(q*M)%p
  assert len({sg*aa%p for aa in a for sg in(-1,1)})==8
  C=[];A=[]
  for i in range(4):
   cc=Poly([1],p)
   for j in range(4):
    if i!=j:cc*=Poly([-x(i,j),1],p)
   C.append(cc);A.append(cc*a[i])
  R=Poly([pp,1],p)**2-Poly([0,z],p);B=[Poly([],p)]
  for i in range(1,4):
   num=C[0]-A[i]+R*(k*inv(z)*beta[i]%p)*Poly([-x(0,i),1],p);bi,rr=divmod(num,Poly([pp,1],p));assert not rr;B.append(bi)
  # z^3 F(V/sigma), with B above already divided by sigma.
  F=[]
  for i in range(4):
   ff=[0]*7
   for j in range(4):ff[2*j]=int(A[i][j])*pow(z,3-j,p)%p
   for j in range(3):ff[2*j+1]=int(B[i][j])*pow(z,3-j,p)%p
   F.append(Poly(ff,p))
  L0=Poly([pp*z,-z,1],p);Ls=[L0];K=Poly([1],p)
  for ee in edge.values():K*=Poly([-z*ee,0,1],p)
  for i in range(1,4):
   j,l=[j for j in range(1,4)if j!=i];hh=(x(0,j)*x(0,l)-a[i]*x(i,j)*x(i,l))*inv(1-a[i])%p;ri=-beta[i]*inv(1-a[i])%p;Li=Poly([z*hh*inv(pp),k*ri,1],p);Ls.append(Li)
   assert not (F[0]-F[i])%L0
   cross=F[0]+Poly([int(v)*((-1)**j)for j,v in enumerate(F[j])],p)
   assert not cross%Li
  for L in Ls:K*=L*Poly([int(v)*((-1)**j)for j,v in enumerate(L)],p)
  collision=K.gcd(K.derivative()).degree();assert K.degree()==28 and collision==12;hist[collision]=hist.get(collision,0)+1
  if not examples:examples.append({'shape':row,'z':z,'p_L0':pp,'quadratics':[list(map(int,L))for L in Ls],'locator_factor_degrees':[(g.degree(),e)for g,e in K.factor()[1]]})
 out[p]={'status':'PASS','candidates':len(d['positive_gcds']),'collision_histogram':hist,'example':examples}
(P/'verify_modular_candidates.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
