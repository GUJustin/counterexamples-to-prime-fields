import json,time
from pathlib import Path
start=time.time();p=7;q=49
# theta²=3, nonsquare modulo7; encode a+7b.
def add(x,y):return (x%7+y%7)%7+7*((x//7+y//7)%7)
def mul(x,y):return ((x%7)*(y%7)+3*(x//7)*(y//7))%7+7*(((x%7)*(y//7)+(x//7)*(y%7))%7)
A=[[add(x,y) for y in range(q)] for x in range(q)]
M=[[mul(x,y) for y in range(q)] for x in range(q)]
neg=[(-x%7)%7+7*((-(x//7))%7) for x in range(q)]
powers=[[1]*48 for _ in range(q)]
for x in range(1,q):
 for d in range(1,48):powers[x][d]=M[powers[x][d-1]][x]
polys=[]
for a in range(q):
 for b in range(q):
  c=A[1][neg[A[a][b]]]
  vals=[A[A[M[a][M[x][x]]][M[b][x]]][c] for x in range(1,q)]
  polys.append((a,b,c,vals))
profiles=[]
for d in range(48):
 word=[powers[x][d] for x in range(1,q)];H={};Hfull={};examples=[]
 for a,b,c,vals in polys:
  k=sum(v==w for v,w in zip(vals,word));assert k>=1
  H[k]=H.get(k,0)+1
  if a and b and c:
   Hfull[k]=Hfull.get(k,0)+1
   if k>=7:examples.append([a,b,c,k])
 hist={k:48*v//k for k,v in H.items()};hf={k:48*v//k for k,v in Hfull.items()}
 assert all(48*v%k==0 for k,v in H.items()) and all(48*v%k==0 for k,v in Hfull.items())
 hist[0]=q**3-sum(hist.values());hf[0]=(q-1)**3-sum(hf.values())
 assert sum(k*v for k,v in hist.items())==48*q*q
 assert sum(k*(k-1)*v for k,v in hist.items())==48*47*q
 assert sum(k*(k-1)*(k-2)*v for k,v in hist.items())==48*47*46
 profiles.append(dict(d=d,histogram=hist,full_coefficient_histogram=hf,rich_count=sum(v for k,v in hist.items() if k>=7),rich_full_count=sum(v for k,v in hf.items() if k>=7),normalized_full_examples=examples))
result=dict(field=dict(p=7,modulus=[4,0,1],encoding='a+7b'),domain='F49*',normalization='Q(1)=1; counts L_A=48 H_A/A',profiles=profiles,seconds=time.time()-start)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps([dict(d=z['d'],rich=z['rich_count'],full=z['rich_full_count']) for z in profiles if z['rich_count']]))
print(time.time()-start)
