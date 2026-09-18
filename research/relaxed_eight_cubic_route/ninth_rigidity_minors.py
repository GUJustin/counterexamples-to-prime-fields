import json,itertools
from pathlib import Path
P=Path(__file__).parent;s=json.loads((P/'local_search.json').read_text());j=json.loads((P/'ninth_quartic_jacobian.json').read_text());p=17
free=[c for c in range(64) if c not in s['pivot_columns']]
gauges=[]
for k in range(4):
 v=[0]*64
 for i in range(8):v[4*i+k]=1
 for a,x in enumerate(s['nodes']):v[48+a]=pow(x,k,p)
 gauges.append(v)
v=sum((c[:] for c in s['polynomials']),[])+[0]*16+s['word'];gauges.append(v)
for typ in range(3):
 v=[0]*64
 for i,c in enumerate(s['polynomials']):
  for k in range(4):
   if k+1<4 and typ==0:v[4*i+k]=-(k+1)*c[k+1]%p
   if typ==1:v[4*i+k]=-k*c[k]%p
   if typ==2 and k>=1:v[4*i+k]=(4-k)*c[k-1]%p
 for a,x in enumerate(s['nodes']):
  v[32+a]=pow(x,typ,p)
  if typ==2:v[48+a]=3*x*s['word'][a]%p
 gauges.append(v)
assert all(sum(r[k]*v[k] for k in range(64))%17==0 for r in j['jacobian'][:56] for v in gauges)
def det(M):
 a=[r[:] for r in M];d=1
 for c in range(len(a)):
  z=next((i for i in range(c,len(a)) if a[i][c]%p),None)
  if z is None:return 0
  if z!=c:a[z],a[c]=a[c],a[z];d=-d
  v=a[c][c]%p;d=d*v%p;iv=pow(v,-1,p)
  for i in range(c+1,len(a)):
   t=a[i][c]*iv%p
   for k in range(c,len(a)):a[i][k]=(a[i][k]-t*a[c][k])%p
 return d%p
G=[[v[k] for v in gauges] for k in free];gd=det(G);assert gd
for S in itertools.combinations(range(8),6):
 M=[[j['jacobian'][56+i][k] for k in range(64,70)] for i in S];d=det(M)
 if d:break
assert d
out={'source_free_columns':free,'gauge_matrix':G,'gauge_minor_det':gd,'new_equation_indices':list(S),'new_variable_columns':list(range(64,70)),'new_minor':M,'new_minor_det':d,'gauges':gauges}
(P/'ninth_rigidity_minors.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ['gauges','gauge_matrix','new_minor']})
