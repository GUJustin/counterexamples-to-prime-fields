import json,sys,math,collections,time,pathlib,hashlib
start=time.monotonic();path=pathlib.Path(sys.argv[1]);d=json.loads(path.read_text());p=d['p'];L=d['L'];nodes=d.get('nodes',d.get('best',{}).get('nodes'))
def prime(n):return n>1 and all(n%i for i in range(2,math.isqrt(n)+1))
assert prime(p)
aa=[];i=2
while len(aa)<L:
 if prime(i):aa.append(i)
 i+=1
assert p>2*aa[-1]**2
core={s*a*b%p for i,a in enumerate(aa) for b in aa[:i] for s in [-1,1]}
assert len(core)==L*(L-1)
assert len(nodes)==L*(L-1)+1 and len(set(nodes))==len(nodes)
hist=collections.Counter();owners={}
for x in nodes:
 assert x and x not in core
 labels=[]
 for i,a in enumerate(aa):
  poly=(x*x*pow(a*a,-1,p)+a*a)%p
  z=(poly-pow(x,4,p))*pow(pow(x,3,p),-1,p)%p
  assert z not in (0,1)
  labels.append(z);hist[z]+=1
 assert len(set(labels))==L
single=sum(c==1 for c in hist.values());claimed=d.get('singletons',d.get('best',{}).get('singletons'));assert single==claimed
out=dict(pass_all=True,input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),p=p,L=L,n=2*L*(L-1)+1,incidences=sum(hist.values()),singletons=single,bad_labels=len(hist),density=single/p,seconds=time.monotonic()-start,scope='Exact incidence arithmetic plus stated degree proof; no exhaustive polynomial scan')
path.with_suffix('.checked.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
