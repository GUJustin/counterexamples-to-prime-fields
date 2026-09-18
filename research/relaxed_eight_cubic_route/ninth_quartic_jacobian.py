import json
from pathlib import Path
P=Path(__file__).parent; s=json.loads((P/'local_search.json').read_text());g=json.loads((P/'ninth_quartic_gate.json').read_text());p=17
N=g['hits'][0]['coefficients']; rows=[]; residual=[]
def ev(c,x):return sum(a*pow(x,j,p) for j,a in enumerate(c))%p
def der(c,x):return sum(j*c[j]*pow(x,j-1,p) for j in range(1,len(c)))%p
for i,S in enumerate(s['selected_supports']):
 for k in S:
  x=s['nodes'][k];w=s['word'][k];row=[0]*70
  for j in range(4):row[4*i+j]=pow(x,j,p)
  row[32+k]=der(s['polynomials'][i],x);row[48+k]=-1%p
  rows.append(row);residual.append((ev(s['polynomials'][i],x)-w)%p)
for k in g['hits'][0]['support']:
 x=s['nodes'][k];w=s['word'][k];row=[0]*70
 row[32+k]=(der(N,x)-w)%p;row[48+k]=-x%p;row[64]=w
 for j in range(5):row[65+j]=pow(x,j,p)
 rows.append(row);residual.append((ev(N,x)-x*w)%p)
assert not any(residual)
a=[r[:] for r in rows];rank=0;piv=[];det=1
for c in range(70):
 z=next((i for i in range(rank,64) if a[i][c]),None)
 if z is None:continue
 if z!=rank:a[z],a[rank]=a[rank],a[z];det=-det%p
 v=a[rank][c];det=det*v%p;iv=pow(v,-1,p);a[rank]=[t*iv%p for t in a[rank]]
 for i in range(rank+1,64):
  v=a[i][c]
  if v:a[i]=[(t-v*u)%p for t,u in zip(a[i],a[rank])]
 piv.append(c);rank+=1
 if rank==64:break
out={'p':p,'equations':64,'variables':70,'rank':rank,'pivot_columns':piv,'minor_determinant':det if rank==64 else None,'residuals_zero':not any(residual),'variable_order':'8 old cubic coefficient vectors;16 nodes;16 word values;pole b;5 numerator coefficients','jacobian':rows}
(P/'ninth_quartic_jacobian.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='jacobian'})
