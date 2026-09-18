import itertools,json,time
from pathlib import Path
import sympy as s
K=s.QQ.algebraic_field(s.sqrt(3)/2+s.I/2)
z=K.from_sympy(s.sqrt(3)/2+s.I/2)
xs=[z**j for j in range(12)]
us=[z**(2*j) for j in (0,1,2,4)]
Hs=[[u*x*x+K.one/u for x in xs] for u in us]
w=[]
for j in range(12):
 p=[(a,b) for a,b in itertools.combinations(range(4),2) if Hs[a][j]==Hs[b][j]]
 assert len(p)==1
 w.append(Hs[p[0][0]][j])
def rank(M):
 M=[r[:] for r in M];k=0
 for j in range(len(M[0])):
  pivot=next((i for i in range(k,len(M)) if M[i][j]),None)
  if pivot is None:continue
  M[k],M[pivot]=M[pivot],M[k];q=M[k][j];M[k]=[v/q for v in M[k]]
  for i in range(len(M)):
   if i!=k and M[i][j]:
    q=M[i][j];M[i]=[a-q*b for a,b in zip(M[i],M[k])]
  k+=1
 return k
def kernel(M):
 M=[r[:] for r in M];k=0;pivs=[]
 for j in range(len(M[0])):
  p=next((i for i in range(k,len(M)) if M[i][j]),None)
  if p is None:continue
  M[k],M[p]=M[p],M[k];v=M[k][j];M[k]=[x/v for x in M[k]]
  for i in range(len(M)):
   if i!=k and M[i][j]:
    v=M[i][j];M[i]=[x-v*y for x,y in zip(M[i],M[k])]
  pivs.append(j);k+=1
 free=[j for j in range(len(M[0])) if j not in pivs];out=[]
 for j in free:
  v=[K.zero]*len(M[0]);v[j]=K.one
  for i,p in enumerate(pivs):v[p]=-M[i][j]
  out.append(v)
 return out
start=time.time();hist={};hits=[];rows=[]
for h in range(4):
 yes=[j for j in range(12) if w[j]==Hs[h][j]]
 no=[j for j in range(12) if w[j]!=Hs[h][j]]
 for r,t in itertools.combinations(yes,2):
  zs=[(xs[j]-xs[r])*(xs[j]-xs[t])/(w[j]-Hs[h][j]) for j in no]
  M=[[K.one,q,q*q,-xs[j],-xs[j]*q,-xs[j]*q*q] for q,j in zip(zs,no)]
  ker=kernel(M);hist[len(ker)]=hist.get(len(ker),0)+1
  row={'old_index':h,'root_indices':[r,t],'kernel_dimension':len(ker)}
  if len(ker)==1:
   v=ker[0];disc=v[4]*v[4]-K.convert(4)*v[3]*v[5]
   row['denominator_discriminant_zero']=not bool(disc)
   if not disc:
    row['kernel']=[str(K.to_sympy(x)) for x in v];hits.append(row)
  elif len(ker)>1:
   row['kernel']=[[str(K.to_sympy(x)) for x in v] for v in ker];hits.append(row)
  rows.append(row)
result={'tests':len(rows),'kernel_dimension_histogram':hist,'square_denominator_or_higher_kernel_cases':hits,'rows':rows,'elapsed_seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
