"""Independent current phase-source power-band threshold replay."""
import json,re
import replay_ledger as q

sources=[tuple(map(int,x.split(','))) for x in re.findall(r'def source : SourceNumbers := ⟨(.*?)⟩',(q.CACHE/'MovingFiberSourceSound6811.lean').read_text())]
assert len(sources)==7
sources+=sources[3:6]

def channel(T,Y,S):
    U=min(T,Y);B=T+1-U;k=min(S,U);n=U-k
    C=(S+1)*(B+S+1)-(S+1)*S//2
    return B*(k+2)*(k+1)//2+(k+2)*(k+1)*k//6+n*C+(S+1)*n*(n-1)//2

def bands(source,r,v,z):
    T,Y,S,gap=source;t=r+v+z;y=r+v
    if t>T or y>Y or r>S:return None
    fuel=min(T//t,Y//y,S//r)
    dc=131071*y-r;Dh=max(0,131071*(Y+1)-S-dc)
    thin=plain=0
    for j in range(1,fuel+1):
        tt=max(0,T-j*t);yy=max(0,Y-j*y);ss=max(0,S-j*r)
        limit=max(0,Dh+ss-1)//131071
        thin+=50214*channel(tt,min(yy,limit),ss)
        plain+=50214*channel(tt,yy,ss)
        Dh=max(0,Dh-50214-dc)
    return thin,plain

checked=inactive=0;improvable=[];minimum_margin=None
for (r,v),row in sorted(q.rows.items()):
    for j,z in enumerate(row['threshold']):
        if z>9275-r-v:inactive+=1;continue
        got=bands(sources[j],r,v,z)
        assert got is not None
        margin=sources[j][3]-min(got)
        assert margin>0,(r,v,j,z,got,sources[j][3])
        checked+=1
        ratio=margin/sources[j][3]
        if minimum_margin is None or ratio<minimum_margin['relative_margin']:
            minimum_margin=dict(location=[r,v,j,z],margin=margin,gap=sources[j][3],relative_margin=ratio)
        if z:
            previous=bands(sources[j],r,v,z-1)
            if previous is not None and min(previous)<sources[j][3]:
                improvable.append([r,v,j,z])
result=dict(active_thresholds_checked=checked,inactive_thresholds=inactive,
            preceding_coordinate_also_passes=improvable,minimum_relative_margin=minimum_margin,
            scope='Phase-band arithmetic only; original kernel dimensions and packing sources not re-proved.')
(q.ROOT/'threshold_replay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(active=checked,inactive=inactive,improvable=len(improvable),minimum_margin=minimum_margin),indent=2))
