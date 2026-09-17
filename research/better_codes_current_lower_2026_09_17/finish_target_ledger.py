"""Apply repaired B, derivative chain, tail, and protocol budgets to target state."""
import ast,json
import replay_ledger as q
import repaired_primary_chain as chain
q.BOUND=json.loads((q.ROOT/'protocol_target_budget.json').read_text())['target_mca_allowance']
state=json.loads((q.CACHE/'regenerated_target_state.json').read_text());q.POT=[tuple(x) for x in state['pot']];q.rows={(r,v):row for r,v,row in state['rows']};state.clear()
tree=ast.parse((q.ROOT/'repeat_phases.py').read_text().replace('9275','9678').replace('9276','9679'));exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in {'pieces','candidates'}],type_ignores=[]),'repeat_phases.py','exec'))
profiles=[(185,40,22192),(189,42,18812)]
outputs=[]
for B in profiles:
 Y,R,L=B;worst=[];failed=0
 for (r,v),row in sorted(q.rows.items()):
  y=r+v;finish=9679-y;cuts=pieces(r,v,row,finish,len(q.POT))
  for cut in [9678-y-(Y-y),9678-y-min(Y-y,R-r)]:
   for z in [cut-1,cut,cut+1]:
    if 0<=z<=finish:cuts.add(z)
  for aa,bb,sign,offset in [(*chain.unit_coeff(y,r),1,y),(*chain.unit_coeff(Y-y,R-r),-1,L-y)]:
   if aa:
    cut=sign*((chain.TAIL_ALLOWANCE-bb)//aa-offset)
    for z in [cut-1,cut,cut+1]:
     if 0<=z<=finish:cuts.add(z)
  best=-1;location=None
  cuts=sorted(cuts)
  for lo,stop in zip(cuts,cuts[1:]):
   if lo>=stop:continue
   points,lines=candidates(r,v,row,lo,stop-1,len(q.POT))
   for z in points:
    value=min(a*z+b for a,b in lines)+chain.ledger_overhead(r,y,y+z,B=B)
    if value>best:best=value;location=[r,v,z]
  failed+=best>q.BOUND;worst.append(dict(location=location,total=best,margin=q.BOUND-best))
 worst.sort(key=lambda x:x['margin']);r,v,z=worst[0]['location'];row=q.rows[r,v]
 witnesses=[(q.line(r,v,z,j),j) for j in range(len(q.POT)+1) if j==0 or row['threshold'][j-1]<=z]
 charge,j=min(witnesses);prefix=q.rows[r-1,v]['prefixValues'][j-1] if j else None
 origins=[]
 if j:
  origins=[[rr,vv] for (rr,vv),p in q.rows.items() if rr<=r-1 and vv<=v and p['prefixValues'][j-1]==prefix]
  origins=sorted(origins,key=lambda x:(sum(x),x))[:10]
 empty=chain.ledger_overhead(0,0,0,B=B)
 out=dict(B=B,budget=q.BOUND,failed_rows=failed,empty_charge=empty,worst=worst[:20],binding_phase=j,binding_phase_charge=charge,binding_prefix=prefix,earliest_prefix_origins=origins,scope='Numerical target pipeline with repairedA/TCap/B/scalar/auxiliary/carrier,8packing sheets,32phases andtargetchain. Complete algebraic target port and independent allgates audit stillrequired; no certificate/score claim.')
 outputs.append(out)
 (q.ROOT/f'target_B_{Y}_{R}_{L}_all_rows.json').write_text(json.dumps(worst,indent=2)+'\n')
(q.ROOT/'target_repaired_B_ledger.json').write_text(json.dumps(outputs,indent=2)+'\n')
print(json.dumps(outputs,indent=2))
