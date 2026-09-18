import json,itertools,math
from pathlib import Path
P=0

def add(a,b):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return trim([x%P for x in c])
def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def scale(a,k):return trim([x*k%P for x in a])
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%P
 return trim(c)
def ev(a,t):
 z=0
 for c in reversed(a):z=(z*t+c)%P
 return z
def div(a,b):
 a=a[:];q=[0]*max(1,len(a)-len(b)+1)
 while len(a)>=len(b) and a!=[0]:
  j=len(a)-len(b);c=a[-1]*pow(b[-1],-1,P)%P;q[j]=c
  a=add(a,[0]*j+scale(b,-c))
 return trim(q),a
def compose(a,b):
 z=[0]
 for c in reversed(a):z=add(mul(z,b),[c])
 return z
class D:
 def __init__(self,v,g=None):self.v=v%P;self.g=g or [0]*15
 def __add__(self,b):
  b=b if isinstance(b,D) else D(b)
  return D(self.v+b.v,[(a+c)%P for a,c in zip(self.g,b.g)])
 __radd__=__add__
 def __neg__(self):return D(-self.v,[-x%P for x in self.g])
 def __sub__(self,b):return self+-b
 def __rsub__(self,b):return -self+b
 def __mul__(self,b):
  b=b if isinstance(b,D) else D(b)
  return D(self.v*b.v,[(a*b.v+c*self.v)%P for a,c in zip(self.g,b.g)])
 __rmul__=__mul__
 def __pow__(self,n):
  z=D(1)
  for _ in range(n):z=z*self
  return z
def rank(a):
 a=[r[:] for r in a];pivot=[];k=0
 for j in range(len(a[0])):
  i=next((i for i in range(k,len(a)) if a[i][j]%P),None)
  if i is None:continue
  a[k],a[i]=a[i],a[k];z=pow(a[k][j],-1,P);a[k]=[x*z%P for x in a[k]]
  for i in range(len(a)):
   if i!=k:
    z=a[i][j];a[i]=[(x-z*y)%P for x,y in zip(a[i],a[k])]
  pivot.append(j);k+=1
  if k==len(a):break
 return pivot

def verify(hit):
 global P;P=hit['p'];aa=hit['a'];a0=hit['first_pole'];c=hit['critical'];b=hit['new_pole'];ts=hit['nodes'];ys=hit['base_nodes'];ws=hit['values']
 N=[0]
 for i,t in enumerate(ts[:8]):
  basis=[1];den=1
  for j,u in enumerate(ts[:8]):
   if i!=j:basis=mul(basis,[-u,1]);den=den*(t-u)%P
  N=add(N,scale(basis,(t-b)*ws[i]*pow(den,-1,P)))
 assert all(ev(N,t)==(t-b)*w%P for t,w in zip(ts,ws))
 assert all((t*t+c-y)%P==0 for t,y in zip(ts,ys))
 E=compose(N[::2],[-c,1]);O=compose(N[1::2],[-c,1]);E+= [0]*(4-len(E));O += [0]*(4-len(O))
 ei=[1]+[sum(math.prod(z) for z in itertools.combinations(aa,j))%P for j in range(1,5)]
 _,e1,e2,e3,e4=ei
 G=compose(scale([-e3*e4,e2*e3-e1*e4,e3-e1*e2,e1],-pow(e3,-1,P)),[c,0,1])
 res=add(N,scale(mul([-b,1],G),-1))
 forced=[t for t,w in zip(ts,ws) if ev(G,t)==w]
 assert len(forced)==5
 factor=[1]
 for t in forced:factor=mul(factor,[-t,1])
 quad,rem=div(res,factor);assert rem==[0]
 base=[];edges=[]
 for i,j in itertools.combinations(range(4),2):
  for sig in (1,-1):base.append(sig*aa[i]*aa[j]%P);edges.append((i,j,sig))
 core=[a0]+base
 assert len(ys)==12 and len(set(ys))==12 and ys.count(a0)==1
 omitted=set(core)-set(ys)
 assert len(omitted)==1 and next(iter(omitted)) in base[::2]
 for y,wv in zip(ys,ws):
  if y==a0: assert wv==0
  else:
   i,j,_=edges[base.index(y)];assert wv==(y-a0)*(aa[i]**2+aa[j]**2)%P
 guards={'seed_nonzero':all(aa),'distinct_squares':len({x*x%P for x in aa})==4,'distinct_base':len(set(base))==12,'first_pole_off':a0 not in base,'first_pole_relation':(e3*a0-e1*e4)%P==0,'critical_off':c not in core,'new_pole_off':(b*b+c)%P not in core,'proper':ev(N,b)!=0,'single_roots':all((ev(O,y)-w)%P!=0 for y,w in zip(ys,ws)),'quadratic':len(quad)==3,'quad_discriminant':len(quad)==3 and (quad[1]**2-4*quad[0]*quad[2])%P!=0,'quad_off_pole':ev(quad,b)!=0}
 guards['quad_off_core']=all(div([c-y,0,1],quad)[1]!=[0] and (lambda r: r!=[0] and (len(r)==1 or ev(quad,-r[0]*pow(r[1],-1,P)%P)!=0))(div([c-y,0,1],quad)[1]) for y in core) if len(quad)==3 else False
 vals=aa+[a0,c,b]+E+O
 vv=[]
 for i,v in enumerate(vals):g=[0]*15;g[i]=1;vv.append(D(v,g))
 av=vv[:4];av0,cv,bv=vv[4:7];ee=vv[7:11];oo=vv[11:15]
 e1v=sum(av);e3v=sum(math.prod(z) for z in itertools.combinations(av,3));e4v=math.prod(av)
 eq=[e3v*av0-e1v*e4v]
 for y,w in zip(ys,ws):
  if y==a0:yv=av0;wv=D(0)
  else:
   idx=base.index(y);i,j,sig=edges[idx];yv=sig*av[i]*av[j];wv=(yv-av0)*(av[i]**2+av[j]**2)
  evv=sum(ee[j]*yv**j for j in range(4));ovv=sum(oo[j]*yv**j for j in range(4))
  eq.append((evv+bv*wv)**2-(yv-cv)*(ovv-wv)**2)
 assert all(f.v==0 for f in eq)
 piv=rank([f.g for f in eq])
 return {'p':P,'a':aa,'N':N,'E':E,'O':O,'G5':G,'forced_roots':forced,'residual_quadratic':quad,'guards':guards,'all_guards':all(guards.values()),'jacobian_rank':len(piv),'pivot_columns':piv,'free_columns':[i for i in range(15) if i not in piv],'variables':vals}
if __name__=='__main__':
 root=Path(__file__).parent
 out=[verify(json.loads(s)) for s in (root/'hits.jsonl').read_text().splitlines() if s]
 (root/'independent_lift.json').write_text(json.dumps(out,indent=2)+'\n')
 for r in out:print({k:r[k] for k in ('p','a','all_guards','jacobian_rank','guards')})
