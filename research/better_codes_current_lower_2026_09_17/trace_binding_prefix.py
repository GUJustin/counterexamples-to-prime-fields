"""Trace the actual target prefix bottleneck through phases into packing."""
import ast,json
import replay_ledger as q
state=json.loads((q.CACHE/'regenerated_target_state.json').read_text());q.POT=[tuple(x) for x in state['pot']];q.rows={(r,v):row for r,v,row in state['rows']};state.clear()
tree=ast.parse((q.ROOT/'repeat_phases.py').read_text().replace('9275','9678').replace('9276','9679'));exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in {'pieces','candidates'}],type_ignores=[]),'repeat_phases.py','exec'))
chain=[];r,v,j=17,45,31
while True:
 value=q.rows[r,v]['prefixValues'][j]
 origin=min((rr,vv) for (rr,vv),row in q.rows.items() if rr<=r and vv<=v and row['prefixValues'][j]==value)
 r,v=origin;row=q.rows[r,v];finish=min(row['threshold'][j],9679-r-v);cuts=sorted(pieces(r,v,row,finish,j));events=[]
 for lo,stop in zip(cuts,cuts[1:]):
  if lo>=stop:continue
  pts,lines=candidates(r,v,row,lo,stop-1,j)
  for z in pts:
   candidates2=[(q.line(r,v,z,w),w) for w in range(j+1) if w==0 or row['threshold'][w-1]<=z]
   cap,w=min(candidates2);needed=cap-q.potential(r,v,z,j)
   events.append((needed,z,w,cap))
 needed,z,w,cap=max(events);assert needed==value,(r,v,j,needed,value)
 chain.append(dict(r=r,v=v,phase=j+1,prefix=value,z=z,winning_witness=w,cap=cap,potential=q.potential(r,v,z,j)))
 if w==0:break
 r-=1;j=w-1
own={}
for lo,hi in [(1,12),(13,36)]:
 data=json.loads((q.ROOT/f'regenerated_singletons_{lo}_{hi}.json').read_text())
 for row in data['rows']:own[row['r'],row['v']]=row['own']
slopes=data['slopes'];packs=[]
for sheet,slope in enumerate(slopes):
 dp=[[0]*(v+1) for _ in range(r+1)];arg={}
 for rr in range(1,r+1):
  for vv in range(v+1):
   val,split=max((own[a,b][sheet]+dp[rr-a][vv-b],(a,b)) for a in range(1,rr+1) for b in range(vv+1))
   dp[rr][vv]=val;arg[rr,vv]=split
 packs.append((slope*z+dp[r][v],sheet,dp,arg))
 cap,sheet,dp,arg=min(packs,key=lambda x:x[0]);assert cap==q.base(q.rows[r,v],z)
rr,vv=r,v;components=[]
while rr:
 a,b=arg[rr,vv];components.append(dict(r=a,v=b,own=own[a,b][sheet]));rr-=a;vv-=b
out=dict(phase_chain=chain,base=dict(r=r,v=v,z=z,cap=cap,sheet=sheet,slope=slopes[sheet],packing_intercept=dp[r][v],components=components,unused_v=vv))
(q.ROOT/'binding_prefix_trace.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
