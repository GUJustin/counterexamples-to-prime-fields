"""Exact F17 cyclic-cubic-cover pilot; no characteristic-zero exclusion claim."""
import itertools,json,time,sys
from pathlib import Path
P=Path(__file__).parent;s=json.loads((P/'local_search.json').read_text());p=17;target=int(sys.argv[1]) if len(sys.argv)>1 else 20;start=time.monotonic()
Y=list(range(1,17));T=[pow(y,11,17) for y in Y];W=s['word']
# Q(T)=E(T^3)+T O(T^3)+T^2 V(T^3); dims4+3+3.
S=[];D=[]
for y,t,w in zip(Y,T,W):
 e=[pow(y,j,p) for j in range(4)];o=[pow(y,j,p) for j in range(3)]
 S.append(e+[t*x%p for x in o]+[t*t*x%p for x in o]+[w])
 D.append([[0]*4+o+[-t*x%p for x in o]+[0],e+[0]*3+[-t*t*x%p for x in o]+[w]])
def solve(rows):
 a=[r[:] for r in rows];piv=[];r=0
 for c in range(10):
  k=next((k for k in range(r,len(a)) if a[k][c]%p),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];u=pow(a[r][c]%p,-1,p);a[r]=[v*u%p for v in a[r]]
  for k in range(len(a)):
   if k!=r and a[k][c]%p:
    u=a[k][c]%p;a[k]=[(x-u*y)%p for x,y in zip(a[k],a[r])]
  piv.append(c);r+=1
  if r==len(a):break
 if any(not any(row[:10]) and row[10]%p for row in a):return None,None
 free=[c for c in range(10) if c not in piv];base=[0]*10
 for i,c in enumerate(piv):base[c]=a[i][10]
 dirs=[]
 for f in free:
  v=[0]*10;v[f]=1
  for i,c in enumerate(piv):v[c]=-a[i][f]%p
  dirs.append(v)
 return base,dirs
hits={};unresolved=[];systems=0;byd={}
for d in range(max(1,(target-16+1)//2),8):
 count=0
 for inds in itertools.combinations(range(16),d):
  rows=[r for j in inds for r in D[j]];b,v=solve(rows)
  if b is None:continue
  dim=len(v);m=target-2*d;miss=16-m
  # A candidate with m single-root matches satisfies >=dim of first miss+dim equations.
  if miss+dim>16:unresolved.append([d,list(inds),dim]);continue
  for ss in itertools.combinations(range(miss+dim),dim):
   systems+=1;bb,vv=solve(rows+[S[j] for j in ss])
   if bb is None:continue
   if vv:
    # Preserve exceptional families for followup; do not silently discard.
    unresolved.append([d,list(inds),list(ss),len(vv)]);continue
   if not any(bb[4:]):continue
   single=sum(sum(x*y for x,y in zip(r[:10],bb))%p==r[10] for r in S)
   double=sum(all(sum(x*y for x,y in zip(r[:10],bb))%p==r[10] for r in rr) for rr in D)
   if single+2*double>=target:hits[tuple(bb)]={'single':single,'double':double,'matches':single+2*double}
  count+=1
 byd[d]=count
out={'field':17,'cover':'Y=T^3','target_matches':target,'degree_bound':9,'systems':systems,'consistent_double_subsets':byd,'hits':[{'coefficients_E_O_V':list(k),**v} for k,v in hits.items()],'unresolved':unresolved,'seconds':time.monotonic()-start,'scope':'F17-rational coefficients; non-even here means not a polynomial in T^3. No exclusion over algebraic closure or characteristic zero.'}
(P/f'cyclic_cubic_nearest_gate_{target}.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ['unresolved','hits']});print('hits',len(hits),'unresolved',len(unresolved))
