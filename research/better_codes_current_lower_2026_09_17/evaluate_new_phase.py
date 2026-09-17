"""All-context finite new-source diagnostic with target31 incumbent base frozen."""
import ast,json,sys
import replay_ledger as q
# Reuse the exact helpers without executing their experiment entry points.
for filename,names in [('repeat_phases.py',{'pieces','candidates'}),('search_new_phase.py',{'channel','threshold','potential'})]:
    tree=ast.parse((q.ROOT/filename).read_text())
    module=ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names],type_ignores=[])
    exec(compile(module,filename,'exec'))
A=181275;n=262144;w=131071;delta=A-w+1
index=int(sys.argv[1]);refined='--refined' in sys.argv
grid='new_phase_refined_grid.json' if refined else 'new_phase_grid.json'
cand=json.loads((q.ROOT/grid).read_text())['best'][index]
state=json.loads((q.CACHE/'target31_state.json').read_text());q.POT=[tuple(x) for x in state['pot']]
q.rows={(r,v):row for r,v,row in state['rows']};phase=len(q.POT);q.POT.append(tuple(cand['potential']))
for (r,v),row in q.rows.items():
    row['threshold'].append(threshold(cand['L'],cand['Y'],cand['s'],cand['gap'],r,v))
    row['prefixValues'].append(0)
prefix_origins={}
for (r,v),row in sorted(q.rows.items()):
    parent=q.rows.get((r-1,v),{}).get('prefixValues',[0]*len(q.POT))
    previous=q.rows.get((r,v-1),{}).get('prefixValues',[0]*len(q.POT))
    finish=min(row['threshold'][phase],9276-r-v);needed=0
    cuts=sorted(pieces(r,v,row,finish,phase))
    for lo,stop in zip(cuts,cuts[1:]):
        if lo>=stop:continue
        points,lines=candidates(r,v,row,lo,stop-1,phase)
        for z in points:needed=max(needed,min(a*z+b for a,b in lines)-q.potential(r,v,z,phase))
    row['prefixValues'][phase]=max(needed,parent[phase],previous[phase])
    origin=[r,v,needed]
    if parent[phase]>needed:origin=prefix_origins[r-1,v]
    if previous[phase]>max(needed,parent[phase]):origin=prefix_origins[r,v-1]
    prefix_origins[r,v]=origin
worst=[];failed=0
for (r,v),row in sorted(q.rows.items()):
    finish=9276-r-v;cuts=pieces(r,v,row,finish,len(q.POT))
    for cut in [9275-r-v-(185-r-v),9275-r-v-min(185-r-v,40-r)]:
        for z in [cut,cut+1]:
            if 0<=z<=finish:cuts.add(z)
    for aa,bb,sign,offset in [(*q.unit_coeff(r+v,r),1,r+v),(*q.unit_coeff(185-r-v,40-r),-1,18992-r-v)]:
        if aa:
            cut=sign*((9000000000000-bb)//aa-offset)
            for z in [cut-1,cut,cut+1]:
                if 0<=z<=finish:cuts.add(z)
    cuts=sorted(cuts);best=-1;loc=None
    for lo,stop in zip(cuts,cuts[1:]):
        if lo>=stop:continue
        points,lines=candidates(r,v,row,lo,stop-1,len(q.POT))
        for z in points:
            cap=min(a*z+b for a,b in lines);t=9275-r-v-z
            complement=8728330260*t+7635583765037*min(t,185-r-v)+35730343721378*min(t,185-r-v,40-r)
            value=cap+complement+r*q.unit(r+v,r+v+z,r)+(40-r)*q.unit(185-r-v,18992-r-v-z,40-r)+18000000000000+1057030663884726
            if value>best:best=value;loc=[r,v,z]
    failed+=best>q.BOUND
    worst.append(dict(location=loc,total=best,margin=q.BOUND-best))
result=dict(candidate=cand,binding_parent_prefix_origin=prefix_origins[34,124],failed_rows=failed,worst=sorted(worst,key=lambda x:x['margin'])[:20],binding_new_source_charge=q.line(35,124,9090,phase+1),scope='Exact32-phase target diagnostic with incumbent base/complement/chain/box frozen. NOT a complete valid certificate.')
stem=f'new_phase_{"refined_" if refined else ""}finalist_{index}'
(q.ROOT/f'{stem}_all_rows.json').write_text(json.dumps(worst,indent=2)+'\n')
(q.CACHE/f'{stem}_state.json').write_text(json.dumps(dict(pot=q.POT,rows=[[r,v,row] for (r,v),row in q.rows.items()])))
(q.ROOT/f'{stem}.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
