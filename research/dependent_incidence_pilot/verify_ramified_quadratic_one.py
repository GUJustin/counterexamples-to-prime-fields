"""Independent stdlib replay of one degree-two ramified obstruction."""
from pathlib import Path
import json
BASE=Path(__file__).resolve().parent;p=41

def rank(rows):
 a=[[x%p for x in row] for row in rows];r=0
 for c in range(len(a[0])):
  j=next((j for j in range(r,len(a)) if a[j][c]),None)
  if j is None:continue
  a[r],a[j]=a[j],a[r];inv=pow(a[r][c],-1,p);a[r]=[x*inv%p for x in a[r]]
  for j in range(r+1,len(a)):
   v=a[j][c]
   if v:a[j]=[(x-v*y)%p for x,y in zip(a[j],a[r])]
  r+=1
  if r==len(a):break
 return r

def main():
 data=json.loads((BASE/'results.json').read_text());cert=json.loads((BASE/'ramified_quadratic_one.json').read_text());pat=data['rows'][cert['pattern_index']]
 assert cert['pattern_index']==min(range(24),key=lambda i:(data['rows'][i]['rank'],i))
 xs=data['nodes'];cs=[data['polynomials'][i] for i in pat['ids']];J=[];b=[]
 for node,a,c in pat['equations']:
  x=xs[node];row=[0]*200
  for j in range(10):
   row[40+10*a+j]=pow(x,j,p);row[40+10*c+j]=-pow(x,j,p)%p
   if j:row[node]=(row[node]+j*(cs[a][j]-cs[c][j])*pow(x,j-1,p))%p
  residual=sum((cs[a][j]-cs[c][j])*pow(x,j,p*p) for j in range(10))%(p*p)
  assert residual%p==0;J.append(row);b.append(-residual//p%p)
 gauge=cert['gauge_columns'];assert gauge[:3]==[xs.index(i) for i in [1,2,3]];assert gauge[3:13]==list(range(40,50));assert 50<=gauge[-1]<60;assert(cs[1][gauge[-1]-50]-cs[0][gauge[-1]-50])%p
 for c in gauge:
  row=[0]*200;row[c]=1;J.append(row);b.append(0)
 Z=cert['kernel'];h=len(Z[0]);assert h==5
 assert rank(J)==195 and rank(Z)==5
 for row in J:
  for t in range(h):assert sum(a*z[t] for a,z in zip(row,Z))%p==0
 def quad(v):
  out=[]
  for node,a,c in pat['equations']:
   x=xs[node];vx=v[node];power=[1,0,0];value=[0,0,0]
   for j in range(10):
    cj=cs[a][j]-cs[c][j];vc=v[40+10*a+j]-v[40+10*c+j]
    for t in range(3):value[t]+=cj*power[t]+(vc*power[t-1] if t else 0)
    power=[power[0]*x,(power[1]*x+power[0]*vx),(power[2]*x+power[1]*vx)]
   out.append(value[2]%p)
  return out+[0]*14
 vectors=[[row[t] for row in Z] for t in range(h)];diag=[quad(v) for v in vectors];Q=[]
 for i,j in cert['quadratic_monomials']:
  Q.append(diag[i] if i==j else [(a-b-c)%p for a,b,c in zip(quad([a+b for a,b in zip(vectors[i],vectors[j])]),diag[i],diag[j])])
 assert rank([row+[col[i] for col in Q] for i,row in enumerate(J)])==195
 witness=cert['constant_obstruction'][0];lam=witness['lambda_vector']
 assert len(lam)==len(J)
 for j in range(200):assert sum(lam[i]*J[i][j] for i in range(len(J)))%p==0
 for q in Q:assert sum(a*b for a,b in zip(lam,q))%p==0
 residual=sum(a*c for a,c in zip(lam,b))%p
 assert residual==witness['residual'] and residual
 out=dict(status='PASS',pattern_index=cert['pattern_index'],normalized_rank=195,tangent_dimension=5,quadratic_cokernel_rank=0,residual=residual,scope='No ramification-index-two lift with these reductions; higher ramification not excluded')
 (BASE/'ramified_quadratic_one_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':main()
