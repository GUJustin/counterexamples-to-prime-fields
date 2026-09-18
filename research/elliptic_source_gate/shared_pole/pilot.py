import json,time
from pathlib import Path
p=211;ell=5;start=time.monotonic();P=Path(__file__).parent
squares={y*y%p:[] for y in range(p)}
for y in range(p):squares[y*y%p].append(y)
for B in range(1,p):
 points=[(x,y) for x in range(p) for y in squares.get((x**3+B)%p,[])]+[None]
 if len(points)==225:break
else:raise Exception('no j0 curve')
A=0
def add(U,V):
 if U is None:return V
 if V is None:return U
 x,y=U;z,t=V
 if x==z and (y+t)%p==0:return None
 slope=((t-y)*pow(z-x,-1,p) if x!=z else (3*x*x+A)*pow(2*y,-1,p))%p
 xx=(slope*slope-x-z)%p;return(xx,(slope*(x-xx)-y)%p)
def mul(U,n):
 V=None
 while n:
  if n&1:V=add(V,U)
  U=add(U,U);n//=2
 return V
H=[T for T in points if mul(T,5) is None];assert len(H)==25
U=next(T for T in H if T is not None);span={mul(U,a) for a in range(5)};V=next(T for T in H if T not in span)
lab={(a,b):add(mul(U,a),mul(V,b)) for a in range(5) for b in range(5)};assert set(lab.values())==set(H)
nu=2
def chi(t):t%=5;return 0 if t==0 else (1 if pow(t,2,5)==1 else -1)
c={T:chi(T[0]**2-nu*T[1]**2) for T in lab}
def plus(S,T):return((S[0]+T[0])%5,(S[1]+T[1])%5)
def neg(S):return((-S[0])%5,(-S[1])%5)
reps=sorted(T for T in lab if T<=neg(T));nonzero=[T for T in reps if T!=(0,0)];assert len(reps)==13 and len(nonzero)==12
for T in lab:assert sum(c[S]*c[plus(T,neg(S))] for S in lab)==(24 if T==(0,0) else -1)
def pmul(a,b):
 z=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%p
 return z
def ev(a,x):
 z=0
 for t in a[::-1]:z=(z*x+t)%p
 return z
D=[1];factors=[]
for T in nonzero:
 t=lab[T][0];f=[t*t%p,-2*t%p,1];factors.append(f);D=pmul(D,f)
assert len(D)==25
polys=[]
for S in reps:
 q=[0]*26
 for i,a in enumerate(D):q[i+1]=2*c[S]*a%p
 for j,T in enumerate(nonzero):
  coeff=c[plus(T,neg(S))]+c[plus(T,S)];t=lab[T][0];num=[2*(A*t+2*B)%p,2*(t*t+A)%p,2*t%p];quot=[1]
  for k,f in enumerate(factors):
   if k!=j:quot=pmul(quot,f)
  f=pmul(quot,num)
  for i,a in enumerate(f):q[i]=(q[i]+coeff*a)%p
 polys.append(q)
assert len(set(map(tuple,polys)))==13;assert all(sum((1 if i==0 else 2)*q[j] for i,q in enumerate(polys))%p==0 for j in range(26))
# Verify direct elliptic evaluation at every nonpole finite rational point.
poles={lab[T][0] for T in nonzero};domain=sorted({T[0] for T in points if T is not None});off=[x for x in domain if x not in poles]
for x in off:
 pt=next(T for T in points if T is not None and T[0]==x)
 for S,q in zip(reps,polys):
  total=0
  for T in lab:
   for sign in [S,neg(S)]:
    Z=add(pt,lab[plus(T,sign)]);assert Z is not None;total+=c[T]*Z[0]
  assert ev(q,x)==ev(D,x)*total%p
records=[]
for x in domain:
 vals=[ev(q,x) for q in polys];buckets={}
 for i,v in enumerate(vals):buckets.setdefault(v,[]).append(i)
 records.append({'x':x,'pole':x in poles,'values':vals,'buckets':[[v,ids] for v,ids in buckets.items()],'max_bucket':max(map(len,buckets.values()))})
order=sorted(records,key=lambda r:(-r['max_bucket'],r['x']));selected=order[:100];top=sum(r['max_bucket'] for r in selected);counts=[0]*13
for r in selected:
 b=min((b for b in r['buckets'] if len(b[1])==r['max_bucket']),key=lambda b:b[0]);r['greedy_word']=b[0]
 for i in b[1]:counts[i]+=1
hist={}
for r in records:hist[r['max_bucket']]=hist.get(r['max_bucket'],0)+1
allfield=[]
for x in range(p):
 vals=[ev(q,x) for q in polys];allfield.append(max(vals.count(v) for v in set(vals)))
allfield.sort(reverse=True)
out={'offpole_incidence_sum':sum(r['max_bucket'] for r in records if not r['pole']),'all_field_top100_incidence_sum':sum(allfield[:100]),'all_field_total_incidence_sum':sum(allfield),'p':p,'ell':ell,'curve_A':A,'curve_B':B,'point_count':len(points),'torsion_count':len(H),'torsion_basis':[U,V],'labels':reps,'torsion_label_points':[[list(T),lab[T]] for T in lab],'coefficients':polys,'degrees':[max(i for i,a in enumerate(q) if a) for q in polys],'finite_x_domain':len(domain),'offpole_domain':len(off),'bucket_histogram':hist,'top100_incidence_sum':top,'upper_min_agreement':top//13,'greedy_counts':counts,'records':records,'seconds':time.monotonic()-start}
(P/'pilot.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ['torsion_label_points','coefficients','records']})
