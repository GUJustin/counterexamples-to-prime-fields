import json,itertools
from pathlib import Path
import numpy as np
p=97;nu=5
assert pow(nu,(p-1)//2,p)==p-1
# Encode a+b theta as a+p*b, theta^2=5.
def add(x,y):return ((x%p+y%p)%p)+p*((x//p+y//p)%p)
def neg(x):return (-x%p)+p*((- (x//p))%p)
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x%p,x//p;c,d=y%p,y//p
 return ((a*c+nu*b*d)%p)+p*((a*d+b*c)%p)
def ev(f,x):
 y=0
 for c in reversed(f):y=add(mul(y,x),c)
 return y
def deriv(f):return [(i*f[i])%p for i in range(1,len(f))]
def roots(x):
 for a in range(p):
  if a*a%p==x:return [a,(-a)%p]
 for a in range(p):
  if nu*a*a%p==x:return [p*a,p*((-a)%p)]
 raise AssertionError(x)
def pmul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return c
root=Path(__file__).parent
hit=json.loads((root/'hits.jsonl').read_text().splitlines()[0]);cert=json.loads((root/'independent_lift.json').read_text())[0]
a=hit['a'];alpha=hit['first_pole'];b=hit['new_pole'];assert hit['critical']==0
G=[]
for z in a:G.append(pmul([-alpha,0,1],[z*z%p,0,0,0,pow(z*z,-1,p)]))
G.append(cert['G5']);N=cert['N']
first_nodes=[];first_word=[]
for i,j in itertools.combinations(range(4),2):
 for y in (a[i]*a[j]%p,-a[i]*a[j]%p):
  for t in roots(y):
   assert t<p
   first_nodes.append(t);first_word.append((y-alpha)*(a[i]*a[i]+a[j]*a[j])%p)
for t in roots(alpha):
 assert t<p
 first_nodes.append(t);first_word.append(0)
for t in [24,52]:first_nodes.append(t);first_word.append(ev(G[4],t))
assert len(set(first_nodes))==28
old_matches=[[j for j,(t,v) in enumerate(zip(first_nodes,first_word)) if ev(g,t)==v] for g in G]
assert all(len(j)==14 for j in old_matches)
new_matches=[j for j,(t,v) in enumerate(zip(first_nodes,first_word)) if ev(N,t)==(t-b)*v%p]
assert len(new_matches)==14
H=[pmul([-b,0,1],sum(([c,0] for c in g[:-1]),[])+[g[-1]]) for g in G]
H.append(sum(([c,0] for c in N[:-1]),[])+[N[-1]])
assert all(len(h)<=15 for h in H) and len({tuple(h) for h in H})==6
nodes=[];word=[]
for t,v in zip(first_nodes,first_word):
 for u in roots(t):nodes.append(u);word.append((t-b)*v%p)
for u in roots(b):nodes.append(u);word.append(0)
for u in [0,1]:nodes.append(u);word.append(ev(H[5],u))
assert len(set(nodes))==60
selected=[]
for i in range(5):selected.append(sorted([2*j+k for j in old_matches[i] for k in (0,1)]+[56,57]))
selected.append(sorted([2*j+k for j in new_matches for k in (0,1)]+[58,59]))
assert all(len(s)==30 for s in selected)
assert all(ev(H[i],nodes[j])==word[j] for i in range(6) for j in selected[i])
fullmatches=[[j for j in range(60) if ev(H[i],nodes[j])==word[j]] for i in range(6)]
at=[[i for i in range(6) if j in selected[i]] for j in range(60)]
assert all(at)
rows=[]
for j,inds in enumerate(at):
 ref=inds[0];x=nodes[j];powers=[1]
 for k in range(14):powers.append(mul(powers[-1],x))
 for i in inds[1:]:
  row=[0]*150
  for k in range(15):row[15*i+k]=powers[k];row[15*ref+k]=neg(powers[k])
  row[90+j]=sub(ev(deriv(H[i]),x),ev(deriv(H[ref]),x));rows.append(row)
assert len(rows)==120
# Restriction of scalars: multiplication a+b theta is [[a,5b],[b,a]].
raw=np.array(rows,dtype=np.int64);aa=raw%p;bb=raw//p
M=np.block([[aa,(nu*bb)%p],[bb,aa]])
rank=0;pivots=[]
for col in range(300):
 cand=np.flatnonzero(M[rank:,col]%p)
 if len(cand)==0:continue
 i=rank+int(cand[0]);M[[rank,i]]=M[[i,rank]]
 M[rank]=(M[rank]*pow(int(M[rank,col]),-1,p))%p
 factors=M[:,col].copy();factors[rank]=0
 M=(M-factors[:,None]*M[rank][None,:])%p
 pivots.append(col);rank+=1
 if rank==240:break
assert rank%2==0
hist={str(i):sum(len(z)==i for z in at) for i in range(1,7)}
out={'p':p,'extension':'theta^2=5','first_domain':first_nodes,'first_word':first_word,'first_candidates':G,'new_numerator':N,'first_pole':alpha,'second_pole':b,'nodes':nodes,'word':word,'candidates':H,'selected_matches':selected,'all_match_counts':list(map(len,fullmatches)),'incidence_histogram':hist,'reduced_rows':120,'reduced_columns':150,'Fp_block_rank':rank,'F97_squared_rank':rank//2,'full_incidence_rank':rank//2+60,'raw_tangent_dimension':210-(rank//2+60),'block_pivot_columns':pivots}
(root/'six_bank_incidence.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:out[k] for k in ('all_match_counts','incidence_histogram','Fp_block_rank','F97_squared_rank','full_incidence_rank','raw_tangent_dimension')})
