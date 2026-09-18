"""Bounded necessary gate for torsion-compatible dual quadratic identities."""
import json, random, time
from pathlib import Path

start=time.monotonic()
mons=[(i,j) for i in range(4) for j in range(i,4)]

def run(p):
    def add(P,Q):
        if P is None:return Q
        if Q is None:return P
        x,y=P;u,v=Q
        if x==u and (y+v)%p==0:return None
        slope=((3*x*x-1)*pow(2*y,-1,p) if P==Q else
               (v-y)*pow(u-x,-1,p))%p
        z=(slope*slope-x-u)%p
        return z,(slope*(x-z)-y)%p
    def neg(P):return None if P is None else (P[0],-P[1]%p)
    def mul(k,P):
        if k<0:return mul(-k,neg(P))
        out=None
        for _ in range(k):out=add(out,P)
        return out
    def embed(P):
        if P is None:return [0,0,0,1]
        x,y=P;return [1,x,y,x*x%p]
    def det3(a):
        return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
               -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
               +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))%p
    def rref(rows,width):
        A=[r[:] for r in rows];piv=[];r=0
        for c in range(width):
            z=next((i for i in range(r,len(A)) if A[i][c]),None)
            if z is None:continue
            A[r],A[z]=A[z],A[r]
            inv=pow(A[r][c],-1,p);A[r]=[v*inv%p for v in A[r]]
            for i in range(len(A)):
                if i!=r and A[i][c]:
                    f=A[i][c];A[i]=[(v-f*w)%p for v,w in zip(A[i],A[r])]
            piv.append(c);r+=1
            if r==len(A):break
        basis=[]
        for c in range(width):
            if c in piv:continue
            v=[0]*width;v[c]=1
            for i,j in enumerate(piv):v[j]=-A[i][c]%p
            basis.append(v)
        return len(piv),basis
    roots={}
    for y in range(p):roots.setdefault(y*y%p,[]).append(y)
    points=[None]+[(x,y) for x in range(p) for y in roots.get((x*x*x-x)%p,[])]
    rng=random.Random(p+20260918)
    out=[]
    for m in range(-3,4):
        for n in range(-3,4):
            planes=[];witnesses=[];seen=set()
            for attempt in range(2500):
                P,Q=rng.sample(points,2)
                R=add(mul(m,P),mul(n,Q));S=neg(add(add(P,Q),R))
                if len({P,Q,R,S})<4:continue
                rows=list(map(embed,(P,Q,R)))
                plane=[((-1)**j*det3([[v[k] for k in range(4) if k!=j] for v in rows]))%p for j in range(4)]
                if not any(plane):continue
                assert sum(v*w for v,w in zip(plane,embed(S)))%p==0
                inv=pow(next(v for v in plane if v),-1,p)
                plane=tuple(v*inv%p for v in plane)
                if plane in seen:continue
                seen.add(plane);planes.append(list(plane));witnesses.append([P,Q,R,S])
                if len(planes)==100:break
            linear_rank,_=rref(planes,4)
            quadrows=[[v[i]*v[j]%p for i,j in mons] for v in planes]
            rank,basis=rref(quadrows,10)
            ranks=[]
            for v in basis:
                M=[[0]*4 for _ in range(4)]
                for a,(i,j) in zip(v,mons):
                    M[i][j]=M[j][i]=a if i==j else a*pow(2,-1,p)%p
                ranks.append(rref(M,4)[0])
            selected=[];indrows=[];old=0
            for i,row in enumerate(quadrows):
                new,_=rref(indrows+[row],10)
                if new>old:
                    selected.append(i);indrows.append(row);old=new
            # All original sample data retained for direct independent replay.
            out.append(dict(m=m,n=n,valid_planes=len(planes),linear_rank=linear_rank,
                            quadratic_rank=rank,kernel=basis,kernel_basis_matrix_ranks=ranks,
                            planes=planes,quadruples=witnesses,independent_row_indices=selected))
    return dict(p=p,curve='y^2=x^3-x',group_order=len(points),cases=out)

data=dict(monomials=mons,field_results=[run(p) for p in (1009,1013)],
          scope='Necessary sampled identity gate; no positive characteristic-zero identity claimed.',
          seconds=time.monotonic()-start)
Path(__file__).with_suffix('.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
for field in data['field_results']:
    print(json.dumps(dict(p=field['p'],group_order=field['group_order'],
        cases=[{k:v for k,v in r.items() if k not in ['planes','quadruples','kernel','independent_row_indices']} for r in field['cases'] if r['quadratic_rank']<10])))
print('seconds',data['seconds'])
