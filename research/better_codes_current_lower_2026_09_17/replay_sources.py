"""Independent integer replay of current lower-certificate interpolation sources."""
import json,re
from pathlib import Path
ROOT=Path(__file__).parent
n,w=262144,131071

def rect(a,b,c,H):
    t=max(0,a+b-2-H)
    assert t<=min(a,b) and c>=a+b-2
    return a*b*c-b*a*(a-1)//2-a*b*(b-1)//2-(c-a-b+2)*t*(t+1)//2-t*(t-1)*(t+1)//3

def rank(m,B,s,U,L,k,n0):
    total=0
    for r in range(m):
        for h in range(s+1):
            total+=rect(r+1,B-2*h+1,L+1-h,U-h)
            q=max((m-r+1)//2,max(0,m-r-(s-h)))
            if q<=r and m-r+2*h<=B:
                total-=rect(r-q+1,B-2*h-q+1,L+1-h-q,U-h-q)
    return total

def coefficients(A,m,B,s,U,L,k,n0):
    total=0
    assert 2*s<=B<=m and m+s<=U<=L and m+B+s<=L
    for h in range(s+1):
        reserve=h if h<n0 else k
        D=m*A-reserve*(A-(w-2))
        assert U<=(D+B-1)//w
        for r in range(B-2*h+1):
            q=max(0,D-(w-2)*h-(w-1)*r)
            y=min(max(0,q-1)//w+1,U+1-h-r)
            C=L+1-h-r
            total+=y*q*C+w*y*(y-1)*(2*y-1)//6-(q+w*C)*y*(y-1)//2
    return total

sources=[]
for file in sorted(ROOT.glob('MovingFiberSources6811[A-D].lean')):
    for idx,body in re.findall(r'namespace ProximityPrize.SubmissionLower.MovingFiberSources6811.P(\d+)\n(.*?)(?=\nend\nend)',file.read_text(),re.S):
        params=[int(re.search(r'def '+name+r' : ℕ := (\d+)',body)[1]) for name in ['m','B','s','U','L','k','n0']]
        expected_c=int(re.search(r'coefficientCount .*?=\s*(\d+) := by decide',body,re.S)[1])
        expected_r=int(re.search(r'theorem local_rank : .*?= (\d+) :=',body)[1])
        R=rank(*params);C=coefficients(181284,*params)
        assert (R,C)==(expected_r,expected_c),(idx,R,C,expected_r,expected_c)
        assert C>n*R
        proposed=coefficients(181275,*params)
        changed=params.copy();changed[4]+=1
        slope=coefficients(181275,*changed)-proposed-n*(rank(*changed)-R)
        gap=proposed-n*R
        increase=max(0,(-gap)//slope+1) if slope>0 else None
        if increase is not None:
            repaired=params.copy();repaired[4]+=increase
            assert coefficients(181275,*repaired)>n*rank(*repaired)
        sources.append(dict(index=int(idx),parameters=params,rank=R,coefficients=C,
                            current_surplus=C-n*R,next_threshold_surplus=gap,
                            L_surplus_slope=slope,min_L_increase= increase))
result=dict(pin='cdb451f13fdc6c84f5fe363e77ee13a89bd30974',current_A=181284,target_A=181275,
            sources=sorted(sources,key=lambda x:x['index']),
            scope='Interpolation dimension gate only; not a complete score certificate.')
assert len(sources)==27
(ROOT/'source_replay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(sources=len(sources),target_passes=sum(x['next_threshold_surplus']>0 for x in sources),
                     L_increases=[(x['index'],x['min_L_increase']) for x in result['sources']]),indent=2))
