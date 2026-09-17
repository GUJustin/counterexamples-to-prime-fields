"""Finite added phase cycles, incumbent A and sources; arithmetic experiment."""
import json,sys
import replay_ledger as q
target='--target' in sys.argv
if target:
    import target_phase_diagnostic  # Rebuild target state, frozen incumbent base.
cycles=int(sys.argv[1]) if len(sys.argv)>1 else 3
schedule=list(range(7))+[3,4,5]+list(range(7))*cycles
original_pot=q.POT[:7]
q.POT=[original_pot[i] for i in schedule]
for row in q.rows.values():
    first=row['threshold'][:7]
    row['threshold']=[first[i] for i in schedule]
    row['prefixValues'] += [0]*(7*cycles)

def pieces(r,v,row,finish,phase):
    cuts={0,1,2,3,finish}
    cuts.update(s[0] for s in row['base'][5]);cuts.update(row['threshold'][:phase])
    return {x for x in cuts if 0<=x<=finish}

def candidates(r,v,row,lo,hi,phase):
    witnesses=[0]+[k+1 for k in range(phase) if row['threshold'][k]<=lo]
    lines=set()
    for ww in witnesses:
        b=q.line(r,v,lo,ww);a=0 if lo==hi else q.line(r,v,lo+1,ww)-b
        lines.add((a,b-a*lo))
    lines=list(lines);points={lo,hi}
    for k,(a,b) in enumerate(lines):
        for aa,bb in lines[:k]:
            if a!=aa:
                x=(bb-b)//(a-aa)
                for xx in [x,x+1]:
                    if lo<=xx<=hi:points.add(xx)
    return points,lines

reductions=[0]*len(schedule);biggest=[0]*len(schedule)
for (r,v),row in sorted(q.rows.items()):
    parent=q.rows.get((r-1,v),{}).get('prefixValues',[0]*len(schedule))
    previous=q.rows.get((r,v-1),{}).get('prefixValues',[0]*len(schedule))
    for j in range(10,len(schedule)):
        finish=min(row['threshold'][j],9276-r-v);needed=0
        cuts=sorted(pieces(r,v,row,finish,j))
        for lo,stop in zip(cuts,cuts[1:]):
            hi=stop-1
            if hi<lo:continue
            points,lines=candidates(r,v,row,lo,hi,j)
            for z in points:needed=max(needed,min(a*z+b for a,b in lines)-q.potential(r,v,z,j))
        new=max(needed,parent[j],previous[j])
        old_index=max(k for k in range(j) if schedule[k]==schedule[j])
        old=row['prefixValues'][old_index]
        assert new<=old,(r,v,j,new,old)
        reductions[j]+=int(new<old);biggest[j]=max(biggest[j],old-new)
        row['prefixValues'][j]=new

worst=[]
for (r,v),row in sorted(q.rows.items()):
    finish=9276-r-v;cuts=pieces(r,v,row,finish,len(schedule))
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
        hi=stop-1
        if hi<lo:continue
        points,lines=candidates(r,v,row,lo,hi,len(schedule))
        for z in points:
            cap=min(a*z+b for a,b in lines);t=9275-r-v-z
            complement=8728330260*t+7635583765037*min(t,185-r-v)+35730343721378*min(t,185-r-v,40-r)
            value=cap+complement+r*q.unit(r+v,r+v+z,r)+(40-r)*q.unit(185-r-v,18992-r-v-z,40-r)+18000000000000+1057030663884726
            if value>best:best=value;loc=[r,v,z]
    worst.append(dict(location=loc,total=best,margin=q.BOUND-best))
result=dict(schedule=schedule,reduced_prefixes_per_phase=reductions,largest_reduction_per_phase=biggest,
            worst=sorted(worst,key=lambda x:x['margin'])[:20],
            scope=('Target A181275 diagnostic with frozen incumbent base and other charges; NOT a valid score certificate.' if target else 'Finite-phase arithmetic with existing base and source validity. Extension of hardcoded Lean receipt not yet proved.'))
(q.ROOT/f'{"target_" if target else ""}repeated_phases_{cycles}.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(phases=len(schedule),reductions=reductions,worst=result['worst'][:2]),indent=2))
