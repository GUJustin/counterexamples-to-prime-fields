"""Build conditional new contexts for primary A box(r36,y163), total9275.

Old singleton and base receipts are deliberately frozen. New singleton bounds
use actual target phase source routes. Extends the eight Bellman tables exactly.
"""
import ast,json,re
from pathlib import Path
# Execute only initialization of the expanded old-slice diagnostic.
ROOT=Path(__file__).parent
exec((ROOT/'expanded_A_old_slice.py').read_text().split('def breakpoints')[0])
TOTAL=9678
q.rows={key:{name:row[name] for name in ['base','threshold','prefixValues']} for key,row in q.rows.items()}
state.clear()
import numpy as np
cy,cr,cz=1+2*w*163,w*71,1+2*w*TOTAL
q.POT=[]
for L,Y,S,g in sources:
 terms=[((n-w)*(cy*S+cr*Y),0),((n-w)*(cr*L+cz*S),(n-A+1)*S),((n-w)*(cy*L+cz*Y),(n-A+1)*Y)]
 q.POT.append(tuple((a+A-w-1)//(A-w)+b for a,b in terms))
cy,cr=1+2*w*185,w*79
L,Y,S=176421,163,36
terms=[((n-w)*(cy*S+cr*Y),0),((n-w)*(cr*L+cz*S),(n-A+1)*S),((n-w)*(cy*L+cz*Y),(n-A+1)*Y)]
new_complement=[(a+A-w-1)//(A-w)+b for a,b in terms]
def pair_charge(A,L):
 leftY,leftR,leftZ,rightY,rightR,rightZ=185,40,18992,312,70,L
 agreement=[max(1+2*w*leftY,1+2*w*rightY),max(w*(2*leftR-1),w*(2*rightR-1)),max(2*w*leftZ+1,2*w*rightZ+1)]
 mixed=[leftR*rightZ+leftZ*rightR,leftY*rightZ+leftZ*rightY,leftY*rightR+leftR*rightY]
 return ((n-w)*sum(a*b for a,b in zip(agreement,mixed))+(n-A+1)*(A-w)*mixed[2])//(A-w)
assert pair_charge(181284,9281)==1057030663884726
pair_overhead=pair_charge(A,9682)

for filename,names in [('search_new_phase.py',{'channel','threshold'}),('repeat_phases.py',{'pieces','candidates'})]:
 tree=ast.parse((ROOT/filename).read_text().replace('9275','9678').replace('9276','9679'));exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names],type_ignores=[]),filename,'exec'))
delta=A-w+1
unique=base_sources+[[new['L'],new['Y'],new['s'],new['gap']]]
unique_pot=q.POT[:7]+q.POT[-1:]
newkeys=[(r,v) for r in range(1,37) for v in range(164-r) if (r,v) not in q.rows]
assert len(newkeys)==268
thresholds={}
allkeys=[(r,v) for r in range(1,37) for v in range(164-r)]
for r,v in allkeys:
 old=q.rows.get((r,v))
 if old:
  previous=old['threshold'][:7]+old['threshold'][-1:]
  ts=[threshold(L,Y,S,g,r,v) if previous[j]>=9276-r-v else previous[j] for j,(L,Y,S,g) in enumerate(unique)]
  old['threshold']=[ts[j] for j in schedule]+[ts[-1]]
 else:ts=[threshold(L,Y,S,g,r,v) for L,Y,S,g in unique]
 assert min(ts)==0 or old,('no singleton route at zero',r,v,ts)
 thresholds[r,v]=ts

def own_bound(r,v,slope,start=0):
 ts=thresholds[r,v];finish=9679-r-v
 cuts=sorted({start,finish}|{t for t in ts if start<t<finish});answer=0
 for lo,stop in zip(cuts,cuts[1:]):
  hi=stop-1;lines=[(a,a*(r+v)+b*(r+v)+c*r) for j,(a,b,c) in enumerate(unique_pot) if ts[j]<=lo]
  points={lo,hi}
  for k,(a,b) in enumerate(lines):
   for aa,bb in lines[:k]:
    if a!=aa:
     cross=(bb-b)//(a-aa)
     points.update(x for x in [cross,cross+1] if lo<=x<=hi)
  for z in points:answer=max(answer,min(a*z+b for a,b in lines)-slope*z)
 return answer

