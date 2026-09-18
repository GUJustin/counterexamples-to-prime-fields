"""Independent equation assembly/order and rational-square replay."""
import json,itertools,time
from pathlib import Path
from flint import fmpq as Q,fmpq_mat as Mat
D=Path(__file__).parent;start=time.monotonic();s=json.loads((D/'rational_seed.json').read_text())
X=list(map(Q,s['affine_nodes']));W=list(map(Q,s['affine_word']))
# Different unknown order: C6,...,C0,B3,...,B0.
def normal(j):
 x,w=X[j],W[j]
 return [x**i for i in range(6,-1,-1)]+[w*x**i for i in range(3,-1,-1)]+[-w*w]
def partials(j):
 x,w=X[j],W[j]
 hy=[Q(0)]*7+[x**i for i in range(3,-1,-1)]+[-2*w]
 hx=[i*x**(i-1) if i else Q(0) for i in range(6,-1,-1)]+[i*w*x**(i-1) if i else Q(0) for i in range(3,-1,-1)]+[Q(0)]
 return [hy,hx]
rows=[normal(j) for j in range(16)];der=[partials(j) for j in range(16)]
def solve(rr):
 a,rank=Mat(rr).rref();out=[Q(0)]*11;piv=[]
 for i in range(rank):
  nz=[j for j in range(12) if a[i,j]!=0];j=nz[0]
  if j==11:return None,0
  out[j]=a[i,11];piv.append(j)
 return out,11-len(piv)
def matches(row,v):return sum((a*b for a,b in zip(row[:11],v)),Q(0))==row[-1]
def canonical(v):return tuple(list(reversed(v[7:]))+list(reversed(v[:7])))
found=set();families=[];counts={};refined=0
for size in (11,12):
 hist={'inconsistent':0,'unique':0,'positive_dimensional':0}
 for sub in itertools.combinations(range(16),size):
  rr=[rows[j] for j in sub];v,dim=solve(rr)
  if v is None:hist['inconsistent']+=1;continue
  if dim:hist['positive_dimensional']+=1
  else:hist['unique']+=1
  if size==12:
   if dim:families.append((sub,dim))
   else:found.add(canonical(v))
  elif not dim:
   if sum(all(matches(row,v) for row in der[j]) for j in sub)>=2:found.add(canonical(v))
  else:
   for a,b in itertools.combinations(sub,2):
    refined+=1;vv,dd=solve(rr+der[a]+der[b])
    if vv is None:continue
    if dd:families.append((sub,(a,b),dd))
    else:found.add(canonical(vv))
 counts[str(size)]=hist
ref=json.loads((D/'exact_general_quadratic_thirteen.json').read_text())
expected={tuple(map(Q,r['B']+r['C'])) for r in ref['records']}
assert found==expected and len(found)==30 and not families
squares=[];zero=0
for v in sorted(found):
 E=[-a/2 for a in v[:4]];J=[-a for a in v[4:]]
 for i,a in enumerate(E):
  for j,b in enumerate(E):J[i+j]+=a*b
 while J and J[-1]==0:J.pop()
 if not J:zero+=1;continue
 deg=len(J)-1;assert deg%2==0
 lead=J[-1];jj=[a/lead for a in J];k=deg//2;root=[Q(0)]*(k+1);root[k]=Q(1)
 for i in range(k-1,-1,-1):
  cross=sum((root[a]*root[b] for a in range(i+1,k+1) for b in range(i+1,k+1) if a+b==k+i),Q(0))
  root[i]=(jj[k+i]-cross)/2
 square=[Q(0)]*(deg+1)
 for i,a in enumerate(root):
  for j,b in enumerate(root):square[i+j]+=a*b
 assert square==jj and (6-deg)%2==0
 squares.append({'J':[str(a) for a in J],'scalar':str(lead),'monic_square_root':[str(a) for a in root],'infinity_order':6-deg})
out=dict(pass_all=True,subset_counts=counts,refined_pair_systems=refined,unique_norms=len(found),unresolved=families,zero_J=zero,nonzero_scalar_squares=len(squares),square_certificates=squares,seconds=time.monotonic()-start)
(D/'exact_general_quadratic_thirteen.verified.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='square_certificates'})
