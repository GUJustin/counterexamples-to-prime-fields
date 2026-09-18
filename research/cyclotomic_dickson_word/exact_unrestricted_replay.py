"""Independent exact cyclotomic Newton replay for completed modular lists."""
import json,argparse,time
from pathlib import Path
from flint import fmpq_poly
ap=argparse.ArgumentParser();ap.add_argument('directory');args=ap.parse_args();P=Path(args.directory);d=json.loads((P/'survivors.json').read_text());start=time.monotonic()
k,n,target=d['k'],d['n'],d['target'];assert n==4*k
mods={36:{0:1,6:-1,12:1},40:{0:1,4:-1,8:1,12:-1,16:1}}
m=mods[n];F=fmpq_poly([m.get(i,0) for i in range(max(m)+1)]);zero=fmpq_poly([]);one=fmpq_poly([1]);z=fmpq_poly([0,1])
def mul(a,b):return a*b%F
def inv(a):
 g,u,v=a.xgcd(F);assert g==one
 return u%F
xs=[one]
for i in range(1,n):xs.append(mul(xs[-1],z))
assert mul(xs[-1],z)==one
w=[(one+xs[(2*k*i)%n])/2-xs[(k*i)%n] for i in range(n)]
def ev(c,x):
 a=zero
 for b in reversed(c):a=mul(a,x)+b
 return a

def interp(S):
 c=[zero]*k;b=[one]
 for i in reversed(S[-k:]):
  t=mul(w[i]-ev(c,xs[i]),inv(ev(b,xs[i])))
  for j,a in enumerate(b):c[j]+=mul(t,a)
  nxt=[zero]*(len(b)+1)
  for j,a in enumerate(b):nxt[j]-=mul(a,xs[i]);nxt[j+1]+=a
  b=nxt
 return c

def key(c):return tuple(tuple(str(v) for v in a) for a in c)
def support(c):return [i for i in range(n) if ev(c,xs[i])==w[i]]
def mod(a):
 v=0
 for q in reversed(list(a)):v=(v*d['root']+int(q.numerator)*pow(int(q.denominator),-1,d['p']))%d['p']
 return v
rows=[];bank={}
for row in d['candidates']:
 S=row['support'];assert len(S)==target # Essential for exhaustive lift rejection.
 c=interp(S);hits=support(c);assert [mod(a) for a in c]==row['coefficients']
 orbit={key([mul(a,xs[(4*t*j)%n]) for j,a in enumerate(c)]):[mul(a,xs[(4*t*j)%n]) for j,a in enumerate(c)] for t in range(k)}
 if len(hits)>=target:bank.update(orbit)
 rows.append({'modular_support':S,'exact_support':hits,'failed_support_indices':sorted(set(S)-set(hits)),'qualifies':len(hits)>=target,'orbit_size':len(orbit),'coefficients':key(c)})
out={'n':n,'k':k,'target':target,'modulus_ascending':[str(a) for a in F], 'representatives':rows,'exact_qualifying_count':len(bank),'full_bank':[{'coefficients':key(c),'support':support(c)} for c in bank.values()], 'seconds':time.monotonic()-start,'scope':'Every modular survivor has exactly target matches, so exact rejection from any k of its support is exhaustive; modular census completeness separately required.'}
(P/'exact_replay.json').write_text(json.dumps(out,indent=2)+'\n');print({a:b for a,b in out.items() if a not in ('representatives','full_bank')});print([(r['exact_support'],r['failed_support_indices']) for r in rows])
