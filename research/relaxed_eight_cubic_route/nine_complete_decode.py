"""Exhaust all five-point quartic interpolants over F17(theta), theta^2=7."""
from pathlib import Path
import json,itertools,time,hashlib
from array import array
P=Path(__file__).parent;raw=(P/'local_search.json').read_bytes();s=json.loads(raw);start=time.monotonic();p=17;q=289
# Encode a+b theta by a+17b. Exact tables are generated from theta^2=7.
ADD=array('H');MUL=array('H');NEG=[];INV=[0]*q
for u in range(q):
 a,b=u%p,u//p;NEG.append((-a)%p+p*((-b)%p))
 if u:
  ni=pow((a*a-7*b*b)%p,-1,p);INV[u]=(a*ni)%p+p*((-b*ni)%p)
 for v in range(q):
  c,d=v%p,v//p;ADD.append((a+c)%p+p*((b+d)%p));MUL.append((a*c+7*b*d)%p+p*((a*d+b*c)%p))
def add(a,b):return ADD[q*a+b]
def mul(a,b):return MUL[q*a+b]
def ev(c,x):
 v=0
 for a in reversed(c):v=add(mul(v,x),a)
 return v
N=[2,15,8,5,13];polys=[[0]+c for c in s['polynomials']]+[N]
X=s['nodes']+[0,17];W=[x*w%p for x,w in zip(s['nodes'],s['word'])]+[0,ev(N,17)]
assert len(set(X))==18;seen={};count=0
for sub in itertools.combinations(range(18),5):
 count+=1;locator=[1]
 for j in sub:
  x=X[j];n=[0]*(len(locator)+1)
  for k,c in enumerate(locator):n[k]=add(n[k],mul(c,NEG[x]));n[k+1]=add(n[k+1],c)
  locator=n
 coeff=[0]*5
 for j in sub:
  x=X[j];basis=[0]*5;basis[4]=locator[5]
  for k in range(3,-1,-1):basis[k]=add(locator[k+1],mul(x,basis[k+1]))
  denominator=ev(basis,x);assert denominator
  weight=mul(W[j],INV[denominator])
  for k in range(5):coeff[k]=add(coeff[k],mul(weight,basis[k]))
 key=tuple(coeff)
 if key not in seen:seen[key]=[j for j,x in enumerate(X) if ev(coeff,x)==W[j]]
assert count==8568
hits=[{'coefficients_encoded':list(c),'support':m,'agreements':len(m)} for c,m in seen.items() if len(m)>=8]
known={tuple(c) for c in polys};found={tuple(r['coefficients_encoded']) for r in hits}
out={'prime':17,'field':'F17[theta]/(theta^2-7)','encoding':'a+17*b represents a+b*theta','input_sha256':hashlib.sha256(raw).hexdigest(),'nodes_encoded':X,'word_encoded':W,'five_subsets':count,'distinct_interpolants':len(seen),'maximum_agreement':max(map(len,seen.values())),'hits':hits,'exactly_known_nine':found==known,'seconds':time.monotonic()-start}
(P/'nine_complete_decode.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k not in ['hits','nodes_encoded','word_encoded']}))
