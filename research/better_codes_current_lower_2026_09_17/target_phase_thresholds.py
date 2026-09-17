"""Target-A phase thresholds on the incumbent component box; partial diagnostic."""
import json,re,sys
from functools import lru_cache
import replay_ledger as q
lo,hi=map(int,sys.argv[1:3])
A=181275;delta=A-131071+1
kernel={x['name']:x for x in json.loads((q.ROOT/'phase_kernel_replay.json').read_text())}
sources=[]
for j in range(7):
    k=kernel[f'Source{j:02}']
    sources.append((k['L'],(A*k['m']+k['s']-1)//131071,k['s'],k['target_gap']))

def channel(T,Y,S):
    U=min(T,Y);B=T+1-U;k=min(S,U);n=U-k
    C=(S+1)*(B+S+1)-(S+1)*S//2
    return B*(k+2)*(k+1)//2+(k+2)*(k+1)*k//6+n*C+(S+1)*n*(n-1)//2

@lru_cache(maxsize=10000)
def feasible(j,r,v,z):
    if z>9275-r-v:return True
    T,Y,S,gap=sources[j];t=r+v+z;y=r+v
    if t>T or y>Y or r>S:return False
    fuel=min(T//t,Y//y,S//r)
    dc=131071*y-r;Dh=max(0,131071*(Y+1)-S-dc)
    thin=0
    for h in range(1,fuel+1):
        tt=max(0,T-h*t);yy=max(0,Y-h*y);ss=max(0,S-h*r)
        limit=max(0,Dh+ss-1)//131071
        thin+=delta*channel(tt,min(yy,limit),ss)
        if thin>=gap:return False
        Dh=max(0,Dh-delta-dc)
    return True

rows=[]
for (r,v),row in sorted(q.rows.items()):
    if not lo<=r<=hi:continue
    ts=[]
    for j in range(7):
        finish=9276-r-v;old=min(row['threshold'][j],finish)
        if feasible(j,r,v,old):left,right=0,old
        else:
            left=old+1;step=256;right=min(finish,old+step)
            while not feasible(j,r,v,right):
                left=right+1;step*=2;right=min(finish,old+step)
        # Monotone binary search under the same power-band theorem.
        while left<right:
            mid=(left+right)//2
            if feasible(j,r,v,mid):right=mid
            else:left=mid+1
        ts.append(left)
        assert feasible(j,r,v,left)
        if left:assert not feasible(j,r,v,left-1)
    rows.append(dict(r=r,v=v,threshold=ts+ts[3:6]))
out=dict(A=A,r_range=[lo,hi],sources=sources,rows=rows,
         scope='Phase threshold arithmetic on fixed incumbent component box; not complete score certificate.')
(q.ROOT/f'target_thresholds_{lo}_{hi}.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(r_range=[lo,hi],rows=len(rows)),indent=2))
