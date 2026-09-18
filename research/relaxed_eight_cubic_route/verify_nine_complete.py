import json,itertools,runpy
from pathlib import Path
D=Path(__file__).parent
v=runpy.run_path(str(D/'verify_nine_exchange.py'))
s=v['s'];M=v['M'];X=v['nodes'];W=v['word'];polys=v['polys'];add=v['add'];mul=v['mul'];ev=v['ev'];p=17
neg=lambda a:((-a[0])%p,(-a[1])%p)
sub=lambda a,b:add(a,neg(b))
def inv(a):
 n=pow((a[0]*a[0]-7*a[1]*a[1])%p,-1,p)
 return (a[0]*n%p,-a[1]*n%p)
seen={}
for I in itertools.combinations(range(18),5):
 xx=[X[j] for j in I]; d=[W[j] for j in I]
 for k in range(1,5):
  for j in range(4,k-1,-1):d[j]=mul(sub(d[j],d[j-1]),inv(sub(xx[j],xx[j-k])))
 c=[d[4]]
 for k in range(3,-1,-1):
  o=[(0,0)]*(len(c)+1)
  for j,a in enumerate(c):o[j]=sub(o[j],mul(xx[k],a));o[j+1]=add(o[j+1],a)
  o[0]=add(o[0],d[k]);c=o
 key=tuple(c)
 if key in seen:continue
 matches=[]
 for j,x in enumerate(X):
  y=(0,0)
  for a in reversed(c):y=add(mul(y,x),a)
  if y==W[j]:matches.append(j)
 seen[key]=matches
hits={c:vs for c,vs in seen.items() if len(vs)>=8}
known={tuple((a,0) for a in c) for c in polys}
assert len(seen)==5628 and set(hits)==known and max(map(len,seen.values()))==9
# Reconstruct integral equation values divided by17, then verify left-null receipts.
f=[]
for i,S in enumerate(s['selected_supports']):
 for j in S:
  x=s['nodes'][j];f.append(sum(a*x**k for k,a in enumerate(s['polynomials'][i]))-s['word'][j])
for j in v['ns']:
 x=s['nodes'][j];f.append(sum(a*x**k for k,a in enumerate(v['N']))-x*s['word'][j])
assert all(x%17==0 for x in f);defect=[x//17%17 for x in f]
z=json.loads((D/'ninth_mod289.json').read_text());assert defect==z['defect']
for cert in z['certificates']:
 l=cert['left_null'];assert all(sum(l[i]*M[i][j] for i in range(64))%17==0 for j in range(70))
 assert sum(a*b for a,b in zip(l,defect))%17==cert['dot_defect']
 assert (l[0]*13+l[56]*2)%17==cert['dot_defect']
l1,l2=[c['left_null'] for c in z['certificates']]
assert (l1[0]*l2[56]-l1[56]*l2[0])%17!=0
out=dict(five_subsets=8568,distinct_interpolants=len(seen),maximum_residue_agreement=9,exactly_known_nine=True,deleted_equation_residual_div17=[13,2],left_null_verified=True,all_pass=True)
(D/'nine_complete.verified.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
