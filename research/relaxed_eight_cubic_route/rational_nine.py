from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json,time
P=Path(__file__).parent;s=json.loads((P/'rational_seed.json').read_text());xs=list(map(F,s['affine_nodes']));ys=list(map(F,s['affine_word']));ps=[tuple(map(F,c)) for c in s['affine_polynomials']];Q=tuple(map(F,s['fresh_affine']))
def ev(c,x):
 y=F(0)
 for a in c[::-1]:y=y*x+a
 return y
def interp(S,xs,ys):
 # Newton divided differences, then independent conversion to monomials.
 xx=[xs[i] for i in S];dd=[ys[i] for i in S]
 for j in range(1,4):
  for i in range(3,j-1,-1):dd[i]=(dd[i]-dd[i-1])/(xx[i]-xx[i-j])
 c=[dd[3]]
 for i in range(2,-1,-1):
  out=[F(0)]*(len(c)+1)
  for k,a in enumerate(c):out[k]-=xx[i]*a;out[k+1]+=a
  out[0]+=dd[i];c=out
 return tuple(c)
assert len(set(xs))==16
assert [[i for i,x in enumerate(xs) if ev(c,x)==ys[i]] for c in ps]==s['selected_supports']
# Check the projective-to-affine transform by binomial expansion.
from math import comb
for old,new in zip(s['projective_polynomials'],ps):
 old=list(map(F,old));out=[F(0)]*4
 for j,a in enumerate(old):
  for k in range(j+1):out[3-k]+=a*comb(j,k)*3**(j-k)
 assert tuple(out)==new
source={interp(S,xs,ys) for S in combinations(range(16),4)};hist={};nearest=[]
for c in source:
 a=sum(ev(c,x)==y for x,y in zip(xs,ys));hist[a]=hist.get(a,0)+1
 if a>=7:nearest.append(c)
assert set(nearest)==set(ps);assert Q in source
fresh=[]
for t in range(1,1000):
 x=F(t)
 if x in xs:continue
 if all(c==Q or ev(c,x)!=ev(Q,x) for c in source):fresh.append(x)
 if len(fresh)==2:break
assert len(fresh)==2
xx=xs+fresh;yy=ys+[ev(Q,x) for x in fresh]
allc={interp(S,xx,yy) for S in combinations(range(18),4)};hh={};nn=[]
for c in allc:
 a=sum(ev(c,x)==y for x,y in zip(xx,yy));hh[a]=hh.get(a,0)+1
 if a>=7:nn.append(c)
assert set(nn)==set(ps+[Q]);assert max(hh)==7
out={'arithmetic':'stdlib Fraction/Newton divided differences','source_subset_count':1820,'source_distinct_interpolants':len(source),'source_agreement_histogram':hist,'fresh_nodes':list(map(str,fresh)),'fresh_values':[str(ev(Q,x)) for x in fresh],'nodes':list(map(str,xx)),'word':list(map(str,yy)),'polynomials':[[str(a) for a in c] for c in ps+[Q]],'padded_subset_count':3060,'padded_distinct_interpolants':len(allc),'padded_agreement_histogram':hh,'maximum_agreement':7,'complete_nearest_list':9}
(P/'rational_nine.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ['nodes','word','polynomials']})
