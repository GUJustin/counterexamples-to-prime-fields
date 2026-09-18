import json,random,time,math,pathlib
start=time.monotonic()
def prime(n):
 return n>1 and all(n%d for d in range(2,math.isqrt(n)+1))
L=25; aa=[x for x in range(2,100) if prime(x)][:L]
p=20011
assert prime(p) and p>2*max(aa)**2
N0=L*(L-1); t=N0+1
core={s*a*b%p for i,a in enumerate(aa) for b in aa[i+1:] for s in [-1,1]}
assert len(core)==N0
coeff=[(a*a,pow(a*a,-1,p)) for a in aa]
rng=random.Random(20260918)
best=None; trials=[]
for trial in range(20):
 nodes=[]; hist={}; scanned=0
 for x in rng.sample(range(1,p),p-1):
  if x in core: continue
  scanned+=1; ix=pow(x,-1,p); ix3=ix**3%p
  labels=[(c*ix3+d*ix-x)%p for c,d in coeff]
  assert len(set(labels))==L
  if 0 in labels or 1 in labels: continue
  nodes.append(x)
  for z in labels: hist[z]=hist.get(z,0)+1
  if len(nodes)==t: break
 assert len(nodes)==t
 singles=sum(v==1 for v in hist.values())
 row=dict(trial=trial,singletons=singles,distinct_labels=len(hist),max_multiplicity=max(hist.values()),scanned=scanned)
 trials.append(row)
 if best is None or singles>best['singletons']:
  best=dict(row,nodes=nodes)
out=dict(L=L,p=p,n=2*N0+1,K=3,A=2*(L-1),threshold=2*L-1,incidences=L*t,trials=trials,best=best,seconds=time.monotonic()-start)
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['trials','best']}));print(json.dumps({k:v for k,v in best.items() if k!='nodes'}))
