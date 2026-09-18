"""Complete algebraic-closure norm gate for non-even degree-six candidates."""
import itertools,json,hashlib,time
from pathlib import Path
P=Path(__file__).parent;raw=(P/'local_search.json').read_bytes();d=json.loads(raw);p=17
X=d['nodes'];W=d['word'];start=time.monotonic()
def trim(a):
 a=list(a)
 while len(a)>1 and a[-1]%p==0:a.pop()
 return [x%p for x in a]
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return trim(c)
def val(a,x):
 r=0
 for y in reversed(a):r=(r*x+y)%p
 return r
def square_over_closure(q):
 q=trim(q)
 if q==[0]:return {'zero':True,'root_monic':[0],'leading':0}
 deg=len(q)-1
 if deg%2:return None
 lead=q[-1];qn=[x*pow(lead,-1,p)%p for x in q];m=deg//2;r=[0]*m+[1]
 for j in range(m-1,-1,-1):
  already=mul(r,r);c=already[m+j] if m+j<len(already) else 0
  r[j]=(qn[m+j]-c)*pow(2,-1,p)%p
 if mul(r,r)!=qn:return None
 return {'zero':False,'root_monic':r,'leading':lead}
rows=[[W[j]*pow(X[j],i,p)%p for i in range(4)]+[pow(X[j],i,p) for i in range(7)]+[-W[j]*W[j]%p] for j in range(16)]
counts={};unique={};positive_dim=[];consistent_subsets=0
for sub in itertools.combinations(range(16),12):
 A=[rows[j][:] for j in sub];r=0;piv=[]
 for c in range(11):
  k=next((k for k in range(r,12) if A[k][c]),None)
  if k is None:continue
  A[r],A[k]=A[k],A[r];inv=pow(A[r][c],-1,p);A[r]=[x*inv%p for x in A[r]]
  for k in range(12):
   if k!=r and A[k][c]:
    z=A[k][c];A[k]=[(a-z*b)%p for a,b in zip(A[k],A[r])]
  piv.append(c);r+=1
 inconsistent=any(all(x==0 for x in row[:11]) and row[11] for row in A)
 key=f'rank{r}_'+('inconsistent' if inconsistent else 'consistent');counts[key]=counts.get(key,0)+1
 if inconsistent:continue
 consistent_subsets+=1
 if r<11:positive_dim.append({'subset':sub,'rank':r});continue
 sol=tuple(A[i][11] for i in range(11));unique.setdefault(sol,sub)
records=[];hits=[]
for sol,sub in unique.items():
 B=list(sol[:4]);C=list(sol[4:]);E=[-z*pow(2,-1,p)%p for z in B];EE=mul(E,E)+[0]*7;J=[(EE[i]-C[i])%p for i in range(7)]
 record={'subset':sub,'B':B,'C':C,'E':E}
 if J[0] or J[6]:record['rejection']='not divisible by X or quotient degree greater than four'
 else:
  q=trim(J[1:6]);sq=square_over_closure(q)
  if sq is None:record['rejection']='O_squared is not a square over algebraic closure'
  else:
   norm_hits=[i for i in range(16) if (W[i]*W[i]+val(B,X[i])*W[i]+val(C,X[i]))%p==0]
   full=[i for i in norm_hits if val(q,X[i])==0 and val(E,X[i])==W[i]]
   count=len(norm_hits)+len(full)
   record.update({'O_squared':q,'square':sq,'norm_hits':norm_hits,'full_fibers':full,'agreement_count':count})
   if not sq['zero'] and count>=14:hits.append(record)
 records.append(record)
out={'status':'NO_NON_EVEN_CANDIDATE' if not positive_dim and not hits else 'UNRESOLVED_OR_HIT','prime':p,'input_sha256':hashlib.sha256(raw).hexdigest(),'all_subsets':1820,'rank_counts':counts,'consistent_subsets':consistent_subsets,'unique_norms':len(unique),'positive_dimensional_subsets':positive_dim,'records':records,'hits':hits,'seconds':time.monotonic()-start,'scope':'All coefficients over algebraic closure; leading scalar square is automatic. Positive-dimensional consistent kernels are retained.'}
(P/'quadratic_pullback_gate.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k not in ['records','hits']}))
