"""Exact first-jet kernel dimensions for the actual current phase sources."""
import json,re,math
from pathlib import Path
ROOT=Path(__file__).parent;CACHE=ROOT.parents[1]/'tmp/current-lower-primary-cache'

def rank(m,L,s):
    assert 2*s<=m and m+s<=L+1
    source=(s+1)*m*(m+1)*(6*(L+1)-2*(m-1)-3*s)
    c=2*L+2-m-s;p0=(m+1)*(s+1);p1=-(m+2*s+3);k=s
    removed=6*p0*c*k+3*(p0+p1*c)*k*(k+1)+(p1+2*c)*k*(k+1)*(2*k+1)+3*k*k*(k+1)*(k+1)
    assert (source-removed)%12==0
    return (source-removed)//12

def count(D,L,s):
    w=131071;q,r=divmod(D,w)
    assert s<=q<=L
    if r+s>w:
        total=0
        for j in range(s+1):
            d=max(0,D-(w-1)*j);C=L+1-j
            nn=min((d-1)//w+1,C) if d else 0
            total+=nn*d*C+w*nn*(nn-1)*(2*nn-1)//6-(d+w*C)*nn*(nn-1)//2
        return total
    U=L+1-q
    c1=U*(r+q);c2=U*(w-2)+r+q+w-1;c3=2*(w-2)+1
    return sum(c*(math.comb(q+2,j)-math.comb(q+1-s,j)) for c,j in [(c1,2),(c2,3),(c3,4)])

text=(CACHE/'MovingFiberKernels6811.lean').read_text()
rows=[]
for name,body in re.findall(r'namespace (\w+)\n(.*?)\nend \1',text,re.S):
    match=re.search(r'coefficient_exact : coefficientCount (\d+) 131071 (\d+) (\d+) = (\d+)',body)
    if match is None:continue
    D,L,s,C=map(int,match.groups())
    m,LL,ss,R=map(int,re.search(r'rank_exact : localRankBound (\d+) (\d+) (\d+) = (\d+)',body).groups())
    assert (LL,ss)==(L,s) and D==181284*m
    assert count(D,L,s)==C and rank(m,L,s)==R
    newC=count(181275*m,L,s)
    rows.append(dict(name=name,m=m,L=L,s=s,rank=R,coefficients=C,current_gap=C-262144*R,
                     target_gap=newC-262144*R,coefficient_loss=C-newC))
assert len(rows)==10
(ROOT/'phase_kernel_replay.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
