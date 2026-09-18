import json
from pathlib import Path
D=Path(__file__).parent
s=json.loads((D/'local_search.json').read_text()); N=[2,15,8,5,13]; p=17
pe=lambda c,x:sum(a*pow(x,j,p) for j,a in enumerate(c))%p
de=lambda c,x:sum(j*a*pow(x,j-1,p) for j,a in enumerate(c) if j)%p
ns=[j for j,x in enumerate(s['nodes']) if pe(N,x)==x*s['word'][j]%p]
M=[]
for i,S in enumerate(s['selected_supports']):
 for k in S:
  x=s['nodes'][k]; r=[0]*70
  r[4*i:4*i+4]=[pow(x,j,p) for j in range(4)]
  r[32+k]=de(s['polynomials'][i],x);r[48+k]=16; M.append(r)
for k in ns:
 x=s['nodes'][k]; w=s['word'][k];r=[0]*70
 r[32+k]=(de(N,x)-w)%p;r[48+k]=-x%p;r[64]=w
 r[65:]=[pow(x,j,p) for j in range(5)];M.append(r)
rows=[i for i in range(64) if i not in (0,56)]
a=[M[i][:] for i in rows];cols=[];rr=0
for j in range(70):
 z=next((i for i in range(rr,62) if a[i][j]),None)
 if z is None:continue
 a[rr],a[z]=a[z],a[rr];inv=pow(a[rr][j],-1,p)
 for i in range(rr+1,62):
  f=a[i][j]*inv%p
  a[i]=[(v-f*u)%p for v,u in zip(a[i],a[rr])]
 cols.append(j);rr+=1
 if rr==62:break
assert rr==62
# Exact integer Bareiss on original square minor.
b=[[M[i][j] for j in cols] for i in rows];sgn=1;last=1
for k in range(61):
 if not b[k][k]:
  z=next(i for i in range(k+1,62) if b[i][k]);b[k],b[z]=b[z],b[k];sgn=-sgn
 v=b[k][k]
 for i in range(k+1,62):
  for j in range(k+1,62):
   q=b[i][j]*v-b[i][k]*b[k][j];assert q%last==0;b[i][j]=q//last
  b[i][k]=0
 last=v
minor=sgn*b[-1][-1]%p;assert minor
# Tuple arithmetic F17[theta]/(theta^2-7).
add=lambda a,b:((a[0]+b[0])%p,(a[1]+b[1])%p)
mul=lambda a,b:((a[0]*b[0]+7*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def ev(c,x):
 r=(0,0)
 for a in reversed(c):r=add(mul(r,x),(a,0))
 return r
assert 7 not in {x*x%p for x in range(p)}
th=(0,1);polys=[[0]+c for c in s['polynomials']]+[N]
nodes=[(x,0) for x in s['nodes']]+[(0,0),th]
word=[(x*w%p,0) for x,w in zip(s['nodes'],s['word'])]+[(0,0),ev(N,th)]
actual=[[j for j,x in enumerate(nodes) if ev(c,x)==word[j]] for c in polys]
selected=[S[:] + [16] for S in s['selected_supports']]+[[j for j in ns if j!=0]+[17]]
selected[0].remove(2);selected[0].append(17)
assert len(set(nodes))==18 and len({tuple(c) for c in polys})==9
assert all(len(S)==8 and set(S)<=set(A) for S,A in zip(selected,actual))
def pmul(a,b):
 o=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):o[i+j]=(o[i+j]+x*y)%p
 return o
fac=[11*x%p for x in pmul(pmul([-5%p,1],[-6%p,1]),[10,0,1])]
diff=[(a-b)%p for a,b in zip(N,[0]+s['polynomials'][0])]
assert fac==diff and ev(diff,th)==(0,0)
deriv=[j*diff[j]%p for j in range(1,5)]
assert ev(deriv,th)!=(0,0) and N[0]!=0
out=dict(rank=rr,minor_mod17=minor,minor_rows=rows,minor_columns=cols,factor_coefficients=fac,fresh_root_derivative=ev(deriv,th),actual_supports=actual,selected_supports=selected,proper_pole_value=N[0],pass_all=True)
(D/'nine_exchange.verified.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k not in ('minor_rows','minor_columns','actual_supports','selected_supports')});print('Actual counts:',list(map(len,actual)))
