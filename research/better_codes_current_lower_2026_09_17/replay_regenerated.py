"""Rebuild target singleton packing and phases; primary B/chain initially frozen."""
import json
import numpy as np
import replay_ledger as q
A=181275;n=262144;w=131071;TOTAL=9678
q.BOUND=json.loads((q.ROOT/'protocol_target_budget.json').read_text())['target_mca_allowance']
pot=json.loads((q.ROOT/'expanded_total_all_contexts.json').read_text())['potentials'];q.POT=[tuple(x) for x in pot]
loaded={}
for lo,hi in [(1,12),(13,36)]:
 data=json.loads((q.ROOT/f'regenerated_singletons_{lo}_{hi}.json').read_text())
 for row in data['rows']:loaded[row['r'],row['v']]=row
slopes=data['slopes'];assert len(loaded)==5238
sheets=[];pairs=0
for j,slope in enumerate(slopes):
 own={r:[loaded[r,v]['own'][j] for v in range(164-r)] for r in range(1,37)}
 packed={r:np.zeros(164-r,dtype=np.int64) for r in range(37)}
 for R in range(1,37):
  out=packed[R]
  for rr in range(1,R+1):
   right=packed[R-rr]
   for u,a in enumerate(own[rr][:len(out)]):
    count=min(len(right),len(out)-u)
    np.maximum(out[u:u+count],a+right[:count],out=out[u:u+count]);pairs+=count
  assert np.max(out)<2**62
 sheets.append((slope,{r:a.tolist() for r,a in packed.items()}))
 print('packing sheet',j,'done',flush=True)
q.rows={};schedule=list(range(7))+[3,4,5]+list(range(7))*3
for (r,v),row in loaded.items():
 lines=[(slope,packed[r][v]) for slope,packed in sheets];finish=TOTAL+1-r-v;breaks={3,finish}
 for k,(a,b) in enumerate(lines):
  for aa,bb in lines[:k]:
   if a!=aa:
    cross=(bb-b)//(a-aa)
    breaks.update(x for x in [cross,cross+1,cross+2] if 3<=x<finish)
 seg=[]
 for z in sorted(breaks-{finish}):
  a,b=min(lines,key=lambda ab:ab[0]*z+ab[1])
  if not seg or a!=seg[-1][2]:seg.append([z,a*z+b,a])
 ts=row['threshold']
 q.rows[r,v]=dict(base=[r,v,*[min(a*z+b for a,b in lines) for z in range(3)],seg],threshold=[ts[j] for j in schedule]+[ts[-1]],prefixValues=[0]*32)
cy,cr,cz=1+2*w*185,w*79,1+2*w*TOTAL
L,Y,S=176421,163,36
terms=[((n-w)*(cy*S+cr*Y),0),((n-w)*(cr*L+cz*S),(n-A+1)*S),((n-w)*(cy*L+cz*Y),(n-A+1)*Y)]
new_complement=[(a+A-w-1)//(A-w)+b for a,b in terms]
pair_overhead=json.loads((q.ROOT/'expanded_total_context_construction.json').read_text())['pair_overhead']
old_prefix={key:row['prefixValues'][:] for key,row in q.rows.items()}
body=(q.ROOT/'expanded_A_old_slice.py').read_text().split('def breakpoints')[1]
body=('def breakpoints'+body).replace('9275','9678').replace('9276','9679').replace('1057030663884726',str(pair_overhead))
body=body.replace("q.ROOT/'expanded_A_old_slice.json'","q.ROOT/'regenerated_target_ledger.json'")
body=body.replace("Only old4970 contexts tested; base/chain/B/TCap and auxiliary sources frozen. NOT a certificate;268 extra contexts excluded.","All5238 contexts,total9678; allsingletons rebuilt from repaired27auxiliary sources,8phase sources,target-validcarrier;8Bellman sheets and32phases rebuilt. A/TCap/scalarrepaired;B/chain stillincumbent. NOT a complete certificate.")
exec(body)
empty_charge=new_complement[0]*TOTAL+new_complement[1]*185+new_complement[2]*40+40*q.unit(185,18992,40)+18000000000000+pair_overhead
assert empty_charge<=q.BOUND
(q.ROOT/'regenerated_target_all_rows.json').write_text(json.dumps(worst,indent=2)+'\n')
(q.ROOT/'regenerated_target_packing.json').write_text(json.dumps(dict(contexts=5238,empty_charge=empty_charge,bellman_pairs=pairs,slopes=slopes,budget=q.BOUND,scope='All8packing sheets rebuilt from regenerated target singleton envelopes; primaryB/chain not yet repaired.'),indent=2)+'\n')
(q.CACHE/'regenerated_target_state.json').write_text(json.dumps(dict(pot=q.POT,rows=[[r,v,row] for (r,v),row in q.rows.items()])))
