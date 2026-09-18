"""Exact rational norm census, retaining every subset before deduplication."""
import json,itertools,time
from pathlib import Path
from flint import fmpq,fmpq_mat,fmpq_poly
P=Path(__file__).parent;s=json.loads((P/'rational_seed.json').read_text());X=list(map(fmpq,s['affine_nodes']));W=list(map(fmpq,s['affine_word']));start=time.monotonic()
def solve(rows):
 A,r=fmpq_mat(rows).rref();piv=[]
 for i in range(r):
  c=next(j for j in range(12) if A[i,j])
  if c==11:return None
  piv.append(c)
 free=[j for j in range(11) if j not in piv];v=[fmpq(0)]*11
 for i,c in enumerate(piv):v[c]=A[i,11]
 return v,free
norm=[[w*x**i for i in range(4)]+[x**i for i in range(7)]+[-w*w] for x,w in zip(X,W)]
full=[[[x**i for i in range(4)]+[0]*7+[-2*w],[0]+[i*w*x**(i-1) for i in range(1,4)]+[0]+[i*x**(i-1) for i in range(1,7)]+[0]] for x,w in zip(X,W)]
def valid(row,v):return sum(a*b for a,b in zip(row[:11],v))==row[11]
unique={};unresolved=[];counts={}
for size in [12,11]:
 for sub in itertools.combinations(range(16),size):
  rows=[norm[j] for j in sub];sol=solve(rows)
  if sol is None:continue
  v,free=sol
  if size==12:
   if free:unresolved.append({'subset':sub,'dimension':len(free)})
   else:unique.setdefault(tuple(map(str,v)),{'subset':sub})
  elif not free:
   ff=[j for j in sub if all(valid(row,v) for row in full[j])]
   if len(ff)>=2:unique.setdefault(tuple(map(str,v)),{'subset':sub,'full_pair':ff[:2]})
  else:
   for pair in itertools.combinations(sub,2):
    ss=solve(rows+[row for j in pair for row in full[j]])
    if ss is None:continue
    vv,fr=ss
    if fr:unresolved.append({'subset':sub,'full_pair':pair,'dimension':len(fr)})
    else:unique.setdefault(tuple(map(str,vv)),{'subset':sub,'full_pair':pair})
records=[]
for key,origin in unique.items():
 v=list(map(fmpq,key));E=fmpq_poly([-z/2 for z in v[:4]]);J=E*E-fmpq_poly(v[4:]);fac=J.factor() if J else None
 odddegree=0 if not J else sum(f.degree() for f,e in fac[1] if e%2)+(6-J.degree())%2
 rec=dict(origin,B=list(key[:4]),C=list(key[4:]),J=list(map(str,J)),binary_squarefree_degree=odddegree)
 if fac:rec['factors']=[{'coefficients':list(map(str,f)),'exponent':e} for f,e in fac[1]]
 records.append(rec);counts[str(odddegree)]=counts.get(str(odddegree),0)+1
out={'field':'Q','all_eleven_subsets':4368,'all_twelve_subsets':1820,'unique_norms':len(unique),'unresolved':unresolved,'squarefree_degree_counts':counts,'records':records,'seconds':time.monotonic()-start}
(P/'exact_general_quadratic_thirteen.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items() if k!='records'})
