"""Complete P2(F29) normalization-point necessary filter on F3; not a char0 exclusion."""
import json,math,time
from pathlib import Path
P=Path(__file__).parent;d=json.loads((P.parent.parent/'gate.json').read_text())[0];p=29
base=[[(k,l,c)for(k,l),c in zip(d['columns'],v)if c]for v in d['kernel']]
charts=[base, [[(k,10-l,c)for k,l,c in f]for f in base], [[(34-k-3*l,l,c)for k,l,c in f]for f in base], [[(34-k-3*l,10-l,c)for k,l,c in f]for f in base]]
def jet(f,x,y,a,b):return sum(c*math.comb(k,a)*math.comb(l,b)*pow(x,k-a,p)*pow(y,l-b,p) for k,l,c in f if k>=a and l>=b)%p
pts=[]
for chart,coords in enumerate([[(x,y)for x in range(p)for y in range(p)],[(x,0)for x in range(p)],[(0,y)for y in range(p)],[(0,0)]]):
 for x,y in coords:
  fs=charts[chart];pts.append((chart,x,y,[[jet(f,x,y,a,b)for f in fs]for a,b in [(0,0),(1,0),(0,1)]]))
cache={}
def homogeneous(chart,x,y,m):
 key=chart,x,y,m
 if key not in cache:cache[key]=[[jet(f,x,y,m-b,b)for f in charts[chart]]for b in range(m+1)]
 return cache[key]
def trim(f):
 while f and f[-1]==0:f.pop()
 return f
def rem(f,g):
 f=f[:];iv=pow(g[-1],-1,p)
 while len(f)>=len(g):
  c=f[-1]*iv%p;j=len(f)-len(g)
  for i,a in enumerate(g):f[i+j]=(f[i+j]-c*a)%p
  trim(f)
 return f
def squarefree(f):
 f=trim(f[:]);g=trim([i*f[i]%p for i in range(1,len(f))])
 while g:f,g=g,rem(f,g)
 return len(f)==1
def cone(co):
 # F(dx,dy)=sum co[b] dx^(m-b)dy^b. dy/dx finite, plus dx=0.
 m=len(co)-1;v=m-next(i for i in range(m,-1,-1)if co[i]);sf=v<=1 and squarefree(co)
 nr=int(v>0)+sum(sum(c*pow(t,i,p)for i,c in enumerate(co))%p==0 for t in range(p))
 return sf,nr
members=[(1,a,b)for a in range(p)for b in range(p)]+[(0,1,a)for a in range(p)]+[(0,0,1)]
out=[]
for pars in members:
 known=0;unknown=[];ordinary=[];smooth=0
 for ch,x,y,vals in pts:
  z=[sum(a*b for a,b in zip(v,pars))%p for v in vals]
  if z[0]:continue
  if z[1] or z[2]:known+=1;smooth+=1;continue
  for m in range(2,12):
   co=[sum(a*b for a,b in zip(v,pars))%p for v in homogeneous(ch,x,y,m)]
   if any(co):break
  if not any(co):unknown.append([ch,x,y,'multiplicity>11']);continue
  sf,nr=cone(co)
  if sf:known+=nr;ordinary.append([ch,x,y,m,nr])
  else:unknown.append([ch,x,y,m,co])
 status='excluded_lower_bound' if known>30 else ('unresolved_nonordinary' if unknown else ('point_count_candidate' if known==30 else 'excluded_exact_count'))
 out.append(dict(parameters=pars,known_normalization_points=known,smooth_points=smooth,ordinary_singularities=ordinary,unknown_singularities=unknown,status=status))
summary={s:sum(r['status']==s for r in out)for s in sorted(set(r['status']for r in out))}
(P/'count.json').write_text(json.dumps(dict(p=p,surface_points=len(pts),members=len(out),summary=summary,results=out),indent=2));print(summary)
