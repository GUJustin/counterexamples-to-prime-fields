"""Exact Jacobian and geometric tangent checks for the full-row limit."""
from math import comb
from pathlib import Path
import json
from verify_ramified_obstruction import ev,matrix_rank


def check(p,labels):
    n=p-1;k=n//4;D=k-1
    cs=[[comb((p+1)//2,2*j+1)*pow(a,(p+1)//2-2*j-1,p)%p for j in range(k)] for a in labels]
    xs=list(range(1,p))
    word=[((1+(1 if pow(x,n//2,p)==1 else -1))//2-pow(x,k,p))%p for x in xs]
    incidence=[[i for i,c in enumerate(cs) if ev(c,x,p)==w] for x,w in zip(xs,word)]
    covered=[(x,inc) for x,inc in zip(xs,incidence) if inc];c=len(covered);M=c+k*len(cs)
    assert len({tuple(poly) for poly in cs})==len(cs)
    J=[]
    for u,(x,inc) in enumerate(covered):
        ref=inc[0]
        for i in inc[1:]:
            row=[0]*M
            row[u]=sum(t*(cs[i][t]-cs[ref][t])*pow(x,t-1,p) for t in range(1,k))%p
            for t in range(k):row[c+i*k+t]=pow(x,t,p);row[c+ref*k+t]=-pow(x,t,p)%p
            J.append(row)
    motions=[]
    for t in range(k):
        row=[0]*M
        for i in range(len(cs)):row[c+i*k+t]=1
        motions.append(row)
    motions.append([0]*c+[a for poly in cs for a in poly])
    motions.append([-1%p]*c+[(t+1)*poly[t+1]%p if t+1<k else 0 for poly in cs for t in range(k)])
    motions.append([-x%p for x,inc in covered]+[t*poly[t]%p for poly in cs for t in range(k)])
    motions.append([x*x%p for x,inc in covered]+[(k-t)*poly[t-1]%p if t else 0 for poly in cs for t in range(k)])
    assert matrix_rank(motions,p)==k+4
    assert all(sum(x*y for x,y in zip(row,z))%p==0 for row in J for z in motions)
    rank=matrix_rank(J,p) if J else 0
    forced=sum(len(inc) for x,inc in covered)-2*c+k+4-k*len(cs)
    assert rank<=M-k-4 and len(J)-rank>=forced
    return dict(p=p,k=k,L=len(cs),covered_nodes=c,equations=len(J),variables=M,rank=rank,geometric_kernel=k+4,forced_row_dependencies=max(0,forced),actual_row_dependencies=len(J)-rank)


def main():
    out=[check(17,list(range(1,9))),check(41,list(range(1,21))),check(41,[3,8,10,11,12,13,16,17,18,20]),check(41,[3,8])]
    assert [x['rank'] for x in out[:3]]==[32,216,110]
    report=dict(status='passed',cases=out,scope='Necessary bound for the uncompressed full-row Jacobian lifting test, not a nonexistence theorem for lifts or growing lists.')
    Path(__file__).with_name('full_row_limit_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
