"""Exact piecewise-affine optimization of stored prefixes with sources fixed."""
import json
import replay_ledger as q

changes=[]
for (r,v),row in sorted(q.rows.items()):
    parent=q.rows.get((r-1,v),{}).get('prefixValues',[0]*10)
    previous=q.rows.get((r,v-1),{}).get('prefixValues',[0]*10)
    for j in range(10):
        finish=min(row['threshold'][j],9276-r-v)
        cuts={0,1,2,3,finish}
        cuts.update(s[0] for s in row['base'][5])
        cuts.update(row['threshold'][:j])
        cuts=sorted(x for x in cuts if 0<=x<=finish)
        needed=0
        for lo,stop in zip(cuts,cuts[1:]):
            hi=stop-1
            if hi<lo:continue
            witnesses=[0]+[k+1 for k in range(j) if row['threshold'][k]<=lo]
            lines=[]
            for w in witnesses:
                b=q.line(r,v,lo,w)
                a=0 if lo==hi else q.line(r,v,lo+1,w)-b
                lines.append((a,b-a*lo))
            points={lo,hi}
            for k,(a,b) in enumerate(lines):
                for aa,bb in lines[:k]:
                    if a!=aa:
                        x=(bb-b)//(a-aa)
                        for xx in [x,x+1]:
                            if lo<=xx<=hi:points.add(xx)
            for z in points:
                cap=min(a*z+b for a,b in lines)
                needed=max(needed,cap-q.potential(r,v,z,j))
        needed=max(needed,parent[j],previous[j])
        old=row['prefixValues'][j]
        assert needed<=old,(r,v,j,needed,old)
        if needed<old:changes.append([r,v,j,old,needed])
        row['prefixValues'][j]=needed

worst=[]
for (r,v),row in q.rows.items():
    start=0;best=0;loc=None
    for stop,w,mode in row['ledgerRuns']:
        for z in [start,stop-1]:
            value=q.branch(r,v,z,w,mode)
            if value>best:best=value;loc=[r,v,z,w,mode]
        start=stop
    worst.append(dict(location=loc,upper_bound=best,margin=q.BOUND-best))
result=dict(scope='Fixed stored base and phase-source validity assumed; exact prefix optimization only.',
            changed_prefixes=len(changes),largest_changes=sorted(changes,key=lambda x:x[3]-x[4],reverse=True)[:20],
            worst=sorted(worst,key=lambda x:x['margin'])[:20])
(q.ROOT/'prefix_optimization.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(changed_prefixes=len(changes),worst=result['worst'][:2]),indent=2))
