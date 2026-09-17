"""Finite phase05 shape grid; exact necessary local-prefix filter, not certificate."""
import sys,json
sys.argv=['repeat_phases.py','3','--target']
import repeat_phases as ext
import replay_phase_kernels as ker
q=ext.q
A=181275;n=262144;w=131071;delta=A-w+1
r,v=34,124;row=q.rows[r,v];finish=9276-r-v
cuts=sorted(ext.pieces(r,v,row,finish,len(q.POT)))
critical=set()
for lo,stop in zip(cuts,cuts[1:]):
    if lo<stop:
        pts,lines=ext.candidates(r,v,row,lo,stop-1,len(q.POT))
        critical.update(pts)
critical=sorted(critical)
def cap(z):
    return min(q.line(r,v,z,j) for j in range(len(q.POT)+1) if j==0 or row['threshold'][j-1]<=z)
values={z:cap(z) for z in critical}
def channel(T,Y,S):
    U=min(T,Y);B=T+1-U;k=min(S,U);nn=U-k
    C=(S+1)*(B+S+1)-(S+1)*S//2
    return B*(k+2)*(k+1)//2+(k+2)*(k+1)*k//6+nn*C+(S+1)*nn*(nn-1)//2

def threshold(L,Y,S,gap,r,v):
    def passes(z):
        if z>9275-r-v:return True
        t=r+v+z;y=r+v
        if t>L or y>Y or r>S:return False
        fuel=min(L//t,Y//y,S//r);dc=w*y-r;Dh=max(0,w*(Y+1)-S-dc);thin=0
        for h in range(1,fuel+1):
            ss=S-h*r;limit=max(0,Dh+ss-1)//w
            thin+=delta*channel(L-h*t,min(Y-h*y,limit),ss)
            if thin>=gap:return False
            Dh=max(0,Dh-delta-dc)
        return True
    lo,hi=0,9276-r-v
    while lo<hi:
        mid=(lo+hi)//2
        if passes(mid):hi=mid
        else:lo=mid+1
    return lo

def potential(L,Y,S):
    cy,cr,cz=1+2*w*159,w*69,1+2*w*9275
    return tuple((a+A-w-1)//(A-w)+b for a,b in [((n-w)*(cy*S+cr*Y),0),((n-w)*(cr*L+cz*S),(n-A+1)*S),((n-w)*(cy*L+cz*Y),(n-A+1)*Y)])

def evaluate(m,L,s):
    gap=ker.count(A*m,L,s)-n*ker.rank(m,L,s)
    if gap<=0:return None
    Y=(A*m+s-1)//w
    th=threshold(L,Y,s,gap,r,v)
    if threshold(L,Y,s,gap,35,124)>9090:return None
    a,b,c=potential(L,Y,s)
    pts=[z for z in critical if z<th]
    if th:pts.append(th-1)
    prefix=max([0]+[(values[z] if z in values else cap(z))-a*(r+v+z)-b*(r+v)-c*r for z in pts])
    charge=prefix+a*(35+124+9090)+b*159+c*35
    return dict(m=m,L=L,s=s,Y=Y,gap=gap,threshold_parent=th,potential=[a,b,c],necessary_local_prefix=prefix,optimistic_binding_source_charge=charge)

results=[];tested=0
for m in [250,400,600,800,1000,1200,1500,2000]:
    for sr in [270,285,300,308,315,330,345]:
        for lr in [65000,75000,80000,85000,88902,93000,100000,110000,125000]:
            tested+=1
            got=evaluate(m,(m*lr+999)//1000,m*sr//1000)
            if got:results.append(got)
results.sort(key=lambda x:x['optimistic_binding_source_charge'])
out=dict(tested=tested,feasible=len(results),scope='Necessary local prefix filter at parent34,124; excludes inherited monotonicity and other contexts. Candidate ranking only.',best=results[:40])
(q.ROOT/'new_phase_grid.json').write_text(json.dumps(out,indent=2)+'\n')
# Persist arithmetic target state so finalist jobs need not rebuild it.
(q.CACHE/'target31_state.json').write_text(json.dumps(dict(pot=q.POT,rows=[[r,v,row] for (r,v),row in q.rows.items()])))
print(json.dumps(out,indent=2))
