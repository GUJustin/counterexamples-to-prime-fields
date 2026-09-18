"""Independent stdlib verification through unisolvent degree-three evaluations."""
from pathlib import Path
from itertools import product
import json
from verify_ramified_quadratic_one import rank
BASE=Path(__file__).resolve().parent;p=41

def dot(a,b):return sum(x*y for x,y in zip(a,b))%p
def valmon(mon,t):
 v=1
 for e,x in zip(mon,t):v=v*pow(x,e,p)%p
 return v

def mul(a,b):return [sum(a[j]*b[i-j] for j in range(i+1))%p for i in range(4)]
def main():
 data=json.loads((BASE/'results.json').read_text());quad=json.loads((BASE/'ramified_quadratic_one.json').read_text());cert=json.loads((BASE/'ramified_cubic_one.json').read_text());assert cert['pattern_index']==quad['pattern_index']==11
 pat=data['rows'][11];xs=data['nodes'];cs=[data['polynomials'][i] for i in pat['ids']];eq=pat['equations'];Z=quad['kernel'];W=cert['quadratic_correction'];T=cert['cubic_coefficients'];J=[];rhs=[]
 for node,a,b in eq:
  x=xs[node];row=[0]*200
  for j in range(10):
   row[40+10*a+j]=pow(x,j,p);row[40+10*b+j]=-pow(x,j,p)%p
   if j:row[node]=(row[node]+j*(cs[a][j]-cs[b][j])*pow(x,j-1,p))%p
  residual=sum((cs[a][j]-cs[b][j])*pow(x,j,p*p) for j in range(10))%(p*p)
  assert residual%p==0;rhs.append(-residual//p%p);J.append(row)
 for c in quad['gauge_columns']:
  row=[0]*200;row[c]=1;J.append(row);rhs.append(0)
 assert rank(J)==195 and rank([a+b for a,b in zip(J,T)])==195
 assert rank(Z)==5
 for row in J:
  for t in range(5):assert dot(row,[z[t] for z in Z])==0
 # Lower-set grid is unisolvent in total degree<=3: multivariate falling
 # factorial basis has triangular evaluation matrix and diagonal units j!.
 grid=[t for t in product(range(4),repeat=5) if sum(t)<=3];assert len(grid)==56
 for t in grid:
  v=[dot(z,t) for z in Z];qvals=[valmon(m,t) for m in cert['quadratic_monomials']];w=[dot(row,qvals) for row in W];cvals=[valmon(m,t) for m in cert['cubic_monomials']]
  for rowidx,(node,a,b) in enumerate(eq):
   nodepoly=[xs[node],v[node],w[node],0];power=[1,0,0,0];out=[0]*4
   for j in range(10):
    aa=40+10*a+j;bb=40+10*b+j
    cp=[(cs[a][j]-cs[b][j])%p,(v[aa]-v[bb])%p,(w[aa]-w[bb])%p,0]
    term=mul(cp,power);out=[(x+y)%p for x,y in zip(out,term)];power=mul(power,nodepoly)
   assert out[:3]==[0,0,0]
   assert out[3]==dot(T[rowidx],cvals)
  for q,c in enumerate(quad['gauge_columns']):
   assert v[c]==w[c]==0;assert dot(T[len(eq)+q],cvals)==0
 witness=cert['constant_obstruction'][0];lam=witness['lambda_vector']
 for col in range(200):assert dot(lam,[row[col] for row in J])==0
 for col in range(35):assert dot(lam,[row[col] for row in T])==0
 residue=dot(lam,rhs);assert residue==witness['residual']==18
 out=dict(status='PASS',pattern_index=11,normalized_rank=195,tangent_dimension=5,cubic_cokernel_rank=0,unisolvent_checks=56,cubic_monomials=35,residual=residue,scope='No ramification-index-three lift; higher ramification not excluded')
 (BASE/'ramified_cubic_one_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':main()
