import json,itertools,hashlib
from pathlib import Path
P=Path(__file__).parent
raw=(P/'local_search.json').read_bytes(); data=json.loads(raw); p=data['p']; xs=data['nodes']; ys=[x*y%p for x,y in zip(xs,data['word'])]
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):c[i+j]=(c[i+j]+u*v)%p
 return c
def interp(S):
 out=[0]*5
 for i in S:
  b=[1]; den=1
  for j in S:
   if j!=i:b=mul(b,[-xs[j]%p,1]);den=den*(xs[i]-xs[j])%p
  t=ys[i]*pow(den,-1,p)%p
  for k,v in enumerate(b):out[k]=(out[k]+t*v)%p
 return tuple(out)
def ev(c,x):
 y=0
 for a in c[::-1]:y=(y*x+a)%p
 return y
seen=set(); hist={}; hits=[]; best=[]; maximum=0
for S in itertools.combinations(range(16),5):
 c=interp(S)
 if c in seen:continue
 seen.add(c)
 if c[0]==0:continue
 support=[i for i,x in enumerate(xs) if ev(c,x)==ys[i]]; a=len(support)
 hist[a]=hist.get(a,0)+1
 if a>maximum:maximum=a;best=[]
 if a==maximum:best.append({'coefficients':c,'support':support})
 if a>=8:hits.append({'coefficients':c,'support':support})
out={'source_sha256':hashlib.sha256(raw).hexdigest(),'p':p,'pole':0,'interpolation_subsets':4368,'distinct_interpolants':len(seen),'proper_agreement_histogram':hist,'maximum_proper_agreement':maximum,'best':best,'hits':hits}
(P/'ninth_quartic_gate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['best','hits']}));print('hits',len(hits))
