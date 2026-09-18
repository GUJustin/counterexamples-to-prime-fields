"""Two cost-selected m3 shapes, each below its sum of local ranks."""
import json,time
from pathlib import Path
from math import comb
from flint import fmpq as Q,fmpq_mat
P=Path(__file__).parent;start=time.monotonic();d=json.loads((P/'three_graph_gate.json').read_text());xs=list(map(Q,d['nodes']));ys=list(map(Q,d['word']));out=[]
for q,s in [(2,1),(2,2)]:
 cols=[(a,i,j) for j in range(s+1) for i in range(q-j+1) for a in range(max(12-2*i-j,0))];terms=[];keys=set()
 for a,i,j in cols:
  cc=[]
  for u in range(min(i,2)+1):
   for v in range(min(i-u,(2-u)//2)+1):
    for h in range(min(a,2-u-2*v)+1):
     key=(h+u+2*v,j+u,v);cc.append((key,comb(a,h)*comb(i,u)*comb(i-u,v),a-h,i-u-v));keys.add(key)
  terms.append(cc)
 keys=sorted(keys);ix={key:i for i,key in enumerate(keys)}
 for control in [0,1,2]:
  word=ys[:] if control<2 else list(map(Q,[2,3,5,7,11,13]))
  if control==1:word[0]+=1
  rows=[[Q(0)]*len(cols) for _ in range(len(xs)*len(keys))]
  for c,cc in enumerate(terms):
   for key,coef,a,i in cc:
    for k,(x,y) in enumerate(zip(xs,word)):rows[k*len(keys)+ix[key]][c]+=coef*x**a*y**i
  _,rank=fmpq_mat(rows).rref();_,local=fmpq_mat(rows[:len(keys)]).rref();result={'m':3,'q':q,'s':s,'columns':len(cols),'local_rank':local,'sum_local_ranks':6*local,'control':control,'rank':rank,'nullity':len(cols)-rank};out.append(result);print(result)
(P/'m3_three_graph_gate.json').write_text(json.dumps({'cases':out,'seconds':time.monotonic()-start},indent=2))
