import json,time
from pathlib import Path
start=time.time();base=Path(__file__).parent
src=json.loads((base/'gate.json').read_text());ds=[14,21,22,28,29,36]
# Direct complete enumeration, no orbit normalization. Separate component Horner formula.
def multiply(x,y):return ((x[0]*y[0]+3*x[1]*y[1])%7,(x[0]*y[1]+x[1]*y[0])%7)
def power(x,d):
 out=(1,0)
 for _ in range(d):out=multiply(out,x)
 return out
els=[(i%7,i//7) for i in range(49)];xs=els[1:]
look=[]
for x in xs:
 tab={}
 for j,d in enumerate(ds):tab.setdefault(power(x,d),[]).append(j)
 look.append(tab)
hist=[[0]*49 for _ in ds];full=[[0]*49 for _ in ds];banks=[[] for _ in ds]
for ai,a in enumerate(els):
 for bi,b in enumerate(els):
  ab=[]
  for x in xs:
   ax=multiply(a,x);ab.append(multiply(((ax[0]+b[0])%7,(ax[1]+b[1])%7),x))
  for ci,c in enumerate(els):
   counts=[0]*len(ds)
   for v,tab in zip(ab,look):
    val=((v[0]+c[0])%7,(v[1]+c[1])%7)
    for j in tab.get(val,[]):counts[j]+=1
   for j,k in enumerate(counts):
    hist[j][k]+=1
    if ai and bi and ci:
     full[j][k]+=1
     if k>=7:banks[j].append([ai,bi,ci,k])
for j,d in enumerate(ds):
 old=src['profiles'][d]
 assert {int(k):v for k,v in old['histogram'].items() if v}=={k:v for k,v in enumerate(hist[j]) if v}
 assert {int(k):v for k,v in old['full_coefficient_histogram'].items() if v}=={k:v for k,v in enumerate(full[j]) if v}
# Independent coefficient rank via inversion by repeated powers.
def inv(x):return power(x,47)
def rank(rows):
 a=[[els[v] for v in row[:3]] for row in rows];r=0
 for j in range(3):
  pivot=next((i for i in range(r,len(a)) if a[i][j]!=(0,0)),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];u=inv(a[r][j]);a[r]=[multiply(v,u) for v in a[r]]
  for i in range(r+1,len(a)):
   c=a[i][j]
   a[i]=[((v[0]-w[0])%7,(v[1]-w[1])%7) for v,w in zip(a[i],[multiply(c,t) for t in a[r]])]
  r+=1
 return r
out=dict(method='all 49^3 coefficient triples, direct tuple Horner; no normalization',seconds=time.time()-start,profiles=[dict(d=d,full_rich_bank=banks[j],coefficient_rank=rank(banks[j])) for j,d in enumerate(ds)])
(base/'replay.json').write_text(json.dumps(out,indent=2)+'\n');print([(z['d'],len(z['full_rich_bank']),z['coefficient_rank']) for z in out['profiles']]);print(out['seconds'])
