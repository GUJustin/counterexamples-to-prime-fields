"""Independent Fraction/Newton interpolation and quadratic quotient arithmetic."""
import json,itertools,time
from pathlib import Path
from fractions import Fraction as F
D=Path(__file__).parent;start=time.monotonic();s=json.loads((D/'rational_seed.json').read_text())
X=list(map(F,s['affine_nodes']));W=list(map(F,s['affine_word']));seen={}
def ev(c,x):
 r=F(0)
 for a in reversed(c):r=r*x+a
 return r
for sub in itertools.combinations(range(16),4):
 xs=[X[i] for i in sub];dd=[W[i] for i in sub]
 for k in range(1,4):
  for j in range(3,k-1,-1):dd[j]=(dd[j]-dd[j-1])/(xs[j]-xs[j-k])
 c=[dd[3]]
 for k in range(2,-1,-1):
  o=[F(0)]*(len(c)+1)
  for j,a in enumerate(c):o[j]-=xs[k]*a;o[j+1]+=a
  o[0]+=dd[k];c=o
 key=tuple(c)
 if key not in seen:seen[key]=[j for j,x in enumerate(X) if ev(c,x)==W[j]]
old={c:hit for c,hit in seen.items() if len(hit)>=5}
assert len(old)==16 and max(map(len,seen.values()))==7
Q=list(map(F,[0,-9,-34,-32]));g=[F(-25),F(125),F(358)]
def rem(c):
 r=list(c)
 while len(r)>2:
  a=r.pop()/g[2];r[-1]-=a*g[1];r[-2]-=a*g[0]
 return tuple(r+[F(0)]*(2-len(r)))
wr=rem(Q);assert wr==(F(-51075,32041),F(-104594,32041))
assert all(ev(g,x)!=0 for x in X)
assert 125**2+4*358*25==55**2*17
hits=[];summary=[]
for c,ss in sorted(old.items()):
 rr=rem([a-b for a,b in zip(c,Q)]);new=2 if rr==(0,0) else 0
 summary.append(dict(coefficients=list(map(str,c)),old_support=ss,new_matches=new,total=len(ss)+new,remainder=list(map(str,rr))))
 if len(ss)+new>=7:hits.append(c)
assert len(hits)==10 and max(r['total'] for r in summary)==7
assert sum(r['new_matches']==2 for r in summary)==2
known={tuple(map(F,c)) for c in s['affine_polynomials']}
assert known<=set(hits) and all(len(old[c])==5 for c in set(hits)-known)
ref=json.loads((D/'ten_cubic_certificate.json').read_text())
assert set(hits)-known=={tuple(map(F,c)) for c in ref['new_candidate_coefficients']}
out=dict(pass_all=True,four_subsets=1820,distinct_interpolants=len(seen),old_ge5_count=len(old),complete_list_size=10,maximum_agreement=7,fresh_word_remainder=list(map(str,wr)),quadratic_discriminant=51425,all_old_ge5=summary,seconds=time.monotonic()-start)
(D/'ten_cubic_certificate.verified.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='all_old_ge5'})
