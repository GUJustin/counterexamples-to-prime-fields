"""A181275 phase propagation with incumbent base/other charges frozen.

Not a soundness certificate: primary and packing source repairs are omitted.
"""
import json
import replay_ledger as q
A=181275;n=262144;w=131071;gap=A-w
loaded={}
for lo,hi in [(1,7),(8,14),(15,21),(22,28),(29,35)]:
    data=json.loads((q.ROOT/f'target_thresholds_{lo}_{hi}.json').read_text())
    for row in data['rows']:loaded[row['r'],row['v']]=row['threshold']
assert loaded.keys()==q.rows.keys()
old_prefix={(r,v):row['prefixValues'][:] for (r,v),row in q.rows.items()}
for key,row in q.rows.items():row['threshold']=loaded[key]
sources=data['sources']
cy,cr,cz=1+2*w*159,w*(2*35-1),1+2*w*9275
pot=[]
for L,Y,S,g in sources:
    terms=[((n-w)*(cy*S+cr*Y),0),((n-w)*(cr*L+cz*S),(n-A+1)*S),((n-w)*(cy*L+cz*Y),(n-A+1)*Y)]
    pot.append(tuple((a+gap-1)//gap+b for a,b in terms))
q.POT=pot+pot[3:6]

def breakpoints(row,finish,phase):
    cuts={0,1,2,3,finish}
    cuts.update(s[0] for s in row['base'][5]);cuts.update(row['threshold'][:phase])
    return {x for x in cuts if 0<=x<=finish}

def candidates(r,v,row,lo,hi,phase):
    witnesses=[0]+[k+1 for k in range(phase) if row['threshold'][k]<=lo]
    lines=[]
    for ww in witnesses:
        b=q.line(r,v,lo,ww);a=0 if lo==hi else q.line(r,v,lo+1,ww)-b
        lines.append((a,b-a*lo))
    points={lo,hi}
    for k,(a,b) in enumerate(lines):
        for aa,bb in lines[:k]:
            if a!=aa:
                x=(bb-b)//(a-aa)
                for xx in [x,x+1]:
                    if lo<=xx<=hi:points.add(xx)
    return points,lines

for (r,v),row in sorted(q.rows.items()):
    parent=q.rows.get((r-1,v),{}).get('prefixValues',[0]*10)
    previous=q.rows.get((r,v-1),{}).get('prefixValues',[0]*10)
    for j in range(10):
        finish=min(row['threshold'][j],9276-r-v)
        cuts=sorted(breakpoints(row,finish,j));needed=0
        for lo,stop in zip(cuts,cuts[1:]):
            hi=stop-1
            if hi<lo:continue
            points,lines=candidates(r,v,row,lo,hi,j)
            for z in points:
                needed=max(needed,min(a*z+b for a,b in lines)-q.potential(r,v,z,j))
        row['prefixValues'][j]=max(needed,parent[j],previous[j])

worst=[];failed=0
for (r,v),row in sorted(q.rows.items()):
    finish=9276-r-v;cuts=breakpoints(row,finish,10)
    # Exact breakpoints for the frozen complement and chain max terms.
    for cut in [9275-r-v-(185-r-v),9275-r-v-min(185-r-v,40-r)]:
        for z in [cut,cut+1]:
            if 0<=z<=finish:cuts.add(z)
    aa,bb=q.unit_coeff(r+v,r)
    cc,dd=q.unit_coeff(185-r-v,40-r)
    if aa:
        cut=(9000000000000-bb)//aa-(r+v)
        for z in [cut,cut+1]:
            if 0<=z<=finish:cuts.add(z)
    if cc:
        cut=18992-r-v-(9000000000000-dd)//cc
        for z in [cut-1,cut,cut+1]:
            if 0<=z<=finish:cuts.add(z)
    cuts=sorted(cuts);best=-1;loc=None
    for lo,stop in zip(cuts,cuts[1:]):
        hi=stop-1
        if hi<lo:continue
        points,lines=candidates(r,v,row,lo,hi,10)
        for z in points:
            cap=min(a*z+b for a,b in lines)
            t=9275-r-v-z
            complement=8728330260*t+7635583765037*min(t,185-r-v)+35730343721378*min(t,185-r-v,40-r)
            value=cap+complement+r*q.unit(r+v,r+v+z,r)+(40-r)*q.unit(185-r-v,18992-r-v-z,40-r)+18000000000000+1057030663884726
            if value>best:best=value;loc=[r,v,z]
    if best>q.BOUND:failed+=1
    worst.append(dict(location=loc,total=best,margin=q.BOUND-best))
result=dict(A=A,scope='Recomputed phase kernels, thresholds, potentials and prefixes; incumbent base/complement/chain/box frozen. NOT a complete or valid score certificate.',
            failed_rows=failed,worst=sorted(worst,key=lambda x:x['margin'])[:20],
            old_worst_parent_prefix=old_prefix[34,124][5],new_worst_parent_prefix=q.rows[34,124]['prefixValues'][5],
            potentials=q.POT)
(q.ROOT/'target_phase_diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
