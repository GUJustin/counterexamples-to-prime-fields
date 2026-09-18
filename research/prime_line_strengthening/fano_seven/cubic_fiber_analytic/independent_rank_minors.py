"""Independent full2187 verification via modular determinants, no cyclotomic CAS.
A nonzero reduced integral minor proves the characteristic-zero minor nonzero.
Constant/single-anomaly patterns have explicit improper solutions in the note.
"""
import itertools,json,time
from pathlib import Path
primes=[43,127,211,337]
fields=[]
for p in primes:
 assert all(p%d for d in range(2,int(p**0.5)+1))
 z=next(x for x in range(2,p) if pow(x,21,p)==1 and pow(x,7,p)!=1 and pow(x,3,p)!=1)
 fields.append((p,z))
perms={}
for n in [3,4]:
 perms[n]=[(t,(-1)**sum(t[i]>t[j] for i in range(n) for j in range(i+1,n))) for t in itertools.permutations(range(n))]
def det(a,p):
 ans=0
 for t,sign in perms[len(a)]:
  v=sign
  for i,j in enumerate(t):v=v*a[i][j]%p
  ans=(ans+v)%p
 return ans
out=[];start=time.time()
for phases in itertools.product(range(3),repeat=7):
 count=[phases.count(i) for i in range(3)];m=max(count)
 if m==7:
  out.append({'phases':phases,'kind':'constant','symbolic_rank':2});continue
 n=3 if m==6 else 4;found=None
 for p,z in fields:
  zz=[pow(z,j,p) for j in range(21)]
  F=[sum(zz[(3*k*j+7*phases[j])%21] for j in range(7))%p for k in range(7)]
  G=[sum(zz[(3*k*j+14*phases[j])%21] for j in range(7))%p for k in range(7)]
  mat=[[F[(d+5-l)%7] for d in range(3)]+[(-7 if l==5 else 0)%p] for l in [4,5,6]]
  mat += [[G[(d+10-l)%7] for d in range(3)]+[0] for l in [4,6]]
  for rr in itertools.combinations(range(5),n):
   value=det([mat[j][:n] for j in rr],p)
   if value:
    found={'phases':phases,'kind':'single_anomaly' if m==6 else 'inconsistent','prime':p,'zeta21':z,'rows':rr,'determinant':value};break
  if found:break
 assert found is not None,phases
 out.append(found)
summary={'assignments':len(out),'constant':sum(x['kind']=='constant' for x in out),'single_anomaly':sum(x['kind']=='single_anomaly' for x in out),'inconsistent':sum(x['kind']=='inconsistent' for x in out),'primes_used':sorted({x['prime'] for x in out if 'prime'in x}),'seconds':time.time()-start}
Path(__file__).with_name('independent_rank_minors.json').write_text(json.dumps({'summary':summary,'certificates':out},indent=2))
print(json.dumps(summary))
