"""Exhaust the complete above-capacity profile of one quadratic-tower fixture."""
from itertools import combinations
from collections import Counter
from math import comb,isqrt
from pathlib import Path
import json
from verify import interpolate,evaluate
BASE=Path(__file__).resolve().parent

def roots(a,p):
 a%=p
 if not a or pow(a,(p-1)//2,p)!=1:return []
 x=pow(a,(p+1)//4,p)
 assert x*x%p==a
 return sorted((x,p-x))

def profile(xs,ys,k,p):
 seen=set();hist=Counter();high={}
 for I in combinations(range(len(xs)),k):
  c=interpolate([xs[i] for i in I],[ys[i] for i in I],p)
  if c in seen:continue
  seen.add(c);a=sum(evaluate(c,x,p)==y for x,y in zip(xs,ys))
  hist[a]+=1
  if a>k:high[c]=a
 return hist,high,len(seen)

def main():
 p=1000000007;assert p%4==3 and all(p%d for d in range(2,isqrt(p)+1))
 source=[-2,-1,0,1,2];word=[2,1,0,1,2]
 t1=next(t for t in range(100000) if all(roots(t+a,p) for a in source))
 middle=[];middle_word=[]
 for a,w in zip(source,word):middle+=roots(t1+a,p);middle_word += [w]*2
 t2=next(t for t in range(100000) if all(roots(t+a,p) for a in middle))
 nodes=[];received=[]
 for a,w in zip(middle,middle_word):nodes+=roots(t2+a,p);received += [w]*2
 assert len(set(nodes))==20
 H=[(t2*t2-t1)%p,0,-2*t2%p,0,1,0,0,0]
 assert all(evaluate(H,x,p)==source[i//4]%p for i,x in enumerate(nodes))
 hist,high,total=profile(nodes,received,8,p)
 expected={tuple(H):12,tuple(-a%p for a in H):12}
 assert high==expected,(hist,high)
 # Each possible extra codeword above dimension8 is determined by an
 # eight-node support, all125970 of which were enumerated.
 out=dict(status='passed',p=p,t1=t1,t2=t2,n=20,dimension=8,
  cover_polynomial=H,determining_supports=comb(20,8),distinct_interpolants=total,
  agreement_histogram=dict(sorted(hist.items())),complete_above_capacity_list=[
   dict(coefficients=c,agreement=a) for c,a in sorted(high.items())],
  scope='One exact finite specialization verifies the entire above-capacity profile; the all-scales theorem is proved separately.')
 (BASE/'profile_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