sheets=[];new_own_count=0;packing_pairs=0
for j in range(8):
 text=(q.CACHE/f'MovingFiberPackingData6811S{j}.lean').read_text()
 slope=int(re.search(r'def slope : Nat := (\d+)',text)[1]);own={};packed={}
 for typ,r,nums in re.findall(r'def (own|packed)(\d+) : Array Nat := #\[([^\]]*)\]',text):
  (own if typ=='own' else packed)[int(r)]=[int(a) for a in nums.split(',')]
 for r in range(1,37):
  own.setdefault(r,[]);packed.setdefault(r,[])
  for v in range(164-r):
   if v<len(own[r]):own[r][v]=max(own[r][v],own_bound(r,v,slope,9276-r-v))
   else:own[r].append(own_bound(r,v,slope))
   new_own_count+=1
  packed[r]+=[0]*(164-r-len(packed[r]))
 packed[0]+=[0]*(164-len(packed[0]))
 arrays={r:np.array(a,dtype=np.int64) for r,a in packed.items()}
 for R in range(1,37):
  out=arrays[R]
  for rr in range(1,R+1):
   right=arrays[R-rr]
   for u,a in enumerate(own[rr][:len(out)]):
    count=min(len(right),len(out)-u)
    np.maximum(out[u:u+count],a+right[:count],out=out[u:u+count]);packing_pairs+=count
  assert np.max(out)<2**62
 packed={r:a.tolist() for r,a in arrays.items()}
 sheets.append((slope,own,packed))
 print('extended packing sheet',j,flush=True)

for r,v in allkeys:
 lines=[(slope,packed[r][v]) for slope,own,packed in sheets]
 finish=9679-r-v;breaks={3,finish}
 for k,(a,b) in enumerate(lines):
  for aa,bb in lines[:k]:
   if a!=aa:
    cross=(bb-b)//(a-aa)
    breaks.update(x for x in [cross,cross+1,cross+2] if 3<=x<finish)
 seg=[]
 for z in sorted(breaks-{finish}):
  a,b=min(lines,key=lambda ab:ab[0]*z+ab[1])
  if not seg or a!=seg[-1][2]:seg.append([z,a*z+b,a])
 ts=thresholds[r,v]
 q.rows[r,v]=dict(base=[r,v,*[min(a*z+b for a,b in lines) for z in range(3)],seg],threshold=[ts[j] for j in schedule]+[ts[-1]],prefixValues=[0]*32)
assert len(q.rows)==5238
# Run the same complete prefix and ledger propagation, with the new rows included.
body=(ROOT/'expanded_A_old_slice.py').read_text().split('def breakpoints')[1]
body=('def breakpoints'+body).replace('9275','9678').replace('9276','9679').replace('1057030663884726',str(pair_overhead))
body=body.replace("q.ROOT/'expanded_A_old_slice.json'","q.ROOT/'expanded_total_all_contexts.json'")
body=body.replace("Only old4970 contexts tested; base/chain/B/TCap and auxiliary sources frozen. NOT a certificate;268 extra contexts excluded.","All5238 contexts through total9678; old singleton allowances below9275 frozen, tails/newcontexts constructed and fullpacking rebuilt. TCap9682/total9678 and newA complement/pair overhead; oldB/chain/auxiliary inputs frozen. NOT a certificate.")
exec(body)
(ROOT/'expanded_total_context_construction.json').write_text(json.dumps(dict(new_contexts=len(newkeys),new_singleton_bounds=new_own_count,packing_pairs=packing_pairs,all_new_contexts_have_source_threshold_zero=True,total_cap=TOTAL,pair_overhead=pair_overhead,scope='New contexts use target source potentials and exact packing extension; old singleton/base inputs remain frozen.'),indent=2)+'\n')
