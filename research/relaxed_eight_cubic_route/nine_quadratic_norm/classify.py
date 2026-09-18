import json
from pathlib import Path
P=Path(__file__).parent;d=json.loads((P/'screen.json').read_text());s=json.loads((P.parent/'nine_complete_decode.json').read_text());q=289;p=17
A=[[0]*q for _ in range(q)];M=[[0]*q for _ in range(q)];N=[];I=[0]*q
for u in range(q):
 a,b=u%p,u//p;N.append((-a)%p+p*((-b)%p))
 for v in range(q):
  c,e=v%p,v//p;A[u][v]=(a+c)%p+p*((b+e)%p);M[u][v]=(a*c+7*b*e)%p+p*((a*e+b*c)%p)
for u in range(1,q):I[u]=M[u].index(1)
def tr(a):
 while len(a)>1 and not a[-1]:a.pop()
 return a
def sub(a,b):return A[a][N[b]]
def div(a,b):
 a=a[:];out=[0]*max(1,len(a)-len(b)+1)
 while a!=[0] and len(a)>=len(b):
  k=len(a)-len(b);t=M[a[-1]][I[b[-1]]];out[k]=t
  for j,v in enumerate(b):a[k+j]=sub(a[k+j],M[t][v])
  tr(a)
 return tr(out),a
def gcd(a,b):
 while b!=[0]:a,b=b,div(a,b)[1]
 return [M[v][I[a[-1]]] for v in a]
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):c[i+j]=A[c[i+j]][M[u][v]]
 return tr(c)
def ev(c,x):
 r=0
 for v in c[::-1]:r=A[M[r][x]][v]
 return r
hist={};hits=[]
for v in d['all_norms']:
 E=[M[N[a]][9] for a in v[:5]];J=mul(E,E)+[0]*9;J=J[:9]
 for i in range(9):J[i]=sub(J[i],v[5+i])
 tr(J)
 if J==[0]:key='zero';hist[key]=hist.get(key,0)+1;continue
 df=tr([M[i][J[i]] for i in range(1,len(J))]or[0]);c=gcd(J,df);w=div(J,c)[0];odd=[1];O=[1];i=1
 while len(w)>1:
  y=gcd(w,c);z=div(w,y)[0]
  if i%2:odd=mul(odd,z)
  for _ in range(i//2):O=mul(O,z)
  w=y;c=div(c,y)[0];i+=1
 key=f'degree{len(J)-1}_odd{len(odd)-1}';hist[key]=hist.get(key,0)+1
 weak=(len(odd)-1+(8-(len(J)-1))%2)<=2
 assert weak == (v in d['accepted'])
 normcount=fullcount=0
 for x,a in zip(s['nodes_encoded'],s['word_encoded']):
  if A[A[M[a][a]][M[ev(v[:5],x)][a]]][ev(v[5:],x)]==0:
   normcount+=1
   db=ev([M[i][v[i]] for i in range(1,5)],x);dc=ev([M[i][v[5+i]] for i in range(1,9)],x)
   if ev(v[:5],x)==N[M[2][a]] and A[M[a][db]][dc]==0:fullcount+=1
 assert normcount+min(3,fullcount)>=15
 if len(J)>8 or len(odd)!=2:continue
 branch=M[N[odd[0]]][I[odd[1]]]
 if branch in s['nodes_encoded']:continue
 norm=[];full=[]
 for k,(x,a) in enumerate(zip(s['nodes_encoded'],s['word_encoded'])):
  if A[A[M[a][a]][M[ev(v[:5],x)][a]]][ev(v[5:],x)]==0:
   norm.append(k)
   if ev(E,x)==a and ev(O,x)==0:full.append(k)
 assert len(norm)+len(full)>=15
 hits.append({'E':E,'O_monic':O,'square_scale':J[-1],'branch':branch,'norm_support':norm,'full_support':full,'agreements':len(norm)+len(full),'B_C':v})
out={'histogram':hist,'proper_polynomial_cover_hits':hits};(P/'classified.json').write_text(json.dumps(out,indent=2)+'\n');print('hist',hist,'properhits',len(hits));print(hits[:3])
