"""Exact Q(theta) replay of every survivor of the closed modular screen."""
import json,time
from pathlib import Path
from flint import fmpq as Q,fmpq_mat
import sympy as S
P=Path(__file__).parent;start=time.monotonic();d=json.loads((P/'rational_seed.json').read_text());fr=json.loads((P/'pair_padding_gate.json').read_text())['candidates'];screen=json.loads((P/'eleven_quadratic_norm_screen.json').read_text());assert not screen['unresolved_systems']
z=(Q(0),Q(0));one=(Q(1),Q(0));t0=Q('-4525/15304');t1=Q('-4175/3826')
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def mul(a,b):return a[0]*b[0]+a[1]*b[1]*t0,a[0]*b[1]+a[1]*b[0]+a[1]*b[1]*t1
def scale(a,k):return a[0]*k,a[1]*k
def powr(a,i):
 r=one
 for _ in range(i):r=mul(r,a)
 return r
def ev(c,x):
 r=z
 for a in reversed(c):r=add(mul(r,x),a)
 return r
X=[(Q(a),Q(0)) for a in d['affine_nodes']]+[(Q('-80/163'),Q(0)),(Q('-135/262'),Q(0)),(Q(0),Q(1))];W=[(Q(a),Q(0)) for a in d['affine_word']];F=[(Q(a),Q(0)) for a in fr[0]['coefficients']];F2=[(Q(a),Q(0)) for a in fr[2]['coefficients']];W.extend([ev(F,X[16]),ev(F,X[17]),ev(F2,X[18])])
norm=[[mul(w,powr(x,i)) for i in range(4)]+[powr(x,i) for i in range(7)]+[neg(mul(w,w))] for x,w in zip(X,W)]
full=[[[powr(x,i) for i in range(4)]+[z]*7+[scale(w,-2)],[z]+[scale(mul(w,powr(x,i-1)),i) for i in range(1,4)]+[z]+[scale(powr(x,i-1),i) for i in range(1,7)]+[z]] for x,w in zip(X,W)]
def solve(rows):
 out=[]
 for row in rows:
  a=[];b=[]
  for u,v in row[:11]:a.extend([u,v*t0]);b.extend([v,u+v*t1])
  out.extend([a+[row[11][0]],b+[row[11][1]]])
 A,r=fmpq_mat(out).rref();piv=[]
 for i in range(r):
  c=next(j for j in range(23) if A[i,j])
  if c==22:return None
  piv.append(c)
 if r<22:return 'free'
 v=[Q(0)]*22
 for i,c in enumerate(piv):v[c]=A[i,22]
 return [(v[2*i],v[2*i+1]) for i in range(11)]
unique={};unresolved=[]
for rec in screen['accepted_systems']+screen['rank_exceptional_systems']:
 rows=[norm[j] for j in rec['subset']];sol=solve(rows)
 if sol=='free' and 'full_pair' in rec:sol=solve(rows+[row for j in rec['full_pair'] for row in full[j]])
 if sol=='free' and len(rec['subset'])==11:
  for pair in __import__('itertools').combinations(rec['subset'],2):
   ss=solve(rows+[row for j in pair for row in full[j]])
   if ss=='free':unresolved.append(dict(rec,full_pair=pair));continue
   if ss is None:continue
   key=tuple(tuple(map(str,a)) for a in ss);unique.setdefault(key,dict(rec,full_pair=pair))
  continue
 if sol=='free':unresolved.append(rec);continue
 if sol is None:continue
 if len(rec['subset'])==11:
  def satisfies(row):
   val=z
   for a,b in zip(row[:11],sol):val=add(val,mul(a,b))
   return val==row[11]
  good=[j for j in rec['subset'] if all(satisfies(row) for row in full[j])]
  if len(good)<2:continue
 key=tuple(tuple(map(str,a)) for a in sol);unique.setdefault(key,rec)
x=S.Symbol('x');theta=(-4175+55*S.sqrt(39))/7652;records=[];hits=[]
def sx(a):return S.Rational(str(a[0]))+S.Rational(str(a[1]))*theta
for key,origin in unique.items():
 v=[tuple(map(Q,a)) for a in key];E=[scale(a,Q(-1,2)) for a in v[:4]];J=[neg(a) for a in v[4:]]
 for i,a in enumerate(E):
  for j,b in enumerate(E):J[i+j]=add(J[i+j],mul(a,b))
 poly=S.Poly(sum(sx(a)*x**i for i,a in enumerate(J)),x,extension=S.sqrt(39));odd=0 if poly.is_zero else sum(f.degree() for f,e in poly.sqf_list()[1] if e%2)+(6-poly.degree())%2
 nh=[j for j in range(19) if add(add(mul(W[j],W[j]),mul(ev(v[:4],X[j]),W[j])),ev(v[4:],X[j]))==z]
 ff=[j for j in nh if ev(E,X[j])==W[j] and ev(J,X[j])==z]
 # For smooth selected fibers J=B O², a double zero of J is required at each full fiber.
 der=[scale(J[i],i) for i in range(1,7)];ff=[j for j in ff if ev(der,X[j])==z]
 rr={'B':key[:4],'C':key[4:],'binary_odd_degree':odd,'norm_hits':nh,'full_fibers':ff,'origin':origin}
 records.append(rr)
 if odd==2 and len(nh)+len(ff)>=13:hits.append(rr)
out={'field':'Q(theta), theta²+4175theta/3826+4525/15304=0','screen_systems':len(screen['accepted_systems']),'rank_exceptional_systems':len(screen['rank_exceptional_systems']),'exact_norms':len(unique),'unresolved':unresolved,'odd_degree_counts':{str(k):sum(r['binary_odd_degree']==k for r in records) for k in [0,2,4,6]},'hits':hits,'records':records,'seconds':time.monotonic()-start}
(P/'eleven_quadratic_norm_exact.json').write_text(json.dumps(out,indent=2));print({k:(len(v) if isinstance(v,list) else v) for k,v in out.items() if k!='records'})
