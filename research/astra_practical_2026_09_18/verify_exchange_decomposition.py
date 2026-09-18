from itertools import combinations
from collections import Counter,defaultdict
from math import comb,prod
from pathlib import Path
import json

def check(p,m,r,h):
 domain=list(range(1,m+1))
 def sig(T):return tuple(sum(pow(x,j,p) for x in T)%p for j in range(1,h+1))+(prod(T)%p,)
 supports=list(combinations(domain,r)); fibers=Counter(map(sig,supports)); lhs=sum(v*v for v in fibers.values())
 layers=[];rhs=0
 for t in range(min(r,m-r)+1):
  banks=defaultdict(list)
  for T in combinations(domain,t):banks[sig(T)].append(frozenset(T))
  dt=sum(A.isdisjoint(B) for bank in banks.values() for A in bank for B in bank)
  assert t==0 or t>h+1 or dt==0
  contribution=dt*comb(m-2*t,r-t)
  layers.append({'t':t,'ordered_disjoint_equal_signature_pairs':dt,'contribution':contribution});rhs+=contribution
 assert lhs==rhs
 return {'p':p,'m':m,'r':r,'moments':h,'direct_collisions':lhs,'decomposed_collisions':rhs,'layers':layers}
r=[check(13,12,6,2),check(17,12,5,2),check(17,12,6,3)]
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'passed':len(r),'collision_counts':[x['direct_collisions'] for x in r]}))
